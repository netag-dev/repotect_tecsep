from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from modulo_home import login

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(846, 536)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint) # Configurando as flags da janela
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, -50, 851, 561))
        self.pushButton.setAutoFillBackground(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./img/splash-tecpro2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(3000, 1000))
        self.pushButton.setObjectName("pushButton")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(190, 390, 491, 31))
        
        self.countdown_time = 0  # Contar em segundos.
        self.timer = QtCore.QTimer(self.centralwidget)
        
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setStyleSheet("""
        QProgressBar{
            color:white;
        }
        """)
        self.label = QtWidgets.QPushButton(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(800, 20, 31, 41))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                         "font: 24pt \"MS Shell Dlg 2\";\n"
                         "background-color: rgba(0, 0, 0, 0);")

        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 846, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
        self.timer.start(100)  # Intervalo de tempo em milissegundos (por exemplo, 100ms)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.progressBar.setFormat(_translate("MainWindow", "%v%/%m%"))
        self.label.setText(_translate("MainWindow", "X"))
        self.label.clicked.connect(lambda:close())

        self.timer.timeout.connect(lambda:update_progress_bar())

        def close():
            MainWindow.close()
    
        def update_progress_bar():
            self.countdown_time += 1
            self.progressBar.setValue(self.countdown_time)
            if self.countdown_time >= 1:
                open_next_window()
                self.timer.stop()
                MainWindow.close()

        def open_next_window():
            
            MainWindow = QtWidgets.QMainWindow()
            ui = login.Ui_MainWindow()
            ui.setupUi(MainWindow)
            MainWindow.show()
            
        
        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
