import sys
sys.path.append("..")

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget,QMessageBox
from modulo_personnel.personnel import form_personeel_list
import modulo_wbco.wbcoController
import tank_cleanning.pack_daily_progress.dayshift_activityController
import tank_cleanning.pack_report.reportController
import tank_cleanning.pack_shift.shiftController
import tank_cleanning.pack_hse.hseController
import tank_cleanning.pack_produtive_man.produtive_manController
import tank_cleanning.pack_non_produtive_type.non_produtive_typeController
import tank_cleanning.pack_non_produtive_man.non_produtive_manController
import tank_cleanning.pack_inventory_imob.inventory_imobController
import tank_cleanning.pack_employee.employeeController
import tank_cleanning.report.tank_cleaning_report
import tank_cleanning.pack_tank_information.tank_informationController
import tank_cleanning.tank_cleaning_view
import tank_cleanning.pack_consumables.consumablesController
import tank_cleanning.pack_pipe.pipeController
from PyQt5.QtGui import QIntValidator
import res


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

        self.gerador_report = tank_cleanning.report.tank_cleaning_report.GerarReport()

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
        icon9.addPixmap(QtGui.QPixmap("img/img/file-lines-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.cbx_aproved_by.setGeometry(QtCore.QRect(10, 310, 491, 41))
        
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
        self.txt_project_description = QtWidgets.QLineEdit(self.tab_report_information)
        self.txt_project_description.setGeometry(QtCore.QRect(530, 400, 491, 41))
        self.txt_project_description.setStyleSheet("""
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
        self.txt_project_description.setText("")
        self.txt_project_description.setPlaceholderText("")
        self.txt_project_description.setObjectName("txt_project_description")
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
        self.lbl_contacto_7 = QtWidgets.QLabel(self.tab_report_information)
        self.lbl_contacto_7.setGeometry(QtCore.QRect(10, 190, 101, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_contacto_7.setFont(font)
        self.lbl_contacto_7.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_contacto_7.setObjectName("lbl_contacto_7")
        self.lbl_approved_by = QtWidgets.QLabel(self.tab_report_information)
        self.lbl_approved_by.setGeometry(QtCore.QRect(10, 280, 101, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_approved_by.setFont(font)
        self.lbl_approved_by.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_approved_by.setObjectName("lbl_approved_by")
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
        self.lbl_description = QtWidgets.QLabel(self.tab_report_information)
        self.lbl_description.setGeometry(QtCore.QRect(530, 370, 231, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_description.setFont(font)
        self.lbl_description.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_description.setObjectName("lbl_description")
        self.btn_next_step_tank_information = QtWidgets.QPushButton(self.tab_report_information)
        self.btn_next_step_tank_information.setGeometry(QtCore.QRect(10, 400, 491, 41))
        self.btn_next_step_tank_information.setStyleSheet("\n"
"\n"
"QPushButton#btn_next_step_tank_information{\n"
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
"QPushButton#btn_next_step_tank_information:hover{\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_next_step_tank_information:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"background-color: #033029;\n"
"padding:10px;\n"
" }\n"
"")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("img/img/check-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_next_step_tank_information.setIcon(icon10)
        self.btn_next_step_tank_information.setObjectName("btn_next_step_tank_information")
        self.lbl_description.raise_()
        self.lbl_approved_by.raise_()
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
        self.cbx_aproved_by.raise_()
        self.txt_job_type.raise_()
        self.txt_project_description.raise_()
        self.dateEdit.raise_()
        self.btn_next_step_tank_information.raise_()
        self.tab_menus_wbco.addTab(self.tab_report_information, "")
        self.tab_tank = QtWidgets.QWidget()
        self.tab_tank.setObjectName("tab_tank")
        self.btn_next_step_dayshift_activities = QtWidgets.QPushButton(self.tab_tank)
        self.btn_next_step_dayshift_activities.setGeometry(QtCore.QRect(730, 220, 351, 41))
        self.btn_next_step_dayshift_activities.setStyleSheet("\n"
"\n"
"QPushButton#btn_next_step_dayshift_activities{\n"
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
"QPushButton#btn_next_step_dayshift_activities:hover{\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_next_step_dayshift_activities:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"background-color: #033029;\n"
"padding:10px;\n"
" }\n"
"")
        self.btn_next_step_dayshift_activities.setIcon(icon10)
        self.btn_next_step_dayshift_activities.setObjectName("btn_next_step_dayshift_activities")

        # ----------------------- Inicio Botao  Adicionar Tank ----------------------------------
        
        self.btn_add_tank_informatiion = QtWidgets.QPushButton(self.tab_tank)
        self.btn_add_tank_informatiion.setGeometry(QtCore.QRect(370, 220, 351, 41))
        self.btn_add_tank_informatiion.setStyleSheet("\n"
"\n"
"QPushButton#btn_add_tank_informatiion{\n"
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
"QPushButton#btn_add_tank_informatiion:hover{\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_add_tank_informatiion:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"background-color: #033029;\n"
"padding:10px;\n"
" }\n"
"")
        self.btn_add_tank_informatiion.setIcon(icon10)
        self.btn_add_tank_informatiion.setObjectName("btn_add_tank_informatiion")

        #------------------- FIn Botao Tank
        self.lbl_type_hse_2 = QtWidgets.QLabel(self.tab_tank)
        self.lbl_type_hse_2.setGeometry(QtCore.QRect(10, 100, 191, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_type_hse_2.setFont(font)
        self.lbl_type_hse_2.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_type_hse_2.setObjectName("lbl_type_hse_2")
        self.lbl_quantity_hse_2 = QtWidgets.QLabel(self.tab_tank)
        self.lbl_quantity_hse_2.setGeometry(QtCore.QRect(370, 100, 281, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_quantity_hse_2.setFont(font)
        self.lbl_quantity_hse_2.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_quantity_hse_2.setObjectName("lbl_quantity_hse_2")
        self.lbl_volume_waste = QtWidgets.QLabel(self.tab_tank)
        self.lbl_volume_waste.setGeometry(QtCore.QRect(720, 100, 200, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_volume_waste.setFont(font)
        self.lbl_volume_waste.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_volume_waste.setObjectName("lbl_volume_waste")

        self.lbl_tank_type = QtWidgets.QLabel(self.tab_tank)
        self.lbl_tank_type.setGeometry(QtCore.QRect(10, 185, 200, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_tank_type.setFont(font)
        self.lbl_tank_type.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_tank_type.setObjectName("lbl_tank_type")
        self.lbl_tank_type.setText("Tank Type")

        self.txt_number_tank = QtWidgets.QLineEdit(self.tab_tank)
        self.txt_number_tank.setGeometry(QtCore.QRect(10, 130, 351, 41))
        self.txt_number_tank.setStyleSheet("""
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
        self.txt_number_tank.setPlaceholderText("")
        self.txt_number_tank.setObjectName("txt_number_tank")

        self.txt_tank_type = QtWidgets.QLineEdit(self.tab_tank)
        self.txt_tank_type.setGeometry(QtCore.QRect(10, 220, 351, 41))
        self.txt_tank_type.setStyleSheet("""
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
        self.txt_tank_type.setPlaceholderText("")
        self.txt_tank_type.setObjectName("txt_tank_type")

        self.txt_type_west = QtWidgets.QLineEdit(self.tab_tank)
        self.txt_type_west.setGeometry(QtCore.QRect(370, 130, 351, 41))
        self.txt_type_west.setStyleSheet("""
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
        self.txt_type_west.setPlaceholderText("")
        self.txt_type_west.setObjectName("txt_type_west")
        self.txt_volume_west = QtWidgets.QLineEdit(self.tab_tank)
        self.txt_volume_west.setGeometry(QtCore.QRect(730, 130, 351, 41))
        self.txt_volume_west.setStyleSheet("""
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
        self.txt_volume_west.setPlaceholderText("")
        self.txt_volume_west.setObjectName("txt_volume_west")
        self.lbl_volume_waste.raise_()
        self.lbl_quantity_hse_2.raise_()
        self.lbl_type_hse_2.raise_()
        self.btn_next_step_dayshift_activities.raise_()
        self.txt_number_tank.raise_()
        self.txt_type_west.raise_()
        self.txt_volume_west.raise_()
        
        self.tb_dayshift_activities = QtWidgets.QWidget()
        self.tb_dayshift_activities.setObjectName("tb_dayshift_activities")
        self.lbl_daily_progress = QtWidgets.QLabel(self.tb_dayshift_activities)
        self.lbl_daily_progress.setGeometry(QtCore.QRect(10, 10, 301, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_daily_progress.setFont(font)
        self.lbl_daily_progress.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_daily_progress.setObjectName("lbl_daily_progress")
        self.btn_next_step_dayshift_per_person = QtWidgets.QPushButton(self.tb_dayshift_activities)
        self.btn_next_step_dayshift_per_person.setGeometry(QtCore.QRect(10, 410, 491, 41))
        self.btn_next_step_dayshift_per_person.setStyleSheet("\n"
"\n"
"QPushButton#btn_next_step_dayshift_per_person{\n"
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
"QPushButton#btn_next_step_dayshift_per_person:hover{\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_next_step_dayshift_per_person:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"background-color: #033029;\n"
"padding:10px;\n"
" }\n"
"")
        self.btn_next_step_dayshift_per_person.setIcon(icon10)
        self.btn_next_step_dayshift_per_person.setObjectName("btn_next_step_dayshift_per_person")
        self.txt_area_daily_progress = QtWidgets.QPlainTextEdit(self.tb_dayshift_activities)
        self.txt_area_daily_progress.setGeometry(QtCore.QRect(10, 40, 1051, 61))
        self.txt_area_daily_progress.setStyleSheet("background-color:#fff;\n"
"border: 1px solid #8ec0af;\n"
"border-radius: 6px")
        self.txt_area_daily_progress.setObjectName("txt_area_daily_progress")
        self.lbl_planned_activities = QtWidgets.QLabel(self.tb_dayshift_activities)
        self.lbl_planned_activities.setGeometry(QtCore.QRect(10, 110, 411, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_planned_activities.setFont(font)
        self.lbl_planned_activities.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_planned_activities.setObjectName("lbl_planned_activities")
        self.txt_area_planed_activities = QtWidgets.QPlainTextEdit(self.tb_dayshift_activities)
        self.txt_area_planed_activities.setGeometry(QtCore.QRect(10, 140, 1051, 61))
        self.txt_area_planed_activities.setStyleSheet("background-color:#fff;\n"
"border: 1px solid #8ec0af;\n"
"border-radius: 6px")
        self.txt_area_planed_activities.setObjectName("txt_area_planed_activities")
        self.lbl_norm_reading = QtWidgets.QLabel(self.tb_dayshift_activities)
        self.lbl_norm_reading.setGeometry(QtCore.QRect(10, 210, 331, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_norm_reading.setFont(font)
        self.lbl_norm_reading.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_norm_reading.setObjectName("lbl_norm_reading")
        self.txt_area_norm_reading = QtWidgets.QPlainTextEdit(self.tb_dayshift_activities)
        self.txt_area_norm_reading.setGeometry(QtCore.QRect(10, 240, 1051, 61))
        self.txt_area_norm_reading.setStyleSheet("background-color:#fff;\n"
"border: 1px solid #8ec0af;\n"
"border-radius: 6px")
        self.txt_area_norm_reading.setObjectName("txt_area_norm_reading")
        self.lbl_equipament_material = QtWidgets.QLabel(self.tb_dayshift_activities)
        self.lbl_equipament_material.setGeometry(QtCore.QRect(10, 310, 141, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_equipament_material.setFont(font)
        self.lbl_equipament_material.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_equipament_material.setObjectName("lbl_equipament_material")
        self.txt_area_equipament_material = QtWidgets.QPlainTextEdit(self.tb_dayshift_activities)
        self.txt_area_equipament_material.setGeometry(QtCore.QRect(10, 340, 1051, 61))
        self.txt_area_equipament_material.setStyleSheet("background-color:#fff;\n"
"border: 1px solid #8ec0af;\n"
"border-radius: 6px")
        self.txt_area_equipament_material.setObjectName("txt_area_equipament_material")
        self.tab_menus_wbco.addTab(self.tb_dayshift_activities, "")
        self.tab_menus_wbco.addTab(self.tab_tank, "")
        self.tab_dayshift_per_person = QtWidgets.QWidget()
        self.tab_dayshift_per_person.setObjectName("tab_dayshift_per_person")
        self.lbl_name_person_dayshift = QtWidgets.QLabel(self.tab_dayshift_per_person)
        self.lbl_name_person_dayshift.setGeometry(QtCore.QRect(10, 20, 51, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_name_person_dayshift.setFont(font)
        self.lbl_name_person_dayshift.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_name_person_dayshift.setObjectName("lbl_name_person_dayshift")
        self.lbl_personel_position = QtWidgets.QLabel(self.tab_dayshift_per_person)
        self.lbl_personel_position.setGeometry(QtCore.QRect(530, 20, 150, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_personel_position.setFont(font)
        self.lbl_personel_position.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_personel_position.setObjectName("lbl_personel_position")
        self.txt_crew_change = QtWidgets.QLineEdit(self.tab_dayshift_per_person)
        self.txt_crew_change.setGeometry(QtCore.QRect(530, 140, 231, 41))
        self.txt_crew_change.setStyleSheet("""
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
        self.txt_crew_change.setPlaceholderText("")
        self.txt_crew_change.setObjectName("txt_crew_change")
        
        self.cbx_person_dayshift = QtWidgets.QComboBox(self.tab_dayshift_per_person)
        self.cbx_person_dayshift.setGeometry(QtCore.QRect(10, 50, 491, 41))
        self.cbx_person_dayshift.setStyleSheet("""
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
        self.cbx_person_dayshift.setObjectName("cbx_person_dayshift")
        
        self.lbl_planed_dembed = QtWidgets.QLabel(self.tab_dayshift_per_person)
        self.lbl_planed_dembed.setGeometry(QtCore.QRect(10, 110, 211, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_planed_dembed.setFont(font)
        self.lbl_planed_dembed.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_planed_dembed.setObjectName("lbl_planed_dembed")
        self.lbl_crew_change = QtWidgets.QLabel(self.tab_dayshift_per_person)
        self.lbl_crew_change.setGeometry(QtCore.QRect(530, 110, 191, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_crew_change.setFont(font)
        self.lbl_crew_change.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_crew_change.setObjectName("lbl_crew_change")
        
        self.cbx_personel_position = QtWidgets.QComboBox(self.tab_dayshift_per_person)
        self.cbx_personel_position.setGeometry(QtCore.QRect(530, 50, 491, 41))
        self.cbx_personel_position.setStyleSheet("""
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
        self.cbx_personel_position.setObjectName("cbx_personel_position")
       
       
        self.cbx_planned_demeb = QtWidgets.QComboBox(self.tab_dayshift_per_person)
        self.cbx_planned_demeb.setGeometry(QtCore.QRect(10, 140, 491, 41))
        self.cbx_planned_demeb.setStyleSheet("""
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
        self.cbx_planned_demeb.setObjectName("cbx_planned_demeb")
        self.btn_next_step_hse = QtWidgets.QPushButton(self.tab_dayshift_per_person)
        self.btn_next_step_hse.setGeometry(QtCore.QRect(530, 210, 491, 41))
        self.btn_next_step_hse.setStyleSheet("\n"
"\n"
"QPushButton#btn_next_step_hse{\n"
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
"QPushButton#btn_next_step_hse:hover{\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_next_step_hse:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"background-color: #033029;\n"
"padding:10px;\n"
" }\n"
"")
        self.btn_next_step_hse.setIcon(icon10)
        self.btn_next_step_hse.setObjectName("btn_next_step_hse")
        self.btn_add_information_dayshift = QtWidgets.QPushButton(self.tab_dayshift_per_person)
        self.btn_add_information_dayshift.setGeometry(QtCore.QRect(10, 210, 491, 41))
        self.btn_add_information_dayshift.setStyleSheet("\n"
"\n"
"QPushButton#btn_add_information_dayshift{\n"
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
"QPushButton#btn_add_information_dayshift:hover{\n"
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
        self.btn_add_information_dayshift.setIcon(icon10)
        self.btn_add_information_dayshift.setObjectName("btn_add_information_dayshift")
        self.cbx_dayshift = QtWidgets.QComboBox(self.tab_dayshift_per_person)
        self.cbx_dayshift.setGeometry(QtCore.QRect(770, 140, 245, 41))
        self.cbx_dayshift.setStyleSheet("""
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
        self.cbx_dayshift.setObjectName("cbx_dayshift")
        self.lbl_shift_dayshift = QtWidgets.QLabel(self.tab_dayshift_per_person)
        self.lbl_shift_dayshift.setGeometry(QtCore.QRect(780, 110, 41, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_shift_dayshift.setFont(font)
        self.lbl_shift_dayshift.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_shift_dayshift.setObjectName("lbl_shift_dayshift")
        self.lbl_shift_dayshift.raise_()
        self.lbl_planed_dembed.raise_()
        self.lbl_crew_change.raise_()
        self.lbl_name_person_dayshift.raise_()
        self.lbl_personel_position.raise_()
        self.txt_crew_change.raise_()
        self.cbx_person_dayshift.raise_()
        self.cbx_personel_position.raise_()
        self.cbx_planned_demeb.raise_()
        self.btn_next_step_hse.raise_()
        self.btn_add_information_dayshift.raise_()
        self.cbx_dayshift.raise_()
        self.tab_menus_wbco.addTab(self.tab_dayshift_per_person, "")
        self.tab_hse = QtWidgets.QWidget()
        self.tab_hse.setObjectName("tab_hse")
        self.lbl_type_hse = QtWidgets.QLabel(self.tab_hse)
        self.lbl_type_hse.setGeometry(QtCore.QRect(10, 80, 41, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_type_hse.setFont(font)
        self.lbl_type_hse.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_type_hse.setObjectName("lbl_type_hse")
        self.lbl_comments = QtWidgets.QLabel(self.tab_hse)
        self.lbl_comments.setGeometry(QtCore.QRect(540, 80, 181, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_comments.setFont(font)
        self.lbl_comments.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_comments.setObjectName("lbl_comments")
        self.cbx_type_hse = QtWidgets.QComboBox(self.tab_hse)
        self.cbx_type_hse.setGeometry(QtCore.QRect(10, 110, 251, 41))
        self.cbx_type_hse.setStyleSheet("""
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
        self.cbx_type_hse.setObjectName("cbx_type_hse")
        self.txt_quantity = QtWidgets.QLineEdit(self.tab_hse)
        self.txt_quantity.setGeometry(QtCore.QRect(270, 110, 231, 41))
        self.txt_quantity.setStyleSheet("""
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
        self.txt_quantity.setPlaceholderText("")
        self.txt_quantity.setObjectName("txt_quantity")
        self.lbl_quantity_hse = QtWidgets.QLabel(self.tab_hse)
        self.lbl_quantity_hse.setGeometry(QtCore.QRect(270, 80, 161, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_quantity_hse.setFont(font)
        self.lbl_quantity_hse.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_quantity_hse.setObjectName("lbl_quantity_hse")
        self.txt_comments = QtWidgets.QLineEdit(self.tab_hse)
        self.txt_comments.setGeometry(QtCore.QRect(540, 110, 491, 41))
        self.txt_comments.setStyleSheet("""
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
        self.txt_comments.setPlaceholderText("")
        self.txt_comments.setObjectName("txt_comments")
        self.btn_add_information_hse = QtWidgets.QPushButton(self.tab_hse)
        self.btn_add_information_hse.setGeometry(QtCore.QRect(10, 180, 491, 41))
        self.btn_add_information_hse.setStyleSheet("\n"
"\n"
"QPushButton#btn_add_information_hse{\n"
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
"QPushButton#btn_add_information_hse:hover{\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_add_information_hse:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"background-color: #033029;\n"
"padding:10px;\n"
" }\n"
"")
        self.btn_add_information_hse.setIcon(icon10)
        self.btn_add_information_hse.setObjectName("btn_add_information_hse")
        self.btn_next_step_produtive_man = QtWidgets.QPushButton(self.tab_hse)
        self.btn_next_step_produtive_man.setGeometry(QtCore.QRect(540, 180, 491, 41))
        self.btn_next_step_produtive_man.setStyleSheet("\n"
"\n"
"QPushButton#btn_next_step_produtive_man{\n"
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
"QPushButton#btn_next_step_produtive_man:hover{\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_next_step_produtive_man:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"background-color: #033029;\n"
"padding:10px;\n"
" }\n"
"")
        self.btn_next_step_produtive_man.setIcon(icon10)
        self.btn_next_step_produtive_man.setObjectName("btn_next_step_produtive_man")
        self.lbl_quantity_hse.raise_()
        self.lbl_type_hse.raise_()
        self.lbl_comments.raise_()
        self.cbx_type_hse.raise_()
        self.txt_quantity.raise_()
        self.txt_comments.raise_()
        self.btn_add_information_hse.raise_()
        self.btn_next_step_produtive_man.raise_()
        self.tab_menus_wbco.addTab(self.tab_hse, "")
        self.tab_productive_man_hour = QtWidgets.QWidget()
        self.tab_productive_man_hour.setObjectName("tab_productive_man_hour")
        self.lbl_visual_complete = QtWidgets.QLabel(self.tab_productive_man_hour)
        self.lbl_visual_complete.setGeometry(QtCore.QRect(780, 280, 160, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_visual_complete.setFont(font)
        self.lbl_visual_complete.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_visual_complete.setObjectName("lbl_visual_complete")

        self.lbl_visual_complete_user = QtWidgets.QLabel(self.tab_productive_man_hour)
        self.lbl_visual_complete_user.setGeometry(QtCore.QRect(530, 280, 200, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_visual_complete_user.setFont(font)
        self.lbl_visual_complete_user.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_visual_complete_user.setObjectName("lbl_visual_complete_user")

        self.lbl_visual_complete_user.setText(" User Perception %")

        self.lbl_original_hour = QtWidgets.QLabel(self.tab_productive_man_hour)
        self.lbl_original_hour.setGeometry(QtCore.QRect(10, 190, 371, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_original_hour.setFont(font)
        self.lbl_original_hour.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_original_hour.setObjectName("lbl_original_hour")
        self.txt_booked_today = QtWidgets.QLineEdit(self.tab_productive_man_hour)
        self.txt_booked_today.setGeometry(QtCore.QRect(10, 310, 491, 41))
        self.txt_booked_today.setStyleSheet("""
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
        self.txt_booked_today.setPlaceholderText("")
        self.txt_booked_today.setObjectName("txt_booked_today")
        self.txt_hour_remaining = QtWidgets.QLineEdit(self.tab_productive_man_hour)
        self.txt_hour_remaining.setGeometry(QtCore.QRect(530, 230, 491, 41))
        self.txt_hour_remaining.setStyleSheet("""
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
        self.txt_hour_remaining.setPlaceholderText("")
        self.txt_hour_remaining.setObjectName("txt_hour_remaining")
        self.txt_hour_booked_date = QtWidgets.QLineEdit(self.tab_productive_man_hour)
        self.txt_hour_booked_date.setGeometry(QtCore.QRect(530, 140, 491, 41))
        self.txt_hour_booked_date.setStyleSheet("""
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
        self.txt_hour_booked_date.setPlaceholderText("")
        self.txt_hour_booked_date.setObjectName("txt_hour_booked_date")
        self.lbl_hour_booked_date = QtWidgets.QLabel(self.tab_productive_man_hour)
        self.lbl_hour_booked_date.setGeometry(QtCore.QRect(530, 110, 351, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_hour_booked_date.setFont(font)
        self.lbl_hour_booked_date.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_hour_booked_date.setObjectName("lbl_hour_booked_date")
        self.txt_qt_booked_today = QtWidgets.QLineEdit(self.tab_productive_man_hour)
        self.txt_qt_booked_today.setGeometry(QtCore.QRect(530, 50, 491, 41))
        self.txt_qt_booked_today.setStyleSheet("""
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
        self.txt_qt_booked_today.setPlaceholderText("")
        self.txt_qt_booked_today.setObjectName("txt_qt_booked_today")
        self.lbl_description_man_hour = QtWidgets.QLabel(self.tab_productive_man_hour)
        self.lbl_description_man_hour.setGeometry(QtCore.QRect(10, 110, 81, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_description_man_hour.setFont(font)
        self.lbl_description_man_hour.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_description_man_hour.setObjectName("lbl_description_man_hour")
        self.lbl_Ot_Worked_today = QtWidgets.QLabel(self.tab_productive_man_hour)
        self.lbl_Ot_Worked_today.setGeometry(QtCore.QRect(530, 20, 430, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_Ot_Worked_today.setFont(font)
        self.lbl_Ot_Worked_today.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_Ot_Worked_today.setObjectName("lbl_Ot_Worked_today")
        self.lbl_hour_remaining = QtWidgets.QLabel(self.tab_productive_man_hour)
        self.lbl_hour_remaining.setGeometry(QtCore.QRect(530, 200, 311, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_hour_remaining.setFont(font)
        self.lbl_hour_remaining.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_hour_remaining.setObjectName("lbl_hour_remaining")
        self.txt_visual_complete = QtWidgets.QLineEdit(self.tab_productive_man_hour)
        self.txt_visual_complete.setGeometry(QtCore.QRect(780, 310, 240, 41))
        self.txt_visual_complete.setStyleSheet("""
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
        self.txt_visual_complete.setPlaceholderText("")
        self.txt_visual_complete.setObjectName("txt_visual_complete")

        self.txt_visual_complete_user = QtWidgets.QLineEdit(self.tab_productive_man_hour)
        self.txt_visual_complete_user.setGeometry(QtCore.QRect(530, 310, 240, 41))
        self.txt_visual_complete_user.setStyleSheet("""
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
        self.txt_visual_complete_user.setPlaceholderText("")
        self.txt_visual_complete_user.setObjectName("txt_visual_complete_user")

        self.lbl_numer_work = QtWidgets.QLabel(self.tab_productive_man_hour)
        self.lbl_numer_work.setGeometry(QtCore.QRect(10, 20, 341, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_numer_work.setFont(font)
        self.lbl_numer_work.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_numer_work.setObjectName("lbl_numer_work")
        self.lbl_booked_today = QtWidgets.QLabel(self.tab_productive_man_hour)
        self.lbl_booked_today.setGeometry(QtCore.QRect(10, 280, 341, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_booked_today.setFont(font)
        self.lbl_booked_today.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_booked_today.setObjectName("lbl_booked_today")
        self.btn_next_step_non_produtive_man = QtWidgets.QPushButton(self.tab_productive_man_hour)
        self.btn_next_step_non_produtive_man.setGeometry(QtCore.QRect(530, 380, 491, 41))
        self.btn_next_step_non_produtive_man.setStyleSheet("\n"
"\n"
"QPushButton#btn_next_step_non_produtive_man{\n"
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
"QPushButton#btn_next_step_non_produtive_man:hover{\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_next_step_non_produtive_man:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"background-color: #033029;\n"
"padding:10px;\n"
" }\n"
"")
        self.btn_next_step_non_produtive_man.setIcon(icon10)
        self.btn_next_step_non_produtive_man.setObjectName("btn_next_step_non_produtive_man")
        self.btn_add_information_productive_man = QtWidgets.QPushButton(self.tab_productive_man_hour)
        self.btn_add_information_productive_man.setGeometry(QtCore.QRect(10, 380, 491, 41))
        self.btn_add_information_productive_man.setStyleSheet("\n"
"\n"
"QPushButton#btn_add_information_productive_man{\n"
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
"QPushButton#btn_add_information_productive_man:hover{\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_add_information_productive_man:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"background-color: #033029;\n"
"padding:10px;\n"
" }\n"
"")
        self.btn_add_information_productive_man.setIcon(icon10)
        self.btn_add_information_productive_man.setObjectName("btn_add_information_productive_man")
        self.txt_numbrt_work = QtWidgets.QLineEdit(self.tab_productive_man_hour)
        self.txt_numbrt_work.setGeometry(QtCore.QRect(10, 50, 491, 41))
        self.txt_numbrt_work.setStyleSheet("""
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
        self.txt_numbrt_work.setPlaceholderText("")
        self.txt_numbrt_work.setObjectName("txt_numbrt_work")
        self.txt_description_man_hour = QtWidgets.QLineEdit(self.tab_productive_man_hour)
        self.txt_description_man_hour.setGeometry(QtCore.QRect(10, 140, 491, 41))
        self.txt_description_man_hour.setStyleSheet("""
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
        self.txt_description_man_hour.setPlaceholderText("")
        self.txt_description_man_hour.setObjectName("txt_description_man_hour")
        self.txt_original_hour = QtWidgets.QLineEdit(self.tab_productive_man_hour)
        self.txt_original_hour.setGeometry(QtCore.QRect(10, 220, 491, 41))
        self.txt_original_hour.setStyleSheet("""
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
        self.txt_original_hour.setPlaceholderText("")
        self.txt_original_hour.setObjectName("txt_original_hour")
        self.lbl_booked_today.raise_()
        self.lbl_description_man_hour.raise_()
        self.lbl_hour_remaining.raise_()
        self.lbl_hour_booked_date.raise_()
        self.lbl_Ot_Worked_today.raise_()
        self.lbl_visual_complete.raise_()
        self.lbl_original_hour.raise_()
        self.txt_booked_today.raise_()
        self.txt_hour_remaining.raise_()
        self.txt_hour_booked_date.raise_()
        self.txt_qt_booked_today.raise_()
        self.txt_visual_complete.raise_()
        self.lbl_numer_work.raise_()
        self.btn_next_step_non_produtive_man.raise_()
        self.btn_add_information_productive_man.raise_()
        self.txt_numbrt_work.raise_()
        self.txt_description_man_hour.raise_()
        self.txt_original_hour.raise_()
        self.tab_menus_wbco.addTab(self.tab_productive_man_hour, "")
        self.tab_non_productive_man_hour = QtWidgets.QWidget()
        self.tab_non_productive_man_hour.setObjectName("tab_non_productive_man_hour")
        self.cbx_non_produtive_man = QtWidgets.QComboBox(self.tab_non_productive_man_hour)
        self.cbx_non_produtive_man.setGeometry(QtCore.QRect(10, 110, 251, 41))
        self.cbx_non_produtive_man.setStyleSheet("""
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
        self.cbx_non_produtive_man.setObjectName("cbx_non_produtive_man")
        self.txt_comments_non_produtive_man = QtWidgets.QLineEdit(self.tab_non_productive_man_hour)
        self.txt_comments_non_produtive_man.setGeometry(QtCore.QRect(540, 110, 491, 41))
        self.txt_comments_non_produtive_man.setStyleSheet("""
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
        self.txt_comments_non_produtive_man.setPlaceholderText("")
        self.txt_comments_non_produtive_man.setObjectName("txt_comments_non_produtive_man")
        self.txt_hour_non_produtive_man = QtWidgets.QLineEdit(self.tab_non_productive_man_hour)
        self.txt_hour_non_produtive_man.setGeometry(QtCore.QRect(270, 110, 231, 41))
        self.txt_hour_non_produtive_man.setStyleSheet("""
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
        self.txt_hour_non_produtive_man.setPlaceholderText("")
        self.txt_hour_non_produtive_man.setObjectName("txt_hour_non_produtive_man")
        self.btn_next_step_imob_inventy = QtWidgets.QPushButton(self.tab_non_productive_man_hour)
        self.btn_next_step_imob_inventy.setGeometry(QtCore.QRect(540, 180, 491, 41))
        self.btn_next_step_imob_inventy.setStyleSheet("\n"
"\n"
"QPushButton#btn_next_step_imob_inventy{\n"
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
"QPushButton#btn_next_step_imob_inventy:hover{\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_next_step_imob_inventy:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"background-color: #033029;\n"
"padding:10px;\n"
" }\n"
"")
        self.btn_next_step_imob_inventy.setIcon(icon10)
        self.btn_next_step_imob_inventy.setObjectName("btn_next_step_imob_inventy")
        self.btn_add_information_non_productive = QtWidgets.QPushButton(self.tab_non_productive_man_hour)
        self.btn_add_information_non_productive.setGeometry(QtCore.QRect(10, 180, 491, 41))
        self.btn_add_information_non_productive.setStyleSheet("\n"
"\n"
"QPushButton#btn_add_information_non_productive{\n"
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
"QPushButton#btn_add_information_non_productive:hover{\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_add_information_non_productive:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"background-color: #033029;\n"
"padding:10px;\n"
" }\n"
"")
        self.btn_add_information_non_productive.setIcon(icon10)
        self.btn_add_information_non_productive.setObjectName("btn_add_information_non_productive")
        self.lbl_hour_non_produtive_man = QtWidgets.QLabel(self.tab_non_productive_man_hour)
        self.lbl_hour_non_produtive_man.setGeometry(QtCore.QRect(270, 80, 161, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_hour_non_produtive_man.setFont(font)
        self.lbl_hour_non_produtive_man.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_hour_non_produtive_man.setObjectName("lbl_hour_non_produtive_man")
        self.lbl_comments_non_produtive_man = QtWidgets.QLabel(self.tab_non_productive_man_hour)
        self.lbl_comments_non_produtive_man.setGeometry(QtCore.QRect(540, 80, 181, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_comments_non_produtive_man.setFont(font)
        self.lbl_comments_non_produtive_man.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_comments_non_produtive_man.setObjectName("lbl_comments_non_produtive_man")
        self.lbl_type_non_produtive_man = QtWidgets.QLabel(self.tab_non_productive_man_hour)
        self.lbl_type_non_produtive_man.setGeometry(QtCore.QRect(10, 80, 141, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_type_non_produtive_man.setFont(font)
        self.lbl_type_non_produtive_man.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_type_non_produtive_man.setObjectName("lbl_type_non_produtive_man")
        self.lbl_comments_non_produtive_man.raise_()
        self.lbl_hour_non_produtive_man.raise_()
        self.lbl_type_non_produtive_man.raise_()
        self.cbx_non_produtive_man.raise_()
        self.txt_comments_non_produtive_man.raise_()
        self.txt_hour_non_produtive_man.raise_()
        self.btn_next_step_imob_inventy.raise_()
        self.btn_add_information_non_productive.raise_()
        self.tab_menus_wbco.addTab(self.tab_non_productive_man_hour, "")
        self.tab_imobe_inventory = QtWidgets.QWidget()
        self.tab_imobe_inventory.setObjectName("tab_imobe_inventory")
        
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        

        self.txt_daily_used_consumables = QtWidgets.QLineEdit(self.tab_imobe_inventory)
        self.txt_daily_used_consumables.setGeometry(QtCore.QRect(10, 150, 491, 41))
        self.txt_daily_used_consumables.setStyleSheet("""
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
        self.txt_daily_used_consumables.setPlaceholderText("")
        self.txt_daily_used_consumables.setObjectName("txt_daily_used_consumables")


        self.cbx_ppe = QtWidgets.QComboBox(self.tab_imobe_inventory)
        self.cbx_ppe.setGeometry(QtCore.QRect(530, 60, 491, 41))
        self.cbx_ppe.setStyleSheet("""
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
        self.cbx_ppe.setPlaceholderText("")
        self.cbx_ppe.setObjectName("cbx_ppe")
        self.txt_daily_used_consumable = QtWidgets.QLineEdit(self.tab_imobe_inventory)
        self.txt_daily_used_consumable.setGeometry(QtCore.QRect(10, 60, 491, 41))
        self.txt_daily_used_consumable.setStyleSheet("""
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
        self.txt_daily_used_consumable.setPlaceholderText("")
        self.txt_daily_used_consumable.setObjectName("txt_daily_used_consumable")



        ########### Texto para Opening Stock ####

        self.txt_opening_stock = QtWidgets.QLineEdit(self.tab_imobe_inventory)
        self.txt_opening_stock.setGeometry(QtCore.QRect(10, 230, 491, 41))
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
        self.txt_opening_stock.setEnabled(False)
    

        ##########################################

        

        self.lbl_daily_used = QtWidgets.QLabel(self.tab_imobe_inventory)
        self.lbl_daily_used.setGeometry(QtCore.QRect(10, 119, 141, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_daily_used.setFont(font)
        self.lbl_daily_used.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_daily_used.setObjectName("lbl_daily_used")

        #################### lbl,txt para PPE #########################

        self.lbl_daily_used_ppe = QtWidgets.QLabel(self.tab_imobe_inventory)
        self.lbl_daily_used_ppe.setGeometry(QtCore.QRect(530, 119, 141, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_daily_used_ppe.setFont(font)
        self.lbl_daily_used_ppe.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_daily_used_ppe.setObjectName("lbl_daily_used_ppe")
        self.lbl_daily_used_ppe.setText("Daily Used")


        self.lbl_opening_stock_ppe = QtWidgets.QLabel(self.tab_imobe_inventory)
        self.lbl_opening_stock_ppe.setGeometry(QtCore.QRect(530, 200, 151, 29))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_opening_stock_ppe.setFont(font)
        self.lbl_opening_stock_ppe.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_opening_stock_ppe.setObjectName("lbl_opening_stock")
        self.lbl_opening_stock_ppe.setText("Opening Stock")


        self.txt_daily_used_ppe = QtWidgets.QLineEdit(self.tab_imobe_inventory)
        self.txt_daily_used_ppe.setGeometry(QtCore.QRect(530, 150, 491, 41))
        self.txt_daily_used_ppe.setStyleSheet("""
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
        self.txt_daily_used_ppe.setPlaceholderText("")
        self.txt_daily_used_ppe.setObjectName("txt_daily_used_ppe")



        ########### Texto para Opening Stock ####

        self.txt_opening_stock_ppe = QtWidgets.QLineEdit(self.tab_imobe_inventory)
        self.txt_opening_stock_ppe.setGeometry(QtCore.QRect(530, 230, 491, 41))
        self.txt_opening_stock_ppe.setStyleSheet("""
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
        self.txt_opening_stock_ppe.setPlaceholderText("")
        self.txt_opening_stock_ppe.setObjectName("txt_opening_stock")
        self.txt_opening_stock_ppe.setEnabled(False)

        ###############################################################

        self.lbl_opening_stock = QtWidgets.QLabel(self.tab_imobe_inventory)
        self.lbl_opening_stock.setGeometry(QtCore.QRect(10, 200, 151, 29))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_opening_stock.setFont(font)
        self.lbl_opening_stock.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_opening_stock.setObjectName("lbl_opening_stock")
        self.lbl_material_ppe = QtWidgets.QLabel(self.tab_imobe_inventory)
        self.lbl_material_ppe.setGeometry(QtCore.QRect(530, 30, 311, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_material_ppe.setFont(font)
        self.lbl_material_ppe.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_material_ppe.setObjectName("lbl_material_ppe")
        self.lbl_consumambles = QtWidgets.QLabel(self.tab_imobe_inventory)
        self.lbl_consumambles.setGeometry(QtCore.QRect(10, 30, 370, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_consumambles.setFont(font)
        self.lbl_consumambles.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_consumambles.setObjectName("lbl_consumambles")
        
        self.lbl_additional_stock = QtWidgets.QLabel(self.tab_imobe_inventory)
        self.lbl_additional_stock.setFont(font)
        self.lbl_additional_stock.setObjectName("lbl_additional_stock")
        self.lbl_additional_stock.setText("Additional Stock")
        self.lbl_additional_stock.setGeometry(QtCore.QRect(530, 280, 491, 41))

        self.lbl_additional_stock_consumivel = QtWidgets.QLabel(self.tab_imobe_inventory)
        self.lbl_additional_stock_consumivel.setFont(font)
        self.lbl_additional_stock_consumivel.setObjectName("lbl_additional_stock_consumivel")
        self.lbl_additional_stock_consumivel.setText("Additional Stock")
        self.lbl_additional_stock_consumivel.setGeometry(QtCore.QRect(10, 280, 491, 41))

        self.txt_aditin_stock = QtWidgets.QLineEdit(self.tab_imobe_inventory)
        self.txt_aditin_stock.setObjectName("txt_aditin_stock")
        self.txt_aditin_stock.setStyleSheet("""
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

        self.txt_aditin_stock.setGeometry(QtCore.QRect(530,320,491,41))
        self.txt_aditin_stock.setText(str("0"))

        self.txt_aditin_stock_consumivel = QtWidgets.QLineEdit(self.tab_imobe_inventory)
        self.txt_aditin_stock_consumivel.setObjectName("txt_aditin_stock_consumivel")
        self.txt_aditin_stock_consumivel.setStyleSheet("""
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

        self.txt_aditin_stock_consumivel.setGeometry(QtCore.QRect(10,320,491,41))
        self.txt_aditin_stock_consumivel.setText(str("0"))

        self.btn_add_information_inventory_mob = QtWidgets.QPushButton(self.tab_imobe_inventory)
        self.btn_add_information_inventory_mob.setGeometry(QtCore.QRect(530, 390, 491, 41))
        self.btn_add_information_inventory_mob.setStyleSheet("\n"
"\n"
"QPushButton#btn_add_information_inventory_mob{\n"
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
"QPushButton#btn_add_information_inventory_mob:hover{\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_add_information_inventory_mob:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"background-color: #033029;\n"
"padding:10px;\n"
" }\n"
"")
        self.btn_add_information_inventory_mob.setIcon(icon10)
        self.btn_add_information_inventory_mob.setObjectName("btn_add_information_inventory_mob")
        self.btn_save_report = QtWidgets.QPushButton(self.tab_imobe_inventory)
        self.btn_save_report.setGeometry(QtCore.QRect(10, 390, 491, 41))
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
        self.cbx_consumables = QtWidgets.QComboBox(self.tab_imobe_inventory)
        self.cbx_consumables.setGeometry(QtCore.QRect(10, 60, 491, 41))
        self.cbx_consumables.setStyleSheet("""
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
        self.cbx_consumables.setPlaceholderText("")
        self.cbx_consumables.setObjectName("cbx_consumables")

        


        self.lbl_opening_stock.raise_()
        self.lbl_daily_used.raise_()
        self.lbl_material_ppe.raise_()
        self.lbl_consumambles.raise_()
        self.txt_daily_used_consumables.raise_()
        self.cbx_ppe.raise_()
        self.txt_daily_used_consumable.raise_()
        self.btn_add_information_inventory_mob.raise_()
        self.btn_save_report.raise_()
        self.cbx_consumables.raise_()
        self.tab_menus_wbco.addTab(self.tab_imobe_inventory, "")
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
        self.btn_compliance.setText(_translate("MainWindow", " A. M. Compliance"))
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
        self.lbl_user_logado.setText(_translate("MainWindow", "Victor Manuel"))
        self.lbl_form_tittle.setText(_translate("MainWindow", "Tank Cleaning - Add new Report"))
        self.lbl_form_text.setText(_translate("MainWindow", "Below are the fields to be filled in to generate a new report"))
        self.btn_list_report.setText(_translate("MainWindow", "List all report"))
        self.btn_list_report.clicked.connect(lambda:call_form_tank_cleaning_list())


        self.lbl_customer.setText(_translate("MainWindow", "Customer"))
        self.lbl_well_number.setText(_translate("MainWindow", "Well Number"))
        self.lbl_job_ref.setText(_translate("MainWindow", "Job Ref. Number"))
        self.lbl_rig_name.setText(_translate("MainWindow", "Rig Name"))
        self.lbl_field_location.setText(_translate("MainWindow", "Field/Location"))
        self.lbl_job_type.setText(_translate("MainWindow", "Job Type"))
        self.lbl_contacto_7.setText(_translate("MainWindow", "Report Date"))
        self.lbl_approved_by.setText(_translate("MainWindow", "Approved By"))
        self.lbl_description.setText(_translate("MainWindow", "Project Description"))

        self.btn_next_step_tank_information.setText(_translate("MainWindow", "Next Step"))
        self.btn_next_step_tank_information.clicked.connect(lambda:validator_report_information())
        
        self.tab_menus_wbco.setTabText(self.tab_menus_wbco.indexOf(self.tab_report_information), _translate("MainWindow", "Report Information"))
        
        self.btn_next_step_dayshift_activities.setText(_translate("MainWindow", "Next Step"))
        self.btn_next_step_dayshift_activities.clicked.connect(lambda:validator_dayshift_activity())

        self.lbl_type_hse_2.setText(_translate("MainWindow", "Number of Tank"))
        self.lbl_quantity_hse_2.setText(_translate("MainWindow", "Type of Waste"))
        self.lbl_volume_waste.setText(_translate("MainWindow", "Volume of Waste"))
        self.tab_menus_wbco.setTabText(self.tab_menus_wbco.indexOf(self.tab_tank), _translate("MainWindow", "Tank Information"))
        self.lbl_daily_progress.setText(_translate("MainWindow", "Daily Progress"))
        
        self.btn_next_step_dayshift_per_person.setText(_translate("MainWindow", "Next Step"))
        self.btn_next_step_dayshift_per_person.clicked.connect(lambda:validator_dayshift_per_person())

        self.txt_area_daily_progress.setPlaceholderText(_translate("MainWindow", " Write here..."))
        self.lbl_planned_activities.setText(_translate("MainWindow", "Planned Activites (Next 24hrs)"))
        self.txt_area_planed_activities.setPlaceholderText(_translate("MainWindow", " Write here..."))
        self.lbl_norm_reading.setText(_translate("MainWindow", "NORM Reading result and contamination control"))
        self.txt_area_norm_reading.setPlaceholderText(_translate("MainWindow", " Write here..."))
        self.lbl_equipament_material.setText(_translate("MainWindow", "Equipament Slash Material"))
        self.txt_area_equipament_material.setPlaceholderText(_translate("MainWindow", " Write here..."))
        self.tab_menus_wbco.setTabText(self.tab_menus_wbco.indexOf(self.tb_dayshift_activities), _translate("MainWindow", "Daily Shift Activities"))
        self.lbl_name_person_dayshift.setText(_translate("MainWindow", "Name"))
        self.lbl_personel_position.setText(_translate("MainWindow", "Personnel Position"))
        self.lbl_planed_dembed.setText(_translate("MainWindow", "Planned Demob"))
        self.lbl_crew_change.setText(_translate("MainWindow", "Crew Change"))

        self.cbx_personel_position.addItems(["Supervisor","Operator","Trainned"])
        self.cbx_planned_demeb.addItems(["TBC"])

        self.btn_next_step_hse.setText(_translate("MainWindow", "Next Step"))
        self.btn_next_step_hse.clicked.connect(lambda:validator_hse())
        
        self.btn_add_information_dayshift.setText(_translate("MainWindow", "Add the filled information to report"))
        self.btn_add_information_dayshift.clicked.connect(lambda:add_personel_shift_to_report())

        self.lbl_shift_dayshift.setText(_translate("MainWindow", "Shift"))
        self.tab_menus_wbco.setTabText(self.tab_menus_wbco.indexOf(self.tab_dayshift_per_person), _translate("MainWindow", "Personnel Daily Shift"))
        self.lbl_type_hse.setText(_translate("MainWindow", "Type"))
        self.lbl_comments.setText(_translate("MainWindow", "Comments"))
        self.lbl_quantity_hse.setText(_translate("MainWindow", "Quantity"))
        self.btn_add_information_hse.setText(_translate("MainWindow", "Add the filled information to report"))
        self.btn_add_information_hse.clicked.connect(lambda:add_hse_to_report())
        

        self.btn_next_step_produtive_man.setText(_translate("MainWindow", "Next Step"))
        self.btn_next_step_produtive_man.clicked.connect(lambda:validator_produtive_man_hour())

        self.tab_menus_wbco.setTabText(self.tab_menus_wbco.indexOf(self.tab_hse), _translate("MainWindow", "HSE(updated daily)"))
        self.lbl_visual_complete.setText(_translate("MainWindow", "Visual  Complete %"))
        self.lbl_original_hour.setText(_translate("MainWindow", "Original Hours Estimated"))
        self.lbl_hour_booked_date.setText(_translate("MainWindow", "Hours Worked To Date"))
        self.lbl_description_man_hour.setText(_translate("MainWindow", "Description"))
        self.lbl_Ot_Worked_today.setText(_translate("MainWindow", "O/T (Overtime Worked to day)"))
        self.lbl_hour_remaining.setText(_translate("MainWindow", "Hours Remainig"))
        self.lbl_numer_work.setText(_translate("MainWindow", "Work Order Number"))

        self.lbl_booked_today.setText(_translate("MainWindow", "Hours Worked Today"))
        self.btn_next_step_non_produtive_man.setText(_translate("MainWindow", "Next Step"))
        self.btn_next_step_non_produtive_man.clicked.connect(lambda:validator_non_produtive_man_hour())


        self.btn_add_information_productive_man.setText(_translate("MainWindow", "Add the filled information to report"))
        self.btn_add_information_productive_man.clicked.connect(lambda:add_produtive_man_to_report())
        self.tab_menus_wbco.setTabText(self.tab_menus_wbco.indexOf(self.tab_productive_man_hour), _translate("MainWindow", "Productive Man Hour "))
        
        self.btn_next_step_imob_inventy.setText(_translate("MainWindow", "Next Step"))
        self.btn_next_step_imob_inventy.clicked.connect(lambda:validator_imob_inventory())
        
        self.btn_add_information_non_productive.setText(_translate("MainWindow", "Add the filled information to report"))
        self.btn_add_information_non_productive.clicked.connect(lambda:add_non_produtive_to_report())

        self.btn_add_tank_informatiion.setText(_translate("MainWindow","Add the filled information to report"))
        self.btn_add_tank_informatiion.clicked.connect(lambda:add_tank_information())

        self.lbl_hour_non_produtive_man.setText(_translate("MainWindow", "Hours Today"))
        self.lbl_comments_non_produtive_man.setText(_translate("MainWindow", "Comments"))
        self.lbl_type_non_produtive_man.setText(_translate("MainWindow", "Type"))
        self.tab_menus_wbco.setTabText(self.tab_menus_wbco.indexOf(self.tab_non_productive_man_hour), _translate("MainWindow", "Non Prod Man Hour "))
        self.lbl_daily_used.setText(_translate("MainWindow", "Daily Used"))
        self.lbl_opening_stock.setText(_translate("MainWindow", "Opening Stock"))
        self.lbl_material_ppe.setText(_translate("MainWindow", "Material PPEs"))
        self.lbl_consumambles.setText(_translate("MainWindow", "Material Consumambles"))
        
        self.btn_add_information_inventory_mob.setText(_translate("MainWindow", "Add the filled information to report"))
        self.btn_add_information_inventory_mob.clicked.connect(lambda:add_inventory())

        self.btn_save_report.setText(_translate("MainWindow", "Save Report"))
        self.tab_menus_wbco.setTabText(self.tab_menus_wbco.indexOf(self.tab_imobe_inventory), _translate("MainWindow", "Inventory Mob"))
        self.cbx_customer.textActivated.connect(lambda: getPoco(self.cbx_customer.currentText()))

        self.cbx_ppe.currentTextChanged.connect(lambda:buscar_quantidade_stock())
        self.cbx_consumables.currentTextChanged.connect(lambda:buscar_quantidade_stock_consumiveis())

        self.btn_save_report.clicked.connect(lambda:report())

        self.tab_menus_wbco.setTabText(self.tab_menus_wbco.indexOf(self.tab_imobe_inventory), _translate("MainWindow", "Inventory Mob"))

        self.btn_compliance.clicked.connect(lambda:show_form_compliance())
        self.btn_wbco.clicked.connect(lambda:call_form_wbco())
        self.btn_logout.clicked.connect(lambda: logout())
        self.btn_customer.clicked.connect(lambda: call_form_client())
        self.btn_filtration.clicked.connect(lambda:show_add_filtration())
        self.btn_tank_cleaning.clicked.connect(lambda:show_add_tank_cleaning())
        self.btn_user_profile.clicked.connect(lambda:show_perfil_user())

        self.lbl_user_logado.setText(str(user_logado))

        id_poco = modulo_wbco.wbcoController.carregar_buscar_id_poco(self.cbx_well_number.currentText())
        id_supervisor = modulo_wbco.wbcoController.carregar_id_supervisor_by_email(self.lbl_user_logado.text())
        
        id_cliente = modulo_wbco.wbcoController.carregar_buscar_id_cliente(self.cbx_customer.currentText())

        def buscar_quantidade_stock():
            if tank_cleanning.pack_pipe.pipeController.buscar_quantidade_stoke(self.cbx_ppe.currentText()) is not None:
                quantidade = tank_cleanning.pack_pipe.pipeController.buscar_quantidade_stoke(self.cbx_ppe.currentText())
                self.txt_opening_stock_ppe.setText(str(quantidade[0]))
            else:
                message_error_validation("Error loading quantity","Quantity")

        def buscar_quantidade_stock_consumiveis():
            if tank_cleanning.pack_consumables.consumablesController.buscar_quantidade_stoke(self.cbx_consumables.currentText()) is not None:
                quantidade = tank_cleanning.pack_consumables.consumablesController.buscar_quantidade_stoke(self.cbx_consumables.currentText())
                self.txt_opening_stock.setText(str(quantidade[0]))
            else:
                message_error_validation("Error loading quantity","Quantity")
                
                 

        def show_message_sucess():
            msg_error = QMessageBox()
            msg_error.setIcon(QMessageBox.Information)
            msg_error.setText('Data has been added successfully')
            msg_error.setWindowTitle('Adding data')
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(".img/img/sucess_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg_error.setWindowIcon(icon)
            msg_error.exec_()

        def show_message_report_saved():
            msg_error = QMessageBox()
            msg_error.setIcon(QMessageBox.Information)
            msg_error.setText('Report has been saved successfully')
            msg_error.setWindowTitle('Adding Report')
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(".img/img/sucess_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg_error.setWindowIcon(icon)
            msg_error.exec_()

        def carregar_supervisor():
            self.cbx_person_dayshift.addItems(tank_cleanning.pack_employee.employeeController.listar())

        def carregar_turno():
             self.cbx_dayshift.addItems(tank_cleanning.pack_shift.shiftController.carregar_listagem_tipo_shift())

        def carregar_tipo_hse():
             self.cbx_type_hse.addItems(tank_cleanning.pack_hse.hseController.carregar_listagem_tipo_hse())

        def carregar_person_aproved():
            self.cbx_aproved_by.addItems(tank_cleanning.pack_employee.employeeController.listar())

        def carregar_listagem_tipo_non_produtive():
             self.cbx_non_produtive_man.addItems(tank_cleanning.pack_non_produtive_type.non_produtive_typeController.carregar_listagem())

        def carregar_listagem_consumiveis():
             self.cbx_consumables.addItems(tank_cleanning.pack_consumables.consumablesController.listar())
             print(tank_cleanning.pack_consumables.consumablesController.listar())

        def carregar_listagem_ppe():
             self.cbx_ppe.addItems(tank_cleanning.pack_pipe.pipeController.listar())

        

        

        carregar_supervisor()
        carregar_turno()
        carregar_tipo_hse()
        carregar_listagem_tipo_non_produtive()
        carregar_person_aproved()
        carregar_listagem_consumiveis()
        carregar_listagem_ppe()

        def getPoco(cliente):
            self.cbx_well_number.clear()
            well_number_items = modulo_wbco.wbcoController.carregar_poco(cliente)
            self.cbx_well_number.addItems(well_number_items)

        def carregar_cliente():
            self.cbx_customer.addItems(modulo_wbco.wbcoController.carregar_cliente())

        carregar_cliente()

        

        def message_error_validation(text_input_error,tittle_windows):
            msg_error = QMessageBox()
            msg_error.setIcon(QMessageBox.Critical)
            msg_error.setText(str(text_input_error))
            msg_error.setWindowTitle(str(tittle_windows))
            msg_error.exec_()

        def validator_report_information():

            countVezes = False

            caracter_especial = '1234567890!#$%&/=?*+ªº^~-"'
            only_special_character = '!#$%&/=?*+ªº^~-"'

            # Text Rig Name
            txt_job_ref = str(self.txt_job_ref.text())
            txt_rig = str(self.txt_rig_name.text())
            txt_job_type = str(self.txt_job_type.text())
            txt_field_location = str(self.txt_field_location.text())
            cbx_aproved_by = str(self.cbx_aproved_by.currentText())
            txt_project_description = str(self.txt_project_description.text())

            

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

            elif  (txt_project_description == ""):
                message_error_validation("This field does not accept special characters or is empty", "Error inserting Project Description")

            else:
                self.tab_menus_wbco.setCurrentIndex(1)

        
        def validator_dayshift_activity():


               
                self.tab_menus_wbco.setCurrentIndex(3)
                     

                

        def validator_dayshift_per_person():


                print(self.cbx_customer.currentText())
                id_cliente = modulo_wbco.wbcoController.carregar_buscar_id_cliente(self.cbx_customer.currentText())
                #Função para salvar as informações do Daily Shift Report
                tank_cleanning.pack_daily_progress.dayshift_activityModel.salvar_dayshift_activity(self.txt_project_description.text(),id_supervisor,self.txt_area_daily_progress.toPlainText(),self.txt_area_planed_activities.toPlainText(),self.txt_area_norm_reading.toPlainText(),self.txt_area_equipament_material.toPlainText())

                id_shift_activity =  tank_cleanning.pack_report.reportController.carregar_id_dayshift()
                id_empregador = tank_cleanning.pack_employee.employeeController.carregar_buscar_id_empregador_por_nome(self.cbx_aproved_by.currentText())

                print(id_empregador)

               # Função para salvar as informaçẽos do Report 
                print(id_cliente)
                tank_cleanning.pack_report.reportController.carregar_cadastro(self.txt_job_ref.text(),self.txt_field_location.text(),self.txt_job_type.text(),"Days/Nigth",self.dateEdit.text(),id_supervisor,self.txt_rig_name.text())

                id_ultimo_registo_report_header = modulo_wbco.wbcoController.buscar_id_report_header_ultimo()

                tank_cleanning.pack_report.reportController.salvar_info_report(id_supervisor,id_cliente,id_shift_activity,id_empregador,id_ultimo_registo_report_header)
                self.tab_menus_wbco.setCurrentIndex(2)

        
        def add_personel_shift_to_report():
          
          id_tipo_turno = tank_cleanning.pack_shift.shiftController.carregar_id_por_tipo_shift(self.cbx_dayshift.currentText())
          id_report = tank_cleanning.pack_report.reportController.carregar_id_report()
        
          id_empregador_tecnico = tank_cleanning.pack_employee.employeeController.carregar_buscar_id_empregador_por_nome(self.cbx_person_dayshift.currentText())

          if self.cbx_person_dayshift.currentText() == "":
                message_error_validation("This field does not accept empty value","Input Name Error")
          else:
               tank_cleanning.pack_shift.shiftController.carregar_cadastro(self.cbx_personel_position.currentText(),self.cbx_planned_demeb.currentText(),self.txt_crew_change.text(),id_tipo_turno[0],id_empregador_tecnico,id_report)
               show_message_sucess()

           


        def add_hse_to_report():
             
             id_tipo_hse = tank_cleanning.pack_hse.hseController.carregar_id_por_tipo_hse(self.cbx_type_hse.currentText())
             id_report = tank_cleanning.pack_report.reportController.carregar_id_report()

             if self.txt_quantity.text() == "":
                message_error_validation("This field does not acept empty value","Input Quantity Error")
             else:
                tank_cleanning.pack_hse.hseController.carregar_cadastro(id_tipo_hse,self.txt_quantity.text(),self.txt_comments.text(),id_report)
                show_message_sucess()

        def add_tank_information():
             id_report = tank_cleanning.pack_report.reportController.carregar_id_report()
             if(self.txt_number_tank.text() != ""):
                if(self.txt_type_west.text() != ""):
                   tank_cleanning.pack_tank_information.tank_informationController.cadastrar(self.txt_number_tank.text(),self.txt_type_west.text(),self.txt_volume_west.text(),self.txt_tank_type.text(),id_report)
                   show_message_sucess()
                   self.txt_tank_type.setText("")
                   self.txt_number_tank.setText("")
                   self.txt_type_west.setText("")
                   self.txt_volume_west.setText("")
                else:
                   message_error_validation("This field number tank is empty","Input Tank Error")
             else:
                message_error_validation("This field number tank is empty","Input Tank Error")
                
        def verificar_registo_produtive_man():
             id_report = tank_cleanning.pack_report.reportController.carregar_id_report()
             retorno_varificar_valor = tank_cleanning.pack_produtive_man.produtive_manController.verificar_registo_existente_com_report(id_report)
             self.txt_hour_booked_date.setEnabled(False)
             self.txt_hour_remaining.setEnabled(False)
             self.txt_visual_complete.setEnabled(False)
        verificar_registo_produtive_man()

        def add_produtive_man_to_report():
             
             only_special_character = '!#$%&/=?*+ªº^~-"'
             
             

             def has_special_characters(input_str, special_chars):
                for char in input_str:
                    if char in special_chars:
                        return True
                return False

             if has_special_characters(self.txt_description_man_hour.text(), only_special_character) or (self.txt_description_man_hour.text() == ""):
                message_error_validation("This field does not accept special characters or is empty", "Input Description Error")
            
             elif has_special_characters(self.txt_visual_complete_user.text(),only_special_character) or (self.txt_visual_complete_user.text() == ""):
                message_error_validation("This field does not accept special characters or is empty", "Field Location entry Error")
        
             elif has_special_characters(self.txt_booked_today.text(),only_special_character) or (self.txt_booked_today.text() == ""):
                message_error_validation("This field does not accept special characters or is empty", "Field Location entry Error")
             
             else:
                id_report = tank_cleanning.pack_report.reportController.carregar_id_report()
             
             
                val_hour_to_day = int(self.txt_booked_today.text())

                val_estimated = int(self.txt_original_hour.text())

                retorno_varificar_valor = tank_cleanning.pack_produtive_man.produtive_manController.verificar_registo_existente_com_report(id_report)
                valor_to_date = retorno_varificar_valor

                valor_to_date = int(valor_to_date)

                valor_to_date += int(val_hour_to_day)

                hour_remainig = val_estimated - valor_to_date
                if retorno_varificar_valor != -1:
                  self.txt_original_hour.setEnabled(False)

                  #tank_cleanning.pack_produtive_man.produtive_manController.carregar_cadastro(self.txt_numbrt_work.text(),self.txt_description_man_hour.text(),self.txt_original_hour.text(),self.txt_booked_today.text(),self.txt_qt_booked_today.text(),valor_to_date,hour_remainig,self.txt_visual_complete.text(),id_report)
                else:
             
                    visual_complete = (100 * valor_to_date)/val_estimated
                    visual_complete_user = int(self.txt_visual_complete_user.text())

                    if visual_complete_user < visual_complete:
                            self.lbl_visual_complete.setStyleSheet("color: red;")
                    elif visual_complete_user > visual_complete:
                        self.lbl_visual_complete.setStyleSheet("color: green;")
                    else:
                            self.lbl_visual_complete.setStyleSheet("color: blue;")
                    print(f"{visual_complete} %")
                    
                    self.txt_hour_booked_date.setText(str(valor_to_date))

                    
                    self.txt_hour_remaining.setText(str(hour_remainig))

                    self.txt_visual_complete.setText(str(visual_complete))
                        
                    tank_cleanning.pack_produtive_man.produtive_manController.carregar_cadastro(self.txt_numbrt_work.text(),self.txt_description_man_hour.text(),self.txt_original_hour.text(),self.txt_booked_today.text(),self.txt_qt_booked_today.text(),val_hour_to_day,self.txt_hour_remaining.text(),self.txt_visual_complete.text(),id_report)

                show_message_sucess()

        def add_non_produtive_to_report():
             
             id_report = tank_cleanning.pack_report.reportController.carregar_id_report()   
             id_tipo_non_produtive_man = tank_cleanning.pack_non_produtive_type.non_produtive_typeController.carregar_id_por_tipo_non_produtive(self.cbx_non_produtive_man.currentText())
             
             tank_cleanning.pack_non_produtive_man.non_produtive_manController.carregar_cadastro(id_tipo_non_produtive_man,self.txt_hour_non_produtive_man.text(),self.txt_comments_non_produtive_man.text(),id_report)
             show_message_sucess()

        def add_inventory():
              
              id_report = tank_cleanning.pack_report.reportController.carregar_id_report() 
              id_ppe = tank_cleanning.pack_inventory_imob.inventory_imobController.get_id_ppe(self.cbx_ppe.currentText())
              id_consumable = tank_cleanning.pack_inventory_imob.inventory_imobController.get_id_consumibele(self.cbx_consumables.currentText())
              
              stoq_consumivel = tank_cleanning.pack_inventory_imob.inventory_imobController.get_stoq_consumivel(id_consumable)
              stoq_consumivel = int(stoq_consumivel)
              stoq_ppe = tank_cleanning.pack_inventory_imob.inventory_imobController.get_stoq_ppe(id_ppe)
              stoq_ppe = int(stoq_ppe)
              
              only_special_character = '!#$%&/=?*+ªº^~-"abcdefghijklmnopqrstuvwyxz'

              def has_special_characters(input_str, special_chars):
                for char in input_str:
                    if char in special_chars:
                        return True
                return False

              if has_special_characters(self.txt_daily_used_consumable.text(), only_special_character):
                 message_error_validation("This field does not accept special characters ", "Input Quantity Consumable Error")
            
              elif has_special_characters(self.txt_daily_used_consumables.text(),only_special_character):
                 message_error_validation("This field does not accept special characters", "Input Quantity PPE Error")
        
              else:
                   ############################ Validação Dos Consumiveis ###########################################
                   if self.txt_daily_used_consumables.text() != "":
                        print("entrou")
                        quantidade_consumivel = int(self.txt_daily_used_consumables.text())
                        stock_adicional_consumivel = int(self.txt_aditin_stock_consumivel.text())
                        open_stock_consumivel = int(self.txt_opening_stock.text())
                        
                        

                        if stoq_consumivel >= quantidade_consumivel:
                                
                                total_stock = open_stock_consumivel + stock_adicional_consumivel
                        
                                closing_bal = total_stock - quantidade_consumivel

                                retorno_cadastro = tank_cleanning.pack_inventory_imob.inventory_imobController.cadastrar_consumivel(id_consumable,id_report,quantidade_consumivel,open_stock_consumivel,stock_adicional_consumivel,total_stock,closing_bal)
                                quantidade_consumivel = stoq_consumivel - quantidade_consumivel
                                retorno_update_stoque = tank_cleanning.pack_inventory_imob.inventory_imobController.update_stoque_consumiveis(id_consumable,closing_bal)
                                
                                if retorno_cadastro == 0 and retorno_update_stoque == 0:
                                     self.txt_daily_used_consumables.setText("")
                                     self.txt_aditin_stock_consumivel.setText("0")
                                     show_message_sucess()
                                     buscar_quantidade_stock_consumiveis()
                                else:
                                     message_error_validation("Erro na inserção dos dados", "Input Quantity Error")
                                     self.txt_daily_used_consumables.setText("")
                        else:
                             message_error_validation("Quantidade Introduzida é menor que a quantidade em stoque", "Input Quantity Error")
                             self.txt_daily_used_consumables.setText("")
                   
                   ########################### Validação dos PPE ###########################################################
                   if self.txt_daily_used_ppe.text() != "":

                        quantidade_ppe = int(self.txt_daily_used_ppe.text())
                        stock_adicional = int(self.txt_aditin_stock.text())
                        open_stock = int(self.txt_opening_stock_ppe.text())


                        total_stock = open_stock + stock_adicional
                        
                        closing_bal = total_stock - quantidade_ppe

                        if stoq_ppe >= quantidade_ppe:
                                
                                retorno_cadastro = tank_cleanning.pack_inventory_imob.inventory_imobController.cadastrar_ppe(id_ppe,id_report,quantidade_ppe,open_stock,stock_adicional,total_stock,closing_bal)
                                quantidade_ppe = stoq_ppe - quantidade_ppe
                                retorno_update_stoque = tank_cleanning.pack_inventory_imob.inventory_imobController.update_stoque_ppe(id_ppe,closing_bal)
                                
                                if retorno_cadastro == 0 and retorno_update_stoque == 0:
                                    self.txt_daily_used_ppe.setText("")
                                    self.txt_aditin_stock.setText("0")
                                    show_message_sucess()
                                    buscar_quantidade_stock()
                                else:
                                    message_error_validation("Erro na inserção dos dados", "Input Quantity Error")
                                    self.txt_daily_used_ppe.setText("")
                        else:
                            message_error_validation("Quantidade Introduzida é menor que a quantidade em stoque", "Input Quantity Error")
                            self.txt_daily_used_ppe.setText("")


        def validator_hse():

                self.tab_menus_wbco.setCurrentIndex(4)

        def validator_produtive_man_hour():

                self.tab_menus_wbco.setCurrentIndex(5)

        def validator_non_produtive_man_hour():

                self.tab_menus_wbco.setCurrentIndex(6)

        def validator_imob_inventory():

                self.tab_menus_wbco.setCurrentIndex(7)

        def report():
            show_message_sucess()



        def call_form_tank_cleaning_list():
            self.window = QtWidgets.QMainWindow()

            self.ui = tank_cleanning.tank_cleaning_view.Ui_MainWindow()
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

        def call_form_client():
            self.window = QtWidgets.QMainWindow()
            import modulo_customer.customer
            self.ui = modulo_customer.customer.Ui_MainWindow()
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
