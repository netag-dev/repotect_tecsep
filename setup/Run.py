from PyQt5 import QtWidgets
from modulo_home import splash















if __name__ == "__main__":
    import sys
    
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = splash.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())