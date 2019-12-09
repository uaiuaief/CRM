from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import database_manager as dm


class UiMainWindow(object):
    def __init__(self, mainwindow):
        self.main_window = mainwindow
        self.main_window.setObjectName("MainWindow")
        self.main_window.resize(807, 661)
        self.main_window.setMaximumSize(807, 661)

        self.centralwidget = QtWidgets.QWidget(self.main_window)
        self.centralwidget.setObjectName("centralwidget")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 641))
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

        self.set_tab_order()

    def init_add_tab(self):
        self.Adicionar = QtWidgets.QWidget()
        self.Adicionar.setObjectName("Adicionar")

        self.add_button = QtWidgets.QPushButton(self.Adicionar)
        self.add_button.setGeometry(QtCore.QRect(10, 110, 181, 28))
        self.add_button.setObjectName("add_button")
        self.add_button.clicked.connect(self.add_customer)


        self.add_st_label = QtWidgets.QLabel(self.Adicionar)
        self.add_st_label.setGeometry(QtCore.QRect(210, 0, 33, 28))
        self.add_st_label.setObjectName("add_st_label")
        self.add_st_field = QtWidgets.QLineEdit(self.Adicionar)
        self.add_st_field.setGeometry(QtCore.QRect(210, 20, 181, 28))
        self.add_st_field.setText("")
        self.add_st_field.setObjectName("add_st_field")

        self.add_na_label = QtWidgets.QLabel(self.Adicionar)
        self.add_na_label.setGeometry(QtCore.QRect(10, 0, 46, 28))
        self.add_na_label.setObjectName("add_na_label")
        self.add_na_field = QtWidgets.QLineEdit(self.Adicionar)
        self.add_na_field.setGeometry(QtCore.QRect(10, 20, 181, 28))
        self.add_na_field.setText("")
        self.add_na_field.setObjectName("add_na_field")

        self.add_ba_label = QtWidgets.QLabel(self.Adicionar)
        self.add_ba_label.setGeometry(QtCore.QRect(610, 0, 41, 28))
        self.add_ba_label.setObjectName("add_ba_label")
        self.add_ba_field = QtWidgets.QLineEdit(self.Adicionar)
        self.add_ba_field.setGeometry(QtCore.QRect(610, 20, 181, 28))
        self.add_ba_field.setObjectName("add_ba_field")

        self.add_nu_label = QtWidgets.QLabel(self.Adicionar)
        self.add_nu_label.setGeometry(QtCore.QRect(410, 0, 101, 28))
        self.add_nu_label.setObjectName("add_nu_label")
        self.add_nu_field = QtWidgets.QLineEdit(self.Adicionar)
        self.add_nu_field.setGeometry(QtCore.QRect(410, 20, 181, 28))
        self.add_nu_field.setText("")
        self.add_nu_field.setObjectName("add_nu_field")

        self.add_re_label = QtWidgets.QLabel(self.Adicionar)
        self.add_re_label.setGeometry(QtCore.QRect(10, 50, 71, 28))
        self.add_re_label.setObjectName("add_re_label")
        self.add_re_field = QtWidgets.QLineEdit(self.Adicionar)
        self.add_re_field.setGeometry(QtCore.QRect(10, 70, 181, 28))
        self.add_re_field.setObjectName("add_re_field")

        self.add_ph_label = QtWidgets.QLabel(self.Adicionar)
        self.add_ph_label.setGeometry(QtCore.QRect(210, 50, 69, 28))
        self.add_ph_label.setObjectName("add_ph_label")
        self.add_ph_field = QtWidgets.QLineEdit(self.Adicionar)
        self.add_ph_field.setGeometry(QtCore.QRect(210, 70, 181, 28))
        self.add_ph_field.setObjectName("add_ph_field")

        self.add_product_label = QtWidgets.QLabel(self.Adicionar)
        self.add_product_label.setGeometry(QtCore.QRect(410, 50, 69, 28))
        self.add_product_label.setObjectName("add_product_label")
        self.add_product_field = QtWidgets.QLineEdit(self.Adicionar)
        self.add_product_field.setGeometry(QtCore.QRect(410, 70, 81, 28))
        self.add_product_field.setObjectName("add_product_field")

        self.add_price_label = QtWidgets.QLabel(self.Adicionar)
        self.add_price_label.setGeometry(QtCore.QRect(510, 50, 69, 28))
        self.add_price_label.setObjectName("add_price_label")
        self.add_price_field = QtWidgets.QLineEdit(self.Adicionar)
        self.add_price_field.setGeometry(QtCore.QRect(510, 70, 81, 28))
        self.add_price_field.setObjectName("add_price_field")

        self.add_date_label = QtWidgets.QLabel(self.Adicionar)
        self.add_date_label.setGeometry(QtCore.QRect(610, 50, 69, 28))
        self.add_date_label.setObjectName("add_date_label")
        self.add_dateEdit = QtWidgets.QDateEdit(self.Adicionar)
        self.add_dateEdit.setGeometry(QtCore.QRect(610, 70, 181, 28))
        self.add_dateEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.add_dateEdit.setMinimumDate(QtCore.QDate(1752, 9, 14))
        self.add_dateEdit.setMinimumTime(QtCore.QTime(0, 0, 0))
        self.add_dateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.add_dateEdit.setCalendarPopup(True)

        date = datetime.today().strftime('%d-%m-%Y')
        d, m, y = int(date[:2]), int(date[3:5]), int(date[6:])
        self.add_dateEdit.setDate(QtCore.QDate(y, m, d))
        self.add_dateEdit.setObjectName("add_dateEdit")



        self.tabWidget.addTab(self.Adicionar, "")

    def init_search_tab(self):
        self.Busca = QtWidgets.QWidget()
        self.Busca.setObjectName("Clientes")

        self.search_nu_label = QtWidgets.QLabel(self.Busca)
        self.search_nu_label.setGeometry(QtCore.QRect(550, 50, 51, 28))
        self.search_nu_label.setObjectName("search_nu_label")
        self.search_nu_field = QtWidgets.QLineEdit(self.Busca)
        self.search_nu_field.setGeometry(QtCore.QRect(550, 70, 101, 28))
        self.search_nu_field.setText("")
        self.search_nu_field.setObjectName("search_nu_field")
        self.search_nu_field.textChanged.connect(lambda: self.search_customers(button=False))

        self.search_st_label = QtWidgets.QLabel(self.Busca)
        self.search_st_label.setGeometry(QtCore.QRect(280, 0, 23, 28))
        self.search_st_label.setObjectName("search_st_label")
        self.search_st_field = QtWidgets.QLineEdit(self.Busca)
        self.search_st_field.setGeometry(QtCore.QRect(280, 20, 241, 28))
        self.search_st_field.setText("")
        self.search_st_field.setObjectName("search_st_field")
        self.search_st_field.textChanged.connect(lambda: self.search_customers(button=False))

        self.search_na_label = QtWidgets.QLabel(self.Busca)
        self.search_na_label.setGeometry(QtCore.QRect(10, 0, 36, 28))
        self.search_na_label.setObjectName("search_na_label")
        self.search_na_field = QtWidgets.QLineEdit(self.Busca)
        self.search_na_field.setGeometry(QtCore.QRect(10, 20, 241, 28))
        self.search_na_field.setText("")
        self.search_na_field.setObjectName("search_na_field")
        self.search_na_field.textChanged.connect(lambda: self.search_customers(button=False))

        self.search_ba_label = QtWidgets.QLabel(self.Busca)
        self.search_ba_label.setGeometry(QtCore.QRect(550, 0, 41, 28))
        self.search_ba_label.setObjectName("search_ba_label")
        self.search_ba_field = QtWidgets.QLineEdit(self.Busca)
        self.search_ba_field.setGeometry(QtCore.QRect(550, 20, 241, 28))
        self.search_ba_field.setObjectName("search_ba_field")
        self.search_ba_field.textChanged.connect(lambda: self.search_customers(button=False))

        self.search_ph_label = QtWidgets.QLabel(self.Busca)
        self.search_ph_label.setGeometry(QtCore.QRect(10, 50, 69, 28))
        self.search_ph_label.setObjectName("search_ph_label")
        self.search_ph_field = QtWidgets.QLineEdit(self.Busca)
        self.search_ph_field.setGeometry(QtCore.QRect(10, 70, 241, 28))
        self.search_ph_field.setObjectName("search_ph_field")
        self.search_ph_field.textChanged.connect(lambda: self.search_customers(button=False))

        self.search_re_label = QtWidgets.QLabel(self.Busca)
        self.search_re_label.setGeometry(QtCore.QRect(280, 50, 71, 28))
        self.search_re_label.setObjectName("search_re_label")
        self.search_re_field = QtWidgets.QLineEdit(self.Busca)
        self.search_re_field.setGeometry(QtCore.QRect(280, 70, 241, 28))
        self.search_re_field.setObjectName("search_re_field")
        self.search_re_field.textChanged.connect(lambda: self.search_customers(button=False))

        self.search_button = QtWidgets.QPushButton(self.Busca)
        self.search_button.setGeometry(QtCore.QRect(10, 110, 241, 28))
        self.search_button.setObjectName("search_button")
        self.search_button.clicked.connect(lambda: self.search_customers(button=True))

        self.tableWidget = QtWidgets.QTableWidget(self.Busca)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(10, 150, 781, 461))
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

        self.tableWidget.horizontalHeader().setDefaultSectionSize(111)
        self.tableWidget.horizontalHeader().setHighlightSections(True)

        self.search_checkBox = QtWidgets.QCheckBox(self.Busca)
        self.search_checkBox.setGeometry(QtCore.QRect(682, 100, 150, 26))
        self.search_checkBox.setObjectName("search_checkBox")

        self.search_date_label = QtWidgets.QLabel(self.Busca)
        self.search_date_label.setGeometry(QtCore.QRect(680, 50, 69, 28))
        self.search_date_label.setObjectName("search_date_label")
        self.search_dateEdit = QtWidgets.QDateEdit(self.Busca)
        self.search_dateEdit.setGeometry(QtCore.QRect(680, 70, 111, 26))
        self.search_dateEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.search_dateEdit.setMinimumDate(QtCore.QDate(1752, 9, 14))
        self.search_dateEdit.setMinimumTime(QtCore.QTime(0, 0, 0))
        self.search_dateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.search_dateEdit.setCalendarPopup(True)
        self.search_use_date = False
        self.search_dateEdit.dateChanged.connect(lambda: self.search_customers(button=False))

        date = datetime.today().strftime('%d-%m-%Y')
        d, m, y = int(date[:2]), int(date[3:5]), int(date[6:])
        self.search_dateEdit.setDate(QtCore.QDate(y, m, d))
        self.search_dateEdit.setObjectName("search_dateEdit")

        self.tabWidget.addTab(self.Busca, "")

    def init_sales_tab(self):
        self.Vendas = QtWidgets.QWidget()
        self.Vendas.setObjectName("Vendas")

        self.sales_re_label = QtWidgets.QLabel(self.Vendas)
        self.sales_re_label.setGeometry(QtCore.QRect(280, 50, 71, 28))
        self.sales_re_label.setObjectName("sales_re_label")
        self.sales_re_field = QtWidgets.QLineEdit(self.Vendas)
        self.sales_re_field.setEnabled(False)
        self.sales_re_field.setGeometry(QtCore.QRect(280, 70, 241, 28))
        self.sales_re_field.setObjectName("sales_re_field")

        self.sales_ba_label = QtWidgets.QLabel(self.Vendas)
        self.sales_ba_label.setGeometry(QtCore.QRect(550, 0, 41, 28))
        self.sales_ba_label.setObjectName("sales_ba_label")
        self.sales_ba_field = QtWidgets.QLineEdit(self.Vendas)
        self.sales_ba_field.setGeometry(QtCore.QRect(550, 20, 241, 28))
        self.sales_ba_field.setObjectName("sales_ba_field")
        self.sales_ba_field.textChanged.connect(self.search_month_sales)

        self.sales_checkBox = QtWidgets.QCheckBox(self.Vendas)
        self.sales_checkBox.setGeometry(QtCore.QRect(682, 100, 150, 26))
        self.sales_checkBox.setObjectName("sales_checkBox")

        self.sales_date_label = QtWidgets.QLabel(self.Vendas)
        self.sales_date_label.setGeometry(QtCore.QRect(680, 50, 69, 28))
        self.sales_date_label.setObjectName("sales_date_label")
        self.sales_dateEdit = QtWidgets.QDateEdit(self.Vendas)
        self.sales_dateEdit.setGeometry(QtCore.QRect(680, 70, 111, 26))
        self.sales_dateEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.sales_dateEdit.setMinimumDate(QtCore.QDate(1752, 9, 14))
        self.sales_dateEdit.setMinimumTime(QtCore.QTime(0, 0, 0))
        self.sales_dateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.MonthSection)
        self.sales_use_date = False
        # self.sales_dateEdit.setCalendarPopup(True)

        date = datetime.today().strftime('%d-%m-%Y')
        d, m, y = int(date[:2]), int(date[3:5]), int(date[6:])
        self.sales_dateEdit.setDate(QtCore.QDate(y, m, d))
        self.sales_dateEdit.setObjectName("sales_dateEdit")
        self.sales_dateEdit.dateChanged.connect(self.search_month_sales)

        self.sales_nu_label = QtWidgets.QLabel(self.Vendas)
        self.sales_nu_label.setGeometry(QtCore.QRect(550, 50, 51, 28))
        self.sales_nu_label.setObjectName("sales_nu_label")
        self.sales_nu_field = QtWidgets.QLineEdit(self.Vendas)
        self.sales_nu_field.setEnabled(True)
        self.sales_nu_field.setGeometry(QtCore.QRect(550, 70, 101, 28))
        self.sales_nu_field.setText("")
        self.sales_nu_field.setObjectName("sales_nu_field")
        self.sales_nu_field.textChanged.connect(self.search_month_sales)

        self.sales_na_label = QtWidgets.QLabel(self.Vendas)
        self.sales_na_label.setGeometry(QtCore.QRect(10, 0, 36, 28))
        self.sales_na_label.setObjectName("sales_na_label")
        self.sales_na_field = QtWidgets.QLineEdit(self.Vendas)
        self.sales_na_field.setEnabled(True)
        self.sales_na_field.setGeometry(QtCore.QRect(10, 20, 241, 28))
        self.sales_na_field.setText("")
        self.sales_na_field.setObjectName("sales_na_field")
        self.sales_na_field.textChanged.connect(self.search_month_sales)

        self.sales_ph_label = QtWidgets.QLabel(self.Vendas)
        self.sales_ph_label.setGeometry(QtCore.QRect(10, 50, 69, 28))
        self.sales_ph_label.setObjectName("sales_ph_label")
        self.sales_ph_field = QtWidgets.QLineEdit(self.Vendas)
        self.sales_ph_field.setEnabled(False)
        self.sales_ph_field.setGeometry(QtCore.QRect(10, 70, 241, 28))
        self.sales_ph_field.setReadOnly(True)
        self.sales_ph_field.setObjectName("sales_ph_field")

        self.sales_st_label = QtWidgets.QLabel(self.Vendas)
        self.sales_st_label.setGeometry(QtCore.QRect(280, 0, 23, 28))
        self.sales_st_label.setObjectName("sales_st_label")
        self.sales_st_field = QtWidgets.QLineEdit(self.Vendas)
        self.sales_st_field.setEnabled(True)
        self.sales_st_field.setGeometry(QtCore.QRect(280, 20, 241, 28))
        self.sales_st_field.setText("")
        self.sales_st_field.setObjectName("sales_st_field")
        self.sales_st_field.textChanged.connect(self.search_month_sales)

        self.sales_button = QtWidgets.QPushButton(self.Vendas)
        self.sales_button.setGeometry(QtCore.QRect(10, 110, 241, 28))
        self.sales_button.setObjectName("sales_button")
        self.sales_button.clicked.connect(self.search_month_sales)

        self.sales_tableWidget = QtWidgets.QTableWidget(self.Vendas)
        self.sales_tableWidget.setEnabled(True)
        self.sales_tableWidget.setGeometry(QtCore.QRect(10, 150, 781, 461))
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

        self.sales_tableWidget.horizontalHeader().setDefaultSectionSize(111)
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
        self.add_dateEdit.setDisplayFormat(_translate("MainWindow", "dd/MM/yyyy"))
        self.add_re_label.setText(_translate("MainWindow", "Referência"))
        self.add_product_label.setText(_translate("MainWindow", "Produto*"))
        self.add_price_label.setText(_translate("MainWindow", "Preço*"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Adicionar), _translate("MainWindow", "Adicionar"))

        self.search_nu_label.setText(_translate("MainWindow", "Número"))
        self.search_date_label.setText(_translate("MainWindow", "Data"))
        self.search_button.setText(_translate("MainWindow", "Buscar"))
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
        self.search_dateEdit.setDisplayFormat(_translate("MainWindow", "dd/MM/yyyy"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Busca), _translate("MainWindow", "Clientes"))

        self.search_checkBox.setText(_translate("Form", "Usar data"))
        self.search_checkBox.clicked.connect(self.search_checkbox_clicked)
        self.search_dateEdit.setEnabled(False)

        self.sales_checkBox.setText(_translate("Form", "Usar data"))
        self.sales_checkBox.clicked.connect(self.sales_checkbox_clicked)
        self.sales_dateEdit.setEnabled(False)

        self.sales_date_label.setText(_translate("MainWindow", "Data"))
        self.sales_ba_label.setText(_translate("MainWindow", "Bairro"))
        self.sales_st_label.setText(_translate("MainWindow", "Rua"))
        self.sales_re_label.setText(_translate("MainWindow", "Referência"))
        self.sales_button.setText(_translate("MainWindow", "Buscar"))
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
        self.sales_dateEdit.setDisplayFormat(_translate("MainWindow", "MM/yyyy"))
        self.sales_ph_label.setText(_translate("MainWindow", "Telefone"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Vendas), _translate("MainWindow", "Vendas"))

    def set_tab_order(self):
        self.main_window.setTabOrder(self.add_na_field, self.add_st_field)
        self.main_window.setTabOrder(self.add_st_field, self.add_nu_field)
        self.main_window.setTabOrder(self.add_nu_field, self.add_ba_field)
        self.main_window.setTabOrder(self.add_ba_field, self.add_re_field)
        self.main_window.setTabOrder(self.add_re_field, self.add_ph_field)
        self.main_window.setTabOrder(self.add_ph_field, self.add_product_field)
        self.main_window.setTabOrder(self.add_product_field, self.add_price_field)
        self.main_window.setTabOrder(self.add_price_field, self.add_dateEdit)
        self.main_window.setTabOrder(self.add_dateEdit, self.add_button)
        self.main_window.setTabOrder(self.add_button, self.search_na_field)

        self.main_window.setTabOrder(self.search_na_field, self.search_st_field)
        self.main_window.setTabOrder(self.search_st_field, self.search_ba_field)
        self.main_window.setTabOrder(self.search_ba_field, self.search_ph_field)
        self.main_window.setTabOrder(self.search_ph_field, self.search_re_field)
        self.main_window.setTabOrder(self.search_re_field, self.search_nu_field)
        self.main_window.setTabOrder(self.search_nu_field, self.search_dateEdit)
        self.main_window.setTabOrder(self.search_dateEdit, self.search_button)
        self.main_window.setTabOrder(self.search_button, self.tableWidget)
        self.main_window.setTabOrder(self.sales_st_field, self.sales_ba_field)
        self.main_window.setTabOrder(self.sales_ba_field, self.sales_nu_field)
        self.main_window.setTabOrder(self.sales_nu_field, self.sales_dateEdit)

    def search_customers(self, button=False):
        nome = self.search_na_field.text()
        rua = self.search_st_field.text()
        bairro = self.search_ba_field.text()
        telefone = self.search_ph_field.text()
        referência = self.search_re_field.text()
        número = self.search_nu_field.text()

        if self.search_use_date:
            data = self.search_dateEdit.text()
        else:
            data = ''

        search_results = dm.search_database(nome=nome, rua=rua, bairro=bairro, telefone=telefone,
                                            referencia=referência, número=número, data=data)

        results_found = self.create_customer_table(search_results)

        if not results_found and button:
            msg = QMessageBox()
            msg.setWindowTitle('Alerta')
            msg.setText('Nenhum cliente encontrado')
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()

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
        nome = self.add_na_field.text()
        rua = self.add_st_field.text()
        bairro = self.add_ba_field.text()
        telefone = self.add_ph_field.text()
        referência = self.add_re_field.text()
        número = self.add_nu_field.text()
        produto = self.add_product_field.text()
        preço = self.add_price_field.text()
        data = self.add_dateEdit.text()

        msg = QMessageBox()
        msg.setWindowTitle('Alerta')
        msg.setText('Você tem certeza que quer adicionar esse cliente?')
        msg.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
        msg.setIcon(QMessageBox.Question)
        msg.setDefaultButton(QMessageBox.Yes)
        self.answer = None
        msg.buttonClicked.connect(self.popup_clicked)
        x = msg.exec_()

        if self.answer == '&Yes':
            r = dm.add_to_database(nome, rua, bairro, telefone, referência, número, data, produto=produto, preço=preço)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('Alerta')
            if r == 'Success':
                msg.setWindowTitle('Sucesso')
                msg.setText('Cliente adicionado com sucesso')
                x = msg.exec_()

                self.add_na_field.setText('')
                self.add_ba_field.setText('')
                self.add_nu_field.setText('')
                self.add_st_field.setText('')
                self.add_re_field.setText('')
                self.add_ph_field.setText('')
                self.add_product_field.setText('')
                self.add_price_field.setText('')

                self.search_na_field.setText(nome)
                self.search_ba_field.setText(bairro)
                self.search_nu_field.setText(número)
                self.search_st_field.setText(rua)
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
        else:
            pass

    def search_month_sales(self):
        data = self.sales_dateEdit.text()
        nome = self.sales_na_field.text()
        número = self.sales_nu_field.text()
        rua = self.sales_st_field.text()
        bairro = self.sales_ba_field.text()

        search_results = dm.search_month(nome=nome, número=número, rua=rua, bairro=bairro, data=data)
        self.create_sales_table(search_results)

    def create_sales_table(self, search_results):
        if type(search_results) == list:
            customers = []
            self.sales_tableWidget.setRowCount(len(customers))
            for row, each in enumerate(search_results):
                nome, rua, número, bairro, _, _, _ = each

                if self.sales_use_date:
                    data = self.sales_dateEdit.text()
                else:
                    data = ''
                # data = self.sales_dateEdit.text()

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

    def popup_clicked(self, e):
        self.answer = e.text()
        # print(e.text())

    def search_checkbox_clicked(self):
        if self.search_checkBox.isChecked():
            self.search_use_date = True
            self.search_dateEdit.setEnabled(True)
        elif not self.search_checkBox.isChecked():
            self.search_use_date = False
            self.search_dateEdit.setEnabled(False)
        self.search_customers()

    def sales_checkbox_clicked(self):
        if self.sales_checkBox.isChecked():
            self.sales_use_date = True
            self.sales_dateEdit.setEnabled(True)
        elif not self.sales_checkBox.isChecked():
            self.sales_use_date = False
            self.sales_dateEdit.setEnabled(False)
        self.search_month_sales()

    def search_item_clicked(self, item):
        row = item.row()
        fields = [self.tableWidget.item(row, c).text() for c in range(7)]
        nome, rua, número, bairro, _, _, _ = fields

        self.sales_na_field.setText(nome)
        self.sales_ba_field.setText(bairro)
        self.sales_nu_field.setText(número)
        self.sales_st_field.setText(rua)

        self.tabWidget.setCurrentIndex(1)
