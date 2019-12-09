import sqlite3
from datetime import datetime

conn = sqlite3.connect("clients.db")
c = conn.cursor()


def add_to_database(nome, rua, bairro, telefone, referencia, número, data=datetime.today().strftime('%d-%m-%Y'),
                    produto=None, preço=None):
    rowid = get_customer_id(nome=nome, rua=rua, bairro=bairro, número=número)
    if rowid:
        with conn:
            c.execute("INSERT INTO vendas VALUES (:rowid, :preço, :produto, :data)",
                      {'rowid': rowid, 'preço': preço, 'produto': produto, 'data': data})
        return 'existent customer'
    else:
        if nome != '' and rua != '' and bairro != '' and número != '':
            try:
                d, m, y = data.split('/')
                d = f"{int(d):02d}"
                m = f"{int(m):02d}"
                y = f"{int(y):04d}"
                data = f"{d}/{m}/{y}"
            except ValueError("Data tem que ser no formato dd/mm/yyyy"):
                return 'fail'

            with conn:
                c.execute("INSERT INTO clientes VALUES (:nome, :rua, :número, :bairro, :referencia, :telefone, :data)",
                          {'nome': nome, 'rua': rua, 'bairro': bairro, 'telefone': telefone, 'referencia': referencia,
                           'número': número, 'data': data})

            add_to_database(nome, rua, bairro, telefone, referencia, número, data, produto, preço)
            return 'Success'
        else:
            return 'Fail'


def get_customer_id(nome, rua, bairro, número, data=None):
    with conn:

        query = "SELECT rowid FROM clientes WHERE nome LIKE :nome AND rua LIKE :rua AND " \
                "bairro LIKE :bairro AND número LIKE :número"

        c.execute(query, {'nome': nome, 'rua': rua, 'bairro': bairro, 'número': número})
        result = c.fetchall()

        if result:
            return result[0][0]
        else:
            return False

# print(customer_exists('Pedro Dias', 'rua canadá', 'jardim botânico', '1912'))


def search_database(nome=None, rua=None, bairro=None, telefone=None, referencia=None, número=None, data=None):
    search_elements = {'nome': nome, 'rua': rua, 'bairro': bairro, 'telefone': telefone,
                       'referência': referencia, 'número': número, 'data': data}

    search_elements = {each: search_elements[each] for each in search_elements if search_elements[each] != ''}

    query = "SELECT * FROM clientes WHERE "

    empty = True
    for each in search_elements:
        if empty:
            query += f"{each} LIKE :{each} "
            empty = False
        else:
            query += f"AND {each} LIKE :{each} "

    # print(query)
    if query == "SELECT * FROM clientes WHERE ":
        query = "SELECT * FROM clientes"
        c.execute(query)
    else:
        nome = add_wild_card(nome)
        rua = add_wild_card(rua)
        bairro = add_wild_card(bairro)
        referencia = add_wild_card(referencia)
        telefone = f"%{telefone}%"
        número = f"%{número}%"

        c.execute(query, {'nome': nome, 'rua': rua, 'bairro': bairro, 'telefone': telefone,
                          'referência': referencia, 'número': número, 'data': data})

    result = c.fetchall()
    if result:
        return result
    else:
        return None


def add_wild_card(arg):
    if type(arg) == str:
        n_word = '%'
        for lt in arg:
            n_word += lt+'%'
        return n_word
    elif type(arg) == list:
        n_list = []
        for w in arg:
            wc = add_wild_card(w)
            if wc != '%':
                n_list.append(add_wild_card(w))
        return n_list


def search_month(data, nome='', número='', rua='', bairro=''):
    nome = add_wild_card(nome)
    número = add_wild_card(número)
    rua = add_wild_card(rua)
    bairro = add_wild_card(bairro)

    search_elements = {'nome': nome, 'número': número, 'rua': rua, 'bairro': bairro}
    search_elements = {each: search_elements[each] for each in search_elements if search_elements[each] != ''}

    query = "SELECT * FROM clientes WHERE "
    # data = f"%{data}"
    # query += f"data LIKE :data "

    empty = True
    for each in search_elements:
        if empty:
            query += f"{each} LIKE :{each} "
            empty = False
        else:
            query += f"AND {each} LIKE :{each} "

    with conn:
        # c.execute(query, {'rua': rua, 'bairro': bairro, 'data': data})
        c.execute(query, {'nome': nome, 'número': número, 'rua': rua, 'bairro': bairro})
        result = c.fetchall()
    return result


def search_sales(customer_id, date):
    with conn:
        date = f"%{date}"
        c.execute("SELECT * FROM clientes WHERE rowid=:customer_id", {'customer_id': customer_id})
        fetch1 = c.fetchall()
        c.execute("SELECT * FROM vendas WHERE client_id=:customer_id AND date LIKE :date ORDER BY DATE", {'customer_id': customer_id, 'date': date})
        fetch2 = c.fetchall()
        result = []
        if fetch1 and fetch2:
            nome, rua, número, bairro, _, _, _ = fetch1[0]
            for each in fetch2:
                preço, produto, data = each[1:]
                result.append([nome, rua, número, bairro, produto, preço, data])
            return result
        else:
            return False