


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
from compliance.pack_model_average import average_modelController as controlloer



class Ui_MainWindow(QtWidgets.QMainWindow):

    

    def setupUi(self, MainWindow, user_logado):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 230)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 230))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 230))
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
        self.frame.setStyleSheet("background-color:#fff;\n"
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
        icon.addPixmap(QtGui.QPixmap(".\\../../../../../../.designer/backup/user_dark.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.lbl_form_tittle.setGeometry(QtCore.QRect(40, 0, 391, 41))
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
        self.lbl_form_text.setGeometry(QtCore.QRect(40, 40, 391, 21))
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
        self.lbl_model = QtWidgets.QLabel(self.frame)
        self.lbl_model.setGeometry(QtCore.QRect(10, 100, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_model.setFont(font)
        self.lbl_model.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_model.setObjectName("lbl_model")
        self.txt_model = QtWidgets.QLineEdit(self.frame)
        self.txt_model.setGeometry(QtCore.QRect(10, 130, 321, 41))
        self.txt_model.setStyleSheet("""
            QLineEdit {
                border: 1px solid #8ec0af;
                border-radius: 2px;
                padding: 5px;
                background-color: #fff;
            }
            QLineEdit:focus {
                border: 1px solid #4CAF50;
            }
            QLineEdit {
                background-color: white;
                border: 1px solid #8ec0af;
                border-radius: 6px;
                min-width: 10em;
                padding: 6px;
            }
            QLineEdit:hover {
                border: 2px solid #bbb;
            }
            QLineEdit:enabled {
                background-color: white;
            }
            QLineEdit:disabled {
                background-color: #eee;
            }
            QLineEdit:read-only {
                background-color: #eee;
            }
            QLineEdit::placeholder {
                color: #ccc;
            }
        """)
        self.txt_model.setPlaceholderText("")
        self.txt_model.setObjectName("txt_model")
        self.txt_sn = QtWidgets.QLineEdit(self.frame)
        self.txt_sn.setGeometry(QtCore.QRect(340, 130, 321, 41))
        self.txt_sn.setStyleSheet("""
            QLineEdit {
                border: 1px solid #8ec0af;
                border-radius: 2px;
                padding: 5px;
                background-color: #fff;
            }
            QLineEdit:focus {
                border: 1px solid #4CAF50;
            }
            QLineEdit {
                background-color: white;
                border: 1px solid #8ec0af;
                border-radius: 6px;
                min-width: 10em;
                padding: 6px;
            }
            QLineEdit:hover {
                border: 2px solid #bbb;
            }
            QLineEdit:enabled {
                background-color: white;
            }
            QLineEdit:disabled {
                background-color: #eee;
            }
            QLineEdit:read-only {
                background-color: #eee;
            }
            QLineEdit::placeholder {
                color: #ccc;
            }
        """)
        self.txt_sn.setPlaceholderText("")
        self.txt_sn.setObjectName("txt_sn")
        self.lbl_sn = QtWidgets.QLabel(self.frame)
        self.lbl_sn.setGeometry(QtCore.QRect(340, 100, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_sn.setFont(font)
        self.lbl_sn.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_sn.setObjectName("lbl_sn")
        self.btn_save = QtWidgets.QPushButton(self.frame)
        self.btn_save.setGeometry(QtCore.QRect(670, 130, 161, 41))
        self.btn_save.setStyleSheet("\n"
        "\n"
        "QPushButton#btn_save{\n"
        "\n"
        "border:none;\n"
        "background-color:#044e42;\n"
        "color:white;\n"
        "font-size:14px;\n"
        "border-radius: 6px;\n"
        "transition: background-color 0.5s ease;\n"
        "padding:10px;\n"
        "text-align:rigth;\n"
        "}\n"
        "\n"
        "QPushButton#btn_save:hover{\n"
        " background-color: #044e42;\n"
        "border-radius: 6px;\n"
        "transition: background-color 0.5s ease;\n"
        "padding:10px;\n"
        "}\n"
        "\n"
        "QPushButton#btn_save:pressed {\n"
        " background-color: #044e42;\n"
        "border-radius: 6px;\n"
        "background-color: #033029;\n"
        "padding:10px;\n"
        " }\n"
        "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\../../../../../../img/check-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_save.setIcon(icon1)
        self.btn_save.setObjectName("btn_save")


        self.btn_cancel = QtWidgets.QPushButton(self.frame)
        self.btn_cancel.setGeometry(QtCore.QRect(835, 130, 161, 41))
        self.btn_cancel.setStyleSheet("\n"
        "\n"
        "QPushButton#btn_cancel{\n"
        "\n"
        "border:none;\n"
        "background-color:#044e42;\n"
        "color:white;\n"
        "font-size:14px;\n"
        "border-radius: 6px;\n"
        "transition: background-color 0.5s ease;\n"
        "padding:10px;\n"
        "text-align:rigth;\n"
        "}\n"
        "\n"
        "QPushButton#btn_cancel:hover{\n"
        " background-color: #044e42;\n"
        "border-radius: 6px;\n"
        "transition: background-color 0.5s ease;\n"
        "padding:10px;\n"
        "}\n"
        "\n"
        "QPushButton#btn_cancel:pressed {\n"
        " background-color: #044e42;\n"
        "border-radius: 6px;\n"
        "background-color: #033029;\n"
        "padding:10px;\n"
        " }\n"
        "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\../../../../../../img/check-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cancel.setIcon(icon1)
        self.btn_cancel.setObjectName("btn_cancel")


        self.lbl_sn.raise_()
        self.frame_2.raise_()
        self.frame_3.raise_()
        self.frame_9.raise_()
        self.line_2.raise_()
        self.lbl_model.raise_()
        self.txt_model.raise_()
        self.txt_sn.raise_()
        self.btn_save.raise_()
        self.btn_cancel.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        

        self.retranslateUi(MainWindow,user_logado)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    

    
    def retranslateUi(self, MainWindow,user_logado):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dashboard"))
        self.lbl_form_tittle.setText(_translate("MainWindow", "Model Drying Equipment"))
        self.lbl_form_text.setText(_translate("MainWindow", "Fill in the fields to save a Model Drying Equipment in system"))
        self.lbl_model.setText(_translate("MainWindow", "Model"))
        self.lbl_sn.setText(_translate("MainWindow", "S/N"))
        self.btn_save.setText(_translate("MainWindow", "Save data"))
        self.btn_save.clicked.connect(lambda:save_data())
        self.btn_cancel.setText(_translate("MainWindow","Cancel"))
        self.btn_cancel.clicked.connect(lambda:close_windows())


        def show_form_add_model_average():
            self.window = QtWidgets.QMainWindow()
            import compliance.pack_model_average.model_average as list_average
            self.ui = list_average.Ui_MainWindow()
            self.ui.setupUi(self.window,self.lbl_user_logado.text())
            self.window.show()
            MainWindow.close()

        def show_compliance_view():
            self.window = QtWidgets.QMainWindow()
            import compliance.pack_model_average.model_average as view
            self.ui = view.Ui_MainWindow()
            self.ui.setupUi(self.window,user_logado)
            self.window.show()
            MainWindow.close()

        def show_message(title,message):
             msg = QMessageBox()
             msg.setIcon(QMessageBox.Information)
             msg.setText(title)
             msg.setInformativeText(str(message))
             msg.setWindowTitle("Error")
             msg.exec_()

        def show_message_error(title,message):
             msg = QMessageBox()
             msg.setIcon(QMessageBox.Critical)
             msg.setText(title)
             msg.setInformativeText(str(message))
             msg.setWindowTitle("Error")
             msg.exec_()

        def close_windows():
            self.window = QtWidgets.QMainWindow()
            import compliance.pack_model_average.model_average as view
            self.ui = view.Ui_MainWindow()
            self.ui.setupUi(self.window,user_logado)
            self.window.show()
            MainWindow.close()

        def save_data():
            try:
                model = self.txt_model.text()
                serial_number = self.txt_sn.text()
                salvar = controlloer.cadastrar(model,serial_number)
                if salvar == 0:
                    show_message("Add","Data Saved")
                    MainWindow.close()
                    show_compliance_view()
                    
                else:
                    show_message_error("Add","Error saving data")
            except (TypeError,ValueError,Exception,) as e:
                print(f" Erro {e}")
    
                




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
