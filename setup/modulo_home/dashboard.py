import sys
sys.path.append("..")

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtGui import QPixmap
from modulo_personnel.personnel import form_personeel_list
import res
import psycopg2
import conection.connect as connecao

class Ui_dashboard_ui(object):




    def setupUi(self, dashboard_ui,user_name):
        dashboard_ui.setObjectName("dashboard_ui")
        dashboard_ui.resize(1400, 850)
        dashboard_ui.setMinimumSize(QtCore.QSize(1400, 850))
        dashboard_ui.setMaximumSize(QtCore.QSize(1400, 850))

        desktop = QDesktopWidget()
        screenRect = desktop.screenGeometry()
        windowRect = dashboard_ui.geometry()

        x = (screenRect.width() - windowRect.width()) // 2
        y = (screenRect.height() - windowRect.height()) // 2

        # Define a posição da janela
        dashboard_ui.move(x, y) 


        self.centralwidget = QtWidgets.QWidget(dashboard_ui)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_aside_menu = QtWidgets.QFrame(self.centralwidget)
        self.frame_aside_menu.setGeometry(QtCore.QRect(0, -10, 251, 861))
        self.frame_aside_menu.setStyleSheet("\n" "background-color:#2f6d58")
        self.frame_aside_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_aside_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_aside_menu.setObjectName("frame_aside_menu")

        img_logo_tecsep = QPixmap("img/TECSEP_Logo.png")
        redimens = img_logo_tecsep.scaled(220,70)

        self.lbl_logo_tecseo = QtWidgets.QPushButton(self.frame_aside_menu)
        self.lbl_logo_tecseo.setGeometry(QtCore.QRect(1, 30, 240, 105))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/TECSEP_Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lbl_logo_tecseo.setIcon(icon)
        self.lbl_logo_tecseo.setIconSize(QtCore.QSize(230, 230))
        self.lbl_logo_tecseo.setFlat(False)
        self.lbl_logo_tecseo.setStyleSheet("\n" "\n" "QPushButton#lbl_logo_tecseo{\n" "\n" "border:none;\n" "color:white;\n" "font-size:18px;\n" "border-radius: 12px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "text-align:left;\n" "}\n" "\n" "QPushButton#btn_dashboard:hover{\n" " background-color: #044e42;\n" "border-radius: 12px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "}\n" "\n" "QPushButton#btn_dashboard:pressed {\n" " background-color: #044e42;\n" "border-radius: 12px;\n" "background-color: #033029;\n" "padding:10px;\n" " }\n" "\n" "\n" "")
        self.lbl_logo_tecseo.setObjectName("lbl_logo_tecseo")

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
        self.frame.setMinimumSize(QtCore.QSize(0, 861))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 861))
        self.frame.setStyleSheet("background-color:#fff;\n" "\n" "")
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
        self.lbl_user_logado.setGeometry(QtCore.QRect(1020, 15, 111, 20))
        self.lbl_user_logado.setStyleSheet("")
        self.lbl_user_logado.setObjectName("lbl_user_logado")
        self.lbl_user_logado.setText(user_name)

        self.img_user_logado = QtWidgets.QPushButton(self.frame_2)
        self.img_user_logado.setGeometry(QtCore.QRect(980, 10, 31, 31))
        self.img_user_logado.setStyleSheet("background-color: #fff;\n" "border-radius:30px;\n" "width:30px;\n" "height:30px;")
        self.img_user_logado.setText("")

        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("img/user_dark.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.img_user_logado.setIcon(icon8)
        self.img_user_logado.setIconSize(QtCore.QSize(25, 25))
        self.img_user_logado.setObjectName("img_user_logado")

        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(0, 50, 1151, 151))
        self.frame_3.setStyleSheet("background-color:#2d6b56;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")

        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(30, 30, 151, 31))
        self.label.setStyleSheet("font-size: 30px;\n" "color:#fff;")
        self.label.setObjectName("label")

        self.line = QtWidgets.QFrame(self.frame_3)
        self.line.setGeometry(QtCore.QRect(-10, 0, 21, 151))
        self.line.setStyleSheet("color: rgb(255, 255, 255);\n" "border-color: rgb(255, 255, 255);")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")

        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(10, 160, 251, 121))
        self.frame_4.setStyleSheet("background-color:#0c6ffe;\n" "border-radius:10px;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setObjectName("frame_4")

        self.lbl_compliance = QtWidgets.QLabel(self.frame_4)
        self.lbl_compliance.setGeometry(QtCore.QRect(20, 20, 231, 31))
        self.lbl_compliance.setStyleSheet("font-size:18px;\n" "color:#fff;")
        self.lbl_compliance.setObjectName("lbl_compliance")

        self.img_fluid_compliance = QtWidgets.QPushButton(self.frame_4)
        self.img_fluid_compliance.setGeometry(QtCore.QRect(170, 50, 61, 61))
        self.img_fluid_compliance.setStyleSheet("background-color: #fff;\n" "border-radius:30px;\n" "width:30px;\n" "height:30px;")
        self.img_fluid_compliance.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("img/vial_card.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.img_fluid_compliance.setIcon(icon9)
        self.img_fluid_compliance.setIconSize(QtCore.QSize(30, 30))
        self.img_fluid_compliance.setObjectName("img_fluid_compliance")
        self.lbl_total_compliance = QtWidgets.QLabel(self.frame_4)
        self.lbl_total_compliance.setGeometry(QtCore.QRect(20, 80, 51, 31))
        self.lbl_total_compliance.setStyleSheet("font-size:20px;\n" "color:#fff;")
        self.lbl_total_compliance.setObjectName("lbl_total_compliance")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setGeometry(QtCore.QRect(290, 160, 271, 121))
        self.frame_5.setStyleSheet("background-color:#fec107;\n" "border-radius:10px;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_5.setObjectName("frame_5")

        self.lbl_wbco_tools = QtWidgets.QLabel(self.frame_5)
        self.lbl_wbco_tools.setGeometry(QtCore.QRect(20, 20, 231, 31))
        self.lbl_wbco_tools.setStyleSheet("font-size:18px;\n" "color:#fff;")
        self.lbl_wbco_tools.setObjectName("lbl_wbco_tools")
        self.lbl_total_wbco_tools = QtWidgets.QLabel(self.frame_5)
        self.lbl_total_wbco_tools.setGeometry(QtCore.QRect(20, 80, 31, 31))
        self.lbl_total_wbco_tools.setStyleSheet("font-size:20px;\n" "color:#fff;")
        self.lbl_total_wbco_tools.setObjectName("lbl_total_wbco_tools")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 50, 61, 61))
        self.pushButton_2.setStyleSheet("background-color: #fff;\n" "border-radius:30px;\n" "width:30px;\n" "height:30px;")
        self.pushButton_2.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("img/tools_card.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon10)
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setGeometry(QtCore.QRect(570, 160, 271, 121))
        self.frame_6.setStyleSheet("background-color:#1a8655;\n" "border-radius:10px;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_6.setObjectName("frame_6")
        self.lbl_filtration = QtWidgets.QLabel(self.frame_6)
        self.lbl_filtration.setGeometry(QtCore.QRect(20, 20, 231, 31))
        self.lbl_filtration.setStyleSheet("font-size:18px;\n" "color:#fff;")
        self.lbl_filtration.setObjectName("lbl_filtration")
        self.lbl_total_filtration = QtWidgets.QLabel(self.frame_6)
        self.lbl_total_filtration.setGeometry(QtCore.QRect(20, 80, 31, 31))
        self.lbl_total_filtration.setStyleSheet("font-size:20px;\n" "color:#fff;")
        self.lbl_total_filtration.setObjectName("lbl_total_filtration")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 50, 61, 61))
        self.pushButton_3.setStyleSheet("background-color: #fff;\n" "border-radius:30px;\n" "width:30px;\n" "height:30px;")
        self.pushButton_3.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("img/oil_well_card.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon11)
        self.pushButton_3.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.frame_7 = QtWidgets.QFrame(self.frame)
        self.frame_7.setGeometry(QtCore.QRect(850, 160, 271, 121))
        self.frame_7.setStyleSheet("background-color:#dc3644;\n" "border-radius:10px;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_7.setObjectName("frame_7")
        self.lbl_tank_cleaning = QtWidgets.QLabel(self.frame_7)
        self.lbl_tank_cleaning.setGeometry(QtCore.QRect(20, 20, 231, 31))
        self.lbl_tank_cleaning.setStyleSheet("font-size:18px;\n" "color:#fff;")
        self.lbl_tank_cleaning.setObjectName("lbl_tank_cleaning")
        self.lbl_total_tank_cleaning = QtWidgets.QLabel(self.frame_7)
        self.lbl_total_tank_cleaning.setGeometry(QtCore.QRect(20, 80, 31, 31))
        self.lbl_total_tank_cleaning.setStyleSheet("font-size:20px;\n" "color:#fff;")
        self.lbl_total_tank_cleaning.setObjectName("lbl_total_tank_cleaning")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_4.setGeometry(QtCore.QRect(190, 50, 61, 61))
        self.pushButton_4.setStyleSheet("background-color: #fff;\n" "border-radius:30px;\n" "width:30px;\n" "height:30px;")
        self.pushButton_4.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("img/tank_card.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon12)
        self.pushButton_4.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_4.setObjectName("pushButton_4")
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
        dashboard_ui.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(dashboard_ui)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1400, 26))
        self.menubar.setObjectName("menubar")
        dashboard_ui.setMenuBar(self.menubar)

        self.retranslateUi(dashboard_ui)
        QtCore.QMetaObject.connectSlotsByName(dashboard_ui)



    def retranslateUi(self, dashboard_ui):
        _translate = QtCore.QCoreApplication.translate
        dashboard_ui.setWindowTitle(_translate("dashboard_ui", "Dashboard"))
        self.btn_dashboard.setText(_translate("dashboard_ui", " Dashboard"))
        self.btn_compliance.setText(_translate("dashboard_ui", " A. M. Compliance"))
        self.btn_compliance.clicked.connect(lambda:show_form_compliance())

        self.btn_wbco.setText(_translate("dashboard_ui", " WBCO Tools"))
        self.btn_wbco.clicked.connect(lambda:call_form_wbco())
       
        self.btn_filtration.setText(_translate("dashboard_ui", " Filtration"))
        self.btn_filtration.clicked.connect(lambda:show_add_filtration())
        self.btn_tank_cleaning.setText(_translate("dashboard_ui", " Tank Cleaning"))
        self.btn_tank_cleaning.clicked.connect(lambda:show_add_tank_cleaning())
        self.btn_user_profile.setText(_translate("dashboard_ui", "User Profile"))
        self.btn_user_profile.clicked.connect(lambda:show_perfil_user())

        self.btn_user.clicked.connect(lambda: call_form_user())

        self.btn_logout.setText(_translate("dashboard_ui", "Logout"))
        self.btn_logout.clicked.connect(lambda: logout())

        self.btn_user.setText(_translate("dashboard_ui", " Personnel"))

        self.btn_customer.setText(_translate("dashboard_ui", "Customers"))
        self.btn_customer.clicked.connect(lambda: call_form_client())

        self.label.setText(_translate("dashboard_ui", "Dashboard"))
    
        def listar_drilling_fluid():
            try:
                connection = connecao.cria_connecao()
                cursor = connection.cursor()
                cursor.execute("SELECT COUNT(*) FROM report_information_cp")
                dados = cursor.fetchone()
                cursor.close()
            except Exception as e:
                print(f"Erro na Base de dados: {e}")
            finally:
                if connection:
                    cursor.close()
                return dados[0]
                 
        
        self.lbl_compliance.setText(_translate("dashboard_ui", "Audit Monitor Compliance"))
        self.lbl_total_compliance.setText(_translate("dashboard_ui", str(listar_drilling_fluid())))
        
        def listar_wbco():
            try:
                connection = connecao.cria_connecao()
                cursor = connection.cursor()
                cursor.execute("SELECT COUNT(*) FROM tb_report_wbco")
                dados = cursor.fetchone()
                cursor.close()
            except Exception as e:
                print(f"Erro na Base de dados: {e}")
            finally:
                if connection:
                    cursor.close()
                return dados[0]
        
        self.lbl_wbco_tools.setText(_translate("dashboard_ui", "WBCO Tools Services"))
        self.lbl_total_wbco_tools.setText(_translate("dashboard_ui", str(listar_wbco())))
        
        def listar_filtration():
            try:
                connection = connecao.cria_connecao()
                cursor = connection.cursor()
                cursor.execute("SELECT COUNT(*) FROM tb_report_ft")
                dados = cursor.fetchone()
                cursor.close()
            except Exception as e:
                print(f"Erro na Base de dados: {e}")
            finally:
                if connection:
                    cursor.close()
                return dados[0]
        
        self.lbl_filtration.setText(_translate("dashboard_ui", "Filtration"))
        self.lbl_total_filtration.setText(_translate("dashboard_ui", str(listar_filtration())))
        
        def listar_tank_cleaning():
            try:
                connection = connecao.cria_connecao()
                cursor = connection.cursor()
                cursor.execute("SELECT COUNT(*) FROM tb_report_tc ")
                dados = cursor.fetchone()
                cursor.close()
            except Exception as e:
                print(f"Erro na Base de dados: {e}")
            finally:
                if connection:
                    cursor.close()
                return dados[0]
        
        self.lbl_tank_cleaning.setText(_translate("dashboard_ui", " Tank Cleaning "))
        self.lbl_total_tank_cleaning.setText(_translate("dashboard_ui", str(listar_tank_cleaning())))

        def call_form_user():
            self.window = QtWidgets.QMainWindow()
            self.ui = form_personeel_list()
            self.ui.setupUi(self.window,self.lbl_user_logado.text())
            self.window.show()
            dashboard_ui.close()

        def call_form_client():
            self.window = QtWidgets.QMainWindow()
            import modulo_customer.customer
            self.ui = modulo_customer.customer.Ui_MainWindow()
            self.ui.setupUi(self.window,self.lbl_user_logado.text())
            self.window.show()
            dashboard_ui.close()

        def call_form_wbco():
            self.window = QtWidgets.QMainWindow()
            import modulo_wbco.wbco
            self.ui = modulo_wbco.wbco.Ui_MainWindow()
            self.ui.setupUi(self.window,self.lbl_user_logado.text())
            self.window.show()
            dashboard_ui.close()

        def show_add_tank_cleaning():
            self.window = QtWidgets.QMainWindow()
            import  tank_cleanning.tank_cleaning_view
            self.ui = tank_cleanning.tank_cleaning_view.Ui_MainWindow()
            self.ui.setupUi(self.window,self.lbl_user_logado.text())
            self.window.show()
            dashboard_ui.close()

        def show_add_filtration():
            self.window = QtWidgets.QMainWindow()
            import  filtration.filtration
            self.ui = filtration.filtration.Ui_MainWindow()
            self.ui.setupUi(self.window,self.lbl_user_logado.text())
            self.window.show()
            dashboard_ui.close()

        def show_form_compliance():
            self.window = QtWidgets.QMainWindow()
            import  compliance.compliance_view as list
            self.ui = list.Ui_MainWindow()
            self.ui.setupUi(self.window,self.lbl_user_logado.text())
            self.window.show()
            dashboard_ui.close()

        def show_perfil_user():
            self.window = QtWidgets.QMainWindow()
            import modulo_home.user_profile as user
            self.ui = user.Ui_MainWindow()
            self.ui.setupUi(self.window,self.lbl_user_logado.text())
            self.window.show()

        def logout():
            self.window = QtWidgets.QMainWindow()
            import  modulo_home.login
            self.ui = modulo_home.login.Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.window.show()
            dashboard_ui.close()












if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dashboard_ui = QtWidgets.QMainWindow()
    ui = Ui_dashboard_ui()
    ui.setupUi(dashboard_ui)
    dashboard_ui.show()
    sys.exit(app.exec_())
