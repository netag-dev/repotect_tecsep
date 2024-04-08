from PyQt5 import QtCore, QtGui, QtWidgets
import compliance.pack_physical_person.physicalController

class Ui_MainWindow(object):
    def setupUi(self, MainWindow,user_logado):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 350)
        MainWindow.setMinimumSize(QtCore.QSize(700, 350))
        MainWindow.setMaximumSize(QtCore.QSize(700, 350))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1050, 861))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(1050, 861))
        self.frame.setMaximumSize(QtCore.QSize(1050, 861))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.frame.setFont(font)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color:#eff2f9;\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 1201, 51))
        self.frame_2.setStyleSheet("background-color:#fff")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.img_user_logado = QtWidgets.QPushButton(self.frame_2)
        self.img_user_logado.setGeometry(QtCore.QRect(980, 10, 31, 31))
        self.img_user_logado.setStyleSheet("background-color: #fff;\n"
"border-radius:30px;\n"
"width:30px;\n"
"height:30px;")
        self.img_user_logado.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\../../../../../.designer/backup/user_dark.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.img_user_logado.setIcon(icon)
        self.img_user_logado.setIconSize(QtCore.QSize(25, 25))
        self.img_user_logado.setObjectName("img_user_logado")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(0, 20, 1201, 71))
        self.frame_3.setStyleSheet("background-color:#2d6b56;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.lbl_form_tittle = QtWidgets.QLabel(self.frame_3)
        self.lbl_form_tittle.setGeometry(QtCore.QRect(40, 0, 421, 41))
        self.lbl_form_tittle.setStyleSheet("font-size: 30px;\n"
"color:#fff;")
        self.lbl_form_tittle.setObjectName("lbl_form_tittle")
        self.line = QtWidgets.QFrame(self.frame_3)
        self.line.setGeometry(QtCore.QRect(-10, 0, 21, 151))
        self.line.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.lbl_form_text = QtWidgets.QLabel(self.frame_3)
        self.lbl_form_text.setGeometry(QtCore.QRect(40, 40, 511, 21))
        self.lbl_form_text.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 9pt \"MS Shell Dlg 2\";")
        self.lbl_form_text.setObjectName("lbl_form_text")
        self.frame_9 = QtWidgets.QFrame(self.frame)
        self.frame_9.setGeometry(QtCore.QRect(-1, 830, 1151, 31))
        self.frame_9.setStyleSheet("background-color:#2d6b56;")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(-40, 750, 41, 151))
        self.line_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.lbl_nome = QtWidgets.QLabel(self.frame)
        self.lbl_nome.setGeometry(QtCore.QRect(10, 120, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_nome.setFont(font)
        self.lbl_nome.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_nome.setObjectName("lbl_nome")
        self.txt_nome = QtWidgets.QLineEdit(self.frame)
        self.txt_nome.setGeometry(QtCore.QRect(10, 150, 321, 41))
        self.txt_nome.setStyleSheet("QLineEdit{\n"
"\n"
"\n"
"background-color:#fff;\n"
"border: 1px solid #8ec0af;\n"
"border-radius: 6px\n"
"}")
        
        
                
        
        self.txt_nome.setObjectName("txt_nome")
        self.txt_email = QtWidgets.QLineEdit(self.frame)
        self.txt_email.setGeometry(QtCore.QRect(350, 150, 321, 41))
        self.txt_email.setStyleSheet("QLineEdit{\n"
"\n"
"\n"
"background-color:#fff;\n"
"border: 1px solid #8ec0af;\n"
"border-radius: 6px\n"
"}")
        self.txt_email.setObjectName("txt_email")
        self.lbl_email = QtWidgets.QLabel(self.frame)
        self.lbl_email.setGeometry(QtCore.QRect(350, 120, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_email.setFont(font)
        self.lbl_email.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_email.setObjectName("lbl_email")
        self.txt_senha = QtWidgets.QLineEdit(self.frame)
        self.txt_senha.setGeometry(QtCore.QRect(10, 240, 321, 41))
        self.txt_senha.setStyleSheet("QLineEdit{\n"
"\n"
"\n"
"background-color:#fff;\n"
"border: 1px solid #8ec0af;\n"
"border-radius: 6px\n"
"}")
        self.txt_senha.setObjectName("txt_senha")
        self.lbl_senha = QtWidgets.QLabel(self.frame)
        self.lbl_senha.setGeometry(QtCore.QRect(10, 210, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_senha.setFont(font)
        self.lbl_senha.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_senha.setObjectName("lbl_senha")
        self.lbl_nivel_acesso = QtWidgets.QLabel(self.frame)
        self.lbl_nivel_acesso.setGeometry(QtCore.QRect(350, 210, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_nivel_acesso.setFont(font)
        self.lbl_nivel_acesso.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_nivel_acesso.setObjectName("lbl_nivel_acesso")
        self.txt_nivel_acesso = QtWidgets.QLineEdit(self.frame)
        self.txt_nivel_acesso.setGeometry(QtCore.QRect(350, 240, 321, 41))
        self.txt_nivel_acesso.setStyleSheet("QLineEdit{\n"
"\n"
"\n"
"background-color:#fff;\n"
"border: 1px solid #8ec0af;\n"
"border-radius: 6px\n"
"}")
        self.txt_nivel_acesso.setObjectName("txt_nivel_acesso")
        self.lbl_email.raise_()
        self.lbl_nivel_acesso.raise_()
        self.lbl_senha.raise_()
        self.frame_2.raise_()
        self.frame_3.raise_()
        self.frame_9.raise_()
        self.line_2.raise_()
        self.lbl_nome.raise_()
        self.txt_nome.raise_()
        self.txt_email.raise_()
        self.txt_senha.raise_()
        self.txt_nivel_acesso.raise_()

        self.txt_nome.setEnabled(False)
        self.txt_email.setEnabled(False)
        self.txt_senha.setEnabled(False)
        self.txt_nivel_acesso.setEnabled(False)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        list_physical =  compliance.pack_physical_person.physicalController.listar_physical(user_logado)

        self.txt_nome.setText(str(list_physical[0]))
        self.txt_email.setText(str(list_physical[1]))
        self.txt_nivel_acesso.setText(str(list_physical[2]))
        self.txt_senha.setText(str(list_physical[3]))


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dashboard"))
        self.lbl_form_tittle.setText(_translate("MainWindow", "User Profile"))
        self.lbl_form_text.setText(_translate("MainWindow", "Below is the user information"))
        self.lbl_nome.setText(_translate("MainWindow", "Name"))
        self.lbl_email.setText(_translate("MainWindow", "E-mail"))
        self.lbl_senha.setText(_translate("MainWindow", "Password"))
        self.lbl_nivel_acesso.setText(_translate("MainWindow", "Acess Level"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
