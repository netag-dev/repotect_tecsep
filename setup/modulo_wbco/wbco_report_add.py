from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import modulo_wbco.wbcoController
import modulo_wbco.report_wbco
import modulo_wbco.sizeController
import modulo_wbco.threadController
from modulo_wbco import wbcoController as controller
from modulo_wbco import enginierwbcoController as controller_enginer
from reportlab.platypus import Image, Paragraph, Table
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas


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

        self.gerador_report = modulo_wbco.report_wbco.GerarReport()

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
        self.btn_logout.setStyleSheet("QPushButton#btn_logout{\n""\n""border:none;\n""color:white;\n""font-size:18px;\n""border-radius: 12px;\n""transition: background-color 0.5s ease;\n""padding:10px;\n""text-align:left;\n""}\n""\n""QPushButton#btn_logout:hover{\n"" background-color: #044e42;\n""border-radius: 12px;\n""transition: background-color 0.5s ease;\n""padding:10px;\n""}\n""\n""QPushButton#btn_logout:pressed {\n"" background-color: #044e42;\n""border-radius: 12px;\n""background-color: #033029;\n"" }")
       
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
        self.lbl_user_logado.setGeometry(QtCore.QRect(1020, 20, 111, 20))
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
        
        self.lbl_form_tittle = QtWidgets.QLabel(self.frame_3)
        self.lbl_form_tittle.setGeometry(QtCore.QRect(40, 50, 391, 31))
        self.lbl_form_tittle.setStyleSheet("font-size: 30px;\n" "color:#fff;")
        self.lbl_form_tittle.setObjectName("lbl_form_tittle")
       
        self.line = QtWidgets.QFrame(self.frame_3)
        self.line.setGeometry(QtCore.QRect(-10, 0, 21, 151))
        self.line.setStyleSheet("color: rgb(255, 255, 255);\n" "border-color: rgb(255, 255, 255);")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
       
        self.lbl_form_text = QtWidgets.QLabel(self.frame_3)
        self.lbl_form_text.setGeometry(QtCore.QRect(40, 90, 391, 21))
        self.lbl_form_text.setStyleSheet("color: rgb(255, 255, 255);\n" "font: 9pt \"MS Shell Dlg 2\";")
        self.lbl_form_text.setObjectName("lbl_form_text")
       
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
        self.line_3.setGeometry(QtCore.QRect(20, 270, 1071, 20))
        self.line_3.setStyleSheet("color: rgb(255, 255, 255);\n" "")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        
        self.btn_list_report = QtWidgets.QPushButton(self.frame)
        self.btn_list_report.setGeometry(QtCore.QRect(900, 240, 191, 31))
        self.btn_list_report.setStyleSheet("\n" "\n" "QPushButton#btn_list_report{\n" "\n" "border:none;\n" "background-color:#044e42;\n" "color:white;\n" "font-size:14px;\n" "border-radius: 6px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "text-align:rigth;\n" "}\n" "\n" "QPushButton#btn_list_report:hover{\n" " background-color: #044e42;\n" "border-radius: 6px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "}\n" "\n" "QPushButton#btn_list_report:pressed {\n" " background-color: #044e42;\n" "border-radius: 6px;\n" "background-color: #033029;\n" "padding:10px;\n" " }\n" "")
       
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("img/file-lines-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.btn_list_report.setIcon(icon9)
        self.btn_list_report.setObjectName("btn_list_report")
        
        self.tab_menus_wbco = QtWidgets.QTabWidget(self.frame)
        self.tab_menus_wbco.setGeometry(QtCore.QRect(20, 310, 1081, 501))
        
        font = QtGui.QFont("Arial")
        font.setPointSize(9)
       
        self.tab_menus_wbco.setFont(font)
        self.tab_menus_wbco.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tab_menus_wbco.setStyleSheet("    \n"
"            QTabWidget::pane {\n"
"\n"
"                      \n"
"\n"
"            }\n"
"            QTabWidget::tab-bar {\n"
"               \n"
"            }\n"
"            QTabBar::tab {\n"
"                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                            stop: 0 #044e42, stop: 0.4 #044e42,\n"
"                                            stop: 0.5 #044e42, stop: 1.0 #044e42);\n"
"                border: 6px solid #eff2f9;\n"
"                \n"
"               \n"
"              \n"
"                padding: 8px;\n"
"                color:white;\n"
"                border-top-left-radius:8px;\n"
"                border-top-right-radius:8px;\n"
"            }\n"
"            QTabBar::tab:selected, QTabBar::tab:hover {\n"
"                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                            stop: 0 #033029, stop: 0.4 #033029,\n"
"                                            stop: 0.5 #033029, stop: 1.0 #033029);\n"
"            }")
        self.tab_menus_wbco.setTabPosition(QtWidgets.QTabWidget.North)
        self.tab_menus_wbco.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tab_menus_wbco.setUsesScrollButtons(True)
        self.tab_menus_wbco.setDocumentMode(False)
        self.tab_menus_wbco.setTabsClosable(False)
        self.tab_menus_wbco.setMovable(False)
        self.tab_menus_wbco.setTabBarAutoHide(False)
        self.tab_menus_wbco.setObjectName("tab_menus_wbco")
       
        self.tab_report_information = QtWidgets.QWidget()
        self.tab_report_information.setObjectName("tab_report_information")
       
        self.lbl_customer = QtWidgets.QLabel(self.tab_report_information)
        self.lbl_customer.setGeometry(QtCore.QRect(10, 20, 161, 31))
        
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
       
        self.lbl_customer.setFont(font)
        self.lbl_customer.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_customer.setObjectName("lbl_customer")
       
        self.cbx_customer = QtWidgets.QComboBox(self.tab_report_information)
        self.cbx_customer.setGeometry(QtCore.QRect(10, 50, 491, 41))
        self.cbx_customer.setStyleSheet("""
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
        self.cbx_customer.setObjectName("cbx_customer")
        self.cbx_customer.addItem("--- Select Customer ---")
        
        
        
        
        
        self.lbl_well_number = QtWidgets.QLabel(self.tab_report_information)
        self.lbl_well_number.setGeometry(QtCore.QRect(10, 110, 111, 31))
       
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
       
        self.lbl_well_number.setFont(font)
        self.lbl_well_number.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_well_number.setObjectName("lbl_well_number")
       
        self.cbx_well_number = QtWidgets.QComboBox(self.tab_report_information)
        self.cbx_well_number.setGeometry(QtCore.QRect(10, 140, 491, 41))
        self.cbx_well_number.setStyleSheet("""
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
        self.cbx_well_number.setObjectName("cbx_well_number")
       
        self.lbl_report_date = QtWidgets.QLabel(self.tab_report_information)
        self.lbl_report_date.setGeometry(QtCore.QRect(10, 198, 101, 31))
       
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
       
        self.lbl_report_date.setFont(font)
        self.lbl_report_date.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_report_date.setObjectName("lbl_report_date")
        
        self.dateEdit = QtWidgets.QDateEdit(self.tab_report_information)
        self.dateEdit.setGeometry(QtCore.QRect(10, 230, 491, 41))
        self.dateEdit.setStyleSheet("QDateEdit{\n" "\n" "background-color:#fff;\n" "border: 1px solid #8ec0af;\n" "border-radius: 6px\n" "\n" "}")
        self.dateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateEdit.setAccelerated(False)
        self.dateEdit.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.dateEdit.setProperty("showGroupSeparator", False)
        self.dateEdit.setObjectName("dateEdit")

        #Adicao de itens na comboBox Casing

       
        self.lbl_job_ref = QtWidgets.QLabel(self.tab_report_information)
        self.lbl_job_ref.setGeometry(QtCore.QRect(530, 20, 141, 31))
        
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        
        self.lbl_job_ref.setFont(font)
        self.lbl_job_ref.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_job_ref.setObjectName("lbl_job_ref")
        self.txt_job_ref = QtWidgets.QLineEdit(self.tab_report_information)
        self.txt_job_ref.setValidator(QIntValidator())
        self.txt_job_ref.setGeometry(QtCore.QRect(530, 50, 491, 41))
        self.txt_job_ref.setStyleSheet("""
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
        self.txt_job_ref.setPlaceholderText("")
        self.txt_job_ref.setObjectName("txt_job_ref")
       
        self.txt_rig_name = QtWidgets.QLineEdit(self.tab_report_information)
        self.txt_rig_name.setGeometry(QtCore.QRect(530, 140, 491, 41))
        self.txt_rig_name.setStyleSheet("""
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
        self.txt_rig_name.setPlaceholderText("")
        self.txt_rig_name.setObjectName("txt_rig_name")
       
        self.txt_field_location = QtWidgets.QLineEdit(self.tab_report_information)
        self.txt_field_location.setGeometry(QtCore.QRect(530, 230, 491, 41))
        self.txt_field_location.setStyleSheet("""
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
        self.txt_field_location.setPlaceholderText("")
        self.txt_field_location.setObjectName("txt_field_location")
       
        self.cbx_aproved_by = QtWidgets.QComboBox(self.tab_report_information)
        self.cbx_aproved_by.setGeometry(QtCore.QRect(10, 320, 491, 41))
        self.cbx_aproved_by.setPlaceholderText("")
        self.cbx_aproved_by.setObjectName("cbx_aproved_by")
        self.cbx_aproved_by.setStyleSheet("""
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
       
        self.txt_job_type = QtWidgets.QLineEdit(self.tab_report_information)
        self.txt_job_type.setGeometry(QtCore.QRect(530, 320, 491, 41))
        self.txt_job_type.setStyleSheet("""
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
        self.txt_job_type.setPlaceholderText("")
        self.txt_job_type.setObjectName("txt_job_type")
      
        

        #Botao Next Step para Avançar ao Report Information (Days)
        self.btn_report_information_next_step = QtWidgets.QPushButton(self.tab_report_information)
        self.btn_report_information_next_step.setGeometry(QtCore.QRect(10,410,491,41))
        self.btn_report_information_next_step.setObjectName("btn_report_information_next_step")
        self.btn_report_information_next_step.setStyleSheet("\n" "\n" "QPushButton#btn_report_information_next_step{\n" "\n" "border:none;\n" "background-color:#044e42;\n" "color:white;\n" "font-size:14px;\n" "border-radius: 6px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "text-align:rigth;\n" "}\n" "\n" "QPushButton#btn_report_information_next_step:hover{\n" " background-color: #044e42;\n" "border-radius: 6px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "}\n" "\n" "QPushButton#btn_report_information_next_step:pressed {\n" " background-color: #044e42;\n" "border-radius: 6px;\n" "background-color: #033029;\n" "padding:10px;\n" " }\n" "")
        self.btn_report_information_next_step.setText("Next Step")
        
       
        self.lbl_rig_name = QtWidgets.QLabel(self.tab_report_information)
        self.lbl_rig_name.setGeometry(QtCore.QRect(530, 110, 141, 31))
       
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
       
        self.lbl_rig_name.setFont(font)
        self.lbl_rig_name.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_rig_name.setObjectName("lbl_rig_name")
       
        self.lbl_field_location = QtWidgets.QLabel(self.tab_report_information)
        self.lbl_field_location.setGeometry(QtCore.QRect(530, 200, 141, 31))
        
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        
        self.lbl_field_location.setFont(font)
        self.lbl_field_location.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_field_location.setObjectName("lbl_field_location")
       
        self.lbl_job_type = QtWidgets.QLabel(self.tab_report_information)
        self.lbl_job_type.setGeometry(QtCore.QRect(530, 290, 91, 31))
       
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        
        self.lbl_job_type.setFont(font)
        self.lbl_job_type.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_job_type.setObjectName("lbl_job_type")
        
       
       
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
       
        
        
        self.lbl_approved_by = QtWidgets.QLabel(self.tab_report_information)
        self.lbl_approved_by.setGeometry(QtCore.QRect(10, 290, 101, 31))
        
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
       
        self.lbl_approved_by.setFont(font)
        self.lbl_approved_by.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_approved_by.setObjectName("lbl_approved_by")
        
        
       
        
       
        self.lbl_approved_by.raise_()
        self.lbl_job_type.raise_()
        self.lbl_field_location.raise_()
        self.lbl_rig_name.raise_()
        
        self.lbl_customer.raise_()
        self.cbx_customer.raise_()
       
        self.lbl_well_number.raise_()
        self.cbx_well_number.raise_()
       
        self.lbl_report_date.raise_()
        self.lbl_job_ref.raise_()
        self.txt_job_ref.raise_()
        self.txt_rig_name.raise_()
        self.txt_field_location.raise_()
        self.cbx_aproved_by.raise_()
        self.txt_job_type.raise_()
        self.dateEdit.raise_()
        
        self.tab_wbco_primary = QtWidgets.QWidget()
        self.tab_wbco_primary.setObjectName("tab_wbco_primary")
       
        self.cbx_thread_primary = QtWidgets.QComboBox(self.tab_wbco_primary)
        self.cbx_thread_primary.setGeometry(QtCore.QRect(10, 140, 491, 41))
        self.cbx_thread_primary.setStyleSheet("""
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
        self.cbx_thread_primary.setPlaceholderText("")
        self.cbx_thread_primary.setObjectName("cbx_thread_primary")
        self.cbx_thread_primary.addItems(modulo_wbco.threadController.listar_thread_para_combo())
       
        self.lbl_thread_conextions_box = QtWidgets.QLabel(self.tab_wbco_primary)
        self.lbl_thread_conextions_box.setGeometry(QtCore.QRect(10, 190, 231, 31))
        
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
       
        self.lbl_thread_conextions_box.setFont(font)
        self.lbl_thread_conextions_box.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_thread_conextions_box.setObjectName("lbl_thread_conextions_box")
        
        self.lbl_drift_size = QtWidgets.QLabel(self.tab_wbco_primary)
        self.lbl_drift_size.setGeometry(QtCore.QRect(530, 190, 81, 31))
        
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        
        self.lbl_drift_size.setFont(font)
        self.lbl_drift_size.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_drift_size.setObjectName("lbl_drift_size")
       
        self.lbl_thread_conections = QtWidgets.QLabel(self.tab_wbco_primary)
        self.lbl_thread_conections.setGeometry(QtCore.QRect(10, 110, 261, 31))
        
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
       
        self.lbl_thread_conections.setFont(font)
        self.lbl_thread_conections.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_thread_conections.setObjectName("lbl_thread_conections")
       
        self.lbl_od = QtWidgets.QLabel(self.tab_wbco_primary)
        self.lbl_od.setGeometry(QtCore.QRect(530, 110, 31, 31))
        
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        
        self.lbl_od.setFont(font)
        self.lbl_od.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_od.setObjectName("lbl_od")
       
        self.txt_id_primary = QtWidgets.QLineEdit(self.tab_wbco_primary)
        self.txt_id_primary.setGeometry(QtCore.QRect(530, 50, 491, 41))
        self.txt_id_primary.setStyleSheet("""
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
        self.txt_id_primary.setPlaceholderText("")
        self.txt_id_primary.setObjectName("txt_id_primary")
        
        self.txt_od_primary = QtWidgets.QLineEdit(self.tab_wbco_primary)
        self.txt_od_primary.setGeometry(QtCore.QRect(530, 140, 491, 41))
        self.txt_od_primary.setStyleSheet("""
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
        self.txt_od_primary.setPlaceholderText("")
        self.txt_od_primary.setObjectName("txt_od_primary")
       
        self.cbx_thread_connections_box = QtWidgets.QComboBox(self.tab_wbco_primary)
        self.cbx_thread_connections_box.setGeometry(QtCore.QRect(10, 220, 491, 41))
        self.cbx_thread_connections_box.setStyleSheet("""
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
        self.cbx_thread_connections_box.setObjectName("cbx_thread_connections_box")
        self.cbx_thread_connections_box.addItems(modulo_wbco.threadController.listar_thread_para_combo())
        
        self.txt_drift_primary = QtWidgets.QLineEdit(self.tab_wbco_primary)
        self.txt_drift_primary.setGeometry(QtCore.QRect(530, 220, 491, 41))
        self.txt_drift_primary.setStyleSheet("""
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
        self.txt_drift_primary.setPlaceholderText("")
        self.txt_drift_primary.setObjectName("txt_drift_primary")
       
        self.lbl_description = QtWidgets.QLabel(self.tab_wbco_primary)
        self.lbl_description.setGeometry(QtCore.QRect(10, 20, 101, 31))
       
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        
        self.lbl_description.setFont(font)
        self.lbl_description.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_description.setObjectName("lbl_description")
       
        self.lbl_id = QtWidgets.QLabel(self.tab_wbco_primary)
        self.lbl_id.setGeometry(QtCore.QRect(530, 20, 41, 31))
       
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        
        self.lbl_id.setFont(font)
        self.lbl_id.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_id.setObjectName("lbl_id")
       
        self.txt_description_primary = QtWidgets.QLineEdit(self.tab_wbco_primary)
        self.txt_description_primary.setGeometry(QtCore.QRect(10, 50, 491, 41))
        self.txt_description_primary.setStyleSheet("""
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
        self.txt_description_primary.setPlaceholderText("")
        self.txt_description_primary.setObjectName("txt_description_primary")
       
        self.btn_add_wbco_primary = QtWidgets.QPushButton(self.tab_wbco_primary)
        self.btn_add_wbco_primary.setGeometry(QtCore.QRect(10, 280, 491, 41))
        self.btn_add_wbco_primary.setStyleSheet("\n" "\n" "QPushButton#btn_add_wbco_primary{\n" "\n" "border:none;\n" "background-color:#044e42;\n" "color:white;\n" "font-size:14px;\n" "border-radius: 6px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "text-align:rigth;\n" "}\n" "\n" "QPushButton#btn_add_wbco_primary:hover{\n" " background-color: #044e42;\n" "border-radius: 6px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "}\n" "\n" "QPushButton#btn_add_wbco_primary:pressed {\n" " background-color: #044e42;\n" "border-radius: 6px;\n" "background-color: #033029;\n" "padding:10px;\n" " }\n" "")

        #Botao Next Step para Avançar ao Report Information (Days)
        self.btn_wbco_primary_next_step = QtWidgets.QPushButton(self.tab_wbco_primary)
        self.btn_wbco_primary_next_step.setGeometry(QtCore.QRect(530,280,491,41))
        self.btn_wbco_primary_next_step.setObjectName("btn_wbco_primary_next_step")
        self.btn_wbco_primary_next_step.setStyleSheet("\n" "\n" "QPushButton#btn_wbco_primary_next_step{\n" "\n" "border:none;\n" "background-color:#044e42;\n" "color:white;\n" "font-size:14px;\n" "border-radius: 6px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "text-align:rigth;\n" "}\n" "\n" "QPushButton#btn_wbco_primary_next_step:hover{\n" " background-color: #044e42;\n" "border-radius: 6px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "}\n" "\n" "QPushButton#btn_wbco_primary_next_step:pressed {\n" " background-color: #044e42;\n" "border-radius: 6px;\n" "background-color: #033029;\n" "padding:10px;\n" " }\n" "")
        self.btn_wbco_primary_next_step.setText("Next Step")
       
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("img/check-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
       
        self.btn_add_wbco_primary.setIcon(icon10)
        self.btn_add_wbco_primary.setObjectName("btn_add_wbco_primary")
       
        self.lbl_thread_conections.raise_()
        self.lbl_id.raise_()
        self.lbl_description.raise_()
        self.cbx_thread_primary.raise_()
        self.lbl_thread_conextions_box.raise_()
        self.lbl_drift_size.raise_()
        self.lbl_od.raise_()
        self.txt_id_primary.raise_()
        self.txt_od_primary.raise_()
        self.cbx_thread_connections_box.raise_()
        self.txt_drift_primary.raise_()
        self.txt_description_primary.raise_()
        self.btn_add_wbco_primary.raise_()
        
        
        self.tab_wbco_backup = QtWidgets.QWidget()
        self.tab_wbco_backup.setObjectName("tab_wbco_backup")
       
        self.cbx_thread_back_up = QtWidgets.QComboBox(self.tab_wbco_backup)
        self.cbx_thread_back_up.setGeometry(QtCore.QRect(10, 140, 491, 41))
        self.cbx_thread_back_up.setStyleSheet("""
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
        self.cbx_thread_back_up.setPlaceholderText("")
        self.cbx_thread_back_up.setObjectName("cbx_thread_back_up")
        self.cbx_thread_back_up.addItems(modulo_wbco.threadController.listar_thread_para_combo())
        
        self.lbl_drift_back_up = QtWidgets.QLabel(self.tab_wbco_backup)
        
        self.lbl_drift_back_up.setGeometry(QtCore.QRect(530, 190, 81, 31))
        
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        
        self.lbl_drift_back_up.setFont(font)
        self.lbl_drift_back_up.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_drift_back_up.setObjectName("lbl_drift_back_up")
       
        self.lbl_description_back_up = QtWidgets.QLabel(self.tab_wbco_backup)
        self.lbl_description_back_up.setGeometry(QtCore.QRect(10, 20, 101, 31))
        
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
       
        self.lbl_description_back_up.setFont(font)
        self.lbl_description_back_up.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_description_back_up.setObjectName("lbl_description_back_up")
       
        self.lbl_thread_conextions_box_back_up = QtWidgets.QLabel(self.tab_wbco_backup)
        self.lbl_thread_conextions_box_back_up.setGeometry(QtCore.QRect(10, 190, 331, 31))
       
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        
        self.lbl_thread_conextions_box_back_up.setFont(font)
        self.lbl_thread_conextions_box_back_up.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_thread_conextions_box_back_up.setObjectName("lbl_thread_conextions_box_back_up")
        
        self.txt_od_back_up = QtWidgets.QLineEdit(self.tab_wbco_backup)
        self.txt_od_back_up.setGeometry(QtCore.QRect(530, 140, 491, 41))
        self.txt_od_back_up.setStyleSheet("""
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
        self.txt_od_back_up.setPlaceholderText("")
        self.txt_od_back_up.setObjectName("txt_od_back_up")
        self.lbl_id_back_up = QtWidgets.QLabel(self.tab_wbco_backup)
        self.lbl_id_back_up.setGeometry(QtCore.QRect(530, 20, 31, 31))
       
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        
        self.lbl_id_back_up.setFont(font)
        self.lbl_id_back_up.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_id_back_up.setObjectName("lbl_id_back_up")
        
        self.cbx_thread_box_back_up = QtWidgets.QComboBox(self.tab_wbco_backup)
        self.cbx_thread_box_back_up.setGeometry(QtCore.QRect(10, 220, 491, 41))
        self.cbx_thread_box_back_up.setStyleSheet("""
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
        self.cbx_thread_box_back_up.setObjectName("cbx_thread_box_back_up")
        self.cbx_thread_box_back_up.addItems(modulo_wbco.threadController.listar_thread_para_combo())
        
        self.lbl_thread_back_up = QtWidgets.QLabel(self.tab_wbco_backup)
        self.lbl_thread_back_up.setGeometry(QtCore.QRect(10, 110, 261, 31))
        
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        
        self.lbl_thread_back_up.setFont(font)
        self.lbl_thread_back_up.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_thread_back_up.setObjectName("lbl_thread_back_up")
        
        self.txt_description_back_up = QtWidgets.QLineEdit(self.tab_wbco_backup)
        self.txt_description_back_up.setGeometry(QtCore.QRect(10, 50, 491, 41))
        self.txt_description_back_up.setStyleSheet("""
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
        self.txt_description_back_up.setPlaceholderText("")
        self.txt_description_back_up.setObjectName("txt_description_back_up")
       
        self.lbl_od_back_up = QtWidgets.QLabel(self.tab_wbco_backup)
        self.lbl_od_back_up.setGeometry(QtCore.QRect(530, 110, 31, 31))
        
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        
        self.lbl_od_back_up.setFont(font)
        self.lbl_od_back_up.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_od_back_up.setObjectName("lbl_od_back_up")
        self.txt_id_back_up = QtWidgets.QLineEdit(self.tab_wbco_backup)
        self.txt_id_back_up.setGeometry(QtCore.QRect(530, 50, 491, 41))
        self.txt_id_back_up.setStyleSheet("""
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
        self.txt_id_back_up.setPlaceholderText("")
        self.txt_id_back_up.setObjectName("txt_id_back_up")
        
        self.txt_drift_back_up = QtWidgets.QLineEdit(self.tab_wbco_backup)
        self.txt_drift_back_up.setGeometry(QtCore.QRect(530, 220, 491, 41))
        self.txt_drift_back_up.setStyleSheet("""
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
        self.txt_drift_back_up.setPlaceholderText("")
        self.txt_drift_back_up.setObjectName("txt_drift_back_up")
        
        self.btn_add_wbco_on_bord = QtWidgets.QPushButton(self.tab_wbco_backup)
        self.btn_add_wbco_on_bord.setGeometry(QtCore.QRect(10, 280, 491, 41))
        self.btn_add_wbco_on_bord.setStyleSheet("\n" "\n" "QPushButton#btn_add_wbco_on_bord{\n" "\n" "border:none;\n" "background-color:#044e42;\n" "color:white;\n" "font-size:14px;\n" "border-radius: 6px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "text-align:rigth;\n" "}\n" "\n" "QPushButton#btn_add_wbco_on_bord:hover{\n" " background-color: #044e42;\n" "border-radius: 6px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "}\n" "\n" "QPushButton#btn_add_wbco_on_bord:pressed {\n" " background-color: #044e42;\n" "border-radius: 6px;\n" "background-color: #033029;\n" "padding:10px;\n" " }\n" "")
        self.btn_add_wbco_on_bord.setIcon(icon10)
        self.btn_add_wbco_on_bord.setObjectName("btn_add_wbco_on_bord")

        #Botao Next Step para Avançar ao Report Information (Days)
        self.btn_gerate_report = QtWidgets.QPushButton(self.tab_wbco_backup)
        self.btn_gerate_report.setGeometry(QtCore.QRect(530,280,491,41))
        self.btn_gerate_report.setObjectName("btn_gerate_report")
        self.btn_gerate_report.setStyleSheet("\n" "\n" "QPushButton#btn_gerate_report{\n" "\n" "border:none;\n" "background-color:#044e42;\n" "color:white;\n" "font-size:14px;\n" "border-radius: 6px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "text-align:rigth;\n" "}\n" "\n" "QPushButton#btn_gerate_report:hover{\n" " background-color: #044e42;\n" "border-radius: 6px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "}\n" "\n" "QPushButton#btn_gerate_report:pressed {\n" " background-color: #044e42;\n" "border-radius: 6px;\n" "background-color: #033029;\n" "padding:10px;\n" " }\n" "")
        self.btn_gerate_report.setText("Gerate Report")
        
        
        self.lbl_thread_back_up.raise_()
        self.lbl_od_back_up.raise_()
        self.cbx_thread_back_up.raise_()
        self.lbl_drift_back_up.raise_()
        self.lbl_description_back_up.raise_()
        self.lbl_thread_conextions_box_back_up.raise_()
        self.txt_od_back_up.raise_()
        self.lbl_id_back_up.raise_()
        self.cbx_thread_box_back_up.raise_()
        self.txt_description_back_up.raise_()
        self.txt_id_back_up.raise_()
        self.txt_drift_back_up.raise_()
        self.btn_add_wbco_on_bord.raise_()
        
        self.tab_well_information = QtWidgets.QWidget()
        self.tab_well_information.setObjectName("tab_well_information")
        
        self.lbl_casing_size_2 = QtWidgets.QLabel(self.tab_well_information)
        self.lbl_casing_size_2.setGeometry(QtCore.QRect(10, 20, 191, 31))
        
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        
        self.lbl_casing_size_2.setFont(font)
        self.lbl_casing_size_2.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_casing_size_2.setObjectName("lbl_casing_size_2")
        
        self.lbl_length = QtWidgets.QLabel(self.tab_well_information)
        self.lbl_length.setGeometry(QtCore.QRect(10, 110, 61, 31))
       
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        
        self.lbl_length.setFont(font)
        self.lbl_length.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_length.setObjectName("lbl_length")
        self.txt_length = QtWidgets.QLineEdit(self.tab_well_information)
        self.txt_length.setGeometry(QtCore.QRect(10, 140, 491, 41))
        self.txt_length.setStyleSheet("""
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
        self.txt_length.setPlaceholderText("")
        self.txt_length.setObjectName("txt_length")
       
        self.cbx_od = QtWidgets.QComboBox(self.tab_well_information)
        self.cbx_od.setGeometry(QtCore.QRect(10, 230, 491, 41))
        self.cbx_od.setStyleSheet("""
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
        self.cbx_od.setPlaceholderText("")
        self.cbx_od.setObjectName("cbx_od")
        self.cbx_od.addItems(modulo_wbco.sizeController.listar_size_para_combo())
       
        self.lbl_od_well = QtWidgets.QLabel(self.tab_well_information)
        self.lbl_od_well.setGeometry(QtCore.QRect(10, 200, 31, 31))
        
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        
        self.lbl_od_well.setFont(font)
        self.lbl_od_well.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_od_well.setObjectName("lbl_od_well")
        
        self.txt_id = QtWidgets.QLineEdit(self.tab_well_information)
        self.txt_id.setGeometry(QtCore.QRect(530, 50, 491, 41))
        self.txt_id.setStyleSheet("""
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
        self.txt_id.setPlaceholderText("")
        self.txt_id.setObjectName("txt_id")

        #Botao Next Step para Avançar ao Tab WBCO Tools Enginer (Days)
        self.btn_well_inf_next_step = QtWidgets.QPushButton(self.tab_well_information)
        self.btn_well_inf_next_step.setGeometry(QtCore.QRect(10, 320,491,41))
        self.btn_well_inf_next_step.setObjectName("btn_well_inf_next_step")
        self.btn_well_inf_next_step.setStyleSheet("\n" "\n" "QPushButton#btn_well_inf_next_step{\n" "\n" "border:none;\n" "background-color:#044e42;\n" "color:white;\n" "font-size:14px;\n" "border-radius: 6px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "text-align:rigth;\n" "}\n" "\n" "QPushButton#btn_well_inf_next_step:hover{\n" " background-color: #044e42;\n" "border-radius: 6px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "}\n" "\n" "QPushButton#btn_well_inf_next_step:pressed {\n" " background-color: #044e42;\n" "border-radius: 6px;\n" "background-color: #033029;\n" "padding:10px;\n" " }\n" "")
        self.btn_well_inf_next_step.setText("Next Step")
        

        
        self.lbl_id_well = QtWidgets.QLabel(self.tab_well_information)
        self.lbl_id_well.setGeometry(QtCore.QRect(530, 20, 41, 31))
       
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        
        self.lbl_id_well.setFont(font)
        self.lbl_id_well.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_id_well.setObjectName("lbl_id_well")
       
        self.cbx_size = QtWidgets.QComboBox(self.tab_well_information)
        self.cbx_size.setGeometry(QtCore.QRect(10, 50, 491, 41))
        self.cbx_size.setStyleSheet("""
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
        self.cbx_size.setObjectName("cbx_size")
        self.cbx_size.addItems(modulo_wbco.sizeController.listar_size_para_combo())
        
        
        
        
        self.lbl_weight = QtWidgets.QLabel(self.tab_well_information)
        self.lbl_weight.setGeometry(QtCore.QRect(530, 110, 141, 31))
        
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        
        self.lbl_weight.setFont(font)
        self.lbl_weight.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_weight.setObjectName("lbl_weight")
        
        self.txt_weigth_range = QtWidgets.QLineEdit(self.tab_well_information)
        self.txt_weigth_range.setGeometry(QtCore.QRect(530, 140, 491, 41))
        self.txt_weigth_range.setStyleSheet("""
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
        self.txt_weigth_range.setPlaceholderText("")
        self.txt_weigth_range.setObjectName("txt_weigth_range")
        
        self.lbl_volume_capacity = QtWidgets.QLabel(self.tab_well_information)
        self.lbl_volume_capacity.setGeometry(QtCore.QRect(530, 200, 141, 31))
        
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        
        self.lbl_volume_capacity.setFont(font)
        self.lbl_volume_capacity.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_volume_capacity.setObjectName("lbl_volume_capacity")
        self.txt_volume_capacity = QtWidgets.QLineEdit(self.tab_well_information)
        self.txt_volume_capacity.setGeometry(QtCore.QRect(530, 230, 491, 41))
        self.txt_volume_capacity.setStyleSheet("""
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
        self.txt_volume_capacity.setPlaceholderText("")
        self.txt_volume_capacity.setObjectName("txt_volume_capacity")
        
        self.lbl_hole_volume = QtWidgets.QLabel(self.tab_well_information)
        self.lbl_hole_volume.setGeometry(QtCore.QRect(530, 290, 111, 31))
        
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
       
        self.lbl_hole_volume.setFont(font)
        self.lbl_hole_volume.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_hole_volume.setObjectName("lbl_hole_volume")
        self.cbx_hole_volume = QtWidgets.QComboBox(self.tab_well_information)
        self.cbx_hole_volume.setGeometry(QtCore.QRect(530, 320, 491, 41))
        self.cbx_hole_volume.setObjectName("cbx_hole_volume")
        self.cbx_hole_volume.addItems(["bbls","m3"])
        self.cbx_hole_volume.setStyleSheet("""
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
        
      
        self.lbl_id_well.raise_()
        self.lbl_od_well.raise_()
        self.lbl_casing_size_2.raise_()
        
        self.lbl_length.raise_()
        self.txt_length.raise_()
        
        self.cbx_od.raise_()
        self.txt_id.raise_()
        self.cbx_size.raise_()
        self.lbl_weight.raise_()
        self.txt_weigth_range.raise_()
        self.lbl_volume_capacity.raise_()
        self.txt_volume_capacity.raise_()
        self.lbl_hole_volume.raise_()
        self.cbx_hole_volume.raise_()
        
        self.tab_activity = QtWidgets.QWidget()
        self.tab_activity.setObjectName("tab_activity")
        
        self.txt_area_on_going = QtWidgets.QPlainTextEdit(self.tab_activity)
        self.txt_area_on_going.setGeometry(QtCore.QRect(10, 53, 1061, 140))
        self.txt_area_on_going.setStyleSheet("background-color:#fff;\n" "border: 1px solid #8ec0af;\n" "border-radius: 6px")
        self.txt_area_on_going.setObjectName("txt_area_on_going")
        
        self.txt_wbco_activity = QtWidgets.QPlainTextEdit(self.tab_activity)
        self.txt_wbco_activity.setGeometry(QtCore.QRect(10, 250, 1061, 140))
        self.txt_wbco_activity.setStyleSheet("background-color:#fff;\n" "border: 1px solid #8ec0af;\n" "border-radius: 6px")
        self.txt_wbco_activity.setObjectName("txt_wbco_activity")
       
        self.lbl_ongoing_rig_activity = QtWidgets.QLabel(self.tab_activity)
        self.lbl_ongoing_rig_activity.setGeometry(QtCore.QRect(10, 20, 171, 31))
        
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
       
        self.lbl_ongoing_rig_activity.setFont(font)
        self.lbl_ongoing_rig_activity.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_ongoing_rig_activity.setObjectName("lbl_ongoing_rig_activity")
        
        self.lbl_wbco_activity = QtWidgets.QLabel(self.tab_activity)
        self.lbl_wbco_activity.setGeometry(QtCore.QRect(10, 220, 171, 31))
        
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        
        self.lbl_wbco_activity.setFont(font)
        self.lbl_wbco_activity.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_wbco_activity.setObjectName("lbl_wbco_activity")
        self.lbl_wbco_activity.raise_()
        
        self.lbl_ongoing_rig_activity.raise_()
        self.txt_area_on_going.raise_()
        self.txt_wbco_activity.raise_()

        #Botao Next Step para Avançar ao Report Information (Days)
        self.btn_activity_next_step = QtWidgets.QPushButton(self.tab_activity)
        self.btn_activity_next_step.setGeometry(QtCore.QRect(10,400,491,41))
        self.btn_activity_next_step.setObjectName("btn_activity_next_step")
        self.btn_activity_next_step.setStyleSheet("\n" "\n" "QPushButton#btn_activity_next_step{\n" "\n" "border:none;\n" "background-color:#044e42;\n" "color:white;\n" "font-size:14px;\n" "border-radius: 6px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "text-align:rigth;\n" "}\n" "\n" "QPushButton#btn_activity_next_step:hover{\n" " background-color: #044e42;\n" "border-radius: 6px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "}\n" "\n" "QPushButton#btn_activity_next_step:pressed {\n" " background-color: #044e42;\n" "border-radius: 6px;\n" "background-color: #033029;\n" "padding:10px;\n" " }\n" "")
        self.btn_activity_next_step.setText("Next Step")
        
       
        self.tab_wbco_engineer = QtWidgets.QWidget()
        self.tab_wbco_engineer.setObjectName("tab_wbco_engineer")
       
        self.lbl_supervisor = QtWidgets.QLabel(self.tab_wbco_engineer)
        self.lbl_supervisor.setGeometry(QtCore.QRect(10, 40, 201, 31))
       
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
       
        self.lbl_supervisor.setFont(font)
        self.lbl_supervisor.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_supervisor.setObjectName("lbl_supervisor")
        
        self.lbl_wbco_tool_enginer_supervisor = QtWidgets.QLabel(self.tab_wbco_engineer)
        self.lbl_wbco_tool_enginer_supervisor.setGeometry(QtCore.QRect(10, 100, 171, 31))
        
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        
        self.lbl_wbco_tool_enginer_supervisor.setFont(font)
        self.lbl_wbco_tool_enginer_supervisor.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_wbco_tool_enginer_supervisor.setObjectName("lbl_wbco_tool_enginer_supervisor")
        
        self.cbx_enginer_supervisor = QtWidgets.QComboBox(self.tab_wbco_engineer)
        self.cbx_enginer_supervisor.setGeometry(QtCore.QRect(10, 130, 491, 41))
        self.cbx_enginer_supervisor.setStyleSheet("""
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
        self.cbx_enginer_supervisor.setObjectName("cbx_enginer_supervisor")
        
        
        
        self.lbl_shift_supervisor = QtWidgets.QLabel(self.tab_wbco_engineer)
        self.lbl_shift_supervisor.setGeometry(QtCore.QRect(10, 190, 61, 31))

        
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        
        self.lbl_shift_supervisor.setFont(font)
        self.lbl_shift_supervisor.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_shift_supervisor.setObjectName("lbl_shift_supervisor")
        self.cbx_shitf_supervisor = QtWidgets.QComboBox(self.tab_wbco_engineer)
        self.cbx_shitf_supervisor.setGeometry(QtCore.QRect(10, 220, 491, 41))
        self.cbx_shitf_supervisor.setStyleSheet("""
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
        self.cbx_shitf_supervisor.setObjectName("cbx_shitf_supervisor")
        self.cbx_shitf_supervisor.addItem("Days")
        self.cbx_shitf_supervisor.addItem("Night")

        
       
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
       
        
        self.lbl_techinical = QtWidgets.QLabel(self.tab_wbco_engineer)
        self.lbl_techinical.setGeometry(QtCore.QRect(560, 40, 201, 31))
        
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        
        self.lbl_techinical.setFont(font)
        self.lbl_techinical.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_techinical.setObjectName("lbl_techinical")
        
        self.cbx_enginer_techinical = QtWidgets.QComboBox(self.tab_wbco_engineer)
        self.cbx_enginer_techinical.setGeometry(QtCore.QRect(560, 130, 491, 41))
        self.cbx_enginer_techinical.setObjectName("cbx_enginer_techinical")
        self.cbx_enginer_techinical.setStyleSheet("""
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


        self.lbl_shift_techinical = QtWidgets.QLabel(self.tab_wbco_engineer)
        self.lbl_shift_techinical.setGeometry(QtCore.QRect(560, 190, 41, 31))
        
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        
        self.lbl_shift_techinical.setFont(font)
        self.lbl_shift_techinical.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_shift_techinical.setObjectName("lbl_shift_techinical")
        
        
        
        self.lbl_wbco_tool_enginer_techinical = QtWidgets.QLabel(self.tab_wbco_engineer)
        self.lbl_wbco_tool_enginer_techinical.setGeometry(QtCore.QRect(560, 100, 171, 31))
        
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        
        self.lbl_wbco_tool_enginer_techinical.setFont(font)
        self.lbl_wbco_tool_enginer_techinical.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_wbco_tool_enginer_techinical.setObjectName("lbl_wbco_tool_enginer_techinical")
        
        self.cdx_shift_techinical = QtWidgets.QComboBox(self.tab_wbco_engineer)
        self.cdx_shift_techinical.setGeometry(QtCore.QRect(560, 220, 491, 41))
        self.cdx_shift_techinical.setStyleSheet("""
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
        self.cdx_shift_techinical.setObjectName("cdx_shift_techinical")
        self.cdx_shift_techinical.addItems(["Days","Night"])
        
       
        
        #self.btn_gerar_report = QtWidgets.QPushButton(self.tab_wbco_engineer)
        #self.btn_gerar_report.setGeometry(QtCore.QRect(10, 380, 251, 51))
        #self.btn_gerar_report.setStyleSheet("\n" "\n" "QPushButton#btn_gerar_report{\n" "\n" "border:none;\n" "background-color:#044e42;\n" "color:white;\n" "font-size:14px;\n" "border-radius: 6px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "text-align:rigth;\n" "}\n" "\n" "QPushButton#btn_gerar_report:hover{\n" " background-color: #044e42;\n" "border-radius: 6px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "}\n" "\n" "QPushButton#btn_gerar_report:pressed {\n" " background-color: #044e42;\n" "border-radius: 6px;\n" "background-color: #033029;\n" "padding:10px;\n" " }\n" "")
        #self.btn_gerar_report.setIcon(icon9)
        #self.btn_gerar_report.setObjectName("btn_gerar_report")

        #Botao Next Step para Avançar ao Report Information (Days)
        self.btn_wbco_enginner_next_step = QtWidgets.QPushButton(self.tab_wbco_engineer)
        self.btn_wbco_enginner_next_step.setGeometry(QtCore.QRect(10,400,491,41))
        self.btn_wbco_enginner_next_step.setObjectName("btn_wbco_enginner_next_step")
        self.btn_wbco_enginner_next_step.setStyleSheet("\n" "\n" "QPushButton#btn_wbco_enginner_next_step{\n" "\n" "border:none;\n" "background-color:#044e42;\n" "color:white;\n" "font-size:14px;\n" "border-radius: 6px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "text-align:rigth;\n" "}\n" "\n" "QPushButton#btn_wbco_enginner_next_step:hover{\n" " background-color: #044e42;\n" "border-radius: 6px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "}\n" "\n" "QPushButton#btn_wbco_enginner_next_step:pressed {\n" " background-color: #044e42;\n" "border-radius: 6px;\n" "background-color: #033029;\n" "padding:10px;\n" " }\n" "")
        self.btn_wbco_enginner_next_step.setText("Next Step")
        
        self.lbl_wbco_tool_enginer_techinical.raise_()

        self.lbl_supervisor.raise_()
        self.lbl_wbco_tool_enginer_supervisor.raise_()
        self.cbx_enginer_supervisor.raise_()
        self.lbl_shift_supervisor.raise_()
        self.cbx_shitf_supervisor.raise_()
        
       
        self.lbl_techinical.raise_()
        self.cbx_enginer_techinical.raise_()
        self.lbl_shift_techinical.raise_()
        self.cdx_shift_techinical.raise_()
        #self.btn_gerar_report.raise_()

        self.tab_menus_wbco.addTab(self.tab_report_information, "")
        self.tab_menus_wbco.addTab(self.tab_well_information, "")
        self.tab_menus_wbco.addTab(self.tab_wbco_engineer, "")
        self.tab_menus_wbco.addTab(self.tab_activity, "")
        self.tab_menus_wbco.addTab(self.tab_wbco_primary, "")
        self.tab_menus_wbco.addTab(self.tab_wbco_backup, "")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1400, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tab_menus_wbco.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add New WBCO Daily Report"))
        self.btn_dashboard.setText(_translate("MainWindow", " Dashboard"))
        self.btn_dashboard.clicked.connect(lambda:show_form_dashboard())
        self.btn_compliance.setText(_translate("MainWindow", " A. M. Compliance"))
        self.btn_wbco.setText(_translate("MainWindow", " WBCO Tools"))
        self.btn_filtration.setText(_translate("MainWindow", " Filtration"))
        self.btn_tank_cleaning.setText(_translate("MainWindow", " Tank Cleaning"))
        self.btn_user_profile.setText(_translate("MainWindow", "User Profile"))
        self.btn_logout.setText(_translate("MainWindow", "Logout"))
        self.btn_logout.clicked.connect(lambda:logout())
        self.btn_user.setText(_translate("MainWindow", " Personnel"))
        self.btn_user.clicked.connect(lambda: call_form_user())
        self.btn_customer.setText(_translate("MainWindow", "Customers"))
        self.btn_customer.clicked.connect(lambda:call_form_client())
        self.lbl_form_tittle.setText(_translate("MainWindow", "WBCO - Add new Report"))
        self.lbl_form_text.setText(_translate("MainWindow", "Below are the fields to be filled in to generate a new report"))
        
        self.btn_list_report.setText(_translate("MainWindow", "List all report"))
        self.btn_list_report.clicked.connect(lambda: call_form_wbco_list())

        self.cbx_customer.textActivated.connect(lambda: getPoco(self.cbx_customer.currentText()))
        
        self.lbl_customer.setText(_translate("MainWindow", "Customers"))
        self.lbl_well_number.setText(_translate("MainWindow", "Well Number"))
        self.lbl_report_date.setText(_translate("MainWindow", "Report Date"))
        self.lbl_job_ref.setText(_translate("MainWindow", "Job Ref. Number"))
        self.lbl_rig_name.setText(_translate("MainWindow", "Rig Name"))
        self.lbl_field_location.setText(_translate("MainWindow", "Field/Location"))
        self.lbl_job_type.setText(_translate("MainWindow", "Job Type"))
        self.lbl_approved_by.setText(_translate("MainWindow", "Approved By"))
        self.tab_menus_wbco.setTabText(self.tab_menus_wbco.indexOf(self.tab_report_information), _translate("MainWindow", "Report Information"))
        self.lbl_thread_conextions_box.setText(_translate("MainWindow", "Thread Connections (BOX)"))
        self.lbl_drift_size.setText(_translate("MainWindow", "Drift Size"))
        self.lbl_thread_conections.setText(_translate("MainWindow", "Thread Connections (PIN)"))
        self.lbl_od.setText(_translate("MainWindow", "OD"))
        self.lbl_description.setText(_translate("MainWindow", "Description"))
        self.lbl_id.setText(_translate("MainWindow", "ID"))

        self.btn_add_wbco_primary.setText(_translate("MainWindow", " Add the filled information"))
        self.btn_add_wbco_primary.clicked.connect(lambda: validatoin_wbco_primary())

        self.tab_menus_wbco.setTabText(self.tab_menus_wbco.indexOf(self.tab_wbco_primary), _translate("MainWindow", "WBCO Tools On Board (Primary)"))
        self.lbl_drift_back_up.setText(_translate("MainWindow", "Drift Size"))
        self.lbl_description_back_up.setText(_translate("MainWindow", "Description"))
        self.lbl_thread_conextions_box_back_up.setText(_translate("MainWindow", "Thread Connections (BOX)"))
        self.lbl_id_back_up.setText(_translate("MainWindow", "ID"))
        self.lbl_thread_back_up.setText(_translate("MainWindow", "Thread Connections (PIN)"))
        self.lbl_od_back_up.setText(_translate("MainWindow", "OD"))
        
        self.btn_add_wbco_on_bord.setText(_translate("MainWindow", " Add the filled information"))
        self.btn_add_wbco_on_bord.clicked.connect(lambda:validatoin_wbco_backup())

        self.tab_menus_wbco.setTabText(self.tab_menus_wbco.indexOf(self.tab_wbco_backup), _translate("MainWindow", "WBCO Tools  On board (Back Up)"))
        self.lbl_casing_size_2.setText(_translate("MainWindow", "Casing Size"))
        self.lbl_length.setText(_translate("MainWindow", "Length"))
        self.lbl_od_well.setText(_translate("MainWindow", "OD"))
        self.lbl_id_well.setText(_translate("MainWindow", "ID"))
        self.lbl_weight.setText(_translate("MainWindow", "Weight Range"))
        self.lbl_volume_capacity.setText(_translate("MainWindow", "Volume Capacity"))
        self.lbl_hole_volume.setText(_translate("MainWindow", "Hole Volume"))
        self.tab_menus_wbco.setTabText(self.tab_menus_wbco.indexOf(self.tab_well_information), _translate("MainWindow", "Well Information"))
        self.txt_area_on_going.setPlaceholderText(_translate("MainWindow", " Write here..."))
        self.txt_wbco_activity.setPlaceholderText(_translate("MainWindow", " Write here..."))
        self.lbl_ongoing_rig_activity.setText(_translate("MainWindow", "Ongoing Rig Activity"))
        self.lbl_wbco_activity.setText(_translate("MainWindow", "WBCO Tools Activity"))
        self.tab_menus_wbco.setTabText(self.tab_menus_wbco.indexOf(self.tab_activity), _translate("MainWindow", "Activity"))
        self.lbl_supervisor.setText(_translate("MainWindow", "Supervisor Information"))
        self.lbl_wbco_tool_enginer_supervisor.setText(_translate("MainWindow", "WBCO Tools Enginer "))
        self.lbl_shift_supervisor.setText(_translate("MainWindow", "Shift"))
        self.lbl_techinical.setText(_translate("MainWindow", "Technician Information"))
        self.lbl_shift_techinical.setText(_translate("MainWindow", "Shift"))
        self.lbl_wbco_tool_enginer_techinical.setText(_translate("MainWindow", "WBCO Tools Enginer "))
       
        #self.btn_gerar_report.setText(_translate("MainWindow", "Generate report"))
        self.btn_wbco_primary_next_step.clicked.connect(lambda: get_next_tab())
        self.btn_report_information_next_step.clicked.connect(lambda: validator_report_information())
        self.btn_well_inf_next_step.clicked.connect(lambda:validatoin_well_information())
        self.btn_wbco_enginner_next_step.clicked.connect(lambda:validatoin_wbco_enginer())
        self.btn_activity_next_step.clicked.connect(lambda:validatoin_activity())
        self.tab_menus_wbco.setTabText(self.tab_menus_wbco.indexOf(self.tab_wbco_engineer), _translate("MainWindow", "WBCO Tools Engineer (Daily)"))
        
        self.btn_gerate_report.setText(_translate("MainWindow", " Gerate a Report"))
        self.btn_gerate_report.clicked.connect(lambda:report())

        self.cbx_enginer_supervisor.currentTextChanged.connect(lambda:buscar_dia_supervisor())

        def show_message_sucess():
            msg_error = QMessageBox()
            msg_error.setIcon(QMessageBox.Information)
            msg_error.setText('Report was generated successfully')
            msg_error.setWindowTitle('Report generation')
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("img/sucess_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg_error.setWindowIcon(icon)
            msg_error.exec_()

        def show_message_sucess_validator(tittle_windows,tittle_message):
            msg_error = QMessageBox()
            msg_error.setIcon(QMessageBox.Information)
            msg_error.setText(tittle_message)
            msg_error.setWindowTitle(tittle_windows)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("img/sucess_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg_error.setWindowIcon(icon)
            msg_error.exec_()

        def buscar_dia_supervisor():
            id_supervisor = modulo_wbco.wbcoController.carregar_id_supervisor_by_email(self.lbl_user_logado.text())
            print(modulo_wbco.wbcoController.buscar_total_days_supervisor(self.txt_job_ref.text(),id_supervisor)) 
    
        def report():

            value_well_information = modulo_wbco.wbcoController.carregar_well_information()
            filemane = "Daily_Report_"+str(value_well_information[8])+"_WBCO_Tools_Service.pdf"
            
            
            self.gerador_report.gerar_pdf(filemane)
            show_message_sucess()

        def get_next_tab():
            self.tab_menus_wbco.setCurrentIndex(5)

        def carregar_supervisor():
            self.cbx_enginer_supervisor.addItems(modulo_wbco.wbcoController.carregar_supervisor())

        def carregar_cliente():
            self.cbx_customer.addItems(modulo_wbco.wbcoController.carregar_cliente())

        def carregar_engenheiro_tecnico():
            self.cbx_enginer_techinical.addItems(modulo_wbco.wbcoController.carregar_tecnico())

        def carregar_person_aproved():
            self.cbx_aproved_by.addItems(modulo_wbco.wbcoController.carregar_tecnico())

        def getPoco(cliente):
            self.cbx_well_number.clear()
            well_number_items = modulo_wbco.wbcoController.carregar_poco(cliente)
            self.cbx_well_number.addItems(well_number_items)


        carregar_cliente()
        carregar_supervisor()
        carregar_engenheiro_tecnico()
        carregar_person_aproved()

        def validator_report_information():

            countVezes = False

            caracter_especial = '1234567890!#$%&/=?*+ªº^~-"'
            only_special_character = '!#$%&/=?*+ªº^~-"'

            # Text Rig Name
            txt_rig = str(self.txt_rig_name.text())
            txt_job_type = str(self.txt_job_type.text())
            txt_field_location = str(self.txt_field_location.text())
            cbx_aproved_by = str(self.cbx_aproved_by.currentText())

            

            def has_special_characters(input_str, special_chars):
                for char in input_str:
                    if char in special_chars:
                        return True
                return False

            if has_special_characters(txt_rig, caracter_especial) or (txt_rig == ""):
                message_error_validation("This field does not accept special characters or is empty", "Input Rig Name Error")
            
            elif has_special_characters(txt_field_location,only_special_character) or (txt_field_location == ""):
                message_error_validation("This field does not accept special characters or is empty", "Field Location entry Error")
            
            elif has_special_characters(txt_job_type, caracter_especial) or (txt_job_type == ""):
                message_error_validation("This field does not accept special characters or is empty", "Job Type entry error")
            
            elif has_special_characters(cbx_aproved_by,caracter_especial) or (cbx_aproved_by == ""):
                message_error_validation("This field does not accept special characters or is empty", "Error inserting person who approves")
            else:
                show_message_sucess_validator("Report Information","This data was entry Sucessful")
                self.tab_menus_wbco.setCurrentIndex(1)

        def validatoin_wbco_primary():

            caracter_especial = '1234567890!#$%&/=?*+ªº^~-"'
            only_special_character = '!#$%&/=?*+ªº^~-"'

            txt_description_primary = str(self.txt_description_primary.text())
            cbx_thread_primary = str(self.cbx_thread_primary.currentText())
            txt_id_primary = str(self.txt_id_primary.text())
            txt_od_primary =  str(self.txt_od_primary.text())
            txt_drift_primary = str(self.txt_drift_primary.text())

            def has_special_characters(input_str, special_chars):
                for char in input_str:
                    if char in special_chars:
                        return True
                return False
            
            if has_special_characters(txt_description_primary,only_special_character) or (txt_description_primary == ""):
                message_error_validation("This field does not accept characters or is empty","Description entry error")
            elif cbx_thread_primary == "":
                message_error_validation("This filed does not accept characters empty","Thread entry error")
            elif txt_od_primary == "":
                message_error_validation("This field does not accept characters empty","OD entry error")
            elif txt_id_primary == "":
                message_error_validation("This field does not accept characters empty","ID entry error")
            elif txt_drift_primary == "":
                message_error_validation("This field does not accept characters empty","Drift entry error")
            else:
                
                id_supervisor = modulo_wbco.wbcoController.carregar_id_supervisor_by_email(self.lbl_user_logado.text())
                id_ultimo_report = modulo_wbco.wbcoController.carregar_buscar_id_report()

                id_thread_connections_box = modulo_wbco.threadController.buscar_id_by_tch(self.cbx_thread_connections_box.currentText())
                id_thread_primary = modulo_wbco.threadController.buscar_id_by_tch(self.cbx_thread_primary.currentText())

                valor_wbco_primary = modulo_wbco.wbcoController.salvar_wbco_primary(txt_description_primary,id_thread_connections_box,id_thread_primary,
                                    txt_od_primary,txt_id_primary,txt_drift_primary,id_supervisor,id_ultimo_report)
                if valor_wbco_primary == 0:
                    self.txt_description_primary.clear()
                    self.txt_id_primary.clear()
                    self.txt_od_primary.clear()
                    self.txt_drift_primary.clear()

                    show_message_sucess_validator("WBCO On Board "," Data was entry sucessful")

                else:
                    message_error_validation("WBCO On Board","Data was entry Error")


        def validatoin_wbco_backup():

            caracter_especial = '1234567890!#$%&/=?*+ªº^~-"'
            only_special_character = '!#$%&/=?*+ªº^~-"'

            txt_description_back_up = str(self.txt_description_back_up.text())
            cbx_thread_back_up = str(self.cbx_thread_back_up.currentText())
            txt_id_back_up = str(self.txt_id_back_up.text())
            txt_od_back_up =  str(self.txt_od_back_up.text())
            txt_drift_back_up = str(self.txt_drift_back_up.text())

            def has_special_characters(input_str, special_chars):
                for char in input_str:
                    if char in special_chars:
                        return True
                return False
            
            if has_special_characters(txt_description_back_up,only_special_character) or (txt_description_back_up == ""):
                message_error_validation("This field does not accept characters or is empty","Description entry error")
            elif cbx_thread_back_up == "":
                message_error_validation("This filed does not accept characters empty","Thread entry error")
            elif txt_od_back_up == "":
                message_error_validation("This field does not accept characters empty","OD entry error")
            elif txt_id_back_up == "":
                message_error_validation("This field does not accept characters empty","ID entry error")
            elif txt_drift_back_up == "":
                message_error_validation("This field does not accept characters empty","Drift entry error")
            else:

                id_thread_backup = modulo_wbco.threadController.buscar_id_by_tch(cbx_thread_back_up)
                id_thread_backup_box = modulo_wbco.threadController.buscar_id_by_tch(self.cbx_thread_connections_box.currentText())

                id_supervisor = modulo_wbco.wbcoController.carregar_id_supervisor_by_email(self.lbl_user_logado.text())
                id_ultimo_report = modulo_wbco.wbcoController.carregar_buscar_id_report()
                valor_wbco_backup = modulo_wbco.wbcoController.salvar_wbco_backup(txt_description_back_up,id_thread_backup_box,id_thread_backup,
                                    txt_od_back_up,txt_id_back_up,txt_drift_back_up,id_supervisor,id_ultimo_report)
                if valor_wbco_backup == 0:
                   
                    self.txt_description_back_up.clear()
                    self.txt_id_back_up.clear()
                    self.txt_od_back_up.clear()
                    self.txt_drift_back_up.clear()

                    show_message_sucess_validator("WBCO On Board "," Data was entry sucessful")

                else:
                    message_error_validation("WBCO On Board","Data was entry Error")

        

        def validatoin_well_information():

            caracter_especial = '1234567890!#$%&/=?*+ªº^~-"'
            only_special_character = '!#$%&/=?*+ªº^~-"'

            txt_length = str(self.txt_length.text())
            cbx_od = self.cbx_od.currentText()
            txt_id = str(self.txt_id.text())
            txt_weigth_range =  str(self.txt_weigth_range.text())
            txt_volume_capacity = str(self.txt_volume_capacity.text())
            cbx_hole_volume = str(self.cbx_hole_volume.currentText())

            def has_special_characters(input_str, special_chars):
                for char in input_str:
                    if char in special_chars:
                        return True
                return False
            
            if has_special_characters(txt_volume_capacity,only_special_character) or (txt_volume_capacity == ""):
                message_error_validation("This field does not accept characters or is empty","Volume capacity entry error")
           
            elif has_special_characters(cbx_hole_volume,only_special_character) or (cbx_hole_volume == ""):
                message_error_validation("This filed does not accept characters empty","Hole Volume entry error")
           
            elif txt_length == "":
                message_error_validation("This field does not accept characters empty","Length entry error")
           
            elif cbx_od == "":
                message_error_validation("This field does not accept characters empty","OD entry error")
           
            elif txt_id == "":
                message_error_validation("This field does not accept characters empty","ID entry error")

            elif txt_weigth_range == "":
                message_error_validation("This field does not accept characters empty","Weigth entry error")

            else:
                show_message_sucess_validator("Well information","Data was entry Sucessful")
                self.tab_menus_wbco.setCurrentIndex(2)

        
        
        def validatoin_wbco_enginer():

            only_special_character = '!#$%&/=?*+ªº^~-"abcdefghijklmnopqrstuvwyxz'
            caracter_especial = '1234567890!#$%&/=?*+ªº^~-"'

            cbx_enginer_techinical = str(self.cbx_enginer_techinical.currentText())
            
            

            
            def has_special_characters(input_str, special_chars):
                for char in input_str:
                    if char in special_chars:
                        return True
                return False
            
            
           
            if has_special_characters(cbx_enginer_techinical,caracter_especial) or (cbx_enginer_techinical == ""):
                message_error_validation("This filed does not accept characters empty","Techinical Enginer entry error")        
            else:
                show_message_sucess_validator("Engineer Information","Data was entry Sucessful")
                self.tab_menus_wbco.setCurrentIndex(3)
               
                    

        def validatoin_activity():

            cbx_enginer_techinical = str(self.cbx_enginer_techinical.currentText())
           
            txt_area_on_going = str(self.txt_area_on_going.toPlainText())
            txt_wbco_activity = str(self.txt_wbco_activity.toPlainText())
            
            def has_special_characters(input_str, special_chars):
                for char in input_str:
                    if char in special_chars:
                        return True
                return False
            
            if txt_area_on_going == "":
                message_error_validation("This field does not accept  empty","On going entry error")
            
            elif txt_wbco_activity == "":
                message_error_validation("This filed does not accept characters empty","WBCO Activity entry error")
            
            else:
                self.tab_menus_wbco.setCurrentIndex(4)
                id_poco = modulo_wbco.wbcoController.carregar_buscar_id_poco(self.cbx_well_number.currentText())
                id_cliente = modulo_wbco.wbcoController.carregar_buscar_id_cliente(self.cbx_customer.currentText())
                id_empregador = modulo_wbco.wbcoController.carregar_buscar_id_empregador_por_nome(self.cbx_aproved_by.currentText())

                id_supervisor = modulo_wbco.wbcoController.carregar_id_supervisor(self.cbx_enginer_supervisor.currentText())

                #Salvar Report Cabecalho
                modulo_wbco.wbcoController.salvar_report_cabecalho(self.txt_job_ref.text(),self.txt_field_location.text(),self.txt_job_type.text(),"Days/Nigth",self.dateEdit.text(),id_supervisor,self.txt_rig_name.text())

                id_ultimo_registo_report_header = modulo_wbco.wbcoController.buscar_id_report_header_ultimo()

                id_od = modulo_wbco.sizeController.buscar_id_by_size(self.cbx_od.currentText())
                id_casing_size = modulo_wbco.sizeController.buscar_id_by_size(self.cbx_size.currentText())

                cout_job_ref = controller.verificar_job_ref(self.txt_job_ref.text(),id_supervisor)

                

                total_days_enginer = int(cout_job_ref) + 1

                modulo_wbco.wbcoController.salvar_report_information(txt_area_on_going,id_casing_size,
                self.txt_length.text(),id_od,self.txt_id.text(),self.txt_weigth_range.text(),self.txt_volume_capacity.text(),
                self.cbx_hole_volume.currentText(),txt_wbco_activity,self.cbx_shitf_supervisor.currentText(),total_days_enginer,id_poco,id_supervisor,id_cliente,id_empregador,id_ultimo_registo_report_header)

                

                id_empregador_tecnico = modulo_wbco.wbcoController.carregar_buscar_id_empregador_por_nome(cbx_enginer_techinical)
                id_ultimo_report = modulo_wbco.wbcoController.carregar_buscar_id_report()
                cout_employees_job = controller_enginer.verificar_job_ref(self.txt_job_ref.text(),id_empregador_tecnico)
                
                total_days_employes = int(cout_employees_job) + 1
                print(total_days_employes)
                valor_retorno = modulo_wbco.wbcoController.salvar_tecnico_em_servico(id_empregador_tecnico,self.cdx_shift_techinical.currentText(),total_days_employes,id_ultimo_report)
                if valor_retorno == 0:
                    show_message_sucess_validator("Activity Information","Data was entry sucessful")
                    self.tab_menus_wbco.setCurrentIndex(4)
                else:
                    message_error_validation("There was an error, the data was not added correctly","Error adding Engineer")



        def message_error_validation(text_input_error,tittle_windows):
            msg_error = QMessageBox()
            msg_error.setIcon(QMessageBox.Critical)
            msg_error.setText(str(text_input_error))
            msg_error.setWindowTitle(str(tittle_windows))
            msg_error.exec_()

        def call_form_wbco_list():
            self.window = QtWidgets.QMainWindow()
            import modulo_wbco.wbco
            self.ui = modulo_wbco.wbco.Ui_MainWindow()
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

        def show_form_dashboard():
            self.window = QtWidgets.QMainWindow()
            import modulo_home.dashboard
            self.ui = modulo_home.dashboard.Ui_dashboard_ui()
            self.ui.setupUi(self.window,self.lbl_user_logado.text())
            self.window.show()
            MainWindow.close()

        def call_form_user():
            self.window = QtWidgets.QMainWindow()
            import modulo_personnel.personnel
            self.ui = modulo_personnel.personnel.form_personeel_list()
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
                

            


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
