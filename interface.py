from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QDialog, QPushButton
import database_manager as dm


class UiMainWindow(object):
    def __init__(self, mainwindow):
        self.main_window = mainwindow
        self.main_window.setObjectName("MainWindow")
        self.main_window.resize(1052, 810)

        self.centralwidget = QtWidgets.QWidget(self.main_window)
        self.centralwidget.setObjectName("centralwidget")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1051, 801))
        self.tabWidget.setObjectName("tabWidget")

        self.init_search_tab()
        self.init_sales_tab()
        self.init_add_tab()

        self.main_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.main_window)
        self.statusbar.setObjectName("statusbar")
        self.main_window.setStatusBar(self.statusbar)

        self.retranslate_ui(self.main_window)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self.main_window)
        self.search_month_sales()
        self.search_customers()

        self.populate_combo_boxes()
        self.set_tab_order()

    def init_add_tab(self):
        self.Adicionar = QtWidgets.QWidget()
        self.Adicionar.setObjectName("Adicionar")

        field_font = QtGui.QFont()
        field_font.setPointSize(16)
        label_font = QtGui.QFont()
        label_font.setPointSize(14)

        self.add_button = QtWidgets.QPushButton(self.Adicionar)
        self.add_button.setGeometry(QtCore.QRect(10, 170, 331, 51))
        self.add_button.setObjectName("add_button")
        self.add_button.clicked.connect(self.add_customer)
        self.add_button.setFont(field_font)

        self.add_st_label = QtWidgets.QLabel(self.Adicionar)
        self.add_st_label.setGeometry(QtCore.QRect(350, 10, 61, 28))
        self.add_st_label.setFont(label_font)
        self.add_st_label.setObjectName("add_st_label")
        self.add_st_field = QtWidgets.QComboBox(self.Adicionar)
        self.add_st_field.setGeometry(QtCore.QRect(350, 34, 341, 41))
        self.add_st_field.setFont(field_font)
        self.add_st_field.setEditable(True)
        self.add_st_field.addItem('')
        self.add_st_field.setObjectName("add_st_field")

        self.add_na_label = QtWidgets.QLabel(self.Adicionar)
        self.add_na_label.setGeometry(QtCore.QRect(10, 10, 91, 28))
        self.add_na_label.setFont(label_font)
        self.add_na_label.setObjectName("add_na_label")
        self.add_na_field = QtWidgets.QLineEdit(self.Adicionar)
        self.add_na_field.setGeometry(QtCore.QRect(10, 34, 331, 41))
        self.add_na_field.setText("")
        self.add_na_field.setFont(field_font)
        self.add_na_field.setObjectName("add_na_field")

        self.add_ba_label = QtWidgets.QLabel(self.Adicionar)
        self.add_ba_label.setGeometry(QtCore.QRect(700, 10, 91, 28))
        self.add_ba_label.setFont(label_font)
        self.add_ba_label.setObjectName("add_ba_label")
        self.add_ba_field = QtWidgets.QComboBox(self.Adicionar)
        self.add_ba_field.setGeometry(QtCore.QRect(700, 34, 341, 41))
        self.add_ba_field.setFont(field_font)
        self.add_ba_field.setEditable(True)
        self.add_ba_field.addItem('')
        self.add_ba_field.setObjectName("add_ba_field")

        self.add_nu_label = QtWidgets.QLabel(self.Adicionar)
        self.add_nu_label.setGeometry(QtCore.QRect(700, 90, 131, 28))
        self.add_nu_label.setFont(label_font)
        self.add_nu_label.setObjectName("add_nu_label")
        self.add_nu_field = QtWidgets.QLineEdit(self.Adicionar)
        self.add_nu_field.setGeometry(QtCore.QRect(700, 114, 131, 41))
        self.add_nu_field.setFont(field_font)
        self.add_nu_field.setText("")
        self.add_nu_field.setObjectName("add_nu_field")

        self.add_re_label = QtWidgets.QLabel(self.Adicionar)
        self.add_re_label.setGeometry(QtCore.QRect(350, 90, 141, 28))
        self.add_re_label.setFont(label_font)
        self.add_re_label.setObjectName("add_re_label")
        self.add_re_field = QtWidgets.QLineEdit(self.Adicionar)
        self.add_re_field.setGeometry(QtCore.QRect(350, 114, 341, 41))
        self.add_re_field.setFont(field_font)
        self.add_re_field.setObjectName("add_re_field")

        self.add_ph_label = QtWidgets.QLabel(self.Adicionar)
        self.add_ph_label.setGeometry(QtCore.QRect(10, 90, 91, 28))
        self.add_ph_label.setFont(label_font)
        self.add_ph_label.setObjectName("add_ph_label")
        self.add_ph_field = QtWidgets.QLineEdit(self.Adicionar)
        self.add_ph_field.setGeometry(QtCore.QRect(10, 114, 141, 41))
        self.add_ph_field.setFont(field_font)
        self.add_ph_field.setObjectName("add_ph_field")

        self.add_product_label = QtWidgets.QLabel(self.Adicionar)
        self.add_product_label.setGeometry(QtCore.QRect(160, 90, 81, 28))
        self.add_product_label.setFont(label_font)
        self.add_product_label.setObjectName("add_product_label")
        self.add_product_field = QtWidgets.QComboBox(self.Adicionar)
        self.add_product_field.setGeometry(QtCore.QRect(160, 114, 91, 41))
        self.add_product_field.setFont(field_font)
        self.add_product_field.setEditable(True)
        self.add_product_field.setObjectName("add_product_field")
        self.add_product_field.addItem("Gás")
        self.add_product_field.addItem("Água")

        self.add_price_label = QtWidgets.QLabel(self.Adicionar)
        self.add_price_label.setGeometry(QtCore.QRect(260, 90, 61, 28))
        self.add_price_label.setFont(label_font)
        self.add_price_label.setObjectName("add_price_label")
        self.add_price_field = QtWidgets.QLineEdit(self.Adicionar)
        self.add_price_field.setGeometry(QtCore.QRect(260, 114, 81, 41))
        self.add_price_field.setFont(field_font)
        self.add_price_field.setObjectName("add_price_field")

        self.add_date_label = QtWidgets.QLabel(self.Adicionar)
        self.add_date_label.setGeometry(QtCore.QRect(840, 90, 69, 28))
        self.add_date_label.setFont(label_font)
        self.add_date_label.setObjectName("add_date_label")

        self.add_day_field = QtWidgets.QComboBox(self.Adicionar)
        self.add_day_field.setGeometry(QtCore.QRect(840, 114, 61, 41))
        self.add_day_field.setEditable(True)
        self.add_day_field.setFont(field_font)
        self.add_day_field.setObjectName("add_day_field")

        self.add_month_field = QtWidgets.QComboBox(self.Adicionar)
        self.add_month_field.setGeometry(QtCore.QRect(900, 114, 61, 41))
        self.add_month_field.setEditable(True)
        self.add_month_field.setFont(field_font)
        self.add_month_field.setObjectName("add_month_field")

        self.add_year_field = QtWidgets.QComboBox(self.Adicionar)
        self.add_year_field.setGeometry(QtCore.QRect(960, 114, 81, 41))
        self.add_year_field.setEditable(True)
        self.add_year_field.setFont(field_font)
        self.add_year_field.setObjectName("add_year_field")

        for i in range(31, 0, -1):
            i = f'{i:02}'
            self.add_day_field.addItem(i)
        for i in range(12, 0, -1):
            i = f'{i:02}'
            self.add_month_field.addItem(i)
        for i in range(2030, 2017, -1):
            self.add_year_field.addItem(str(i))

        date = datetime.today().strftime('%d-%m-%Y')
        d, m, y = int(date[:2]), int(date[3:5]), int(date[6:])
        # self.add_day_field.setCurrentText(str(d))
        self.add_day_field.setCurrentIndex(31-d)
        # self.add_month_field.setCurrentText(str(m))
        self.add_month_field.setCurrentIndex(12-m)
        # self.add_year_field.setCurrentText(str(y))
        self.add_year_field.setCurrentIndex(2030-y)

        self.tabWidget.addTab(self.Adicionar, "")

    def init_search_tab(self):
        self.Busca = QtWidgets.QWidget()
        self.Busca.setObjectName("Clientes")

        field_font = QtGui.QFont()
        field_font.setPointSize(16)
        label_font = QtGui.QFont()
        label_font.setPointSize(14)

        self.search_nu_label = QtWidgets.QLabel(self.Busca)
        self.search_nu_label.setGeometry(QtCore.QRect(700, 90, 111, 28))
        self.search_nu_label.setFont(label_font)
        self.search_nu_label.setObjectName("search_nu_label")
        self.search_nu_field = QtWidgets.QLineEdit(self.Busca)
        self.search_nu_field.setGeometry(QtCore.QRect(700, 114, 131, 41))
        self.search_nu_field.setText("")
        self.search_nu_field.setFont(field_font)
        self.search_nu_field.setObjectName("search_nu_field")
        self.search_nu_field.textChanged.connect(lambda: self.search_customers(button=False))

        self.search_st_label = QtWidgets.QLabel(self.Busca)
        self.search_st_label.setGeometry(QtCore.QRect(350, 10, 51, 28))
        self.search_st_label.setFont(label_font)
        self.search_st_label.setObjectName("search_st_label")
        self.search_st_field = QtWidgets.QComboBox(self.Busca)
        self.search_st_field.setGeometry(QtCore.QRect(350, 34, 341, 41))
        self.search_st_field.setEditable(True)
        self.search_st_field.setFont(field_font)
        self.search_st_field.setObjectName("search_st_field")
        self.search_st_field.setCurrentText('')
        self.search_st_field.addItem('')
        self.search_st_field.currentTextChanged.connect(lambda: self.search_customers(button=False))

        self.search_na_label = QtWidgets.QLabel(self.Busca)
        self.search_na_label.setGeometry(QtCore.QRect(10, 10, 61, 28))
        self.search_na_label.setFont(label_font)
        self.search_na_label.setObjectName("search_na_label")
        self.search_na_field = QtWidgets.QLineEdit(self.Busca)
        self.search_na_field.setGeometry(QtCore.QRect(10, 34, 331, 41))
        self.search_na_field.setText("")
        self.search_na_field.setFont(field_font)
        self.search_na_field.setObjectName("search_na_field")
        self.search_na_field.textChanged.connect(lambda: self.search_customers(button=False))

        self.search_ba_label = QtWidgets.QLabel(self.Busca)
        self.search_ba_label.setGeometry(QtCore.QRect(700, 10, 61, 28))
        self.search_ba_label.setFont(label_font)
        self.search_ba_label.setObjectName("search_ba_label")
        self.search_ba_field = QtWidgets.QComboBox(self.Busca)
        self.search_ba_field.setGeometry(QtCore.QRect(700, 34, 341, 41))
        self.search_ba_field.setEditable(True)
        self.search_ba_field.setFont(field_font)
        self.search_ba_field.setObjectName("search_ba_field")
        self.search_ba_field.setCurrentText('')
        self.search_ba_field.addItem('')
        self.search_ba_field.currentTextChanged.connect(lambda: self.search_customers(button=False))

        self.search_ph_label = QtWidgets.QLabel(self.Busca)
        self.search_ph_label.setGeometry(QtCore.QRect(10, 90, 131, 28))
        self.search_ph_label.setFont(label_font)
        self.search_ph_label.setObjectName("search_ph_label")
        self.search_ph_field = QtWidgets.QLineEdit(self.Busca)
        self.search_ph_field.setGeometry(QtCore.QRect(10, 114, 331, 41))
        self.search_ph_field.setFont(field_font)
        self.search_ph_field.setObjectName("search_ph_field")
        self.search_ph_field.textChanged.connect(lambda: self.search_customers(button=False))

        self.search_re_label = QtWidgets.QLabel(self.Busca)
        self.search_re_label.setGeometry(QtCore.QRect(350, 90, 121, 28))
        self.search_re_label.setFont(label_font)
        self.search_re_label.setObjectName("search_re_label")
        self.search_re_field = QtWidgets.QLineEdit(self.Busca)
        self.search_re_field.setGeometry(QtCore.QRect(350, 114, 341, 41))
        self.search_re_field.setFont(field_font)
        self.search_re_field.setObjectName("search_re_field")
        self.search_re_field.textChanged.connect(lambda: self.search_customers(button=False))

        self.tableWidget = QtWidgets.QTableWidget(self.Busca)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(10, 180, 1031, 571))
        self.tableWidget.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.tableWidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        self.tableWidget.itemDoubleClicked.connect(self.search_item_clicked)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)

        self.tableWidget.horizontalHeader().setDefaultSectionSize(147)
        self.tableWidget.horizontalHeader().setHighlightSections(True)

        self.search_date_label = QtWidgets.QLabel(self.Busca)
        self.search_date_label.setGeometry(QtCore.QRect(840, 90, 69, 28))
        self.search_date_label.setFont(label_font)
        self.search_date_label.setObjectName("search_date_label")

        self.search_day_field = QtWidgets.QComboBox(self.Busca)
        self.search_day_field.setGeometry(QtCore.QRect(840, 114, 61, 41))
        self.search_day_field.setFont(field_font)
        self.search_day_field.setEditable(True)
        self.search_day_field.setObjectName("search_day_field")

        self.search_month_field = QtWidgets.QComboBox(self.Busca)
        self.search_month_field.setGeometry(QtCore.QRect(900, 114, 61, 41))
        self.search_month_field.setFont(field_font)
        self.search_month_field.setEditable(True)
        self.search_month_field.setObjectName("search_month_field")

        self.search_year_field = QtWidgets.QComboBox(self.Busca)
        self.search_year_field.setGeometry(QtCore.QRect(960, 114, 81, 41))
        self.search_year_field.setFont(field_font)
        self.search_year_field.setEditable(True)
        self.search_year_field.setObjectName("search_year_field")

        for i in range(31, 0, -1):
            i = f'{i:02}'
            self.search_day_field.addItem(i)
        self.search_day_field.addItem('')
        for i in range(12, 0, -1):
            i = f'{i:02}'
            self.search_month_field.addItem(i)
        self.search_month_field.addItem('')
        for i in range(2030, 2017, -1):
            self.search_year_field.addItem(str(i))
        self.search_year_field.addItem('')

        date = datetime.today().strftime('%d-%m-%Y')
        d, m, y = int(date[:2]), int(date[3:5]), int(date[6:])
        # self.search_day_field.setCurrentText(str(d))
        # self.search_month_field.setCurrentText(str(m))
        # self.search_year_field.setCurrentText(str(y))
        self.search_day_field.setCurrentIndex(31)
        self.search_month_field.setCurrentIndex(12)
        self.search_year_field.setCurrentIndex(13)

        self.search_day_field.currentTextChanged.connect(self.search_customers)
        self.search_month_field.currentTextChanged.connect(self.search_customers)
        self.search_year_field.currentTextChanged.connect(self.search_customers)

        self.tabWidget.addTab(self.Busca, "")

    def init_sales_tab(self):
        self.Vendas = QtWidgets.QWidget()
        self.Vendas.setObjectName("Vendas")

        field_font = QtGui.QFont()
        field_font.setPointSize(16)
        label_font = QtGui.QFont()
        label_font.setPointSize(14)

        self.sales_re_label = QtWidgets.QLabel(self.Vendas)
        self.sales_re_label.setGeometry(QtCore.QRect(350, 90, 121, 28))
        self.sales_re_label.setFont(label_font)
        self.sales_re_label.setObjectName("sales_re_label")
        self.sales_re_field = QtWidgets.QLineEdit(self.Vendas)
        self.sales_re_field.setEnabled(False)
        self.sales_re_field.setGeometry(QtCore.QRect(350, 114, 341, 41))
        self.sales_re_field.setFont(field_font)
        self.sales_re_field.setObjectName("sales_re_field")

        self.sales_ba_label = QtWidgets.QLabel(self.Vendas)
        self.sales_ba_label.setGeometry(QtCore.QRect(700, 10, 61, 28))
        self.sales_ba_label.setFont(label_font)
        self.sales_ba_label.setObjectName("sales_ba_label")
        self.sales_ba_field = QtWidgets.QComboBox(self.Vendas)
        self.sales_ba_field.setGeometry(QtCore.QRect(700, 34, 341, 41))
        self.sales_ba_field.setFont(field_font)
        self.sales_ba_field.setEditable(True)
        self.sales_ba_field.setObjectName("sales_ba_field")
        self.sales_ba_field.addItem('')
        self.sales_ba_field.currentTextChanged.connect(self.search_month_sales)

        self.sales_nu_label = QtWidgets.QLabel(self.Vendas)
        self.sales_nu_label.setGeometry(QtCore.QRect(700, 90, 111, 28))
        self.sales_nu_label.setFont(label_font)
        self.sales_nu_label.setObjectName("sales_nu_label")
        self.sales_nu_field = QtWidgets.QLineEdit(self.Vendas)
        self.sales_nu_field.setGeometry(QtCore.QRect(700, 114, 131, 41))
        self.sales_nu_field.setText("")
        self.sales_nu_field.setFont(field_font)
        self.sales_nu_field.setObjectName("sales_nu_field")
        self.sales_nu_field.textChanged.connect(self.search_month_sales)

        self.sales_na_label = QtWidgets.QLabel(self.Vendas)
        self.sales_na_label.setGeometry(QtCore.QRect(10, 10, 61, 28))
        self.sales_na_label.setFont(label_font)
        self.sales_na_label.setObjectName("sales_na_label")
        self.sales_na_field = QtWidgets.QLineEdit(self.Vendas)
        self.sales_na_field.setGeometry(QtCore.QRect(10, 34, 331, 41))
        self.sales_na_field.setText("")
        self.sales_na_field.setFont(field_font)
        self.sales_na_field.setObjectName("sales_na_field")
        self.sales_na_field.textChanged.connect(self.search_month_sales)

        self.sales_ph_label = QtWidgets.QLabel(self.Vendas)
        self.sales_ph_label.setGeometry(QtCore.QRect(10, 90, 131, 28))
        self.sales_ph_label.setFont(label_font)
        self.sales_ph_label.setObjectName("sales_ph_label")
        self.sales_ph_field = QtWidgets.QLineEdit(self.Vendas)
        self.sales_ph_field.setEnabled(False)
        self.sales_ph_field.setGeometry(QtCore.QRect(10, 114, 331, 41))
        self.sales_ph_field.setFont(field_font)
        self.sales_ph_field.setReadOnly(True)
        self.sales_ph_field.setObjectName("sales_ph_field")

        self.sales_st_label = QtWidgets.QLabel(self.Vendas)
        self.sales_st_label.setGeometry(QtCore.QRect(350, 10, 51, 28))
        self.sales_st_label.setFont(label_font)
        self.sales_st_label.setObjectName("sales_st_label")
        self.sales_st_field = QtWidgets.QComboBox(self.Vendas)
        self.sales_st_field.setEnabled(True)
        self.sales_st_field.setEditable(True)
        self.sales_st_field.setGeometry(QtCore.QRect(350, 34, 341, 41))
        self.sales_st_field.setFont(field_font)
        self.sales_st_field.setObjectName("sales_st_field")
        self.sales_st_field.addItem('')
        self.sales_st_field.currentTextChanged.connect(self.search_month_sales)

        self.sales_date_label = QtWidgets.QLabel(self.Vendas)
        self.sales_date_label.setGeometry(QtCore.QRect(840, 90, 69, 28))
        self.sales_date_label.setFont(label_font)
        self.sales_date_label.setObjectName("sales_date_label")

        self.sales_day_field = QtWidgets.QComboBox(self.Vendas)
        self.sales_day_field.setGeometry(QtCore.QRect(840, 114, 61, 41))
        self.sales_day_field.setEditable(True)
        self.sales_day_field.setFont(field_font)
        self.sales_day_field.setObjectName("sales_day_field")

        self.sales_month_field = QtWidgets.QComboBox(self.Vendas)
        self.sales_month_field.setGeometry(QtCore.QRect(900, 114, 61, 41))
        self.sales_month_field.setEditable(True)
        self.sales_month_field.setFont(field_font)
        self.sales_month_field.setObjectName("sales_month_field")

        self.sales_year_field = QtWidgets.QComboBox(self.Vendas)
        self.sales_year_field.setGeometry(QtCore.QRect(960, 114, 81, 41))
        self.sales_year_field.setEditable(True)
        self.sales_year_field.setFont(field_font)
        self.sales_year_field.setObjectName("sales_year_field")

        for i in range(31, 0, -1):
            i = f'{i:02}'
            self.sales_day_field.addItem(i)
        self.sales_day_field.addItem('')
        for i in range(12, 0, -1):
            i = f'{i:02}'
            self.sales_month_field.addItem(i)
        self.sales_month_field.addItem('')
        for i in range(2030, 2017, -1):
            self.sales_year_field.addItem(str(i))
        self.sales_year_field.addItem('')

        date = datetime.today().strftime('%d-%m-%Y')
        d, m, y = int(date[:2]), int(date[3:5]), int(date[6:])

        self.sales_day_field.setCurrentIndex(31)
        self.sales_month_field.setCurrentIndex(12)
        self.sales_year_field.setCurrentIndex(13)

        self.sales_day_field.currentTextChanged.connect(self.search_month_sales)
        self.sales_month_field.currentTextChanged.connect(self.search_month_sales)
        self.sales_year_field.currentTextChanged.connect(self.search_month_sales)

        # self.sales_day_field.setCurrentText(str(d))
        # self.sales_month_field.setCurrentText(str(m))
        # self.sales_year_field.setCurrentText(str(y))

        self.sales_tableWidget = QtWidgets.QTableWidget(self.Vendas)
        self.sales_tableWidget.setEnabled(True)
        self.sales_tableWidget.setGeometry(QtCore.QRect(10, 180, 1031, 571))
        self.sales_tableWidget.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.sales_tableWidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.sales_tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.sales_tableWidget.setAlternatingRowColors(True)
        self.sales_tableWidget.setObjectName("sales_tableWidget")
        self.sales_tableWidget.setColumnCount(7)
        self.sales_tableWidget.setRowCount(0)

        item = QtWidgets.QTableWidgetItem()
        self.sales_tableWidget.setHorizontalHeaderItem(0, item)

        item = QtWidgets.QTableWidgetItem()
        self.sales_tableWidget.setHorizontalHeaderItem(1, item)

        item = QtWidgets.QTableWidgetItem()
        self.sales_tableWidget.setHorizontalHeaderItem(2, item)

        item = QtWidgets.QTableWidgetItem()
        self.sales_tableWidget.setHorizontalHeaderItem(3, item)

        item = QtWidgets.QTableWidgetItem()
        self.sales_tableWidget.setHorizontalHeaderItem(4, item)

        item = QtWidgets.QTableWidgetItem()
        self.sales_tableWidget.setHorizontalHeaderItem(5, item)

        item = QtWidgets.QTableWidgetItem()
        self.sales_tableWidget.setHorizontalHeaderItem(6, item)

        self.sales_tableWidget.horizontalHeader().setDefaultSectionSize(147)
        self.sales_tableWidget.horizontalHeader().setHighlightSections(True)

        self.tabWidget.addTab(self.Vendas, "")

    def retranslate_ui(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.add_button.setText(_translate("MainWindow", "Adicionar"))
        self.add_date_label.setText(_translate("MainWindow", "Data"))
        self.add_ba_label.setText(_translate("MainWindow", "Bairro*"))
        self.add_nu_label.setText(_translate("MainWindow", "Número*"))
        self.add_na_label.setText(_translate("MainWindow", "Nome*"))
        self.add_st_label.setText(_translate("MainWindow", "Rua*"))
        self.add_ph_label.setText(_translate("MainWindow", "Telefone"))
        self.add_re_label.setText(_translate("MainWindow", "Referência"))
        self.add_product_label.setText(_translate("MainWindow", "Produto*"))
        self.add_price_label.setText(_translate("MainWindow", "Preço*"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Adicionar), _translate("MainWindow", "Adicionar"))

        self.search_nu_label.setText(_translate("MainWindow", "Número"))
        self.search_date_label.setText(_translate("MainWindow", "Data"))
        # self.search_button.setText(_translate("MainWindow", "Buscar"))
        self.search_st_label.setText(_translate("MainWindow", "Rua"))
        self.search_na_label.setText(_translate("MainWindow", "Nome"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Rua"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Número"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Bairro"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Referência"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Telefone"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Data"))

        self.search_ph_label.setText(_translate("MainWindow", "Telefone"))
        self.search_ba_label.setText(_translate("MainWindow", "Bairro"))
        self.search_re_label.setText(_translate("MainWindow", "Referência"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Busca), _translate("MainWindow", "Clientes"))

        self.sales_date_label.setText(_translate("MainWindow", "Data"))
        self.sales_ba_label.setText(_translate("MainWindow", "Bairro"))
        self.sales_st_label.setText(_translate("MainWindow", "Rua"))
        self.sales_re_label.setText(_translate("MainWindow", "Referência"))
        self.sales_na_label.setText(_translate("MainWindow", "Nome"))
        self.sales_nu_label.setText(_translate("MainWindow", "Número"))
        item = self.sales_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.sales_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Rua"))
        item = self.sales_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Número"))
        item = self.sales_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Bairro"))
        item = self.sales_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Produto"))
        item = self.sales_tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Preço"))
        item = self.sales_tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Data"))
        self.sales_ph_label.setText(_translate("MainWindow", "Telefone"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Vendas), _translate("MainWindow", "Vendas"))

    def set_tab_order(self):
        self.main_window.setTabOrder(self.add_na_field, self.add_st_field)
        self.main_window.setTabOrder(self.add_st_field, self.add_ba_field)
        self.main_window.setTabOrder(self.add_ba_field, self.add_ph_field)
        self.main_window.setTabOrder(self.add_ph_field, self.add_product_field)
        self.main_window.setTabOrder(self.add_product_field, self.add_price_field)
        self.main_window.setTabOrder(self.add_ph_field, self.add_product_field)
        self.main_window.setTabOrder(self.add_product_field, self.add_price_field)
        self.main_window.setTabOrder(self.add_price_field, self.add_re_field)
        self.main_window.setTabOrder(self.add_re_field, self.add_nu_field)
        self.main_window.setTabOrder(self.add_nu_field, self.add_day_field)
        self.main_window.setTabOrder(self.add_day_field, self.add_month_field)
        self.main_window.setTabOrder(self.add_month_field, self.add_year_field)
        self.main_window.setTabOrder(self.add_year_field, self.add_button)
        self.main_window.setTabOrder(self.add_button, self.search_na_field)

        self.main_window.setTabOrder(self.search_na_field, self.search_st_field)
        self.main_window.setTabOrder(self.search_st_field, self.search_ba_field)
        self.main_window.setTabOrder(self.search_ba_field, self.search_ph_field)
        self.main_window.setTabOrder(self.search_ph_field, self.search_re_field)
        self.main_window.setTabOrder(self.search_re_field, self.search_nu_field)
        self.main_window.setTabOrder(self.search_nu_field, self.search_day_field)
        self.main_window.setTabOrder(self.search_day_field, self.search_month_field)
        self.main_window.setTabOrder(self.search_month_field, self.search_year_field)


        self.main_window.setTabOrder(self.sales_st_field, self.sales_ba_field)
        self.main_window.setTabOrder(self.sales_ba_field, self.sales_nu_field)

    def search_customers(self, button=False):
        rua = self.search_st_field.currentText()
        bairro = self.search_ba_field.currentText()
        nome = self.search_na_field.text()
        telefone = self.search_ph_field.text()
        referência = self.search_re_field.text()
        número = self.search_nu_field.text()

        d = self.search_day_field.currentText()
        m = self.search_month_field.currentText()
        y = self.search_year_field.currentText()
        data = f"{d}/{m}/{y}"

        search_results = dm.search_database(nome=nome, rua=rua, bairro=bairro, telefone=telefone,
                                            referencia=referência, número=número, data=data)

        results_found = self.create_customer_table(search_results)

    def create_customer_table(self, search_results):
        if type(search_results) == list:
            self.tableWidget.setRowCount(len(search_results))
            for row, each in enumerate(search_results):
                for i, field in enumerate(each):
                    item = QtWidgets.QTableWidgetItem()
                    self.tableWidget.setItem(row, i, item)
                    item = self.tableWidget.item(row, i)
                    item.setText(field)
        else:
            if search_results:
                self.tableWidget.setRowCount(1)
            else:
                self.tableWidget.setRowCount(0)
                return False
        return True

    def add_customer(self):
        self.add_st_field.currentText()
        bairro = self.add_ba_field.currentText()
        rua = self.add_st_field.currentText()
        produto = self.add_product_field.currentText()

        nome = self.add_na_field.text()
        telefone = self.add_ph_field.text()
        referência = self.add_re_field.text()
        número = self.add_nu_field.text()
        preço = self.add_price_field.text()

        d = self.add_day_field.currentText()
        m = self.add_month_field.currentText()
        y = self.add_year_field.currentText()
        data = f"{d}/{m}/{y}"


        msg = QMessageBox()
        msg.setWindowTitle('Alerta')
        msg.setText('Deseja cadastrar esta venda?')
        msg.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
        msg.button(msg.Yes).setText('Sim')
        msg.button(msg.No).setText('Não')
        msg.setIcon(QMessageBox.Question)
        msg.setDefaultButton(QMessageBox.Yes)
        self.add_customer_answer = None
        msg.buttonClicked.connect(self.add_customer_popup_clicked)
        x = msg.exec_()

        if self.add_customer_answer == 'Sim':
            r = dm.add_to_database(nome, rua, bairro, telefone, referência, número, data, produto=produto, preço=preço)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('Alerta')
            if r == 'Success':
                msg.setWindowTitle('Sucesso')
                msg.setText('Cliente adicionado com sucesso')
                x = msg.exec_()

                self.add_st_field.clearEditText()
                self.add_ba_field.clearEditText()
                self.add_product_field.clearEditText()

                self.add_na_field.setText('')
                self.add_nu_field.setText('')
                self.add_re_field.setText('')
                self.add_ph_field.setText('')
                self.add_price_field.setText('')

                self.search_st_field.setCurrentText(rua)
                self.search_ba_field.setCurrentText(bairro)
                self.search_na_field.setText(nome)
                self.search_nu_field.setText(número)
                self.search_re_field.setText(referência)
                self.search_ph_field.setText(telefone)

                self.tabWidget.setCurrentIndex(0)
                self.search_customers(button=False)
                self.search_month_sales()

            elif r == 'Fail':
                msg.setWindowTitle('Alerta')
                msg.setText('Por favor preencha os campos obrigatórios*')
                x = msg.exec_()
            elif r == 'existent customer':
                msg.setWindowTitle('Sucesso')
                msg.setText(f'Venda cadastrada para {nome} em {data}')

                x = msg.exec_()
                self.sales_na_field.setText(nome)
                self.sales_st_field.setCurrentText(rua)
                self.sales_nu_field.setText(número)
                self.sales_ba_field.setCurrentText(bairro)
                self.tabWidget.setCurrentIndex(1)
        else:
            pass

    def search_month_sales(self):
        d = self.sales_day_field.currentText()
        m = self.sales_month_field.currentText()
        y = self.sales_year_field.currentText()
        data = f'{d}/{m}/{y}'

        nome = self.sales_na_field.text()
        número = self.sales_nu_field.text()
        rua = self.sales_st_field.currentText()
        bairro = self.sales_ba_field.currentText()

        search_results = dm.search_month(nome=nome, número=número, rua=rua, bairro=bairro, data=data)
        self.create_sales_table(search_results)

    def create_sales_table(self, search_results):
        if type(search_results) == list:
            customers = []
            self.sales_tableWidget.setRowCount(len(customers))

            d = self.sales_day_field.currentText()
            m = self.sales_month_field.currentText()
            y = self.sales_year_field.currentText()
            data = f'{d}/{m}/{y}'

            for row, each in enumerate(search_results):
                nome, rua, número, bairro, _, _, _ = each
                customer_id = dm.get_customer_id(nome=nome, rua=rua, número=número, bairro=bairro)
                customer_data = dm.search_sales(customer_id=customer_id, date=data)
                if customer_data:
                    customers.append(customer_data)

                rowcount = sum([len(each) for each in customers])
                self.sales_tableWidget.setRowCount(rowcount)
            row = 0

            for each_customer in customers:
                for sale in each_customer:
                    for i, field in enumerate(sale):
                        # print(row, i, field)
                        item = QtWidgets.QTableWidgetItem()
                        self.sales_tableWidget.setItem(row, i, item)
                        item = self.sales_tableWidget.item(row, i)
                        item.setText(str(field))
                    row += 1
        else:
            if search_results:
                self.sales_tableWidget.setRowCount(1)
            else:
                self.sales_tableWidget.setRowCount(0)
                msg = QMessageBox()
                msg.setWindowTitle('Alerta')
                msg.setText('Nenhuma venda encontrada')
                msg.setIcon(QMessageBox.Warning)
                x = msg.exec_()

    def add_customer_popup_clicked(self, e):
        self.add_customer_answer = e.text()

    def delete_customer_popup_clicked(self, e):
        self.delete_customer_answer = e.text()

    def update_customer_popup_clicked(self, e):
        self.update_customer_answer = e.text()

    def populate_combo_boxes(self):
        bairros, ruas = dm.get_column_list()
        self.add_ba_field.addItems(bairros)
        self.add_st_field.addItems(ruas)
        self.search_ba_field.addItems(bairros)
        self.search_st_field.addItems(ruas)
        self.sales_ba_field.addItems(bairros)
        self.sales_st_field.addItems(ruas)

        self.add_ba_field.setCurrentText('')
        self.add_st_field.setCurrentText('')
        self.search_ba_field.setCurrentText('')
        self.search_st_field.setCurrentText('')
        self.sales_ba_field.setCurrentText('')
        self.sales_st_field.setCurrentText('')

        # self.search_day_field.setCurrentText('')
        # self.search_month_field.setCurrentText('')
        # self.search_year_field.setCurrentText('')
        # self.sales_day_field.setCurrentText('')
        # self.sales_month_field.setCurrentText('')
        # self.sales_year_field.setCurrentText('')

    def search_item_clicked(self, item):
        row = item.row()
        fields = [self.tableWidget.item(row, c).text() for c in range(7)]
        nome, rua, número, bairro, _, _, _ = fields
        client_id = dm.get_customer_id(nome=nome, rua=rua, número=número, bairro=bairro)

        self.item_clicked_dialog = QDialog()
        self.item_clicked_dialog.resize(380, 150)

        dialog_label_font = QtGui.QFont()
        dialog_label_font.setPointSize(14)
        self.dialog_label = QtWidgets.QLabel(self.item_clicked_dialog)
        self.dialog_label.setGeometry(QtCore.QRect(110, 30, 200, 28))
        self.dialog_label.setText('O que deseja fazer?')
        self.dialog_label.setFont(dialog_label_font)

        self.delete_button = QPushButton("Remover", self.item_clicked_dialog)
        self.delete_button.move(250, 80)
        self.delete_button.clicked.connect(lambda: self.delete_button_function(nome, rua, número, bairro))

        self.edit_button = QPushButton("Editar", self.item_clicked_dialog)
        self.edit_button.move(150, 80)
        self.edit_button.clicked.connect(lambda: self.edit_button_function(fields))

        self.new_sale = QPushButton("Add. Compra", self.item_clicked_dialog)
        self.new_sale.move(50, 80)
        self.new_sale.clicked.connect(lambda: self.new_sale_button_function(fields))

        self.item_clicked_dialog.setWindowTitle(f'{nome}, {rua} {número}')
        self.item_clicked_dialog.exec_()

    def new_sale_button_function(self, fields):
        nome, rua, número, bairro, _, _, _ = fields
        self.add_na_field.setText(nome)
        self.add_st_field.setCurrentText(rua)
        self.add_nu_field.setText(número)
        self.add_ba_field.setCurrentText(bairro)

        self.tabWidget.setCurrentIndex(2)
        self.item_clicked_dialog.close()

    def edit_button_function(self, fields):
        nome, rua, número, bairro, referência, telefone, data = fields
        client_id = dm.get_customer_id(nome=nome, rua=rua, bairro=bairro, número=número)

        # self.item_clicked_dialog.close()
        self.edit_dialog = QDialog()
        self.edit_dialog.resize(330, 270)
        self.edit_dialog.setWindowTitle("Atualizar Cadastro")

        self.edit_na_label = QtWidgets.QLabel(self.edit_dialog)
        self.edit_na_label.setGeometry(QtCore.QRect(20, 20, 61, 28))
        self.edit_na_label.setText('Nome:')
        self.edit_na_field = QtWidgets.QLineEdit(self.edit_dialog)
        self.edit_na_field.setGeometry(QtCore.QRect(100, 20, 200, 28))
        self.edit_na_field.setText(nome)

        self.edit_st_label = QtWidgets.QLabel(self.edit_dialog)
        self.edit_st_label.setGeometry(QtCore.QRect(20, 50, 61, 28))
        self.edit_st_label.setText('Rua:')
        self.edit_st_field = QtWidgets.QLineEdit(self.edit_dialog)
        self.edit_st_field.setGeometry(QtCore.QRect(100, 50, 200, 28))
        self.edit_st_field.setText(rua)

        self.edit_ba_label = QtWidgets.QLabel(self.edit_dialog)
        self.edit_ba_label.setGeometry(QtCore.QRect(20, 80, 61, 28))
        self.edit_ba_label.setText('Bairro:')
        self.edit_ba_field = QtWidgets.QLineEdit(self.edit_dialog)
        self.edit_ba_field.setGeometry(QtCore.QRect(100, 80, 200, 28))
        self.edit_ba_field.setText(bairro)

        self.edit_nu_label = QtWidgets.QLabel(self.edit_dialog)
        self.edit_nu_label.setGeometry(QtCore.QRect(20, 110, 61, 28))
        self.edit_nu_label.setText('Número:')
        self.edit_nu_field = QtWidgets.QLineEdit(self.edit_dialog)
        self.edit_nu_field.setGeometry(QtCore.QRect(100, 110, 200, 28))
        self.edit_nu_field.setText(número)

        self.edit_re_label = QtWidgets.QLabel(self.edit_dialog)
        self.edit_re_label.setGeometry(QtCore.QRect(20, 140, 70, 28))
        self.edit_re_label.setText('Referência:')
        self.edit_re_field = QtWidgets.QLineEdit(self.edit_dialog)
        self.edit_re_field.setGeometry(QtCore.QRect(100, 140, 200, 28))
        self.edit_re_field.setText(referência)

        self.edit_ph_label = QtWidgets.QLabel(self.edit_dialog)
        self.edit_ph_label.setGeometry(QtCore.QRect(20, 170, 61, 28))
        self.edit_ph_label.setText('Telefone:')
        self.edit_ph_field = QtWidgets.QLineEdit(self.edit_dialog)
        self.edit_ph_field.setGeometry(QtCore.QRect(100, 170, 200, 28))
        self.edit_ph_field.setText(telefone)
        # self.edit_name_field.setFont(field_font)

        self.add_button = QtWidgets.QPushButton(self.edit_dialog)
        self.add_button.setGeometry(QtCore.QRect(100, 210, 200, 28))
        self.add_button.setText("Atualizar")
        self.add_button.clicked.connect(lambda: self.update_button_function(client_id=client_id))

        self.edit_dialog.exec_()

    def update_button_function(self, client_id):
        msg = QMessageBox()
        msg.setWindowTitle('Alerta')
        msg.setText('Deseja atualizar esse cadastro?')
        msg.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
        msg.button(msg.Yes).setText('Sim')
        msg.button(msg.No).setText('Não')
        msg.setIcon(QMessageBox.Question)
        msg.setDefaultButton(QMessageBox.Yes)
        self.update_customer_answer = None
        msg.buttonClicked.connect(self.update_customer_popup_clicked)
        x = msg.exec_()

        if self.update_customer_answer == 'Sim':
            novo_nome = self.edit_na_field.text()
            nova_rua = self.edit_st_field.text()
            novo_número = self.edit_nu_field.text()
            novo_bairro = self.edit_ba_field.text()
            nova_referência = self.edit_re_field.text()
            novo_telefone = self.edit_ph_field.text()

            dm.update_customer(rowid=client_id, nome=novo_nome, rua=nova_rua, número=novo_número, bairro=novo_bairro,
                               referência=nova_referência, telefone=novo_telefone)

            msg = QMessageBox()
            msg.setWindowTitle('Sucesso')
            msg.setText('Cadastro atualizado com sucesso')
            x = msg.exec_()

            self.search_customers()
            self.search_month_sales()
            self.edit_dialog.close()
        else:
            pass

    def delete_button_function(self, nome, rua, número, bairro):
        rowid = dm.get_customer_id(nome=nome, rua=rua, número=número, bairro=bairro)

        msg = QMessageBox()
        msg.setWindowTitle('Alerta')
        msg.setText('Você tem certeza que deseja REMOVER esse cliente?')
        msg.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
        msg.button(msg.Yes).setText('Sim')
        msg.button(msg.No).setText('Não')
        msg.setIcon(QMessageBox.Question)
        msg.setDefaultButton(QMessageBox.No)

        self.delete_customer_answer = None
        msg.buttonClicked.connect(self.delete_customer_popup_clicked)

        x = msg.exec_()

        if self.delete_customer_answer == 'Sim':
            dm.delete_customer(rowid=rowid)
            self.search_customers()
            self.search_month_sales()

            msg = QMessageBox()
            msg.setWindowTitle('Alerta')
            msg.setText('Cliente removido com sucesso')
            msg.exec_()
            self.item_clicked_dialog.close()
