from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit, QMessageBox,QDesktopWidget
import res
from . import loginController

class Ui_MainWindow(object):




    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1400, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1400, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1400, 800))

        desktop = QDesktopWidget()
        screenRect = desktop.screenGeometry()
        windowRect = MainWindow.geometry()

        x = (screenRect.width() - windowRect.width()) // 2
        y = (screenRect.height() - windowRect.height()) // 2

        # Define a posição da janela
        MainWindow.move(x, y) 

        font = QtGui.QFont("Corbel")

        
        font.setFamily("Corbel")
        MainWindow.setFont(font)
        MainWindow.setIconSize(QtCore.QSize(40, 40))
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1400, 800))
        self.widget.setMinimumSize(QtCore.QSize(1400, 800))
        self.widget.setMaximumSize(QtCore.QSize(1400, 800))
        self.widget.setStyleSheet("\n" "\n" "QWidget#widget{\n" "\n" "background: url(:/img/bg.jpg);\n" "\n" "}\n" "\n" "*{\n" "    font-family:arial\n" "}\n" "")
        self.widget.setObjectName("widget")

        


        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(470, 180, 451, 501))
        self.widget_2.setStyleSheet("border-radius: 20px;\n" "background-color: rgba(0, 0, 0, 0.6078431373);\n" "")
        self.widget_2.setObjectName("widget_2")

        self.lbl_informacao = QtWidgets.QLabel(self.widget_2)
        self.lbl_informacao.setGeometry(QtCore.QRect(190, 120, 181, 61))
        self.lbl_informacao.setAutoFillBackground(False)
        self.lbl_informacao.setStyleSheet("color: white;\n" "font-weight: bolder;\n" "background:none;\n" "font-size:22px;")
        self.lbl_informacao.setScaledContents(False)
        self.lbl_informacao.setWordWrap(False)
        self.lbl_informacao.setOpenExternalLinks(False)
        self.lbl_informacao.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.lbl_informacao.setObjectName("lbl_informacao")

        self.lbl_email = QtWidgets.QLabel(self.widget_2)
        self.lbl_email.setGeometry(QtCore.QRect(50, 180, 121, 31))
        self.lbl_email.setAutoFillBackground(False)
        self.lbl_email.setStyleSheet("background:none;\n" "color: white;\n" "font-weight: bolder;\n" "font-size:18px\n" "")
        self.lbl_email.setScaledContents(False)
        self.lbl_email.setWordWrap(False)
        self.lbl_email.setOpenExternalLinks(False)
        self.lbl_email.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.lbl_email.setObjectName("lbl_email")

        self.lbl_password = QtWidgets.QLabel(self.widget_2)
        self.lbl_password.setGeometry(QtCore.QRect(50, 280, 81, 41))
        self.lbl_password.setAutoFillBackground(False)
        self.lbl_password.setStyleSheet("background-color: none;\n" "color: white;\n" "font-weight: bolder;\n" "font-size:18px")
        self.lbl_password.setScaledContents(False)
        self.lbl_password.setWordWrap(False)
        self.lbl_password.setOpenExternalLinks(False)
        self.lbl_password.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.lbl_password.setObjectName("lbl_password")

        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setGeometry(QtCore.QRect(40, 400, 371, 41))
        self.pushButton.setStyleSheet("QPushButton#pushButton{\n" "  border-radius: 12px;\n" "  background-color: #00a85d;\n" "  border: none;\n" "  transition: 0.3s;\n" "  color: #fff;\n" "  font-size:18px;\n" "}\n" "\n" "QPushButton#pushButton:hover{\n" "border-radius: 12px;\n" "  background-color: #044e42;\n" "  border: none;\n" "  transition: 0.3s;\n" "\n" "\n" "}")
        self.pushButton.setObjectName("pushButton")
        

        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(80, -30, 271, 211))
        self.label_4.setStyleSheet("image: url(:/img/logo_tecsep-1-removebg-preview.png);\n" "background:none;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")

        self.txt_email = QtWidgets.QLineEdit(self.widget_2)
        self.txt_email.setGeometry(QtCore.QRect(40, 220, 361, 41))
        self.txt_email.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.txt_email.setStyleSheet("background-color: #fff;\n" "font-size:18px;\n" "\n" "\n" "  ")
        self.txt_email.setText("")
        self.txt_email.setObjectName("txt_email")

        self.txt_password = QtWidgets.QLineEdit(self.widget_2)
        self.txt_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_password.setGeometry(QtCore.QRect(40, 320, 361, 41))
        self.txt_password.setStyleSheet("background-color: #fff;\n font-size:18px;" "")
        self.txt_password.setObjectName("txt_password")
        
        self.checkBox = QtWidgets.QCheckBox(self.widget_2)
        self.checkBox.stateChanged.connect(self.toggle_password_echo_mode)
        self.checkBox.setGeometry(QtCore.QRect(50, 370, 151, 20))
        self.checkBox.setStyleSheet("background:none;\n" "color:white;")
        self.checkBox.setObjectName("checkBox_show_password")
        
        self.label_4.raise_()
        self.lbl_informacao.raise_()
        self.lbl_email.raise_()
        self.lbl_password.raise_()
        self.pushButton.raise_()
        self.txt_email.raise_()
        self.txt_password.raise_()
        self.checkBox.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1400, 43))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.lbl_informacao.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Login </span></p></body></html>"))
        self.lbl_email.setText(_translate("MainWindow", "<html><head/><body><p>Email Adress</p></body></html>"))
        self.lbl_password.setText(_translate("MainWindow", "<html><head/><body><p>Password</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.pushButton.clicked.connect(lambda: openWindow())
        self.checkBox.setText(_translate("MainWindow", "Show Password"))

        #Funcção Para Abrir A Dashboard 
        def openWindow():
            lg = loginController.carregar_login(self.txt_email.text(),self.txt_password.text())
            user_logado = self.txt_email.text()
            if(lg == 0):
                print("Entrou")
                self.window = QtWidgets.QMainWindow()
                from . import dashboard
                self.ui = dashboard.Ui_dashboard_ui()
                self.ui.setupUi(self.window,user_logado)
                self.window.show()
                MainWindow.close()
            elif(lg == -1):
                msg_error = QMessageBox()
                msg_error.setIcon(QMessageBox.Critical)
                msg_error.setText('The email entered is incorrect, try agin')
                msg_error.setWindowTitle('Email Error')
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("../img/error_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                msg_error.setWindowIcon(icon)
                msg_error.exec_()
            elif(lg == -2):
                msg_error = QMessageBox()
                msg_error.setIcon(QMessageBox.Critical)
                msg_error.setText('The password entered is incorrect, try agin')
                msg_error.setWindowTitle('Password Error')
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("../img/error_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                msg_error.setWindowIcon(icon)
                msg_error.exec_()
            #else:
            #    print("N Entrou")
            #loginController.LoginController.fazer_login("a","b",self.txt_email.text(),self.txt_password.text())
            """
            if self.txt_email.text() == "admin":
                if self.txt_password.text() == "123":
                    self.window = QtWidgets.QMainWindow()
                    import dashboard
                    self.ui = dashboard.Ui_dashboard_ui()
                    self.ui.setupUi(self.window)
                    self.window.show()
                    MainWindow.close()
                else:
                    msg_error = QMessageBox()
                    msg_error.setIcon(QMessageBox.Critical)
                    msg_error.setText('The password entered is incorrect, try agin')
                    msg_error.setWindowTitle('Password Error')
                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap("../img/error_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    msg_error.setWindowIcon(icon)
                    msg_error.exec_()
            
            else:
                msg_error = QMessageBox()
                msg_error.setIcon(QMessageBox.Critical)
                msg_error.setText('The enail entered is incorrect, try agin')
                msg_error.setWindowTitle('Email Error')
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("../img/error_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                msg_error.setWindowIcon(icon)
                msg_error.exec_()
            """

    def toggle_password_echo_mode(self, state):
        if state == 2:  
            self.txt_password.setEchoMode(QLineEdit.Normal)
        else:
            self.txt_password.setEchoMode(QLineEdit.Password)

    
    
    

        
    

if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

