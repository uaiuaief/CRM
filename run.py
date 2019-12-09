import sys
from PyQt5 import QtWidgets
from interface import UiMainWindow
import database_manager

if __name__ == "__main__":
    database_manager.initialize_database()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
