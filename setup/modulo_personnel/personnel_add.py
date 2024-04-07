
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QDesktopWidget
import modulo_personnel.personnel
import modulo_personnel.personnelController
#import personnelController
import res

class Ui_MainWindow(object):
    def setupUi(self, MainWindow,user_name):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 850)
        MainWindow.setMinimumSize(QtCore.QSize(1400, 850))
        MainWindow.setMaximumSize(QtCore.QSize(1400, 850))

        desktop = QDesktopWidget()
        screenRect = desktop.screenGeometry()
        windowRect = MainWindow.geometry()

        x = (screenRect.width() - windowRect.width()) // 2
        y = (screenRect.height() - windowRect.height()) // 2

        # Define a posição da janela
        MainWindow.move(x, y)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame_aside_menu = QtWidgets.QFrame(self.centralwidget)
        self.frame_aside_menu.setGeometry(QtCore.QRect(0, -10, 251, 861))
        self.frame_aside_menu.setStyleSheet("\n" "background-color:#2f6d58")
        self.frame_aside_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_aside_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_aside_menu.setObjectName("frame_aside_menu")

        self.label_15 = QtWidgets.QLabel(self.frame_aside_menu)
        self.label_15.setGeometry(QtCore.QRect(10, 30, 221, 91))
        self.label_15.setStyleSheet("image: url(:/img/logo_tecsep-1-removebg-preview.png);")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")

        self.btn_dashboard = QtWidgets.QPushButton(self.frame_aside_menu)
        self.btn_dashboard.setGeometry(QtCore.QRect(30, 140, 191, 41))
        self.btn_dashboard.setStyleSheet("\n" "\n" "QPushButton#btn_dashboard{\n" "\n" "border:none;\n" "color:white;\n" "font-size:18px;\n" "border-radius: 12px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "text-align:left;\n" "}\n" "\n" "QPushButton#btn_dashboard:hover{\n" " background-color: #044e42;\n" "border-radius: 12px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "}\n" "\n" "QPushButton#btn_dashboard:pressed {\n" " background-color: #044e42;\n" "border-radius: 12px;\n" "background-color: #033029;\n" "padding:10px;\n" " }\n" "\n" "\n" "")
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/house-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.btn_dashboard.setIcon(icon)
        self.btn_dashboard.setIconSize(QtCore.QSize(25, 25))
        self.btn_dashboard.setFlat(False)
        self.btn_dashboard.setObjectName("btn_dashboard")

        self.btn_compliance = QtWidgets.QPushButton(self.frame_aside_menu)
        self.btn_compliance.setGeometry(QtCore.QRect(30, 290, 191, 41))
        self.btn_compliance.setStyleSheet("QPushButton#btn_compliance{\n" "\n" "border:none;\n" "color:white;\n" "font-size:18px;\n" "border-radius: 12px;\n" "transition: background-color 0.5s ease;\n" "text-align:left;\n" "padding:10px\n" "}\n" "\n" "QPushButton#btn_compliance:hover{\n" " background-color: #044e42;\n" "border-radius: 12px;\n" "transition: background-color 0.5s ease;\n" "}\n" "\n" "QPushButton#btn_compliance:pressed {\n" " background-color: #044e42;\n" "border-radius: 12px;\n" "background-color: #033029;\n" " }\n" "")
        
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/vial-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
       
        self.btn_compliance.setIcon(icon1)
        self.btn_compliance.setIconSize(QtCore.QSize(25, 25))
        self.btn_compliance.setFlat(False)
        self.btn_compliance.setObjectName("btn_compliance")

        self.btn_wbco = QtWidgets.QPushButton(self.frame_aside_menu)
        self.btn_wbco.setGeometry(QtCore.QRect(30, 340, 191, 41))
        self.btn_wbco.setStyleSheet("QPushButton#btn_wbco{\n" "\n" "border:none;\n" "color:white;\n" "font-size:18px;\n" "border-radius: 12px;\n" "transition: background-color 0.5s ease;\n" "text-align:left;\n" "padding:10px;\n" "}\n" "\n" "QPushButton#btn_wbco:hover{\n" " background-color: #044e42;\n" "border-radius: 12px;\n" "transition: background-color 0.5s ease;\n" "}\n" "\n" "QPushButton#btn_wbco:pressed {\n" " background-color: #044e42;\n" "border-radius: 12px;\n" "background-color: #033029;\n" " }")
       
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/tools.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
       
        self.btn_wbco.setIcon(icon2)
        self.btn_wbco.setIconSize(QtCore.QSize(25, 25))
        self.btn_wbco.setFlat(False)
        self.btn_wbco.setObjectName("btn_wbco")

        self.btn_filtration = QtWidgets.QPushButton(self.frame_aside_menu)
        self.btn_filtration.setGeometry(QtCore.QRect(30, 390, 191, 41))
        self.btn_filtration.setStyleSheet("QPushButton#btn_filtration{\n" "\n" "border:none;\n" "color:white;\n" "font-size:19px;\n" "border-radius: 12px;\n" "transition: background-color 0.5s ease;\n" "text-align:left;\n" "padding:10px;\n" "}\n" "\n" "QPushButton#btn_filtration:hover{\n" " background-color: #044e42;\n" "border-radius: 12px;\n" "transition: background-color 0.5s ease;\n" "}\n" "\n" "QPushButton#btn_filtration:pressed {\n" " background-color: #044e42;\n" "border-radius: 12px;\n" "background-color: #033029;\n" " }")
        
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/oil-well-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.btn_filtration.setIcon(icon3)
        self.btn_filtration.setIconSize(QtCore.QSize(25, 25))
        self.btn_filtration.setFlat(False)
        self.btn_filtration.setObjectName("btn_filtration")

        self.btn_tank_cleaning = QtWidgets.QPushButton(self.frame_aside_menu)
        self.btn_tank_cleaning.setGeometry(QtCore.QRect(30, 440, 191, 41))
        self.btn_tank_cleaning.setStyleSheet("QPushButton#btn_tank_cleaning{\n" "\n" "border:none;\n" "color:white;\n" "font-size:18px;\n" "border-radius: 12px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "text-align:left;\n" "}\n" "\n" "QPushButton#btn_tank_cleaning:hover{\n" " background-color: #044e42;\n" "border-radius: 12px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "}\n" "\n" "QPushButton#btn_tank_cleaning:pressed {\n" " background-color: #044e42;\n" "border-radius: 12px;\n" "background-color: #033029;\n" " }")
       
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("img/soap-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.btn_tank_cleaning.setIcon(icon4)
        self.btn_tank_cleaning.setIconSize(QtCore.QSize(25, 25))
        self.btn_tank_cleaning.setFlat(False)
        self.btn_tank_cleaning.setObjectName("btn_tank_cleaning")

        self.btn_user_profile = QtWidgets.QPushButton(self.frame_aside_menu)
        self.btn_user_profile.setGeometry(QtCore.QRect(40, 710, 161, 41))
        self.btn_user_profile.setStyleSheet("QPushButton#btn_user_profile{\n" "\n" "border:none;\n" "color:white;\n" "font-size:18px;\n" "border-radius: 12px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "text-align:left;\n" "}\n" "\n" "QPushButton#btn_user_profile:hover{\n" " background-color: #044e42;\n" "border-radius: 12px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "}\n" "\n" "QPushButton#btn_user_profile:pressed {\n" " background-color: #044e42;\n" "border-radius: 12px;\n" "background-color: #033029;\n" " }")
       
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("img/user-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
       
        self.btn_user_profile.setIcon(icon5)
        self.btn_user_profile.setIconSize(QtCore.QSize(25, 25))
        self.btn_user_profile.setFlat(False)
        self.btn_user_profile.setObjectName("btn_user_profile")

        self.btn_logout = QtWidgets.QPushButton(self.frame_aside_menu)
        self.btn_logout.setGeometry(QtCore.QRect(40, 760, 161, 41))
        self.btn_logout.setStyleSheet("QPushButton#btn_logout{\n" "\n" "border:none;\n" "color:white;\n" "font-size:18px;\n" "border-radius: 12px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "text-align:left;\n" "}\n" "\n" "QPushButton#btn_logout:hover{\n" " background-color: #044e42;\n" "border-radius: 12px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "}\n" "\n" "QPushButton#btn_logout:pressed {\n" " background-color: #044e42;\n" "border-radius: 12px;\n" "background-color: #033029;\n" " }")
        
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("img/right-from-bracket-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.btn_logout.setIcon(icon6)
        self.btn_logout.setIconSize(QtCore.QSize(25, 25))
        self.btn_logout.setFlat(False)
        self.btn_logout.setObjectName("btn_logout")

        self.btn_user = QtWidgets.QPushButton(self.frame_aside_menu)
        self.btn_user.setGeometry(QtCore.QRect(30, 190, 191, 41))
        self.btn_user.setStyleSheet("\n" "\n" "QPushButton#btn_user{\n" "\n" "border:none;\n" "color:white;\n" "font-size:18px;\n" "border-radius: 12px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "text-align:left;\n" "}\n" "\n" "QPushButton#btn_user:hover{\n" " background-color: #044e42;\n" "border-radius: 12px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "}\n" "\n" "QPushButton#btn_user:pressed {\n" " background-color: #044e42;\n" "border-radius: 12px;\n" "background-color: #033029;\n" "padding:10px;\n" " }\n" "\n" "\n" "")
        self.btn_user.setIcon(icon5)
        self.btn_user.setIconSize(QtCore.QSize(25, 25))
        self.btn_user.setFlat(False)
        self.btn_user.setObjectName("btn_user")

        self.btn_customer = QtWidgets.QPushButton(self.frame_aside_menu)
        self.btn_customer.setGeometry(QtCore.QRect(30, 240, 191, 41))
        self.btn_customer.setStyleSheet("\n" "\n" "QPushButton#btn_customer{\n" "\n" "border:none;\n" "color:white;\n" "font-size:18px;\n" "border-radius: 12px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "text-align:left;\n" "}\n" "\n" "QPushButton#btn_customer:hover{\n" " background-color: #044e42;\n" "border-radius: 12px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "}\n" "\n" "QPushButton#btn_customer:pressed {\n" " background-color: #044e42;\n" "border-radius: 12px;\n" "background-color: #033029;\n" "padding:10px;\n" " }\n" "\n" "\n" "")
        
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("img/user-group-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.btn_customer.setIcon(icon7)
        self.btn_customer.setIconSize(QtCore.QSize(25, 25))
        self.btn_customer.setFlat(False)
        self.btn_customer.setObjectName("btn_customer")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(250, 0, 1151, 861))
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(1151, 861))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 861))
        
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        
        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color:#eff2f9;\n" "\n" "")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
       
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 1151, 51))
        self.frame_2.setStyleSheet("background-color:#fff")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        
        self.lbl_user_logado = QtWidgets.QLabel(self.frame_2)
        self.lbl_user_logado.setGeometry(QtCore.QRect(1020, 20, 111, 20))
        self.lbl_user_logado.setStyleSheet("")
        self.lbl_user_logado.setObjectName("lbl_user_logado")
        self.lbl_user_logado.setText(user_name)
        
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_5.setGeometry(QtCore.QRect(980, 10, 31, 31))
        self.pushButton_5.setStyleSheet("background-color: #fff;\n" "border-radius:30px;\n" "width:30px;\n" "height:30px;")
        self.pushButton_5.setText("")
        
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("img/user_dark.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.pushButton_5.setIcon(icon8)
        self.pushButton_5.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_5.setObjectName("pushButton_5")
        
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(0, 50, 1151, 151))
        self.frame_3.setStyleSheet("background-color:#2d6b56;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(40, 50, 151, 31))
        self.label.setStyleSheet("font-size: 30px;\n" "color:#fff;")
        self.label.setObjectName("label")
        
        self.line = QtWidgets.QFrame(self.frame_3)
        self.line.setGeometry(QtCore.QRect(-10, 0, 21, 151))
        self.line.setStyleSheet("color: rgb(255, 255, 255);\n" "border-color: rgb(255, 255, 255); ")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 431, 16))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n" "font: 9pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        
        self.frame_9 = QtWidgets.QFrame(self.frame)
        self.frame_9.setGeometry(QtCore.QRect(-1, 830, 1151, 31))
        self.frame_9.setStyleSheet("background-color:#2d6b56;")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
       
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(-40, 750, 41, 151))
        self.line_2.setStyleSheet("color: rgb(255, 255, 255);\n" "border-color: rgb(255, 255, 255);")
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
       
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(20, 270, 1091, 20))
        self.line_3.setStyleSheet("color: rgb(255, 255, 255);\n" "")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        
        self.btn_list_personeel = QtWidgets.QPushButton(self.frame)
        self.btn_list_personeel.setGeometry(QtCore.QRect(920, 240, 191, 31))
        self.btn_list_personeel.setStyleSheet("\n" "\n" "QPushButton#btn_list_personeel{\n" "\n" "border:none;\n" "background-color:#044e42;\n" "color:white;\n" "font-size:14px;\n" "border-radius: 6px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "text-align:rigth;\n" "}\n" "\n" "QPushButton#btn_list_personeel:hover{\n" " background-color: #044e42;\n" "border-radius: 6px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "}\n" "\n" "QPushButton#btn_list_personeel:pressed {\n" " background-color: #044e42;\n" "border-radius: 6px;\n" "background-color: #033029;\n" "padding:10px;\n" " }\n" "")
        self.btn_list_personeel.setIcon(icon7)
        self.btn_list_personeel.setObjectName("btn_list_personeel")
        
        self.txt_nome = QtWidgets.QLineEdit(self.frame)
        self.txt_nome.setGeometry(QtCore.QRect(30, 390, 341, 41))
        self.txt_nome.setStyleSheet("QLineEdit{\n" "\n" "\n" "background-color:#fff;\n" "border: 1px solid #8ec0af;\n" "border-radius: 6px;\n font-size:16px;" "}")
        self.txt_nome.setPlaceholderText("")
        self.txt_nome.setObjectName("txt_nome")
        
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 360, 81, 31))
        
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(52, 52, 52);")
        self.label_3.setObjectName("label_3")
        
        self.txt_bi_card = QtWidgets.QLineEdit(self.frame)
        self.txt_bi_card.setGeometry(QtCore.QRect(390, 390, 341, 41))
        self.txt_bi_card.setStyleSheet("QLineEdit{\n" "\n" "\n" "background-color:#fff;\n" "border: 1px solid #8ec0af;\n" "border-radius: 6px;\n font-size:16px;" "}")
        self.txt_bi_card.setPlaceholderText("")
        self.txt_bi_card.setObjectName("txt_bi_card")
       
        self.txt_phone_number = QtWidgets.QLineEdit(self.frame)
        self.txt_phone_number.setGeometry(QtCore.QRect(750, 390, 341, 41))
        self.txt_phone_number.setStyleSheet("QLineEdit{\n" "\n" "\n" "background-color:#fff;\n" "border: 1px solid #8ec0af;\n" "border-radius: 6px;\n font-size:16px;" "}")
        self.txt_phone_number.setPlaceholderText("")
        self.txt_phone_number.setObjectName("txt_phone_number")
        
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(390, 360, 191, 31))
        
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(52, 52, 52);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(750, 360, 191, 31))
       
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(52, 52, 52);")
        self.label_5.setObjectName("label_5")
        
        self.txt_email = QtWidgets.QLineEdit(self.frame)
        self.txt_email.setGeometry(QtCore.QRect(30, 520, 341, 41))
        self.txt_email.setStyleSheet("QLineEdit{\n" "\n" "\n" "background-color:#fff;\n" "border: 1px solid #8ec0af;\n" "border-radius: 6px\n" "}")
        self.txt_email.setPlaceholderText("")
        self.txt_email.setObjectName("txt_email")
        
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(30, 490, 81, 31))
       
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
       
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(52, 52, 52);")
        self.label_6.setObjectName("label_6")
        
        self.cb_tipo_usuario = QtWidgets.QComboBox(self.frame)
        self.cb_tipo_usuario.setGeometry(QtCore.QRect(390, 520, 341, 41))
        self.cb_tipo_usuario.setStyleSheet("\n" "QComboBox{\n" "\n" "\n" "background-color:#fff;\n" "border: 1px solid #8ec0af;\n" "border-radius: 6px;\n" "\n" "font-size:18px;\n" "\n" "}")
        self.cb_tipo_usuario.setObjectName("cb_tipo_usuario")
        self.cb_tipo_usuario.addItem("")
        self.cb_tipo_usuario.addItem("")
        self.cb_tipo_usuario.setStyleSheet("""
            QComboBox {
                border: 1px solid #8ec0af;
                border-radius: 6px;
                padding: 1px 18px 1px 3px;
                min-width: 6em;
                background: white;
            }
            QComboBox:editable {
                background: white;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                border-left-width: 1px;
                border-left-color: darkgray;
                border-left-style: solid;
                border-top-right-radius: 3px;
                border-bottom-right-radius: 3px;
            }
            QComboBox::down-arrow {
                image: url(img/arrow_2.png);
            }
        """)
       
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(390, 490, 101, 31))
        
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(52, 52, 52);")
        self.label_7.setObjectName("label_7")
        
        self.btn_salvar_user = QtWidgets.QPushButton(self.frame)
        self.btn_salvar_user.setGeometry(QtCore.QRect(390, 620, 341, 41))
        self.btn_salvar_user.setStyleSheet("\n" "\n" "QPushButton#btn_salvar_user{\n" "\n" "border:none;\n" "background-color:#044e42;\n" "color:white;\n" "font-size:18px;\n" "border-radius: 6px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "text-align:rigth;\n" "}\n" "\n" "QPushButton#btn_salvar_user:hover{\n" " background-color: #044e42;\n" "border-radius: 6px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "}\n" "\n" "QPushButton#btn_salvar_user:pressed {\n" " background-color: #044e42;\n" "border-radius: 6px;\n" "background-color: #033029;\n" "padding:10px;\n" " }\n" "")
        
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("img/check-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.btn_salvar_user.setIcon(icon9)
        self.btn_salvar_user.setIconSize(QtCore.QSize(25, 25))
        self.btn_salvar_user.setObjectName("btn_salvar_user")
        
        self.txt_password = QtWidgets.QLineEdit(self.frame)
        self.txt_password.setGeometry(QtCore.QRect(750, 520, 351, 41))
        self.txt_password.setStyleSheet("QLineEdit{\n" "\n" "\n" "background-color:#fff;\n" "border: 1px solid #8ec0af;\n" "border-radius: 6px\n" "}")
        self.txt_password.setPlaceholderText("")
        self.txt_password.setObjectName("txt_password")
        
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(750, 490, 101, 31))
        
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(52, 52, 52);")
        self.label_8.setObjectName("label_8")
        self.label_8.raise_()
       
        self.label_7.raise_()
        self.label_6.raise_()
        self.label_5.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.frame_2.raise_()
        self.frame_3.raise_()
        self.frame_9.raise_()

        self.line_2.raise_()
        self.line_3.raise_()

        self.btn_list_personeel.raise_()
        self.txt_nome.raise_()
        self.txt_bi_card.raise_()
        self.txt_phone_number.raise_()
        self.txt_email.raise_()
        self.cb_tipo_usuario.raise_()
        self.btn_salvar_user.raise_()
        self.txt_password.raise_()

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1400, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dashboard"))
        
        self.btn_dashboard.setText(_translate("MainWindow", " Dashboard"))
        self.btn_dashboard.clicked.connect(lambda: show_form_dashboard())

        self.btn_compliance.setText(_translate("MainWindow", " A. M. Compliance"))
        self.btn_wbco.setText(_translate("MainWindow", " WBCO Tools"))
        self.btn_wbco.clicked.connect(lambda:call_form_wbco())
        self.btn_filtration.setText(_translate("MainWindow", " Filtration"))
        self.btn_tank_cleaning.setText(_translate("MainWindow", " Tank Cleaning"))
        self.btn_user_profile.setText(_translate("MainWindow", "User Profile"))
        self.btn_logout.setText(_translate("MainWindow", "Logout"))

        self.btn_logout.clicked.connect(lambda: logout())
 
        self.btn_user.setText(_translate("MainWindow", " Personnel"))
        self.btn_user.clicked.connect(lambda: show_form_personeel_list())

        self.btn_customer.setText(_translate("MainWindow", "Customers"))
        self.btn_customer.clicked.connect(lambda:call_form_client())

        self.label.setText(_translate("MainWindow", "Personeel"))
        self.label_2.setText(_translate("MainWindow", "Fill in all the fields to be able to add a new person to the system"))
        self.btn_list_personeel.setText(_translate("MainWindow", "List Personnel"))
        self.btn_list_personeel.clicked.connect(lambda: show_form_personeel_list())
        self.label_3.setText(_translate("MainWindow", "Full name"))
        self.label_4.setText(_translate("MainWindow", "Identity card number"))
        self.label_5.setText(_translate("MainWindow", "Phone number"))
        self.label_6.setText(_translate("MainWindow", "E-mail"))
        self.cb_tipo_usuario.setItemText(0, _translate("MainWindow", " Admin"))
        self.cb_tipo_usuario.setItemText(1, _translate("MainWindow", " Supervisor"))
        self.label_7.setText(_translate("MainWindow", "Acess Level"))

        self.btn_salvar_user.setText(_translate("MainWindow", "Save person data"))
        self.btn_salvar_user.clicked.connect(lambda: validation_add_user())

        self.label_8.setText(_translate("MainWindow", "Password"))

        def show_form_personeel_list():
            self.window = QtWidgets.QMainWindow()
            self.ui = modulo_personnel.personnel.form_personeel_list()
            self.ui.setupUi(self.window,self.lbl_user_logado.text())
            self.window.show()
            MainWindow.close()

        def show_form_dashboard():
            self.window = QtWidgets.QMainWindow()
            import modulo_home.dashboard
            self.ui = modulo_home.dashboard.Ui_dashboard_ui()
            self.ui.setupUi(self.window,self.lbl_user_logado.text())
            self.window.show()
            MainWindow.close()

        def call_form_client():
            self.window = QtWidgets.QMainWindow()
            import modulo_customer.customer
            self.ui = modulo_customer.customer.Ui_MainWindow()
            self.ui.setupUi(self.window,self.lbl_user_logado.text())
            self.window.show()
            MainWindow.close()

        def call_form_wbco():
                self.window = QtWidgets.QMainWindow()
                import modulo_wbco.wbco
                self.ui = modulo_wbco.wbco.Ui_MainWindow()
                self.ui.setupUi(self.window,self.lbl_user_logado.text())
                self.window.show()
                MainWindow.close()

        def logout():
            self.window = QtWidgets.QMainWindow()
            import modulo_home.login
            self.ui = modulo_home.login.Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.window.show()
            MainWindow.close() 

        def show_message_sucess():
            msg_error = QMessageBox()
            msg_error.setIcon(QMessageBox.Information)
            msg_error.setText('User added successfully')
            msg_error.setWindowTitle('Adding User')
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("img/sucess_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg_error.setWindowIcon(icon)
            msg_error.exec_()

        #Funcao para Salvar
        def validation_add_user():
            user_name = self.txt_nome.text()
            identfy_card = self.txt_bi_card.text()
            phone_number = self.txt_phone_number.text()
            email = self.txt_email.text()
            password = self.txt_password.text()
            #u_type = self.cb_tipo_usuario.itemText() 

            # Condicao para adicao de usuario
            if user_name == "" or identfy_card == "" or phone_number == "" or email == "" or password == "":
                msg_validation = QMessageBox()
                msg_validation.setIcon(QMessageBox.Critical)
                msg_validation.setText('Unsuccessful registration, existence of empty fields')
                msg_validation.setWindowTitle(' Error Adding User')
                msg_validation.exec_()
            else:
                modulo_personnel.personnelController.carregar_cadastro( user_name, identfy_card, email, password, phone_number, self.cb_tipo_usuario.currentText())
                show_message_sucess()
                self.txt_nome.clear()
                self.txt_bi_card.clear()
                self.txt_phone_number.clear()
                self.txt_email.clear()
                self.txt_password.clear()



            



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
