

from PyQt5.QtWidgets import QDesktopWidget,QMessageBox
import modulo_wbco.wbcoController
from PyQt5 import QtCore, QtGui, QtWidgets
import filtration.pack_report.reportController
import filtration.pack_prepared_aproved.prepared_aprovedController
import filtration.pack_fluid_information.fluid_informationController
import filtration.pack_filtration_sumary.fluid_sumaryController
import filtration.pack_fluid_analisys.fluid_analisysController
import filtration.pack_fluid_consumables.fluid_consumablesController
import filtration.pack_enginer_day.enginer_dayController
import modulo_wbco.wbcoController as controller
import filtration.pack_employee.employeeController



class Ui_MainWindow(object):
    def setupUi(self, MainWindow,user_logado):
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
        self.frame_aside_menu.setStyleSheet("\n"
"background-color:#2f6d58")
        self.frame_aside_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_aside_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_aside_menu.setObjectName("frame_aside_menu")
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
        self.btn_dashboard.setStyleSheet("\n"
"\n"
"QPushButton#btn_dashboard{\n"
"\n"
"border:none;\n"
"color:white;\n"
"font-size:18px;\n"
"border-radius: 12px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"text-align:left;\n"
"}\n"
"\n"
"QPushButton#btn_dashboard:hover{\n"
" background-color: #044e42;\n"
"border-radius: 12px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_dashboard:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 12px;\n"
"background-color: #033029;\n"
"padding:10px;\n"
" }\n"
"\n"
"\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/house-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_dashboard.setIcon(icon)
        self.btn_dashboard.setIconSize(QtCore.QSize(25, 25))
        self.btn_dashboard.setFlat(False)
        self.btn_dashboard.setObjectName("btn_dashboard")
        self.btn_compliance = QtWidgets.QPushButton(self.frame_aside_menu)
        self.btn_compliance.setGeometry(QtCore.QRect(30, 290, 191, 41))
        self.btn_compliance.setStyleSheet("QPushButton#btn_compliance{\n"
"\n"
"border:none;\n"
"color:white;\n"
"font-size:18px;\n"
"border-radius: 12px;\n"
"transition: background-color 0.5s ease;\n"
"text-align:left;\n"
"padding:10px\n"
"}\n"
"\n"
"QPushButton#btn_compliance:hover{\n"
" background-color: #044e42;\n"
"border-radius: 12px;\n"
"transition: background-color 0.5s ease;\n"
"}\n"
"\n"
"QPushButton#btn_compliance:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 12px;\n"
"background-color: #033029;\n"
" }\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/vial-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_compliance.setIcon(icon1)
        self.btn_compliance.setIconSize(QtCore.QSize(25, 25))
        self.btn_compliance.setFlat(False)
        self.btn_compliance.setObjectName("btn_compliance")
        self.btn_wbco = QtWidgets.QPushButton(self.frame_aside_menu)
        self.btn_wbco.setGeometry(QtCore.QRect(30, 340, 191, 41))
        self.btn_wbco.setStyleSheet("QPushButton#btn_wbco{\n"
"\n"
"border:none;\n"
"color:white;\n"
"font-size:18px;\n"
"border-radius: 12px;\n"
"transition: background-color 0.5s ease;\n"
"text-align:left;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_wbco:hover{\n"
" background-color: #044e42;\n"
"border-radius: 12px;\n"
"transition: background-color 0.5s ease;\n"
"}\n"
"\n"
"QPushButton#btn_wbco:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 12px;\n"
"background-color: #033029;\n"
" }")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/tools.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_wbco.setIcon(icon2)
        self.btn_wbco.setIconSize(QtCore.QSize(25, 25))
        self.btn_wbco.setFlat(False)
        self.btn_wbco.setObjectName("btn_wbco")
        self.btn_filtration = QtWidgets.QPushButton(self.frame_aside_menu)
        self.btn_filtration.setGeometry(QtCore.QRect(30, 390, 191, 41))
        self.btn_filtration.setStyleSheet("QPushButton#btn_filtration{\n"
"\n"
"border:none;\n"
"color:white;\n"
"font-size:19px;\n"
"border-radius: 12px;\n"
"transition: background-color 0.5s ease;\n"
"text-align:left;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_filtration:hover{\n"
" background-color: #044e42;\n"
"border-radius: 12px;\n"
"transition: background-color 0.5s ease;\n"
"}\n"
"\n"
"QPushButton#btn_filtration:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 12px;\n"
"background-color: #033029;\n"
" }")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/oil-well-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_filtration.setIcon(icon3)
        self.btn_filtration.setIconSize(QtCore.QSize(25, 25))
        self.btn_filtration.setFlat(False)
        self.btn_filtration.setObjectName("btn_filtration")
        self.btn_tank_cleaning = QtWidgets.QPushButton(self.frame_aside_menu)
        self.btn_tank_cleaning.setGeometry(QtCore.QRect(30, 440, 191, 41))
        self.btn_tank_cleaning.setStyleSheet("QPushButton#btn_tank_cleaning{\n"
"\n"
"border:none;\n"
"color:white;\n"
"font-size:18px;\n"
"border-radius: 12px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"text-align:left;\n"
"}\n"
"\n"
"QPushButton#btn_tank_cleaning:hover{\n"
" background-color: #044e42;\n"
"border-radius: 12px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_tank_cleaning:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 12px;\n"
"background-color: #033029;\n"
" }")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("img/soap-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_tank_cleaning.setIcon(icon4)
        self.btn_tank_cleaning.setIconSize(QtCore.QSize(25, 25))
        self.btn_tank_cleaning.setFlat(False)
        self.btn_tank_cleaning.setObjectName("btn_tank_cleaning")
        self.btn_user_profile = QtWidgets.QPushButton(self.frame_aside_menu)
        self.btn_user_profile.setGeometry(QtCore.QRect(40, 710, 161, 41))
        self.btn_user_profile.setStyleSheet("QPushButton#btn_user_profile{\n"
"\n"
"border:none;\n"
"color:white;\n"
"font-size:18px;\n"
"border-radius: 12px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"text-align:left;\n"
"}\n"
"\n"
"QPushButton#btn_user_profile:hover{\n"
" background-color: #044e42;\n"
"border-radius: 12px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_user_profile:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 12px;\n"
"background-color: #033029;\n"
" }")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("img/user-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_user_profile.setIcon(icon5)
        self.btn_user_profile.setIconSize(QtCore.QSize(25, 25))
        self.btn_user_profile.setFlat(False)
        self.btn_user_profile.setObjectName("btn_user_profile")
        self.btn_logout = QtWidgets.QPushButton(self.frame_aside_menu)
        self.btn_logout.setGeometry(QtCore.QRect(40, 760, 161, 41))
        self.btn_logout.setStyleSheet("QPushButton#btn_logout{\n"
"\n"
"border:none;\n"
"color:white;\n"
"font-size:18px;\n"
"border-radius: 12px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"text-align:left;\n"
"}\n"
"\n"
"QPushButton#btn_logout:hover{\n"
" background-color: #044e42;\n"
"border-radius: 12px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_logout:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 12px;\n"
"background-color: #033029;\n"
" }")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("img/right-from-bracket-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_logout.setIcon(icon6)
        self.btn_logout.setIconSize(QtCore.QSize(25, 25))
        self.btn_logout.setFlat(False)
        self.btn_logout.setObjectName("btn_logout")
        self.btn_user = QtWidgets.QPushButton(self.frame_aside_menu)
        self.btn_user.setGeometry(QtCore.QRect(30, 190, 191, 41))
        self.btn_user.setStyleSheet("\n"
"\n"
"QPushButton#btn_user{\n"
"\n"
"border:none;\n"
"color:white;\n"
"font-size:18px;\n"
"border-radius: 12px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"text-align:left;\n"
"}\n"
"\n"
"QPushButton#btn_user:hover{\n"
" background-color: #044e42;\n"
"border-radius: 12px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_user:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 12px;\n"
"background-color: #033029;\n"
"padding:10px;\n"
" }\n"
"\n"
"\n"
"")
        self.btn_user.setIcon(icon5)
        self.btn_user.setIconSize(QtCore.QSize(25, 25))
        self.btn_user.setFlat(False)
        self.btn_user.setObjectName("btn_user")
        self.btn_customer = QtWidgets.QPushButton(self.frame_aside_menu)
        self.btn_customer.setGeometry(QtCore.QRect(30, 240, 191, 41))
        self.btn_customer.setStyleSheet("\n"
"\n"
"QPushButton#btn_customer{\n"
"\n"
"border:none;\n"
"color:white;\n"
"font-size:18px;\n"
"border-radius: 12px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"text-align:left;\n"
"}\n"
"\n"
"QPushButton#btn_customer:hover{\n"
" background-color: #044e42;\n"
"border-radius: 12px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_customer:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 12px;\n"
"background-color: #033029;\n"
"padding:10px;\n"
" }\n"
"\n"
"\n"
"")
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
        self.frame.setStyleSheet("background-color:#fff;\n"
"\n"
"")
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
        self.img_user_logado = QtWidgets.QPushButton(self.frame_2)
        self.img_user_logado.setGeometry(QtCore.QRect(980, 10, 31, 31))
        self.img_user_logado.setStyleSheet("background-color: #fff;\n"
"border-radius:30px;\n"
"width:30px;\n"
"height:30px;")
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
        self.lbl_form_tittle.setGeometry(QtCore.QRect(40, 50, 441, 31))
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
        self.lbl_form_text.setGeometry(QtCore.QRect(40, 90, 391, 21))
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
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(20, 270, 1071, 20))
        self.line_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.btn_list_report = QtWidgets.QPushButton(self.frame)
        self.btn_list_report.setGeometry(QtCore.QRect(900, 240, 191, 31))
        self.btn_list_report.setStyleSheet("\n"
"\n"
"QPushButton#btn_list_report{\n"
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
"QPushButton#btn_list_report:hover{\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_list_report:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"background-color: #033029;\n"
"padding:10px;\n"
" }\n"
"")
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
        self.lbl_customer.setGeometry(QtCore.QRect(10, 20, 81, 31))
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
        self.cbx_customer.addItem("Select a Customer") 

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
        self.lbl_job_ref = QtWidgets.QLabel(self.tab_report_information)
        self.lbl_job_ref.setGeometry(QtCore.QRect(530, 20, 141, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_job_ref.setFont(font)
        self.lbl_job_ref.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_job_ref.setObjectName("lbl_job_ref")
        self.txt_job_ref = QtWidgets.QLineEdit(self.tab_report_information)
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
        self.txt_field_location.setGeometry(QtCore.QRect(530, 220, 491, 41))
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
        self.txt_job_type = QtWidgets.QLineEdit(self.tab_report_information)
        self.txt_job_type.setGeometry(QtCore.QRect(530, 310, 491, 41))
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
        self.lbl_rig_name = QtWidgets.QLabel(self.tab_report_information)
        self.lbl_rig_name.setGeometry(QtCore.QRect(530, 110, 141, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_rig_name.setFont(font)
        self.lbl_rig_name.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_rig_name.setObjectName("lbl_rig_name")
        self.lbl_field_location = QtWidgets.QLabel(self.tab_report_information)
        self.lbl_field_location.setGeometry(QtCore.QRect(530, 190, 141, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_field_location.setFont(font)
        self.lbl_field_location.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_field_location.setObjectName("lbl_field_location")
        self.lbl_job_type = QtWidgets.QLabel(self.tab_report_information)
        self.lbl_job_type.setGeometry(QtCore.QRect(530, 280, 91, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_job_type.setFont(font)
        self.lbl_job_type.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_job_type.setObjectName("lbl_job_type")
        self.lbl_contacto_7 = QtWidgets.QLabel(self.tab_report_information)
        self.lbl_contacto_7.setGeometry(QtCore.QRect(10, 190, 101, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_contacto_7.setFont(font)
        self.lbl_contacto_7.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_contacto_7.setObjectName("lbl_contacto_7")
        self.dateEdit = QtWidgets.QDateEdit(self.tab_report_information)
        self.dateEdit.setGeometry(QtCore.QRect(10, 220, 491, 41))
        self.dateEdit.setStyleSheet("QDateEdit{\n"
"\n"
"background-color:#fff;\n"
"border: 1px solid #8ec0af;\n"
"border-radius: 6px\n"
"\n"
"}")
        self.dateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateEdit.setAccelerated(False)
        self.dateEdit.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.dateEdit.setProperty("showGroupSeparator", False)
        self.dateEdit.setObjectName("dateEdit")
        self.btn_next_step_report_information = QtWidgets.QPushButton(self.tab_report_information)
        self.btn_next_step_report_information.setGeometry(QtCore.QRect(10, 310, 491, 41))
        self.btn_next_step_report_information.setStyleSheet("\n"
"\n"
"QPushButton#btn_next_step_report_information{\n"
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
"QPushButton#btn_next_step_report_information:hover{\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_next_step_report_information:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"background-color: #033029;\n"
"padding:10px;\n"
" }\n"
"")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("img/check-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_next_step_report_information.setIcon(icon10)
        self.btn_next_step_report_information.setObjectName("btn_next_step_report_information")
        self.lbl_contacto_7.raise_()
        self.lbl_job_type.raise_()
        self.lbl_field_location.raise_()
        self.lbl_rig_name.raise_()
        self.lbl_customer.raise_()
        self.cbx_customer.raise_()
        self.lbl_well_number.raise_()
        self.cbx_well_number.raise_()
        self.lbl_job_ref.raise_()
        self.txt_job_ref.raise_()
        self.txt_rig_name.raise_()
        self.txt_field_location.raise_()
        self.txt_job_type.raise_()
        self.dateEdit.raise_()
        self.btn_next_step_report_information.raise_()
        self.tab_menus_wbco.addTab(self.tab_report_information, "")
        self.tab_filtration_activity = QtWidgets.QWidget()
        self.tab_filtration_activity.setObjectName("tab_filtration_activity")
        self.txt_area_filtration_activity = QtWidgets.QPlainTextEdit(self.tab_filtration_activity)
        self.txt_area_filtration_activity.setGeometry(QtCore.QRect(0, 40, 1001, 351))
        self.txt_area_filtration_activity.setStyleSheet("background-color:#fff;\n"
"border: 1px solid #8ec0af;\n"
"border-radius: 6px")
        self.txt_area_filtration_activity.setObjectName("txt_area_filtration_activity")
        self.lbl_filtration_activity = QtWidgets.QLabel(self.tab_filtration_activity)
        self.lbl_filtration_activity.setGeometry(QtCore.QRect(0, 10, 141, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_filtration_activity.setFont(font)
        self.lbl_filtration_activity.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_filtration_activity.setObjectName("lbl_filtration_activity")
        self.btn_next_filtration_activity = QtWidgets.QPushButton(self.tab_filtration_activity)
        self.btn_next_filtration_activity.setGeometry(QtCore.QRect(0, 400, 491, 41))
        self.btn_next_filtration_activity.setStyleSheet("\n"
"\n"
"QPushButton#btn_next_filtration_activity{\n"
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
"QPushButton#btn_next_filtration_activity:hover{\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_next_filtration_activity:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"background-color: #033029;\n"
"padding:10px;\n"
" }\n"
"")
        self.btn_next_filtration_activity.setIcon(icon10)
        self.btn_next_filtration_activity.setObjectName("btn_next_filtration_activity")
        self.lbl_filtration_activity.raise_()
        self.txt_area_filtration_activity.raise_()
        self.btn_next_filtration_activity.raise_()
        self.tab_menus_wbco.addTab(self.tab_filtration_activity, "")
        self.tab_ongoing_rig_activity = QtWidgets.QWidget()
        self.tab_ongoing_rig_activity.setObjectName("tab_ongoing_rig_activity")
        self.txt_area_ongoing = QtWidgets.QPlainTextEdit(self.tab_ongoing_rig_activity)
        self.txt_area_ongoing.setGeometry(QtCore.QRect(0, 40, 1001, 351))
        self.txt_area_ongoing.setStyleSheet("background-color:#fff;\n"
"border: 1px solid #8ec0af;\n"
"border-radius: 6px")
        self.txt_area_ongoing.setObjectName("txt_area_ongoing")
        self.lbl_ongoing = QtWidgets.QLabel(self.tab_ongoing_rig_activity)
        self.lbl_ongoing.setGeometry(QtCore.QRect(0, 10, 241, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_ongoing.setFont(font)
        self.lbl_ongoing.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_ongoing.setObjectName("lbl_ongoing")
        self.btn_next_ongoing_rig_activity = QtWidgets.QPushButton(self.tab_ongoing_rig_activity)
        self.btn_next_ongoing_rig_activity.setGeometry(QtCore.QRect(0, 400, 491, 41))
        self.btn_next_ongoing_rig_activity.setStyleSheet("\n"
"\n"
"QPushButton#btn_next_ongoing_rig_activity{\n"
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
"QPushButton#btn_next_ongoing_rig_activity:hover{\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_next_ongoing_rig_activity:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"background-color: #033029;\n"
"padding:10px;\n"
" }\n"
"")
        self.btn_next_ongoing_rig_activity.setIcon(icon10)
        self.btn_next_ongoing_rig_activity.setObjectName("btn_next_ongoing_rig_activity")
        self.lbl_ongoing.raise_()
        self.txt_area_ongoing.raise_()
        self.btn_next_ongoing_rig_activity.raise_()
        self.tab_menus_wbco.addTab(self.tab_ongoing_rig_activity, "")
        self.tasb_prepared_aproved = QtWidgets.QWidget()
        self.tasb_prepared_aproved.setObjectName("tasb_prepared_aproved")
        self.lbl_prepared_by = QtWidgets.QLabel(self.tasb_prepared_aproved)
        self.lbl_prepared_by.setGeometry(QtCore.QRect(10, 20, 191, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_prepared_by.setFont(font)
        self.lbl_prepared_by.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_prepared_by.setObjectName("lbl_prepared_by")
        self.cbx_prepared_by = QtWidgets.QComboBox(self.tasb_prepared_aproved)
        self.cbx_prepared_by.setGeometry(QtCore.QRect(10, 50, 491, 41))
        self.cbx_prepared_by.setStyleSheet("""
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
        self.cbx_prepared_by.setObjectName("cbx_prepared_by")
        self.btn_add_prepared = QtWidgets.QPushButton(self.tasb_prepared_aproved)
        self.btn_add_prepared.setGeometry(QtCore.QRect(10, 120, 491, 41))
        self.btn_add_prepared.setStyleSheet("\n"
"\n"
"QPushButton#btn_add_prepared{\n"
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
"QPushButton#btn_add_prepared:hover{\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_add_prepared:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"background-color: #033029;\n"
"padding:10px;\n"
" }\n"
"")
        self.btn_add_prepared.setIcon(icon10)
        self.btn_add_prepared.setObjectName("btn_add_prepared")
        self.cbx_aproved_by = QtWidgets.QComboBox(self.tasb_prepared_aproved)
        self.cbx_aproved_by.setGeometry(QtCore.QRect(550, 50, 491, 41))
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
        self.cbx_aproved_by.setObjectName("cbx_aproved_by")
        self.btn_add_aproved = QtWidgets.QPushButton(self.tasb_prepared_aproved)
        self.btn_add_aproved.setGeometry(QtCore.QRect(550, 120, 491, 41))
        self.btn_add_aproved.setStyleSheet("\n"
"\n"
"QPushButton#btn_add_aproved{\n"
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
"QPushButton#btn_add_aproved:hover{\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_add_aproved:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"background-color: #033029;\n"
"padding:10px;\n"
" }\n"
"")
        self.btn_add_aproved.setIcon(icon10)
        self.btn_add_aproved.setObjectName("btn_add_aproved")
        self.lbl_prepared_by_2 = QtWidgets.QLabel(self.tasb_prepared_aproved)
        self.lbl_prepared_by_2.setGeometry(QtCore.QRect(550, 20, 191, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_prepared_by_2.setFont(font)
        self.lbl_prepared_by_2.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_prepared_by_2.setObjectName("lbl_prepared_by_2")
        self.btn_next_step_prepared_aproved = QtWidgets.QPushButton(self.tasb_prepared_aproved)
        self.btn_next_step_prepared_aproved.setGeometry(QtCore.QRect(10, 200, 491, 41))
        self.btn_next_step_prepared_aproved.setStyleSheet("\n"
"\n"
"QPushButton#btn_next_step_prepared_aproved{\n"
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
"QPushButton#btn_next_step_prepared_aproved:hover{\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_next_step_prepared_aproved:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"background-color: #033029;\n"
"padding:10px;\n"
" }\n"
"")
        self.btn_next_step_prepared_aproved.setIcon(icon10)
        self.btn_next_step_prepared_aproved.setObjectName("btn_next_step_prepared_aproved")
        self.lbl_prepared_by_2.raise_()
        self.lbl_prepared_by.raise_()
        self.cbx_prepared_by.raise_()
        self.btn_add_prepared.raise_()
        self.cbx_aproved_by.raise_()
        self.btn_add_aproved.raise_()
        self.btn_next_step_prepared_aproved.raise_()
        self.tab_menus_wbco.addTab(self.tasb_prepared_aproved, "")
        self.tab_fluid_information = QtWidgets.QWidget()
        self.tab_fluid_information.setObjectName("tab_fluid_information")
        self.btn_next_step_fluid_information = QtWidgets.QPushButton(self.tab_fluid_information)
        self.btn_next_step_fluid_information.setGeometry(QtCore.QRect(10, 310, 491, 41))
        self.btn_next_step_fluid_information.setStyleSheet("\n"
"\n"
"QPushButton#btn_next_step_fluid_information{\n"
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
"QPushButton#btn_next_step_fluid_information:hover{\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_next_step_fluid_information:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"background-color: #033029;\n"
"padding:10px;\n"
" }\n"
"")
        self.btn_next_step_fluid_information.setIcon(icon10)
        self.btn_next_step_fluid_information.setObjectName("btn_next_step_fluid_information")
        self.lbl_type_filtered = QtWidgets.QLabel(self.tab_fluid_information)
        self.lbl_type_filtered.setGeometry(QtCore.QRect(10, 20, 231, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_type_filtered.setFont(font)
        self.lbl_type_filtered.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_type_filtered.setObjectName("lbl_type_filtered")
        self.txt_daily_total = QtWidgets.QLabel(self.tab_fluid_information)
        self.txt_daily_total.setGeometry(QtCore.QRect(530, 20, 281, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.txt_daily_total.setFont(font)
        self.txt_daily_total.setStyleSheet("color: rgb(52, 52, 52);")
        self.txt_daily_total.setObjectName("txt_daily_total")
        self.lbl_density_type = QtWidgets.QLabel(self.tab_fluid_information)
        self.lbl_density_type.setGeometry(QtCore.QRect(10, 110, 191, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_density_type.setFont(font)
        self.lbl_density_type.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_density_type.setObjectName("lbl_density_type")
        self.lbl_hole_volume = QtWidgets.QLabel(self.tab_fluid_information)
        self.lbl_hole_volume.setGeometry(QtCore.QRect(530, 200, 231, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_hole_volume.setFont(font)
        self.lbl_hole_volume.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_hole_volume.setObjectName("lbl_hole_volume")
        self.txt_fluid_type_filtered = QtWidgets.QLineEdit(self.tab_fluid_information)
        self.txt_fluid_type_filtered.setGeometry(QtCore.QRect(10, 50, 491, 41))
        self.txt_fluid_type_filtered.setStyleSheet("""
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
        self.txt_fluid_type_filtered.setPlaceholderText("")
        self.txt_fluid_type_filtered.setObjectName("txt_fluid_type_filtered")
        self.txt_daily_total_2 = QtWidgets.QLineEdit(self.tab_fluid_information)
        self.txt_daily_total_2.setGeometry(QtCore.QRect(530, 50, 491, 41))
        self.txt_daily_total_2.setStyleSheet("""
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
        self.txt_daily_total_2.setPlaceholderText("")
        self.txt_daily_total_2.setObjectName("txt_daily_total_2")
        self.cbx_type_density = QtWidgets.QComboBox(self.tab_fluid_information)
        self.cbx_type_density.setGeometry(QtCore.QRect(10, 140, 500, 41))
        self.cbx_type_density.setStyleSheet("""
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
        self.cbx_type_density.setObjectName("cbx_type_density")
        self.txt_viscosity = QtWidgets.QLineEdit(self.tab_fluid_information)
        self.txt_viscosity.setGeometry(QtCore.QRect(10, 230, 491, 41))
        self.txt_viscosity.setStyleSheet("""
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
        self.txt_viscosity.setPlaceholderText("")
        self.txt_viscosity.setObjectName("txt_viscosity")
        self.lbl_viscosity = QtWidgets.QLabel(self.tab_fluid_information)
        self.lbl_viscosity.setGeometry(QtCore.QRect(10, 200, 81, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_viscosity.setFont(font)
        self.lbl_viscosity.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_viscosity.setObjectName("lbl_viscosity")
        self.txt_type_density = QtWidgets.QLineEdit(self.tab_fluid_information)
        self.txt_type_density.setGeometry(QtCore.QRect(530, 140, 491, 41))
        self.txt_type_density.setStyleSheet("""
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
        self.txt_type_density.setPlaceholderText("")
        self.txt_type_density.setObjectName("txt_type_density")
        self.lbl_density = QtWidgets.QLabel(self.tab_fluid_information)
        self.lbl_density.setGeometry(QtCore.QRect(530, 110, 81, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_density.setFont(font)
        self.lbl_density.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_density.setObjectName("lbl_density")
        self.cbx_hole_volume_bbls = QtWidgets.QComboBox(self.tab_fluid_information)
        self.cbx_hole_volume_bbls.setGeometry(QtCore.QRect(530, 230, 240, 41))
        self.cbx_hole_volume_bbls.setStyleSheet("""
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
        self.cbx_hole_volume_bbls.setObjectName("cbx_hole_volume_bbls")
        self.cbx_hole_volume_bbls.addItems(["bbls","m3"])

        self.txt_hole_volume = QtWidgets.QLineEdit(self.tab_fluid_information)
        self.txt_hole_volume.setGeometry(QtCore.QRect(780, 230, 240, 41))
        self.txt_hole_volume.setStyleSheet("""
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
        self.txt_hole_volume.setPlaceholderText("")
        self.txt_hole_volume.setObjectName("txt_hole_volume")
        self.lbl_hole_volume_value = QtWidgets.QLabel(self.tab_fluid_information)
        self.lbl_hole_volume_value.setGeometry(QtCore.QRect(780, 200, 181, 25))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_hole_volume_value.setFont(font)
        self.lbl_hole_volume_value.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_hole_volume_value.setObjectName("lbl_hole_volume_value")

        
        self.lbl_vol_filtered_date = QtWidgets.QLabel(self.tab_fluid_information)
        self.lbl_vol_filtered_date.setGeometry(QtCore.QRect(530, 280, 131, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_vol_filtered_date.setFont(font)
        self.lbl_vol_filtered_date.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_vol_filtered_date.setObjectName("lbl_vol_filtered_date")
        self.txt_vol_filtered_date = QtWidgets.QLineEdit(self.tab_fluid_information)
        self.txt_vol_filtered_date.setGeometry(QtCore.QRect(530, 310, 491, 41))
        self.txt_vol_filtered_date.setStyleSheet("""
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
        self.txt_vol_filtered_date.setPlaceholderText("")
        self.txt_vol_filtered_date.setObjectName("txt_vol_filtered_date")
        self.lbl_density.raise_()
        self.lbl_viscosity.raise_()
        self.txt_daily_total.raise_()
        self.lbl_type_filtered.raise_()
        self.btn_next_step_fluid_information.raise_()
        self.lbl_density_type.raise_()
        self.lbl_hole_volume.raise_()
        self.txt_fluid_type_filtered.raise_()
        self.txt_daily_total_2.raise_()
        self.cbx_type_density.raise_()
        self.txt_viscosity.raise_()
        self.txt_type_density.raise_()
        self.cbx_hole_volume_bbls.raise_()
        self.lbl_vol_filtered_date.raise_()
        self.txt_vol_filtered_date.raise_()
        self.tab_menus_wbco.addTab(self.tab_fluid_information, "")
        self.tab_fluid_summary = QtWidgets.QWidget()
        self.tab_fluid_summary.setObjectName("tab_fluid_summary")
        self.btn_next_step_fluid_summary = QtWidgets.QPushButton(self.tab_fluid_summary)
        self.btn_next_step_fluid_summary.setGeometry(QtCore.QRect(10, 390, 491, 41))
        self.btn_next_step_fluid_summary.setStyleSheet("\n"
"\n"
"QPushButton#btn_next_step_fluid_summary{\n"
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
"QPushButton#btn_next_step_fluid_summary:hover{\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_next_step_fluid_summary:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"background-color: #033029;\n"
"padding:10px;\n"
" }\n"
"")
        self.btn_next_step_fluid_summary.setIcon(icon10)
        self.btn_next_step_fluid_summary.setObjectName("btn_next_step_fluid_summary")
        self.lbl_cycles = QtWidgets.QLabel(self.tab_fluid_summary)
        self.lbl_cycles.setGeometry(QtCore.QRect(10, 20, 151, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_cycles.setFont(font)
        self.lbl_cycles.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_cycles.setObjectName("lbl_cycles")
        self.cbx_cycles = QtWidgets.QComboBox(self.tab_fluid_summary)
        self.cbx_cycles.setGeometry(QtCore.QRect(10, 50, 491, 41))
        self.cbx_cycles.setStyleSheet("""
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
        self.cbx_cycles.setObjectName("cbx_cycles")
        self.lbl_start_time = QtWidgets.QLabel(self.tab_fluid_summary)
        self.lbl_start_time.setGeometry(QtCore.QRect(520, 20, 81, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_start_time.setFont(font)
        self.lbl_start_time.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_start_time.setObjectName("lbl_start_time")
        self.txt_start_time = QtWidgets.QLineEdit(self.tab_fluid_summary)
        self.txt_start_time.setGeometry(QtCore.QRect(520, 50, 491, 41))
        self.txt_start_time.setStyleSheet("""
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
        self.txt_start_time.setPlaceholderText("")
        self.txt_start_time.setObjectName("txt_start_time")
        self.lbl_stop_time = QtWidgets.QLabel(self.tab_fluid_summary)
        self.lbl_stop_time.setGeometry(QtCore.QRect(10, 110, 81, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_stop_time.setFont(font)
        self.lbl_stop_time.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_stop_time.setObjectName("lbl_stop_time")
        self.txt_stop_time = QtWidgets.QLineEdit(self.tab_fluid_summary)
        self.txt_stop_time.setGeometry(QtCore.QRect(10, 140, 491, 41))
        self.txt_stop_time.setStyleSheet("""
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
        self.txt_stop_time.setPlaceholderText("")
        self.txt_stop_time.setObjectName("txt_stop_time")
        self.lbl_total_min_cycles = QtWidgets.QLabel(self.tab_fluid_summary)
        self.lbl_total_min_cycles.setGeometry(QtCore.QRect(520, 110, 261, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_total_min_cycles.setFont(font)
        self.lbl_total_min_cycles.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_total_min_cycles.setObjectName("lbl_total_min_cycles")
        self.txt_total_min_cycles = QtWidgets.QLineEdit(self.tab_fluid_summary)
        self.txt_total_min_cycles.setGeometry(QtCore.QRect(520, 140, 491, 41))
        self.txt_total_min_cycles.setStyleSheet("""
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
        self.txt_total_min_cycles.setPlaceholderText("")
        self.txt_total_min_cycles.setObjectName("txt_total_min_cycles")
        self.lbl_volume_per_cycle = QtWidgets.QLabel(self.tab_fluid_summary)
        self.lbl_volume_per_cycle.setGeometry(QtCore.QRect(10, 200, 261, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_volume_per_cycle.setFont(font)
        self.lbl_volume_per_cycle.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_volume_per_cycle.setObjectName("lbl_volume_per_cycle")
        self.cbx_volume_per_cycle = QtWidgets.QComboBox(self.tab_fluid_summary)
        self.cbx_volume_per_cycle.setGeometry(QtCore.QRect(10, 230, 491, 41))
        self.cbx_volume_per_cycle.setStyleSheet("""
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

        self.cbx_volume_per_cycle.setObjectName("cbx_volume_per_cycle")
        self.cbx_volume_per_cycle.addItems(["bbls","m3"])
        
        ###################################################################
        self.lbl_volume_per_cycle_value = QtWidgets.QLabel(self.tab_fluid_summary)
        self.lbl_volume_per_cycle_value.setGeometry(QtCore.QRect(10, 290, 161, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_volume_per_cycle_value.setFont(font)
        self.lbl_volume_per_cycle_value.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_volume_per_cycle_value.setObjectName("lbl_volume_per_cycle_value")
        self.lbl_volume_per_cycle_value.setText("Volume per Cycle")

        self.txt_volume_per_cycle_value = QtWidgets.QLineEdit(self.tab_fluid_summary)
        self.txt_volume_per_cycle_value.setGeometry(QtCore.QRect(10, 320, 491, 41))
        self.txt_volume_per_cycle_value.setStyleSheet("""
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
        self.txt_volume_per_cycle_value.setPlaceholderText("")
        self.txt_volume_per_cycle_value.setObjectName("txt_volume_per_cycle_value")

        #####################################################################

        self.lbl_total_min_cycles_3 = QtWidgets.QLabel(self.tab_fluid_summary)
        self.lbl_total_min_cycles_3.setGeometry(QtCore.QRect(520, 200, 261, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_total_min_cycles_3.setFont(font)
        self.lbl_total_min_cycles_3.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_total_min_cycles_3.setObjectName("lbl_total_min_cycles_3")
        self.lbl_de_per_cycle = QtWidgets.QLabel(self.tab_fluid_summary)
        self.lbl_de_per_cycle.setGeometry(QtCore.QRect(520, 290, 161, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_de_per_cycle.setFont(font)
        self.lbl_de_per_cycle.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_de_per_cycle.setObjectName("lbl_de_per_cycle")
        self.txt_de_per_cycle = QtWidgets.QLineEdit(self.tab_fluid_summary)
        self.txt_de_per_cycle.setGeometry(QtCore.QRect(520, 320, 491, 41))
        self.txt_de_per_cycle.setStyleSheet("""
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
        self.txt_de_per_cycle.setObjectName("txt_de_per_cycle")
        self.btn_add_fluid_summary = QtWidgets.QPushButton(self.tab_fluid_summary)
        self.btn_add_fluid_summary.setGeometry(QtCore.QRect(520, 390, 491, 41))
        self.btn_add_fluid_summary.setStyleSheet("\n"
"\n"
"QPushButton#btn_add_fluid_summary{\n"
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
"QPushButton#btn_add_fluid_summary:hover{\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_add_fluid_summary:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"background-color: #033029;\n"
"padding:10px;\n"
" }\n"
"")
        self.btn_add_fluid_summary.setIcon(icon10)
        self.btn_add_fluid_summary.setObjectName("btn_add_fluid_summary")
        self.cbx_cartigde = QtWidgets.QComboBox(self.tab_fluid_summary)
        self.cbx_cartigde.setGeometry(QtCore.QRect(520, 230, 491, 41))
        self.cbx_cartigde.setStyleSheet("""
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
        self.cbx_cartigde.setObjectName("cbx_cartigde")
        self.lbl_start_time.raise_()
        self.btn_next_step_fluid_summary.raise_()
        self.lbl_cycles.raise_()
        self.cbx_cycles.raise_()
        self.txt_start_time.raise_()
        self.lbl_stop_time.raise_()
        self.txt_stop_time.raise_()
        self.lbl_total_min_cycles.raise_()
        self.txt_total_min_cycles.raise_()
        self.lbl_volume_per_cycle.raise_()
        self.cbx_volume_per_cycle.raise_()
        self.lbl_total_min_cycles_3.raise_()
        self.lbl_de_per_cycle.raise_()
        self.txt_de_per_cycle.raise_()
        self.btn_add_fluid_summary.raise_()
        self.cbx_cartigde.raise_()
        self.tab_menus_wbco.addTab(self.tab_fluid_summary, "")
        self.tab_fluid_analise = QtWidgets.QWidget()
        self.tab_fluid_analise.setObjectName("tab_fluid_analise")
        self.lbl_wellbore = QtWidgets.QLabel(self.tab_fluid_analise)
        self.lbl_wellbore.setGeometry(QtCore.QRect(10, 20, 361, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_wellbore.setFont(font)
        self.lbl_wellbore.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_wellbore.setObjectName("lbl_wellbore")
        self.lbl_time = QtWidgets.QLabel(self.tab_fluid_analise)
        self.lbl_time.setGeometry(QtCore.QRect(520, 20, 41, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_time.setFont(font)
        self.lbl_time.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_time.setObjectName("lbl_time")
        self.btn_fluid_analysis = QtWidgets.QPushButton(self.tab_fluid_analise)
        self.btn_fluid_analysis.setGeometry(QtCore.QRect(10, 290, 491, 41))
        self.btn_fluid_analysis.setStyleSheet("\n"
"\n"
"QPushButton#btn_fluid_analysis{\n"
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
"QPushButton#btn_fluid_analysis:hover{\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_fluid_analysis:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"background-color: #033029;\n"
"padding:10px;\n"
" }\n"
"")
        self.btn_fluid_analysis.setIcon(icon10)
        self.btn_fluid_analysis.setObjectName("btn_fluid_analysis")
        self.btn_add_information_fluid_analysis = QtWidgets.QPushButton(self.tab_fluid_analise)
        self.btn_add_information_fluid_analysis.setGeometry(QtCore.QRect(520, 290, 491, 41))
        self.btn_add_information_fluid_analysis.setStyleSheet("\n"
"\n"
"QPushButton#btn_add_information_fluid_analysis{\n"
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
"QPushButton#btn_add_information_fluid_analysis:hover{\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_add_information_dayshift:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"background-color: #033029;\n"
"padding:10px;\n"
" }\n"
"")
        self.btn_add_information_fluid_analysis.setIcon(icon10)
        self.btn_add_information_fluid_analysis.setObjectName("btn_add_information_fluid_analysis")
        self.txt_wellbore = QtWidgets.QLineEdit(self.tab_fluid_analise)
        self.txt_wellbore.setGeometry(QtCore.QRect(10, 50, 491, 41))
        self.txt_wellbore.setStyleSheet("""
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
        self.txt_wellbore.setPlaceholderText("")
        self.txt_wellbore.setObjectName("txt_wellbore")
        self.txt_time = QtWidgets.QLineEdit(self.tab_fluid_analise)
        self.txt_time.setGeometry(QtCore.QRect(520, 50, 491, 41))
        self.txt_time.setStyleSheet("""
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
        self.txt_time.setPlaceholderText("")
        self.txt_time.setObjectName("txt_time")
        self.lbl_volume_pumped = QtWidgets.QLabel(self.tab_fluid_analise)
        self.lbl_volume_pumped.setGeometry(QtCore.QRect(520, 100, 181, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_volume_pumped.setFont(font)
        self.lbl_volume_pumped.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_volume_pumped.setObjectName("lbl_volume_pumped")
        self.lbl_pumping_time = QtWidgets.QLabel(self.tab_fluid_analise)
        self.lbl_pumping_time.setGeometry(QtCore.QRect(10, 100, 161, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_pumping_time.setFont(font)
        self.lbl_pumping_time.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_pumping_time.setObjectName("lbl_pumping_time")
        self.cbx_volume_pumped = QtWidgets.QComboBox(self.tab_fluid_analise)
        self.cbx_volume_pumped.setGeometry(QtCore.QRect(520, 130, 240, 41))
        self.cbx_volume_pumped.setStyleSheet("""
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
        self.cbx_volume_pumped.setPlaceholderText("")
        self.cbx_volume_pumped.setObjectName("cbx_volume_pumped")
        self.cbx_volume_pumped.addItems(["bbls","m3"])


#----------------------------------- Botão ComboBox Type volume pumped ------------------------------------------
        
        self.lbl_volume_pumped_value = QtWidgets.QLabel(self.tab_fluid_analise)
        self.lbl_volume_pumped_value.setGeometry(QtCore.QRect(765, 100, 361, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_volume_pumped_value.setFont(font)
        self.lbl_volume_pumped_value.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_volume_pumped_value.setObjectName("lbl_volume_pumped_value")
        self.lbl_volume_pumped_value.setText("Volume Pumped Value")
        
        
        self.txt_volume_pumped_value = QtWidgets.QLineEdit(self.tab_fluid_analise)
        self.txt_volume_pumped_value.setGeometry(QtCore.QRect(765, 130, 243, 41))
        self.txt_volume_pumped_value.setStyleSheet("""
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
        self.txt_volume_pumped_value.setPlaceholderText("")
        self.txt_volume_pumped_value.setObjectName("txt_volume_pumped_value")
        
#----------------------------------------------------------------------------------------------------------------


        self.txt_pumping_time = QtWidgets.QLineEdit(self.tab_fluid_analise)
        self.txt_pumping_time.setGeometry(QtCore.QRect(10, 130, 491, 41))
        self.txt_pumping_time.setStyleSheet("""
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
        self.txt_pumping_time.setPlaceholderText("")
        self.txt_pumping_time.setObjectName("txt_pumping_time")
        self.lbl_ntus = QtWidgets.QLabel(self.tab_fluid_analise)
        self.lbl_ntus.setGeometry(QtCore.QRect(10, 180, 161, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_ntus.setFont(font)
        self.lbl_ntus.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_ntus.setObjectName("lbl_ntus")
        self.txt_tss = QtWidgets.QLineEdit(self.tab_fluid_analise)
        self.txt_tss.setGeometry(QtCore.QRect(520, 210, 491, 41))
        self.txt_tss.setStyleSheet("""
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
        self.txt_tss.setPlaceholderText("")
        self.txt_tss.setObjectName("txt_tss")
        self.lbl_tss = QtWidgets.QLabel(self.tab_fluid_analise)
        self.lbl_tss.setGeometry(QtCore.QRect(520, 180, 161, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_tss.setFont(font)
        self.lbl_tss.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_tss.setObjectName("lbl_tss")
        self.txt_ntus = QtWidgets.QLineEdit(self.tab_fluid_analise)
        self.txt_ntus.setGeometry(QtCore.QRect(10, 210, 491, 41))
        self.txt_ntus.setStyleSheet("""
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
        self.txt_ntus.setPlaceholderText("")
        self.txt_ntus.setObjectName("txt_ntus")
        self.lbl_tss.raise_()
        self.lbl_wellbore.raise_()
        self.lbl_time.raise_()
        self.btn_fluid_analysis.raise_()
        self.btn_add_information_fluid_analysis.raise_()
        self.txt_wellbore.raise_()
        self.txt_time.raise_()
        self.lbl_volume_pumped.raise_()
        self.lbl_pumping_time.raise_()
        self.cbx_volume_pumped.raise_()
        self.txt_pumping_time.raise_()
        self.lbl_ntus.raise_()
        self.txt_tss.raise_()
        self.txt_ntus.raise_()
        self.tab_menus_wbco.addTab(self.tab_fluid_analise, "")
        self.tab_consumables = QtWidgets.QWidget()
        self.tab_consumables.setObjectName("tab_consumables")
        self.lbl_daily_used = QtWidgets.QLabel(self.tab_consumables)
        self.lbl_daily_used.setGeometry(QtCore.QRect(10, 190, 191, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_daily_used.setFont(font)
        self.lbl_daily_used.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_daily_used.setObjectName("lbl_daily_used")
        self.txt_aditional_stocke = QtWidgets.QLineEdit(self.tab_consumables)
        self.txt_aditional_stocke.setGeometry(QtCore.QRect(530, 140, 491, 41))
        self.txt_aditional_stocke.setStyleSheet("""
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
        self.txt_aditional_stocke.setPlaceholderText("")
        self.txt_aditional_stocke.setObjectName("txt_aditional_stocke")
        self.lbl_aditional_stocke = QtWidgets.QLabel(self.tab_consumables)
        self.lbl_aditional_stocke.setGeometry(QtCore.QRect(530, 110, 151, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_aditional_stocke.setFont(font)
        self.lbl_aditional_stocke.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_aditional_stocke.setObjectName("lbl_aditional_stocke")
        self.lbl_opening_stock = QtWidgets.QLabel(self.tab_consumables)
        self.lbl_opening_stock.setGeometry(QtCore.QRect(10, 110, 301, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_opening_stock.setFont(font)
        self.lbl_opening_stock.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_opening_stock.setObjectName("lbl_opening_stock")
        self.lbl_type = QtWidgets.QLabel(self.tab_consumables)
        self.lbl_type.setGeometry(QtCore.QRect(530, 20, 301, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_type.setFont(font)
        self.lbl_type.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_type.setObjectName("lbl_type")
        self.lbl_material_filtration = QtWidgets.QLabel(self.tab_consumables)
        self.lbl_material_filtration.setGeometry(QtCore.QRect(10, 20, 451, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_material_filtration.setFont(font)
        self.lbl_material_filtration.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_material_filtration.setObjectName("lbl_material_filtration")
        self.btn_next_step_consumables = QtWidgets.QPushButton(self.tab_consumables)
        self.btn_next_step_consumables.setGeometry(QtCore.QRect(10, 290, 491, 41))
        self.btn_next_step_consumables.setStyleSheet("\n"
"\n"
"QPushButton#btn_next_step_consumables{\n"
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
"QPushButton#btn_next_step_consumables:hover{\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_next_step_consumables:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"background-color: #033029;\n"
"padding:10px;\n"
" }\n"
"")
        self.btn_next_step_consumables.setIcon(icon10)
        self.btn_next_step_consumables.setObjectName("btn_next_step_consumables")
        self.btn_add_information_consumables = QtWidgets.QPushButton(self.tab_consumables)
        self.btn_add_information_consumables.setGeometry(QtCore.QRect(530, 210, 491, 41))
        self.btn_add_information_consumables.setStyleSheet("\n"
"\n"
"QPushButton#btn_add_information_consumables{\n"
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
"QPushButton#btn_add_information_consumables:hover{\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_add_information_consumables:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"background-color: #033029;\n"
"padding:10px;\n"
" }\n"
"")
        self.btn_add_information_consumables.setIcon(icon10)
        self.btn_add_information_consumables.setObjectName("btn_add_information_consumables")
        self.txt_opening_stock = QtWidgets.QLineEdit(self.tab_consumables)
        self.txt_opening_stock.setGeometry(QtCore.QRect(10, 140, 491, 41))
        self.txt_opening_stock.setStyleSheet("""
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
        self.txt_opening_stock.setPlaceholderText("")
        self.txt_opening_stock.setObjectName("txt_opening_stock")
        self.txt_daily_used = QtWidgets.QLineEdit(self.tab_consumables)
        self.txt_daily_used.setGeometry(QtCore.QRect(10, 220, 491, 41))
        self.txt_daily_used.setStyleSheet("""
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
        self.txt_daily_used.setPlaceholderText("")
        self.txt_daily_used.setObjectName("txt_daily_used")
        self.cbx_material_filtration = QtWidgets.QComboBox(self.tab_consumables)
        self.cbx_material_filtration.setGeometry(QtCore.QRect(10, 50, 491, 41))
        self.cbx_material_filtration.setStyleSheet("""
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
        self.cbx_material_filtration.setObjectName("cbx_material_filtration")
        self.cbx_material_filtration_2 = QtWidgets.QComboBox(self.tab_consumables)
        self.cbx_material_filtration_2.setGeometry(QtCore.QRect(530, 50, 491, 41))
        self.cbx_material_filtration_2.setStyleSheet("""
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
        self.cbx_material_filtration_2.setObjectName("cbx_material_filtration_2")
        self.lbl_opening_stock.raise_()
        self.lbl_aditional_stocke.raise_()
        self.lbl_type.raise_()
        self.lbl_daily_used.raise_()
        self.txt_aditional_stocke.raise_()
        self.lbl_material_filtration.raise_()
        self.btn_next_step_consumables.raise_()
        self.btn_add_information_consumables.raise_()
        self.txt_opening_stock.raise_()
        self.txt_daily_used.raise_()
        self.cbx_material_filtration.raise_()
        self.cbx_material_filtration_2.raise_()
        self.tab_menus_wbco.addTab(self.tab_consumables, "")
        self.tab_enginer_day = QtWidgets.QWidget()
        self.tab_enginer_day.setObjectName("tab_enginer_day")
        self.lbl_numer_work_3 = QtWidgets.QLabel(self.tab_enginer_day)
        self.lbl_numer_work_3.setGeometry(QtCore.QRect(10, 20, 471, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_numer_work_3.setFont(font)
        self.lbl_numer_work_3.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_numer_work_3.setObjectName("lbl_numer_work_3")
        self.lbl_total_days = QtWidgets.QLabel(self.tab_enginer_day)
        self.lbl_total_days.setGeometry(QtCore.QRect(10, 110, 401, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_total_days.setFont(font)
        self.lbl_total_days.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_total_days.setObjectName("lbl_total_days")
        self.txt_total_days = QtWidgets.QLineEdit(self.tab_enginer_day)
        self.txt_total_days.setGeometry(QtCore.QRect(10, 140, 491, 41))
        self.txt_total_days.setStyleSheet("""
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
        self.txt_total_days.setPlaceholderText("")
        self.txt_total_days.setObjectName("txt_total_days")
        self.lbl_shift_enginer = QtWidgets.QLabel(self.tab_enginer_day)
        self.lbl_shift_enginer.setGeometry(QtCore.QRect(530, 20, 51, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_shift_enginer.setFont(font)
        self.lbl_shift_enginer.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_shift_enginer.setObjectName("lbl_shift_enginer")
        self.cbx_filtration_engineer = QtWidgets.QComboBox(self.tab_enginer_day)
        self.cbx_filtration_engineer.setGeometry(QtCore.QRect(10, 50, 491, 41))
        self.cbx_filtration_engineer.setStyleSheet("""
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
        self.cbx_filtration_engineer.setObjectName("cbx_filtration_engineer")
        self.btn_save_report = QtWidgets.QPushButton(self.tab_enginer_day)
        self.btn_save_report.setGeometry(QtCore.QRect(10, 220, 491, 41))
        self.btn_save_report.setStyleSheet("\n"
"\n"
"QPushButton#btn_save_report{\n"
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
"QPushButton#btn_save_report:hover{\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_save_report:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"background-color: #033029;\n"
"padding:10px;\n"
" }\n"
"")
        self.btn_save_report.setIcon(icon10)
        self.btn_save_report.setObjectName("btn_save_report")
        self.btn_add_engineer_day = QtWidgets.QPushButton(self.tab_enginer_day)
        self.btn_add_engineer_day.setGeometry(QtCore.QRect(540, 140, 491, 41))
        self.btn_add_engineer_day.setStyleSheet("\n"
"\n"
"QPushButton#btn_add_engineer_day{\n"
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
"QPushButton#btn_add_engineer_day:hover{\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_add_engineer_day:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"background-color: #033029;\n"
"padding:10px;\n"
" }\n"
"")
        self.btn_add_engineer_day.setIcon(icon10)
        self.btn_add_engineer_day.setObjectName("btn_add_engineer_day")
        self.cbx_shift_engineer = QtWidgets.QComboBox(self.tab_enginer_day)
        self.cbx_shift_engineer.setGeometry(QtCore.QRect(530, 50, 491, 41))
        self.cbx_shift_engineer.setStyleSheet("""
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
        self.cbx_shift_engineer.setObjectName("cbx_shift_engineer")
        self.tab_menus_wbco.addTab(self.tab_enginer_day, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1400, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow,user_logado)
        self.tab_menus_wbco.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow,user_logado):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dashboard"))
        self.btn_dashboard.setText(_translate("MainWindow", " Dashboard"))
        self.btn_dashboard.clicked.connect(lambda:show_form_dashboard())
        self.btn_compliance.setText(_translate("MainWindow", " Compliance"))
        self.btn_wbco.setText(_translate("MainWindow", " WBCO Tools"))
        self.btn_filtration.setText(_translate("MainWindow", " Filtration"))
        self.btn_tank_cleaning.setText(_translate("MainWindow", " Tank Cleaning"))
        self.btn_user_profile.setText(_translate("MainWindow", "User Profile"))
        self.btn_logout.setText(_translate("MainWindow", "Logout"))
        self.btn_logout.clicked.connect(lambda:logout())
        self.btn_user.setText(_translate("MainWindow", " Personnel"))
        self.btn_user.clicked.connect(lambda:call_form_user())
        self.btn_customer.setText(_translate("MainWindow", "Customers"))
        self.btn_customer.clicked.connect(lambda:call_form_client())
        self.lbl_user_logado.setText(_translate("MainWindow", user_logado))
        self.lbl_form_tittle.setText(_translate("MainWindow", "Filtration - Add new Report"))
        self.lbl_form_text.setText(_translate("MainWindow", "Below are the fields to be filled in to generate a new report"))
        self.btn_list_report.setText(_translate("MainWindow", "List all report"))
        self.btn_list_report.clicked.connect(lambda:show_form_list_report())
        self.lbl_customer.setText(_translate("MainWindow", "Customer"))
        self.cbx_customer.textActivated.connect(lambda: getPoco(self.cbx_customer.currentText()))
        self.lbl_well_number.setText(_translate("MainWindow", "Well Number"))
        self.lbl_job_ref.setText(_translate("MainWindow", "Job Ref. Number"))
        self.lbl_rig_name.setText(_translate("MainWindow", "Rig Name"))
        self.lbl_field_location.setText(_translate("MainWindow", "Field/Location"))
        self.lbl_job_type.setText(_translate("MainWindow", "Job Type"))
        self.lbl_contacto_7.setText(_translate("MainWindow", "Report Date"))
        self.btn_next_step_report_information.setText(_translate("MainWindow", "Next Step"))
        self.btn_next_step_report_information.clicked.connect(lambda:validator_report_information())
        self.tab_menus_wbco.setTabText(self.tab_menus_wbco.indexOf(self.tab_report_information), _translate("MainWindow", "Report "))
        self.txt_area_filtration_activity.setPlaceholderText(_translate("MainWindow", " Write here..."))
        self.lbl_filtration_activity.setText(_translate("MainWindow", "Filtration Activity"))
        self.btn_next_filtration_activity.setText(_translate("MainWindow", "Next Step"))
        self.btn_next_filtration_activity.clicked.connect(lambda:validator_activity())
        self.tab_menus_wbco.setTabText(self.tab_menus_wbco.indexOf(self.tab_filtration_activity), _translate("MainWindow", "Filtration Activity"))
        self.txt_area_ongoing.setPlaceholderText(_translate("MainWindow", " Write here..."))
        self.lbl_ongoing.setText(_translate("MainWindow", "Ongoing Rig Activity"))
        self.btn_next_ongoing_rig_activity.setText(_translate("MainWindow", "Next Step"))
        self.btn_next_ongoing_rig_activity.clicked.connect(lambda:validator_ongoing())
        self.tab_menus_wbco.setTabText(self.tab_menus_wbco.indexOf(self.tab_ongoing_rig_activity), _translate("MainWindow", "Ongoing Rig Activity"))
        self.lbl_prepared_by.setText(_translate("MainWindow", "Prepared by"))
        self.btn_add_prepared.setText(_translate("MainWindow", "Add  to report"))
        self.btn_add_prepared.clicked.connect(lambda:add_prepared_by())
        self.btn_add_aproved.setText(_translate("MainWindow", "Add  to report"))
        self.btn_add_aproved.clicked.connect(lambda:add_approved_by())
        self.lbl_prepared_by_2.setText(_translate("MainWindow", "Approved by"))
        self.btn_next_step_prepared_aproved.setText(_translate("MainWindow", "Next Step"))
        self.btn_next_step_prepared_aproved.clicked.connect(lambda:validator_prepared_approved())
        self.tab_menus_wbco.setTabText(self.tab_menus_wbco.indexOf(self.tasb_prepared_aproved), _translate("MainWindow", "Prepared and Approved by"))
        self.btn_next_step_fluid_information.setText(_translate("MainWindow", "Next Step"))
        self.btn_next_step_fluid_information.clicked.connect(lambda:validator_fluid_information())
        self.lbl_type_filtered.setText(_translate("MainWindow", "Fluid Type"))
        self.txt_daily_total.setText(_translate("MainWindow", "Total fluid filtred for day"))
        self.lbl_density_type.setText(_translate("MainWindow", "Density (Unit)"))
        self.lbl_hole_volume.setText(_translate("MainWindow", "Hole Volume (Unit)"))
        self.lbl_viscosity.setText(_translate("MainWindow", "Viscosity"))
        self.lbl_density.setText(_translate("MainWindow", "Density"))
        self.lbl_vol_filtered_date.setText(_translate("MainWindow", "Vol Filter to date"))
        self.tab_menus_wbco.setTabText(self.tab_menus_wbco.indexOf(self.tab_fluid_information), _translate("MainWindow", "Fluid Information"))
        self.btn_next_step_fluid_summary.setText(_translate("MainWindow", "Next Step"))
        self.btn_next_step_fluid_summary.clicked.connect(lambda:validator_fluid_sumary())

        self.cbx_cartigde.addItems(["2","5","10"])

        self.lbl_cycles.setText(_translate("MainWindow", "Cycles"))
        self.lbl_start_time.setText(_translate("MainWindow", "Start Time"))
        self.lbl_stop_time.setText(_translate("MainWindow", "Stop Time"))
        self.lbl_total_min_cycles.setText(_translate("MainWindow", "Total minutes per cycle"))
        self.lbl_volume_per_cycle.setText(_translate("MainWindow", "Volume per Cycle (Unit)"))
        self.lbl_total_min_cycles_3.setText(_translate("MainWindow", "Cartridge Filters (µ)"))
        self.lbl_de_per_cycle.setText(_translate("MainWindow", "D.E per Cycle 20kg sx"))
        self.btn_add_fluid_summary.setText(_translate("MainWindow", "Add the filled information to report"))
        self.btn_add_fluid_summary.clicked.connect(lambda:add_fluid_summary())
        self.tab_menus_wbco.setTabText(self.tab_menus_wbco.indexOf(self.tab_fluid_summary), _translate("MainWindow", "Fluid Summary"))
        self.lbl_wellbore.setText(_translate("MainWindow", "Wellbore Displacement"))
        self.lbl_time.setText(_translate("MainWindow", "Time"))
        self.btn_fluid_analysis.setText(_translate("MainWindow", "Next Step"))
        self.btn_fluid_analysis.clicked.connect(lambda:validator_fluid_analysis())
        self.btn_add_information_fluid_analysis.setText(_translate("MainWindow", "Add the filled information to report"))
        self.btn_add_information_fluid_analysis.clicked.connect(lambda:add_fluid_analys())
        self.lbl_volume_pumped.setText(_translate("MainWindow", "Volume Pumped (Unit)"))
        self.lbl_pumping_time.setText(_translate("MainWindow", "Pumping Time"))
        self.lbl_ntus.setText(_translate("MainWindow", "NTUs"))
        self.lbl_tss.setText(_translate("MainWindow", "TSS % Solids"))
        self.tab_menus_wbco.setTabText(self.tab_menus_wbco.indexOf(self.tab_fluid_analise), _translate("MainWindow", "Fluid Analysis"))
        self.lbl_daily_used.setText(_translate("MainWindow", "Daily Used"))
        self.lbl_aditional_stocke.setText(_translate("MainWindow", "Addtional Stock"))
        self.lbl_opening_stock.setText(_translate("MainWindow", "Opening Stock"))
        self.lbl_type.setText(_translate("MainWindow", "Type"))
        self.lbl_material_filtration.setText(_translate("MainWindow", "Material for Filtration"))
        self.lbl_hole_volume_value.setText(_translate("MainWindow","Hole Volume Value"))
        self.btn_next_step_consumables.setText(_translate("MainWindow", "Next Step"))
        self.btn_next_step_consumables.clicked.connect(lambda:validator_consumiveis())
        self.btn_add_information_consumables.setText(_translate("MainWindow", "Add the filled information to report"))
        self.btn_add_information_consumables.clicked.connect(lambda:add_consumiveis_information())
        self.tab_menus_wbco.setTabText(self.tab_menus_wbco.indexOf(self.tab_consumables), _translate("MainWindow", "Consumables"))
        self.lbl_numer_work_3.setText(_translate("MainWindow", "FIltration Engineer (Days)"))
        self.lbl_total_days.setText(_translate("MainWindow", "Total Days"))
        self.lbl_shift_enginer.setText(_translate("MainWindow", "Shift"))
        
        self.btn_save_report.setText(_translate("MainWindow", "Save Report"))
        self.btn_save_report.clicked.connect(lambda:report())

        self.btn_add_engineer_day.setText(_translate("MainWindow", "Add the filled information to report"))
        self.btn_add_engineer_day.clicked.connect(lambda:add_enginer_to_report())
        self.tab_menus_wbco.setTabText(self.tab_menus_wbco.indexOf(self.tab_enginer_day), _translate("MainWindow", "Engineer (Days)"))
        self.cbx_type_density.addItems(["SG","PPG"])
        self.cbx_material_filtration.currentTextChanged.connect(lambda:buscar_quantidade_stoke())
        self.cbx_shift_engineer.addItems(["Day","Night"])

        self.btn_compliance.clicked.connect(lambda:show_form_compliance())
        self.btn_wbco.clicked.connect(lambda:call_form_wbco())
        self.btn_logout.clicked.connect(lambda: logout())
        self.btn_filtration.clicked.connect(lambda:show_add_filtration())
        self.btn_tank_cleaning.clicked.connect(lambda:show_add_tank_cleaning())
        self.btn_user_profile.clicked.connect(lambda:show_perfil_user())


        def selected_value(tipo_valor_densidade,valor):
            if(tipo_valor_densidade == "SG"):
                if float(valor) >= 1 and float(valor) <= 1.5:
                    return 0
                return -1
            elif (tipo_valor_densidade == "PPG"):
                if float(valor) >= 8.33 and float(valor) <= 12.8:
                    return 0
                return -1


        def carregar_supervisor():
            self.cbx_prepared_by.addItems(modulo_wbco.wbcoController.carregar_supervisor())
            self.cbx_aproved_by.addItems(filtration.pack_employee.employeeController.listar())
            self.cbx_filtration_engineer.addItems(filtration.pack_employee.employeeController.listar())

        

        def show_message_sucess(text_input):
            msg_error = QMessageBox()
            msg_error.setIcon(QMessageBox.Information)
            msg_error.setText(str(text_input))
            msg_error.setWindowTitle('Adding data')
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("img/sucess_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg_error.setWindowIcon(icon)
            msg_error.exec_()

        def getPoco(cliente):
            self.cbx_well_number.clear()
            well_number_items = modulo_wbco.wbcoController.carregar_poco(cliente)
            self.cbx_well_number.addItems(well_number_items)

        def carregar_cliente():
            self.cbx_customer.addItems(modulo_wbco.wbcoController.carregar_cliente())

        def carregar_lista_ciclos():
            self.cbx_cycles.addItems(filtration.pack_filtration_sumary.fluid_sumaryController.listar_ciclos())

        def carregar_lista_tipo_consumiveis():
            self.cbx_material_filtration_2.addItems(filtration.pack_fluid_consumables.fluid_consumablesController.listar_type())

        def carregar_lista_consumiveis():
            self.cbx_material_filtration.addItems(filtration.pack_fluid_consumables.fluid_consumablesController.listar_consumiveis())

        def buscar_quantidade_stoke():
            quantidade = filtration.pack_fluid_consumables.fluid_consumablesController.buscar_quantidade_stoke(self.cbx_material_filtration.currentText())
            self.txt_opening_stock.setText(str(quantidade[0]))

        

        carregar_cliente()
        carregar_supervisor()
        carregar_lista_ciclos()
        carregar_lista_tipo_consumiveis()
        carregar_lista_consumiveis()

        id_supervisor = modulo_wbco.wbcoController.carregar_id_supervisor_by_email(self.lbl_user_logado.text())

        def message_error_validation(text_input_error,tittle_windows):
            msg_error = QMessageBox()
            msg_error.setIcon(QMessageBox.Critical)
            msg_error.setText(str(text_input_error))
            msg_error.setWindowTitle(str(tittle_windows))
            msg_error.exec_()

        def validator_report_information():

            countVezes = False

            caracter_especial = '!#$%&/=?*+ªº^~-"'
            only_special_character = '!#$%&/=?*+ªº^~-"'

            # Text Rig Name
            txt_job_ref = str(self.txt_job_ref.text())
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

            elif has_special_characters(txt_job_ref,only_special_character) or (txt_job_ref == ""):
                message_error_validation("This field does not accept special characters or is empty", "Error inserting Job Referece")

            else:
                self.tab_menus_wbco.setCurrentIndex(1)
                filtration.pack_report.reportController.carregar_cadastro(self.txt_job_ref.text(),self.txt_field_location.text(),self.txt_job_type.text(),"Days/Nigth",self.dateEdit.text(),id_supervisor,self.txt_rig_name.text())

        def validator_activity():
            txt_area_activity = str(self.txt_area_filtration_activity.toPlainText())
            if txt_area_activity == "":
                message_error_validation("This field does not acept empty","Error inserting Filtration Activity")
            else:
                self.tab_menus_wbco.setCurrentIndex(2)

        def validator_ongoing():
            txt_area_ongoing = str(self.txt_area_ongoing.toPlainText())
            txt_area_activity = str(self.txt_area_filtration_activity.toPlainText())
            if txt_area_ongoing == "":
                message_error_validation("This field does not acept empty","Error inserting Filtration Activity")
            else:
                id_cliente = controller.carregar_buscar_id_cliente(self.cbx_customer.currentText())
                id_ultimo_registo_report_header = modulo_wbco.wbcoController.buscar_id_report_header_ultimo()
                filtration.pack_report.reportController.salvar_info_report(txt_area_ongoing,txt_area_activity,id_cliente,id_ultimo_registo_report_header)
                self.tab_menus_wbco.setCurrentIndex(3)

        def validator_prepared_approved():
            self.tab_menus_wbco.setCurrentIndex(4)

        def validator_fluid_information():
            valor_retorno = selected_value(self.cbx_type_density.currentText(),self.txt_type_density.text())

            if valor_retorno == 0:
                id_ultimo_report_ft = filtration.pack_report.reportController.buscar_ultimo_registo_report()
                filtration.pack_fluid_information.fluid_informationController.carregar_cadastro(self.txt_fluid_type_filtered.text(),self.txt_daily_total_2.text(),self.txt_type_density.text(),self.cbx_type_density.currentText(),self.txt_viscosity.text(),self.txt_hole_volume.text(),self.cbx_hole_volume_bbls.currentText(),self.txt_vol_filtered_date.text(),id_ultimo_report_ft)
                show_message_sucess("Added successfully")
                self.tab_menus_wbco.setCurrentIndex(5)
            else:
                 message_error_validation("This unit does not accept this value","Error entering value")

        def validator_fluid_sumary():
            self.tab_menus_wbco.setCurrentIndex(6)

        def validator_fluid_analysis():
            self.tab_menus_wbco.setCurrentIndex(7)

        def validator_consumiveis():
            self.tab_menus_wbco.setCurrentIndex(8)

        def add_prepared_by():
            cbx_prepared = str(self.cbx_prepared_by.currentText())
            id_supervisor_prepared = filtration.pack_prepared_aproved.prepared_aprovedController.buscar_id_supersover_nome_por(cbx_prepared)
            
            id_ultimo_report_ft = filtration.pack_report.reportController.buscar_ultimo_registo_report()


            filtration.pack_prepared_aproved.prepared_aprovedController.add_preapred_to_report(id_supervisor_prepared,id_ultimo_report_ft)
            show_message_sucess("Added successfully")

        def add_approved_by():
            cbx_approved = str(self.cbx_aproved_by.currentText())
            id_supervisor_prepared = filtration.pack_prepared_aproved.prepared_aprovedController.buscar_id_empregado_nome_por(cbx_approved)
            id_ultimo_report_ft = filtration.pack_report.reportController.buscar_ultimo_registo_report()
            filtration.pack_prepared_aproved.prepared_aprovedController.add_approved_to_report(id_supervisor_prepared,id_ultimo_report_ft)
            show_message_sucess("Added successfully")

        def add_fluid_summary():
            cbx_cartigde = str(self.cbx_cartigde.currentText())
            txt_de = str(self.txt_de_per_cycle.text())

            id_ultimo_report_ft = filtration.pack_report.reportController.buscar_ultimo_registo_report()
            filtration.pack_filtration_sumary.fluid_sumaryController.carregar_cadastro(self.txt_start_time.text(),self.txt_stop_time.text(),self.txt_total_min_cycles.text(),self.txt_volume_per_cycle_value.text(),self.cbx_volume_per_cycle.currentText(),txt_de,cbx_cartigde,id_ultimo_report_ft,self.cbx_cycles.currentText())
            
            show_message_sucess("Added successfully")
            self.txt_start_time.clear()
            self.txt_stop_time.clear()
            self.txt_volume_per_cycle_value.clear()
            self.txt_de_per_cycle.clear()





        def add_fluid_analys():
            id_ultimo_report_ft = filtration.pack_report.reportController.buscar_ultimo_registo_report()
            filtration.pack_fluid_analisys.fluid_analisysController.carregar_cadastro(self.txt_wellbore.text(),self.txt_time.text(),self.txt_pumping_time.text(),self.txt_volume_pumped_value.text(),self.cbx_volume_pumped.currentText(),self.txt_ntus.text(),self.txt_tss.text(),id_ultimo_report_ft)
            show_message_sucess("Added successfully")
            self.txt_wellbore.clear()
            self.txt_time.clear()
            self.txt_pumping_time.clear()
            self.txt_volume_pumped_value.clear()
            self.txt_ntus.clear()
            self.txt_tss.clear()


        def add_consumiveis_information():
                stock_atual = int(self.txt_opening_stock.text())
                usado_diario_texto = self.txt_daily_used.text()
                adicional_texto = self.txt_aditional_stocke.text()

                id_consumivel = filtration.pack_fluid_consumables.fluid_consumablesController.buscar_id(self.cbx_material_filtration.currentText())

                id_tipo = filtration.pack_fluid_consumables.fluid_consumablesController.buscar_id_tipo(self.cbx_material_filtration_2.currentText())

                # Verificando se os campos de texto estão vazios ou não numéricos e tratando esses casos
                if usado_diario_texto.strip() == "" or not usado_diario_texto.isdigit():
                 usado_diario = 0
                else:
                 usado_diario = int(usado_diario_texto)

                if adicional_texto.strip() == "" or not adicional_texto.isdigit():
                   adicional = 0
                else:
                   adicional = int(adicional_texto)

                id_consumivel = filtration.pack_fluid_consumables.fluid_consumablesController.buscar_id(self.cbx_material_filtration.currentText())

                id_tipo = filtration.pack_fluid_consumables.fluid_consumablesController.buscar_id_tipo(self.cbx_material_filtration_2.currentText())

                # Calculando o novo estoque
                novo_estoque = stock_atual - usado_diario + adicional
                total_stoke = stock_atual + adicional
                id_ultimo_report_ft = filtration.pack_report.reportController.buscar_ultimo_registo_report()
                filtration.pack_fluid_consumables.fluid_consumablesController.carregar_cadastro(id_consumivel,id_tipo,stock_atual,adicional,total_stoke,usado_diario_texto,usado_diario,novo_estoque,id_ultimo_report_ft)

                show_message_sucess()
               


        
        def add_enginer_to_report():
            
            id_tecnico = filtration.pack_prepared_aproved.prepared_aprovedController.buscar_id_empregado_nome_por(self.cbx_filtration_engineer.currentText())
            id_ultimo_report_ft = filtration.pack_report.reportController.buscar_ultimo_registo_report()
            filtration.pack_enginer_day.enginer_dayController.cadastrar(self.cbx_shift_engineer.currentText(),self.txt_total_days.text(),id_tecnico,id_ultimo_report_ft)

            show_message_sucess()

        def report():
            show_message_sucess()



        def show_form_list_report():
            self.window = QtWidgets.QMainWindow()
            import filtration.filtration
            self.ui = filtration.filtration.Ui_MainWindow()
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


        def show_form_compliance():
            self.window = QtWidgets.QMainWindow()
            import  compliance.compliance_view as list
            self.ui = list.Ui_MainWindow()
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

        def show_add_filtration():
            self.window = QtWidgets.QMainWindow()
            import  filtration.filtration
            self.ui = filtration.filtration.Ui_MainWindow()
            self.ui.setupUi(self.window,self.lbl_user_logado.text())
            self.window.show()
            MainWindow.close()  

        def show_add_tank_cleaning():
            self.window = QtWidgets.QMainWindow()
            import  tank_cleanning.tank_cleaning_view
            self.ui = tank_cleanning.tank_cleaning_view.Ui_MainWindow()
            self.ui.setupUi(self.window,self.lbl_user_logado.text())
            self.window.show()
            MainWindow.close()

        def show_perfil_user():
            self.window = QtWidgets.QMainWindow()
            import modulo_home.user_profile as user
            self.ui = user.Ui_MainWindow()
            self.ui.setupUi(self.window,self.lbl_user_logado.text())
            self.window.show()      
        
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
