import sys
sys.path.append("..")

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget,QMessageBox
import modulo_wbco.wbcoController
import compliance.pacote_report_information.report_informationController as controller
from compliance.pack_mud_type import mud_typeController as controller_mud
from compliance.pack_fluid_proprieties import fluiid_properties_Controller as controller_fluid
from compliance.pack_sample_location import sample_locationController as controller_sample_location
from compliance.pack_model_average import average_modelController as controller_model_average
from compliance.fluid_information import fluid_informationController as controller_fluid_information
from compliance.pack_drilling_fluid_property import drilling_fluid_propertyController as controller_drilling_fluid
from compliance.pack_solids_control import solidsController as solid_controller
from compliance.pack_audit import auditController as audit_controller
from compliance.pack_compliance_enginer import enginierController as enginer_controller


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

        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_aside_menu = QtWidgets.QFrame(self.centralwidget)
        self.frame_aside_menu.setGeometry(QtCore.QRect(0, -10, 251, 861))
        self.frame_aside_menu.setStyleSheet("\n"
"background-color:#2f6d58")
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
        self.btn_customer.setStyleSheet("\n""\n""QPushButton#btn_customer{\n""\n""border:none;\n""color:white;\n""font-size:18px;\n""border-radius: 12px;\n""transition: background-color 0.5s ease;\n""padding:10px;\n""text-align:left;\n""}\n""\n""QPushButton#btn_customer:hover{\n"" background-color: #044e42;\n""border-radius: 12px;\n""transition: background-color 0.5s ease;\n""padding:10px;\n""}\n""\n""QPushButton#btn_customer:pressed {\n"" background-color: #044e42;\n""border-radius: 12px;\n""background-color: #033029;\n""padding:10px;\n"" }\n""\n""\n""")
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
        self.lbl_form_tittle.setGeometry(QtCore.QRect(40, 50, 490, 31))
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
        self.btn_list_report.setGeometry(QtCore.QRect(900, 240, 191, 32))
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
        "padding:4px;\n"
        "text-align:rigth;\n"
        "}\n"
        "\n"
        "QPushButton#btn_list_report:hover{\n"
        " background-color: #044e42;\n"
        "border-radius: 6px;\n"
        "transition: background-color 0.5s ease;\n"
        "padding:4px;\n"
        "}\n"
        "\n"
        "QPushButton#btn_list_report:pressed {\n"
        " background-color: #044e42;\n"
        "border-radius: 6px;\n"
        "background-color: #033029;\n"
        "padding:4px;\n"
        " }\n"
        "")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("img/img/file-lines-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_list_report.setIcon(icon9)
        self.btn_list_report.setObjectName("btn_list_report")

        #-------------------- Botão para listar os Drilling Fluid Proprietes -----------------#

        self.btn_list_dril_flui_prop = QtWidgets.QPushButton(self.frame)
        self.btn_list_dril_flui_prop.setGeometry(QtCore.QRect(700, 240, 191, 32))
        self.btn_list_dril_flui_prop.setStyleSheet("\n"
        "\n"
        "QPushButton#btn_list_dril_flui_prop{\n"
        "\n"
        "border:none;\n"
        "background-color:#044e42;\n"
        "color:white;\n"
        "font-size:14px;\n"
        "border-radius: 6px;\n"
        "transition: background-color 0.5s ease;\n"
        "padding:4px;\n"
        "text-align:rigth;\n"
        "}\n"
        "\n"
        "QPushButton#btn_list_dril_flui_prop:hover{\n"
        " background-color: #044e42;\n"
        "border-radius: 6px;\n"
        "transition: background-color 0.5s ease;\n"
        "padding:4px;\n"
        "}\n"
        "\n"
        "QPushButton#btn_list_dril_flui_prop:pressed {\n"
        " background-color: #044e42;\n"
        "border-radius: 6px;\n"
        "background-color: #033029;\n"
        "padding:4px;\n"
        " }\n"
        "")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("img/img/file-lines-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_list_dril_flui_prop.setIcon(icon9)
        self.btn_list_dril_flui_prop.setObjectName("btn_list_dril_flui_prop")
        self.btn_list_dril_flui_prop.setText("List fluid properties")



        # -------------------- Botão Drilling fluid proprietes Fin ----------------------------#
        self.tab_menus_compliance = QtWidgets.QTabWidget(self.frame)
        self.tab_menus_compliance.setGeometry(QtCore.QRect(20, 310, 1081, 501))
        font = QtGui.QFont("Corbel")
        font.setPointSize(9)
        self.tab_menus_compliance.setFont(font)
        self.tab_menus_compliance.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tab_menus_compliance.setStyleSheet("""
                 QTabWidget::pane {
        
                 }
                 QTabWidget::tab-bar {
                   
                 }
                 QTabBar::tab {
                     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                 stop: 0 #044e42, stop: 0.4 #044e42,
                                                 stop: 0.5 #044e42, stop: 1.0 #044e42);
                     border: 6px solid #eff2f9;
                     padding: 8px;
                     color:white;
                     border-top-left-radius:8px;
                     border-top-right-radius:8px;
                 }
                 QTabBar::tab:selected, QTabBar::tab:hover {
                     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                 stop: 0 #033029, stop: 0.4 #033029,
                                                 stop: 0.5 #033029, stop: 1.0 #033029);
                 }
                                                
                     QTabBar::scroller {
                        width: 30px;
                        background-color: #f0f0f0; 
                        border: 1px solid #ccc; 
                        border-radius: 5px;
            }
            QTabBar::right-arrow:enabled {
                image: url(">");
            }
            QTabBar::right-arrow:disabled {
                image: url(">");
                width: 0;
            }
            QTabBar::left-arrow:enabled {
                image: url("<");
            }
            QTabBar::left-arrow:disabled {
                image: url("<");
                width: 0;
            }""")
        self.tab_menus_compliance.setTabPosition(QtWidgets.QTabWidget.North)
        self.tab_menus_compliance.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tab_menus_compliance.setUsesScrollButtons(True)
        self.tab_menus_compliance.setDocumentMode(False)
        self.tab_menus_compliance.setTabsClosable(False)
        self.tab_menus_compliance.setMovable(False)
        self.tab_menus_compliance.setTabBarAutoHide(False)
        self.tab_menus_compliance.setObjectName("tab_menus_compliance")
        self.tab_report_information = QtWidgets.QWidget()
        self.tab_report_information.setObjectName("tab_report_information")
        self.lbl_customer = QtWidgets.QLabel(self.tab_report_information)
        self.lbl_customer.setGeometry(QtCore.QRect(10, 20, 81, 31))
        font = QtGui.QFont("Corbel")
        font.setPointSize(11)
        self.lbl_customer.setFont(font)
        self.lbl_customer.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_customer.setObjectName("lbl_customer")
        self.cbx_customer = QtWidgets.QComboBox(self.tab_report_information)
        self.cbx_customer.setGeometry(QtCore.QRect(10, 50, 491, 41))
        
        self.cbx_customer.setObjectName("cbx_customer")
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
        
        self.lbl_well_number = QtWidgets.QLabel(self.tab_report_information)
        self.lbl_well_number.setGeometry(QtCore.QRect(10, 110, 111, 31))
        font = QtGui.QFont("Corbel")
        font.setPointSize(11)
        self.lbl_well_number.setFont(font)
        self.lbl_well_number.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_well_number.setObjectName("lbl_well_number")
        self.cbx_well_number = QtWidgets.QComboBox(self.tab_report_information)
        self.cbx_well_number.setGeometry(QtCore.QRect(10, 140, 491, 41))
        
        self.cbx_well_number.setObjectName("cbx_well_number")
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
        self.lbl_job_ref = QtWidgets.QLabel(self.tab_report_information)
        self.lbl_job_ref.setGeometry(QtCore.QRect(530, 20, 141, 31))
        font = QtGui.QFont("Corbel")
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
        font = QtGui.QFont("Corbel")
        font.setPointSize(11)
        self.lbl_rig_name.setFont(font)
        self.lbl_rig_name.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_rig_name.setObjectName("lbl_rig_name")
        self.lbl_field_location = QtWidgets.QLabel(self.tab_report_information)
        self.lbl_field_location.setGeometry(QtCore.QRect(530, 200, 141, 31))
        font = QtGui.QFont("Corbel")
        font.setPointSize(11)
        self.lbl_field_location.setFont(font)
        self.lbl_field_location.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_field_location.setObjectName("lbl_field_location")
        self.lbl_job_type = QtWidgets.QLabel(self.tab_report_information)
        self.lbl_job_type.setGeometry(QtCore.QRect(530, 290, 91, 31))
        font = QtGui.QFont("Corbel")
        font.setPointSize(11)
        self.lbl_job_type.setFont(font)
        self.lbl_job_type.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_job_type.setObjectName("lbl_job_type")
        self.lbl_contacto_7 = QtWidgets.QLabel(self.tab_report_information)
        self.lbl_contacto_7.setGeometry(QtCore.QRect(10, 190, 101, 31))
        font = QtGui.QFont("Corbel")
        font.setPointSize(11)
        self.lbl_contacto_7.setFont(font)
        self.lbl_contacto_7.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_contacto_7.setObjectName("lbl_contacto_7")
        self.lbl_approved_by = QtWidgets.QLabel(self.tab_report_information)
        self.lbl_approved_by.setGeometry(QtCore.QRect(10, 280, 101, 31))
        font = QtGui.QFont("Corbel")
        font.setPointSize(11)
        self.lbl_approved_by.setFont(font)
        self.lbl_approved_by.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_approved_by.setObjectName("lbl_approved_by")
        self.data_report = QtWidgets.QDateEdit(self.tab_report_information)
        self.data_report.setGeometry(QtCore.QRect(10, 220, 491, 41))
        self.data_report.setStyleSheet("QDateEdit{\n"
        "\n"
        "background-color:#fff;\n"
        "border: 1px solid #8ec0af;\n"
        "border-radius: 6px\n"
        "\n"
        "}")
        self.data_report.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.data_report.setAccelerated(False)
        self.data_report.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.data_report.setProperty("showGroupSeparator", False)
        self.data_report.setObjectName("data_report")
        self.lbl_description = QtWidgets.QLabel(self.tab_report_information)
        self.lbl_description.setGeometry(QtCore.QRect(530, 370, 331, 31))
        font = QtGui.QFont("Corbel")
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
        self.data_report.raise_()
        self.btn_next_step_tank_information.raise_()
        self.tab_menus_compliance.addTab(self.tab_report_information, "")
        self.tab_fluid_information = QtWidgets.QWidget()
        self.tab_fluid_information.setObjectName("tab_fluid_information")
        self.btn_next_step_driliing_properties = QtWidgets.QPushButton(self.tab_fluid_information)
        self.btn_next_step_driliing_properties.setGeometry(QtCore.QRect(10, 300, 351, 41))
        self.btn_next_step_driliing_properties.setStyleSheet("\n"
        "\n"
        "QPushButton#btn_next_step_driliing_properties{\n"
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
        "QPushButton#btn_next_step_driliing_properties:hover{\n"
        " background-color: #044e42;\n"
        "border-radius: 6px;\n"
        "transition: background-color 0.5s ease;\n"
        "padding:10px;\n"
        "}\n"
        "\n"
        "QPushButton#btn_next_step_driliing_properties:pressed {\n"
        " background-color: #044e42;\n"
        "border-radius: 6px;\n"
        "background-color: #033029;\n"
        "padding:10px;\n"
        " }\n"
        "")
        self.btn_next_step_driliing_properties.setIcon(icon10)
        self.btn_next_step_driliing_properties.setObjectName("btn_next_step_driliing_properties")

        
        self.lbl_mud_type = QtWidgets.QLabel(self.tab_fluid_information)
        self.lbl_mud_type.setGeometry(QtCore.QRect(10, 10, 191, 31))
        font = QtGui.QFont("Corbel")
        font.setPointSize(11)
        self.lbl_mud_type.setFont(font)
        self.lbl_mud_type.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_mud_type.setObjectName("lbl_mud_type")
        self.lbl_rig_total_volume_type = QtWidgets.QLabel(self.tab_fluid_information)
        self.lbl_rig_total_volume_type.setGeometry(QtCore.QRect(370, 10, 191, 31))
        font = QtGui.QFont("Corbel")
        font.setPointSize(11)
        self.lbl_rig_total_volume_type.setFont(font)
        self.lbl_rig_total_volume_type.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_rig_total_volume_type.setObjectName("lbl_rig_total_volume_type")
        self.lbl_rig_volume = QtWidgets.QLabel(self.tab_fluid_information)
        self.lbl_rig_volume.setGeometry(QtCore.QRect(732, 10, 140, 31))
        font = QtGui.QFont("Corbel")
        font.setPointSize(11)
        self.lbl_rig_volume.setFont(font)
        self.lbl_rig_volume.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_rig_volume.setObjectName("lbl_rig_volume")

        

        self.cbx_mud_type = QtWidgets.QComboBox(self.tab_fluid_information)
        self.cbx_mud_type.setGeometry(QtCore.QRect(10, 40, 351, 41))
        
        self.cbx_mud_type.setPlaceholderText("")
        self.cbx_mud_type.setObjectName("cbx_mud_type")
        self.cbx_mud_type.setStyleSheet("""
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


        self.cbx_rig_volume_type = QtWidgets.QComboBox(self.tab_fluid_information)
        self.cbx_rig_volume_type.setGeometry(QtCore.QRect(370, 40, 351, 41))
        self.cbx_rig_volume_type.addItems(["bbls","m3"])
        self.cbx_rig_volume_type.setPlaceholderText("")
        self.cbx_rig_volume_type.setObjectName("cbx_rig_volume_type")
        self.cbx_rig_volume_type.setStyleSheet("""
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

        self.txt_rig_volume = QtWidgets.QLineEdit(self.tab_fluid_information)
        self.txt_rig_volume.setGeometry(QtCore.QRect(730, 40, 351, 41))
        self.txt_rig_volume.setStyleSheet("""
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
        
        #------------------------ Second Line --------------------------------__#

        self.lbl_density_type = QtWidgets.QLabel(self.tab_fluid_information)
        self.lbl_density_type.setGeometry(QtCore.QRect(10, 100, 191, 31))
        font = QtGui.QFont("Corbel")
        font.setPointSize(11)
        self.lbl_density_type.setFont(font)
        self.lbl_density_type.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_density_type.setObjectName("lbl_density_type")
        self.lbl_density_type.setText("Density (Unit)")

        self.cbx_density_type = QtWidgets.QComboBox(self.tab_fluid_information)
        self.cbx_density_type.setGeometry(QtCore.QRect(10, 132, 351, 41))
        self.cbx_density_type.setObjectName("cbx_density_type")
        self.cbx_density_type.addItems(["PPG","SG"])
        self.cbx_density_type.setStyleSheet("""
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

        self.lbl_density = QtWidgets.QLabel(self.tab_fluid_information)
        self.lbl_density.setGeometry(QtCore.QRect(370, 100, 191, 31))
        font = QtGui.QFont("Corbel")
        font.setPointSize(11)
        self.lbl_density.setFont(font)
        self.lbl_density.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_density.setObjectName("lbl_density")
        self.lbl_density.setText("Density")

        self.txt_density = QtWidgets.QLineEdit(self.tab_fluid_information)
        self.txt_density.setGeometry(QtCore.QRect(370, 132, 351, 41))
        self.txt_density.setObjectName("txt_density")
        self.txt_density.setStyleSheet("""
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

        self.txt_viscosity_pv = QtWidgets.QLineEdit(self.tab_fluid_information)
        self.txt_viscosity_pv.setGeometry(QtCore.QRect(732, 132, 349, 41))
        self.txt_viscosity_pv.setObjectName("txt_density")
        self.txt_viscosity_pv.setStyleSheet("""
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

        self.lbl_viscosity_pv = QtWidgets.QLabel(self.tab_fluid_information)
        self.lbl_viscosity_pv.setGeometry(QtCore.QRect(732, 100, 140, 31))
        font = QtGui.QFont("Corbel")
        font.setPointSize(11)
        self.lbl_viscosity_pv.setFont(font)
        self.lbl_viscosity_pv.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_viscosity_pv.setObjectName("lbl_viscosity_pv")
        self.lbl_viscosity_pv.setText("Viscosity (PV)")
        




        #---------------- Second Line finish -----------------------------------#




        # --------------------- Terceira Lina -----------------------------------#

        self.lbl_viscosity_yp = QtWidgets.QLabel(self.tab_fluid_information)
        self.lbl_viscosity_yp.setGeometry(QtCore.QRect(10, 185, 191, 31))
        font = QtGui.QFont("Corbel")
        font.setPointSize(11)
        self.lbl_viscosity_yp.setFont(font)
        self.lbl_viscosity_yp.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_viscosity_yp.setObjectName("lbl_viscosity_yp")
        self.lbl_viscosity_yp.setText("Viscosity (YP)")

        self.txt_viscosity_yp = QtWidgets.QLineEdit(self.tab_fluid_information)
        self.txt_viscosity_yp.setGeometry(QtCore.QRect(10, 220, 351, 41))
        self.txt_viscosity_yp.setObjectName("cbx_density_type")
        self.txt_viscosity_yp.setStyleSheet("""
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

        self.lbl_hole_volume_type = QtWidgets.QLabel(self.tab_fluid_information)
        self.lbl_hole_volume_type.setGeometry(QtCore.QRect(370, 185, 191, 31))
        font = QtGui.QFont("Corbel")
        font.setPointSize(11)
        self.lbl_hole_volume_type.setFont(font)
        self.lbl_hole_volume_type.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_hole_volume_type.setObjectName("lbl_hole_volume_type")
        self.lbl_hole_volume_type.setText("Hole Volume (Unit)")

        self.cbx_hole_volume_type = QtWidgets.QComboBox(self.tab_fluid_information)
        self.cbx_hole_volume_type.setGeometry(QtCore.QRect(370, 220, 351, 41))
        self.cbx_hole_volume_type.setObjectName("cbx_hole_volume_type")
        self.cbx_hole_volume_type.addItems(["bbls","m3"])
        self.cbx_hole_volume_type.setStyleSheet("""
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
        self.cbx_hole_volume_type.setStyleSheet("""
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

        self.txt_hole_volume = QtWidgets.QLineEdit(self.tab_fluid_information)
        self.txt_hole_volume.setGeometry(QtCore.QRect(732, 220, 349, 41))
        self.txt_hole_volume.setObjectName("txt_hole_volume")
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

        self.lbl_hole_volume = QtWidgets.QLabel(self.tab_fluid_information)
        self.lbl_hole_volume.setGeometry(QtCore.QRect(732, 185, 140, 31))
        font = QtGui.QFont("Corbel")
        font.setPointSize(11)
        self.lbl_hole_volume.setFont(font)
        self.lbl_hole_volume.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_hole_volume.setObjectName("lbl_hole_volume")
        self.lbl_hole_volume.setText("Hole Volume ")



        #---------------- Fin da Terceira Linha ------------------------------------#

        self.txt_rig_volume.setPlaceholderText("")
        self.txt_rig_volume.setObjectName("txt_rig_volume")
        self.lbl_rig_volume.raise_()
        self.lbl_rig_total_volume_type.raise_()
        self.lbl_mud_type.raise_()
        self.btn_next_step_driliing_properties.raise_()
        self.cbx_mud_type.raise_()
        self.cbx_rig_volume_type.raise_()
        self.txt_rig_volume.raise_()
        
        self.tb_driling_information = QtWidgets.QWidget()
        self.tb_driling_information.setObjectName("tb_driling_information")
        self.lbl_hole_size = QtWidgets.QLabel(self.tb_driling_information)
        self.lbl_hole_size.setGeometry(QtCore.QRect(10, 10, 101, 31))
        font = QtGui.QFont("Corbel")
        font.setPointSize(11)
        self.lbl_hole_size.setFont(font)
        self.lbl_hole_size.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_hole_size.setObjectName("lbl_hole_size")
        self.btn_next_step_drilling_information = QtWidgets.QPushButton(self.tb_driling_information)
        self.btn_next_step_drilling_information.setGeometry(QtCore.QRect(530, 240, 491, 41))
        self.btn_next_step_drilling_information.setStyleSheet("\n"
        "\n"
        "QPushButton#btn_next_step_drilling_information{\n"
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
        "QPushButton#btn_next_step_drilling_information:hover{\n"
        " background-color: #044e42;\n"
        "border-radius: 6px;\n"
        "transition: background-color 0.5s ease;\n"
        "padding:10px;\n"
        "}\n"
        "\n"
        "QPushButton#btn_next_step_drilling_information:pressed {\n"
        " background-color: #044e42;\n"
        "border-radius: 6px;\n"
        "background-color: #033029;\n"
        "padding:10px;\n"
        " }\n"
        "")
        self.btn_next_step_drilling_information.setIcon(icon10)
        self.btn_next_step_drilling_information.setObjectName("btn_next_step_drilling_information")
        self.txt_hole_size = QtWidgets.QLineEdit(self.tb_driling_information)
        self.txt_hole_size.setGeometry(QtCore.QRect(10, 40, 491, 41))
        self.txt_hole_size.setStyleSheet("background-color:#fff;\n"
        "border: 1px solid #8ec0af;\n"
        "border-radius: 6px")
        self.txt_hole_size.setObjectName("txt_hole_size")
        self.lbl_total_depth = QtWidgets.QLabel(self.tb_driling_information)
        self.lbl_total_depth.setGeometry(QtCore.QRect(530, 10, 211, 31))
        font = QtGui.QFont("Corbel")
        font.setPointSize(11)
        self.lbl_total_depth.setFont(font)
        self.lbl_total_depth.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_total_depth.setObjectName("lbl_total_depth")
        self.txt_total_depth = QtWidgets.QLineEdit(self.tb_driling_information)
        self.txt_total_depth.setGeometry(QtCore.QRect(530, 40, 491, 41))
        self.txt_total_depth.setStyleSheet("background-color:#fff;\n"
        "border: 1px solid #8ec0af;\n"
        "border-radius: 6px")
        self.txt_total_depth.setObjectName("txt_total_depth")
        self.lbl_feets_drilled = QtWidgets.QLabel(self.tb_driling_information)
        self.lbl_feets_drilled.setGeometry(QtCore.QRect(10, 110, 331, 31))
        font = QtGui.QFont("Corbel")
        font.setPointSize(11)
        self.lbl_feets_drilled.setFont(font)
        self.lbl_feets_drilled.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_feets_drilled.setObjectName("lbl_feets_drilled")
        self.txt_feets_drilled = QtWidgets.QLineEdit(self.tb_driling_information)
        self.txt_feets_drilled.setGeometry(QtCore.QRect(10, 140, 491, 41))
        self.txt_feets_drilled.setStyleSheet("background-color:#fff;\n"
        "border: 1px solid #8ec0af;\n"
        "border-radius: 6px")
        self.txt_feets_drilled.setObjectName("txt_feets_drilled")
        self.lbl_average_rop = QtWidgets.QLabel(self.tb_driling_information)
        self.lbl_average_rop.setGeometry(QtCore.QRect(530, 110, 141, 31))
        font = QtGui.QFont("Corbel")
        font.setPointSize(11)
        self.lbl_average_rop.setFont(font)
        self.lbl_average_rop.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_average_rop.setObjectName("lbl_average_rop")
        self.txt_average_rop = QtWidgets.QLineEdit(self.tb_driling_information)
        self.txt_average_rop.setGeometry(QtCore.QRect(530, 140, 491, 42))
        self.txt_average_rop.setStyleSheet("background-color:#fff;\n"
        "border: 1px solid #8ec0af;\n"
        "border-radius: 6px")
        self.txt_average_rop.setObjectName("txt_average_rop")


        self.lbl_data_edit = QtWidgets.QLabel(self.tb_driling_information)
        self.lbl_data_edit.setGeometry(QtCore.QRect(10, 200, 141, 31))
        font = QtGui.QFont("Corbel")
        font.setPointSize(11)
        self.lbl_data_edit.setFont(font)
        self.lbl_data_edit.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_data_edit.setObjectName("lbl_data_edit")
        self.lbl_data_edit.setText("Time at Depth")

        self.data_at_depth = QtWidgets.QDateEdit(self.tb_driling_information)
        self.data_at_depth.setGeometry(QtCore.QRect(10, 240, 491, 41))
        self.data_at_depth.setStyleSheet("QDateEdit{\n"
        "\n"
        "background-color:#fff;\n"
        "border: 1px solid #8ec0af;\n"
        "border-radius: 6px\n"
        "\n"
        "}")
        self.data_at_depth.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.data_at_depth.setAccelerated(False)
        self.data_at_depth.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.data_at_depth.setProperty("showGroupSeparator", False)
        self.data_at_depth.setObjectName("data_at_depth")

        self.tab_menus_compliance.addTab(self.tb_driling_information, "")


        self.tab_ongoing_rig = QtWidgets.QWidget()
        self.tab_ongoing_rig.setObjectName("tab_ongoing_rig")
        self.tab_menus_compliance.addTab(self.tab_ongoing_rig, "")


        self.tab_audit_compliance_enginner = QtWidgets.QWidget()
        self.tab_audit_compliance_enginner.setObjectName("tab_audit_compliance_enginner")
        self.tab_menus_compliance.addTab(self.tab_audit_compliance_enginner,"")

        self.tab_menus_compliance.addTab(self.tab_fluid_information, "")
        self.tab_drilling_fluid_information = QtWidgets.QWidget()
        self.tab_drilling_fluid_information.setObjectName("tab_drilling_fluid_information")
        self.lbl_fluid_proprietes = QtWidgets.QLabel(self.tab_drilling_fluid_information)
        self.lbl_fluid_proprietes.setGeometry(QtCore.QRect(10, 20, 251, 31))
        font = QtGui.QFont("Corbel")
        font.setPointSize(11)
        self.lbl_fluid_proprietes.setFont(font)
        self.lbl_fluid_proprietes.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_fluid_proprietes.setObjectName("lbl_fluid_proprietes")
        self.lbl_value_drilling_fluid = QtWidgets.QLabel(self.tab_drilling_fluid_information)
        self.lbl_value_drilling_fluid.setGeometry(QtCore.QRect(530, 20, 150, 31))
        font = QtGui.QFont("Corbel")
        font.setPointSize(11)
        self.lbl_value_drilling_fluid.setFont(font)
        self.lbl_value_drilling_fluid.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_value_drilling_fluid.setObjectName("lbl_value_drilling_fluid")
        
        self.cbx_fluid_proprieties = QtWidgets.QComboBox(self.tab_drilling_fluid_information)
        self.cbx_fluid_proprieties.setGeometry(QtCore.QRect(10, 50, 491, 41))
        
        self.cbx_fluid_proprieties.setObjectName("cbx_fluid_proprieties")
        self.cbx_fluid_proprieties.setStyleSheet("""
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
        
        
        self.txt_value = QtWidgets.QLineEdit(self.tab_drilling_fluid_information)
        self.txt_value.setGeometry(QtCore.QRect(530, 50, 491, 41))
        self.txt_value.setStyleSheet("""
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
                
        self.txt_value.setObjectName("txt_value")
        
        self.btn_next_drilling_fluid = QtWidgets.QPushButton(self.tab_drilling_fluid_information)
        self.btn_next_drilling_fluid.setGeometry(QtCore.QRect(530, 190, 491, 41))
        self.btn_next_drilling_fluid.setStyleSheet("\n"
        "\n"
        "QPushButton#btn_next_drilling_fluid{\n"
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
        "QPushButton#btn_next_drilling_fluid:hover{\n"
        " background-color: #044e42;\n"
        "border-radius: 6px;\n"
        "transition: background-color 0.5s ease;\n"
        "padding:10px;\n"
        "}\n"
        "\n"
        "QPushButton#btn_next_drilling_fluid:pressed {\n"
        " background-color: #044e42;\n"
        "border-radius: 6px;\n"
        "background-color: #033029;\n"
        "padding:10px;\n"
        " }\n"
        "")
        self.btn_next_drilling_fluid.setIcon(icon10)
        self.btn_next_drilling_fluid.setObjectName("btn_next_drilling_fluid")
        self.btn_add_information_drilling_fluid = QtWidgets.QPushButton(self.tab_drilling_fluid_information)
        self.btn_add_information_drilling_fluid.setGeometry(QtCore.QRect(10, 190, 491, 41))
        self.btn_add_information_drilling_fluid.setStyleSheet("\n"
        "\n"
        "QPushButton#btn_add_information_drilling_fluid{\n"
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
        "QPushButton#btn_add_information_drilling_fluid:hover{\n"
        " background-color: #044e42;\n"
        "border-radius: 6px;\n"
        "transition: background-color 0.5s ease;\n"
        "padding:10px;\n"
        "}\n"
        "\n"
        "QPushButton#btn_add_information_drilling_fluid:pressed {\n"
        " background-color: #044e42;\n"
        "border-radius: 6px;\n"
        "background-color: #033029;\n"
        "padding:10px;\n"
        " }\n"
        "")
        self.btn_add_information_drilling_fluid.setIcon(icon10)
        self.btn_add_information_drilling_fluid.setObjectName("btn_add_information_drilling_fluid")
        
       
        self.lbl_fluid_proprietes.raise_()
        self.lbl_value_drilling_fluid.raise_()
        self.cbx_fluid_proprieties.raise_()
        self.txt_value.raise_()
        self.btn_next_drilling_fluid.raise_()
        self.btn_add_information_drilling_fluid.raise_()
        self.tab_menus_compliance.addTab(self.tab_drilling_fluid_information, "")
        self.tab_add_sample = QtWidgets.QWidget()
        self.tab_add_sample.setObjectName("tab_add_sample")

        #----------------------------- Primeira Lina Inicio -----------------------___#
        
        self.lbl_depth = QtWidgets.QLabel(self.tab_add_sample)
        self.lbl_depth.setGeometry(QtCore.QRect(10, 10, 250, 31))
        font = QtGui.QFont("Corbel")
        font.setPointSize(11)
        self.lbl_depth.setFont(font)
        self.lbl_depth.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_depth.setObjectName("lbl_depth")
        self.lbl_sample_number = QtWidgets.QLabel(self.tab_add_sample)
        self.lbl_sample_number.setGeometry(QtCore.QRect(748, 10, 300, 31))
        font = QtGui.QFont("Corbel")
        font.setPointSize(11)
        self.lbl_sample_number.setFont(font)
        self.lbl_sample_number.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_sample_number.setObjectName("lbl_sample_number")
        self.txt_depth_location = QtWidgets.QLineEdit(self.tab_add_sample)
        self.txt_depth_location.setGeometry(QtCore.QRect(10, 40, 351, 41))
        self.txt_depth_location.setStyleSheet("""
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
        
        self.txt_depth_location.setObjectName("txt_depth_location")
        self.cbx_sample_location_occ = QtWidgets.QComboBox(self.tab_add_sample)
        self.cbx_sample_location_occ.setGeometry(QtCore.QRect(380, 40, 351, 41))
        self.cbx_sample_location_occ.setStyleSheet("""
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
        self.cbx_sample_location_occ.setPlaceholderText("")
        self.cbx_sample_location_occ.setObjectName("cbx_sample_location_occ")
        self.lbl_sample_location = QtWidgets.QLabel(self.tab_add_sample)
        self.lbl_sample_location.setGeometry(QtCore.QRect(380, 10, 300, 31))
        font = QtGui.QFont("Corbel")
        font.setPointSize(11)
        self.lbl_sample_location.setFont(font)
        self.lbl_sample_location.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_sample_location.setObjectName("lbl_sample_location")
        self.txt_sample_number = QtWidgets.QLineEdit(self.tab_add_sample)
        self.txt_sample_number.setGeometry(QtCore.QRect(750, 40, 300, 41))
        self.txt_sample_number.setStyleSheet("""
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
        self.txt_sample_number.setPlaceholderText("")
        self.txt_sample_number.setObjectName("txt_sample_number")

        # ------------------- Fin primeira linha --------------------------------#


        #----------------------------- Segunda Linha Inicio -----------------------___#

        self.data_test = QtWidgets.QDateEdit(self.tab_add_sample)
        self.data_test.setGeometry(QtCore.QRect(10, 140, 351, 41))
        self.data_test.setStyleSheet("QDateEdit{\n"
        "\n"
        "background-color:#fff;\n"
        "border: 1px solid #8ec0af;\n"
        "border-radius: 6px\n"
        "\n"
        "}")
        self.data_test.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.data_test.setAccelerated(False)
        self.data_test.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.data_test.setProperty("showGroupSeparator", False)
        self.data_test.setObjectName("data_test")
        
        self.lbl_Data_Teste = QtWidgets.QLabel(self.tab_add_sample)
        self.lbl_Data_Teste.setGeometry(QtCore.QRect(10, 115, 250, 20))
        font = QtGui.QFont("Corbel")
        font.setPointSize(11)
        self.lbl_Data_Teste.setFont(font)
        self.lbl_Data_Teste.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_Data_Teste.setObjectName("lbl_Data_Teste")
        self. lbl_Data_Teste.setText("Data of test")

        
        self.time_test = QtWidgets.QTimeEdit(self.tab_add_sample)
        self.time_test.setGeometry(QtCore.QRect(380, 140, 351, 41))
        self.time_test.setStyleSheet("QTimeEdit{\n"
        "\n"
        "\n"
        "background-color:#fff;\n"
        "border: 1px solid #8ec0af;\n"
        "border-radius: 6px\n"
        "}")
        self.time_test.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.time_test.setAccelerated(False)
        self.time_test.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.time_test.setProperty("showGroupSeparator", False)

        self.time_test.setObjectName("time_test")
        self.lbl_data_test = QtWidgets.QLabel(self.tab_add_sample)
        self.lbl_data_test.setGeometry(QtCore.QRect(380, 115, 300, 20))
        font = QtGui.QFont("Corbel")
        font.setPointSize(11)
        self.lbl_data_test.setFont(font)
        self.lbl_data_test.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_data_test.setObjectName("lbl_data_test")
        self.lbl_data_test.setText("Time of test")



        # ------------------- Fin Segunda linha --------------------------------#

        self.btn_add_sample = QtWidgets.QPushButton(self.tab_add_sample)
        self.btn_add_sample.setGeometry(QtCore.QRect(750,230,300,41))
        self.btn_add_sample.setStyleSheet("\n"
        "\n"
        "QPushButton#btn_add_sample{\n"
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
        "QPushButton#btn_add_sample:hover{\n"
        " background-color: #044e42;\n"
        "border-radius: 6px;\n"
        "transition: background-color 0.5s ease;\n"
        "padding:10px;\n"
        "}\n"
        "\n"
        "QPushButton#btn_add_sample:pressed {\n"
        " background-color: #044e42;\n"
        "border-radius: 6px;\n"
        "background-color: #033029;\n"
        "padding:10px;\n"
        " }\n"
        "")

        self.btn_add_sample.setObjectName("btn_add_sample")

        

       

       

        self.lbl_number_of_cutting = QtWidgets.QLabel(self.tab_add_sample)
        self.lbl_number_of_cutting.setGeometry(QtCore.QRect(380,200,250,28))
        self.lbl_number_of_cutting.setText("Number of Cutting Dryer")
        self.lbl_number_of_cutting.setObjectName("lbl_number_of_cutting")

        self.txt_number_of_cutting = QtWidgets.QLineEdit(self.tab_add_sample)
        self.txt_number_of_cutting.setGeometry(QtCore.QRect(380,230,351,41))
        self.txt_number_of_cutting.setObjectName("txt_number_of_cutting")
        self.txt_number_of_cutting.setStyleSheet("""
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

        self.lbl_number_of_shakers = QtWidgets.QLabel(self.tab_add_sample)
        self.lbl_number_of_shakers.setGeometry(QtCore.QRect(10,200,250,28))
        self.lbl_number_of_shakers.setObjectName("lbl_number_of_shakers")
        self.lbl_number_of_shakers.setText("Number of Shakers Online")

        self.txt_number_of_shakers = QtWidgets.QLineEdit(self.tab_add_sample)
        self.txt_number_of_shakers.setGeometry(QtCore.QRect(10,230,351,41))
        self.txt_number_of_shakers.setObjectName("txt_number_of_shakers")
        self.txt_number_of_shakers.setStyleSheet("""
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

        self.cbx_model_average = QtWidgets.QComboBox(self.tab_add_sample)
        self.cbx_model_average.setGeometry(QtCore.QRect(748, 140, 300, 41))
        self.cbx_model_average.addItem("--- Select  Model Average ---")
        
        self.cbx_model_average.setObjectName("cbx_model_average")
        self.cbx_model_average.setStyleSheet("""
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

        

        self.btn_next_step_solid = QtWidgets.QPushButton(self.tab_add_sample)
        self.btn_next_step_solid.setGeometry(QtCore.QRect(10,310,351,41))
        self.btn_next_step_solid.setObjectName("btn_next_step_solid")
        self.btn_next_step_solid.setText("Next Step")
        self.btn_next_step_solid.setStyleSheet("\n"
        "\n"
        "QPushButton#btn_next_step_solid{\n"
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
        "QPushButton#btn_next_step_solid:hover{\n"
        " background-color: #044e42;\n"
        "border-radius: 6px;\n"
        "transition: background-color 0.5s ease;\n"
        "padding:10px;\n"
        "}\n"
        "\n"
        "QPushButton#btn_next_step_solid:pressed {\n"
        " background-color: #044e42;\n"
        "border-radius: 6px;\n"
        "background-color: #033029;\n"
        "padding:10px;\n"
        " }\n"
        "")
        

        self.lbl_sample_location.raise_()
        self.lbl_depth.raise_()
        self.lbl_sample_number.raise_()
        self.txt_depth_location.raise_()
        self.cbx_sample_location_occ.raise_()
        self.txt_sample_number.raise_()
        self.btn_add_sample.raise_()

        self.tab_menus_compliance.addTab(self.tab_add_sample, "")
        self.tab_solid_control = QtWidgets.QWidget()
        self.tab_solid_control.setObjectName("tab_solid_control")
        

        self.lbl_back = QtWidgets.QLabel(self.tab_solid_control)
        self.lbl_back.setGeometry(QtCore.QRect(10, 190, 171, 31))
        font = QtGui.QFont("Corbel")
        font.setPointSize(11)
        self.lbl_back.setFont(font)
        self.lbl_back.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_back.setObjectName("lbl_back")
        self.txt_middle = QtWidgets.QLineEdit(self.tab_solid_control)
        self.txt_middle.setGeometry(QtCore.QRect(10, 310, 491, 41))
        self.txt_middle.setStyleSheet("""
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
        self.txt_middle.setPlaceholderText("")
        self.txt_middle.setObjectName("txt_middle")
        self.txt_hour_run = QtWidgets.QLineEdit(self.tab_solid_control)
        self.txt_hour_run.setGeometry(QtCore.QRect(530, 140, 491, 41))
        self.txt_hour_run.setStyleSheet("""
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
        self.txt_hour_run.setPlaceholderText("")
        self.txt_hour_run.setObjectName("txt_hour_run")
       
        
        self.txt_front = QtWidgets.QLineEdit(self.tab_solid_control)
        self.txt_front.setGeometry(QtCore.QRect(530, 50, 491, 41))
        self.txt_front.setStyleSheet("""
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
        self.txt_front.setPlaceholderText("")
        self.txt_front.setObjectName("txt_front")
        self.lbl_description_man_hour = QtWidgets.QLabel(self.tab_solid_control)
        self.lbl_description_man_hour.setGeometry(QtCore.QRect(10, 110, 250, 31))
        font = QtGui.QFont("Corbel")
        font.setPointSize(11)
        self.lbl_description_man_hour.setFont(font)
        self.lbl_description_man_hour.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_description_man_hour.setObjectName("lbl_description_man_hour")
        self.lbl_front = QtWidgets.QLabel(self.tab_solid_control)
        self.lbl_front.setGeometry(QtCore.QRect(530, 20, 230, 31))
        font = QtGui.QFont("Corbel")
        font.setPointSize(11)
        self.lbl_front.setFont(font)
        self.lbl_front.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_front.setObjectName("lbl_front")
        self.lbl_Hours_run = QtWidgets.QLabel(self.tab_solid_control)
        self.lbl_Hours_run.setGeometry(QtCore.QRect(530, 110, 151, 31))
        font = QtGui.QFont("Corbel")
        font.setPointSize(11)
        self.lbl_Hours_run.setFont(font)
        self.lbl_Hours_run.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_Hours_run.setObjectName("lbl_Hours_run")

        self.cbx_dryer = QtWidgets.QComboBox(self.tab_solid_control)
        self.cbx_dryer.setGeometry(QtCore.QRect(530, 230, 491, 41))
        self.cbx_dryer.addItem("Select")
        self.cbx_dryer.setStyleSheet("""
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
        self.cbx_dryer.setPlaceholderText("")
        self.cbx_dryer.setObjectName("cbx_dryer")
        self.cbx_dryer.setStyleSheet("""
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

        self.cbx_solids_sample_location = QtWidgets.QComboBox(self.tab_solid_control)
        self.cbx_solids_sample_location.addItem("Select Sample Location")
        self.cbx_solids_sample_location.setGeometry(QtCore.QRect(530, 310, 250, 41))
        self.cbx_solids_sample_location.setStyleSheet("""
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
        self.cbx_solids_sample_location.setPlaceholderText("")
        self.cbx_solids_sample_location.setObjectName("cbx_solids_sample_location")


        self.lbl_Dryer_screen = QtWidgets.QLabel(self.tab_solid_control)
        self.lbl_Dryer_screen.setObjectName("lbl_Dryer_screen")
        self.lbl_Dryer_screen.setText("Dryer Screen size (mm)")
        self.lbl_Dryer_screen.setGeometry(QtCore.QRect(800,280,225,31))

        self.txt_dryer_screen_size = QtWidgets.QLineEdit(self.tab_solid_control)
        self.txt_dryer_screen_size.setGeometry(QtCore.QRect(800, 310, 225, 41))
        self.txt_dryer_screen_size.setStyleSheet("""
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
        self.txt_dryer_screen_size.setPlaceholderText("")
        self.txt_dryer_screen_size.setObjectName("txt_dryer_screen_size")

        self.lbl_shalker_api = QtWidgets.QLabel(self.tab_solid_control)
        self.lbl_shalker_api.setGeometry(QtCore.QRect(10, 20, 270, 31))
        font = QtGui.QFont("Corbel")
        font.setPointSize(11)
        self.lbl_shalker_api.setFont(font)
        self.lbl_shalker_api.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_shalker_api.setObjectName("lbl_shalker_api")
        self.lbl_middle = QtWidgets.QLabel(self.tab_solid_control)
        self.lbl_middle.setGeometry(QtCore.QRect(10, 280, 141, 31))
        font = QtGui.QFont("Corbel")
        font.setPointSize(11)
        self.lbl_middle.setFont(font)
        self.lbl_middle.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_middle.setObjectName("lbl_middle")
        self.btn_next_step_solid_control_sample = QtWidgets.QPushButton(self.tab_solid_control)
        self.btn_next_step_solid_control_sample.setGeometry(QtCore.QRect(10, 380, 491, 41))
        self.btn_next_step_solid_control_sample.setStyleSheet("\n"
        "\n"
        "QPushButton#btn_next_step_solid_control_sample{\n"
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
        "QPushButton#btn_next_step_solid_control_sample:hover{\n"
        " background-color: #044e42;\n"
        "border-radius: 6px;\n"
        "transition: background-color 0.5s ease;\n"
        "padding:10px;\n"
        "}\n"
        "\n"
        "QPushButton#btn_next_step_solid_control_sample:pressed {\n"
        " background-color: #044e42;\n"
        "border-radius: 6px;\n"
        "background-color: #033029;\n"
        "padding:10px;\n"
        " }\n"
        "")
        self.btn_next_step_solid_control_sample.setIcon(icon10)
        self.btn_next_step_solid_control_sample.setObjectName("btn_next_step_solid_control_sample")
        
        self.txt_shaker_api = QtWidgets.QLineEdit(self.tab_solid_control)
        self.txt_shaker_api.setGeometry(QtCore.QRect(10, 50, 491, 41))
        self.txt_shaker_api.setStyleSheet("""
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
        self.txt_shaker_api.setPlaceholderText("")
        self.txt_shaker_api.setObjectName("txt_shaker_api")
        self.txt_scaper = QtWidgets.QLineEdit(self.tab_solid_control)
        self.txt_scaper.setGeometry(QtCore.QRect(10, 140, 491, 41))
        self.txt_scaper.setStyleSheet("""
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
        self.txt_scaper.setPlaceholderText("")
        self.txt_scaper.setObjectName("txt_scaper")
        self.txt_back = QtWidgets.QLineEdit(self.tab_solid_control)
        self.txt_back.setGeometry(QtCore.QRect(10, 220, 491, 41))
        self.txt_back.setStyleSheet("""
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
        self.txt_back.setPlaceholderText("")
        self.txt_back.setObjectName("txt_back")
        self.lbl_middle.raise_()
        self.lbl_description_man_hour.raise_()
        self.lbl_Hours_run.raise_()
        self.lbl_front.raise_()
        self.lbl_back.raise_()
        self.txt_middle.raise_()
        self.txt_hour_run.raise_()
        self.txt_front.raise_()
        self.lbl_shalker_api.raise_()
        self.btn_next_step_solid_control_sample.raise_()
        self.txt_shaker_api.raise_()
        self.txt_scaper.raise_()
        self.txt_back.raise_()
        self.tab_menus_compliance.addTab(self.tab_solid_control, "")
        self.tab_solid_control_sample = QtWidgets.QWidget()
        self.tab_solid_control_sample.setObjectName("tab_solid_control_sample")
        self.txt_bwl_speed = QtWidgets.QLineEdit(self.tab_solid_control_sample)
        self.txt_bwl_speed.setGeometry(QtCore.QRect(10, 40, 351, 41))
        self.txt_bwl_speed.setStyleSheet("""
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
        
        self.txt_bwl_speed.setObjectName("txt_bwl_speed")
        self.txt_sample_number_non_produtive_man = QtWidgets.QLineEdit(self.tab_solid_control_sample)
        self.txt_sample_number_non_produtive_man.setGeometry(QtCore.QRect(750, 40, 300, 41))
        self.txt_sample_number_non_produtive_man.setStyleSheet("""
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
        self.txt_sample_number_non_produtive_man.setPlaceholderText("")
        self.txt_sample_number_non_produtive_man.setObjectName("txt_sample_number_non_produtive_man")
        self.txt_flow = QtWidgets.QLineEdit(self.tab_solid_control_sample)
        self.txt_flow.setGeometry(QtCore.QRect(380, 40, 351, 41))
        self.txt_flow.setStyleSheet("""
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
        self.txt_flow.setPlaceholderText("")
        self.txt_flow.setObjectName("txt_flow")
        self.btn_next_step_audit = QtWidgets.QPushButton(self.tab_solid_control_sample)
        self.btn_next_step_audit.setGeometry(QtCore.QRect(10, 200, 351, 41))
        self.btn_next_step_audit.setStyleSheet("\n"
        "\n"
        "QPushButton#btn_next_step_audit{\n"
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
        "QPushButton#btn_next_step_audit:hover{\n"
        " background-color: #044e42;\n"
        "border-radius: 6px;\n"
        "transition: background-color 0.5s ease;\n"
        "padding:10px;\n"
        "}\n"
        "\n"
        "QPushButton#btn_next_step_audit:pressed {\n"
        " background-color: #044e42;\n"
        "border-radius: 6px;\n"
        "background-color: #033029;\n"
        "padding:10px;\n"
        " }\n"
        "")
        self.btn_next_step_audit.setIcon(icon10)
        self.btn_next_step_audit.setObjectName("btn_next_step_audit")
        self.btn_add_information_solid_sample = QtWidgets.QPushButton(self.tab_solid_control_sample)
        self.btn_add_information_solid_sample.setGeometry(QtCore.QRect(750, 130, 300, 41))
        self.btn_add_information_solid_sample.setStyleSheet("\n"
        "\n"
        "QPushButton#btn_add_information_solid_sample{\n"
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
        "QPushButton#btn_add_information_solid_sample:hover{\n"
        " background-color: #044e42;\n"
        "border-radius: 6px;\n"
        "transition: background-color 0.5s ease;\n"
        "padding:10px;\n"
        "}\n"
        "\n"
        "QPushButton#btn_add_information_solid_sample:pressed {\n"
        " background-color: #044e42;\n"
        "border-radius: 6px;\n"
        "background-color: #033029;\n"
        "padding:10px;\n"
        " }\n"
        "")
        self.btn_add_information_solid_sample.setIcon(icon10)
        self.btn_add_information_solid_sample.setObjectName("btn_add_information_solid_sample")
        self.lbl_flow = QtWidgets.QLabel(self.tab_solid_control_sample)
        self.lbl_flow.setGeometry(QtCore.QRect(380, 10, 61, 31))
        font = QtGui.QFont("Corbel")
        font.setPointSize(11)
        self.lbl_flow.setFont(font)
        self.lbl_flow.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_flow.setObjectName("lbl_flow")
        self.lbl_weigth = QtWidgets.QLabel(self.tab_solid_control_sample)
        self.lbl_weigth.setGeometry(QtCore.QRect(750, 10, 81, 31))
        font = QtGui.QFont("Corbel")
        font.setPointSize(11)
        self.lbl_weigth.setFont(font)
        self.lbl_weigth.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_weigth.setObjectName("lbl_weigth")
        self.lbl_bwl_speed = QtWidgets.QLabel(self.tab_solid_control_sample)
        self.lbl_bwl_speed.setGeometry(QtCore.QRect(10, 10, 41, 31))
        font = QtGui.QFont("Corbel")
        font.setPointSize(11)
        self.lbl_bwl_speed.setFont(font)
        self.lbl_bwl_speed.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_bwl_speed.setObjectName("lbl_bwl_speed")
        self.lbl_weigth.raise_()
        self.lbl_flow.raise_()
        self.lbl_bwl_speed.raise_()
        self.txt_bwl_speed.raise_()

        self.daily_occ = QtWidgets.QLabel(self.tab_solid_control_sample)
        self.daily_occ.setGeometry(QtCore.QRect(10, 100, 341, 31))
        font = QtGui.QFont("Corbel")
        font.setPointSize(11)
        self.daily_occ.setFont(font)
        self.daily_occ.setStyleSheet("color: rgb(52, 52, 52);")
        self.daily_occ.setObjectName("daily_occ")
        self.lbl_weigth.raise_()
        self.lbl_flow.raise_()
        self.daily_occ.raise_()
        self.daily_occ.setText("Daily % OOC ( % BFi)")

        self.txt_daily_occ = QtWidgets.QLineEdit(self.tab_solid_control_sample)
        self.txt_daily_occ.setGeometry(QtCore.QRect(10, 130, 351, 41))
        self.txt_daily_occ.setStyleSheet("""
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
        self.txt_daily_occ.setPlaceholderText("")
        self.txt_daily_occ.setObjectName("txt_daily_occ")

        self.lbl_well_selection_average = QtWidgets.QLabel(self.tab_solid_control_sample)
        self.lbl_well_selection_average.setGeometry(QtCore.QRect(380, 100, 361, 31))
        font = QtGui.QFont("Corbel")
        font.setPointSize(11)
        self.lbl_well_selection_average.setFont(font)
        self.lbl_well_selection_average.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_well_selection_average.setObjectName("lbl_well_selection_average")
        self.lbl_well_selection_average.setText("Well Section Average % OOC ")

        self.txt_well_selection_average = QtWidgets.QLineEdit(self.tab_solid_control_sample)
        self.txt_well_selection_average.setGeometry(QtCore.QRect(380, 130, 351, 41))
        self.txt_well_selection_average.setStyleSheet("""
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
        self.txt_well_selection_average.setPlaceholderText("")
        self.txt_well_selection_average.setObjectName("txt_well_selection_average")

        self.txt_sample_number_non_produtive_man.raise_()
        self.txt_flow.raise_()
        self.btn_next_step_audit.raise_()
        self.btn_add_information_solid_sample.raise_()
        self.tab_menus_compliance.addTab(self.tab_solid_control_sample, "")

        

        self.tab_audit_questionary = QtWidgets.QWidget()
        self.tab_audit_questionary.setObjectName("tab_audit_questionary")



        self.lbl_finding = QtWidgets.QLabel(self.tab_audit_questionary)
        self.lbl_finding.setObjectName("lbl_finding")
        self.lbl_finding.setText("Findings")
        self.lbl_finding.setGeometry(QtCore.QRect(10,10,150,31))

        self.cbx_finding = QtWidgets.QComboBox(self.tab_audit_questionary)
        self.cbx_finding.setObjectName("txt_finding")
        self.cbx_finding.setGeometry(QtCore.QRect(10,40,351,41))
        self.cbx_finding.addItems(["-- Select Finding --","Equipment Breakdown","Equipment Repaired","Retort correctly used"])
        self.cbx_finding.setStyleSheet("""
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

        self.lbl_select = QtWidgets.QLabel(self.tab_audit_questionary)
        self.lbl_select.setObjectName("lbl_select")
        self.lbl_select.setText("Yes    No")
        self.lbl_select.setGeometry(QtCore.QRect(380,10,150,31))

        self.radioYes = QtWidgets.QRadioButton(self.tab_audit_questionary)
        self.radioYes.setObjectName("radioYes")
        self.radioYes.setGeometry(QtCore.QRect(380,40,351,41))

        self.radioNo = QtWidgets.QRadioButton(self.tab_audit_questionary)
        self.radioNo.setObjectName("radioNo")
        self.radioNo.setGeometry(QtCore.QRect(415,40,351,41))

        self.lbl_time = QtWidgets.QLabel(self.tab_audit_questionary)
        self.lbl_time.setObjectName("lbl_time")
        self.lbl_time.setText("Time")
        self.lbl_time.setGeometry(QtCore.QRect(450,10,150,31))

        self.txt_time = QtWidgets.QTimeEdit(self.tab_audit_questionary)
        self.txt_time.setObjectName("txt_finding")
        self.txt_time.setGeometry(QtCore.QRect(450,40,300,41))
        self.txt_time.setStyleSheet("QTimeEdit{\n"
        "\n"
        "\n"
        "background-color:#fff;\n"
        "border: 1px solid #8ec0af;\n"
        "border-radius: 6px\n"
        "}")
        self.txt_time.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.txt_time.setAccelerated(False)
        self.txt_time.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.txt_time.setProperty("showGroupSeparator", False)

        self.lbl_contrator = QtWidgets.QLabel(self.tab_audit_questionary)
        self.lbl_contrator.setObjectName("lbl_contrator")
        self.lbl_contrator.setText("Contractor")
        self.lbl_contrator.setGeometry(QtCore.QRect(770,10,150,31))

        self.txt_contrator = QtWidgets.QLineEdit(self.tab_audit_questionary)
        self.txt_contrator.setObjectName("txt_finding")
        self.txt_contrator.setGeometry(QtCore.QRect(770,40,300,41))
        self.txt_contrator.setStyleSheet("""
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

        self.btn_add_information_audit_questions = QtWidgets.QPushButton(self.tab_audit_questionary)
        self.btn_add_information_audit_questions.setGeometry(QtCore.QRect(10, 120, 351, 41))
        self.btn_add_information_audit_questions.setStyleSheet("\n"
        "\n"
        "QPushButton#btn_add_information_audit_questions{\n"
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
        "QPushButton#btn_add_information_audit_questions:hover{\n"
        " background-color: #044e42;\n"
        "border-radius: 6px;\n"
        "transition: background-color 0.5s ease;\n"
        "padding:10px;\n"
        "}\n"
        "\n"
        "QPushButton#btn_add_information_audit_questions:pressed {\n"
        " background-color: #044e42;\n"
        "border-radius: 6px;\n"
        "background-color: #033029;\n"
        "padding:10px;\n"
        " }\n"
        "")
        self.btn_add_information_audit_questions.setIcon(icon10)
        self.btn_add_information_audit_questions.setObjectName("btn_add_information_audit_questions")
        self.btn_add_information_audit_questions.setText("Add the filled information to report")

        self.btn_next_enginer_compliance = QtWidgets.QPushButton(self.tab_audit_questionary)
        self.btn_next_enginer_compliance.setGeometry(QtCore.QRect(380, 120, 368, 41))
        self.btn_next_enginer_compliance.setStyleSheet("\n"
        "\n"
        "QPushButton#btn_next_enginer_compliance{\n"
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
        "QPushButton#btn_next_enginer_compliance:hover{\n"
        " background-color: #044e42;\n"
        "border-radius: 6px;\n"
        "transition: background-color 0.5s ease;\n"
        "padding:10px;\n"
        "}\n"
        "\n"
        "QPushButton#btn_next_enginer_compliance:pressed {\n"
        " background-color: #044e42;\n"
        "border-radius: 6px;\n"
        "background-color: #033029;\n"
        "padding:10px;\n"
        " }\n"
        "")
        self.btn_next_enginer_compliance.setIcon(icon10)
        self.btn_next_enginer_compliance.setObjectName("btn_next_enginer_compliance")
        self.btn_next_enginer_compliance.setText("Next")

       

        

        self.txt_area_monitoring_coments = QtWidgets.QPlainTextEdit(self.tab_ongoing_rig)
        self.txt_area_monitoring_coments.setGeometry(QtCore.QRect(10, 250, 1050, 100))
        self.txt_area_monitoring_coments.setStyleSheet("QPlainTextEdit{\n"
        "\n"
        "\n"
        "background-color:#fff;\n"
        "border: 1px solid #8ec0af;\n"
        "border-radius: 6px\n"
        "}")
        self.txt_area_monitoring_coments.setPlaceholderText("")
        self.txt_area_monitoring_coments.setObjectName("txt_area_monitoring_coments")
        
        self.txt_area_ongoing_rig = QtWidgets.QPlainTextEdit(self.tab_ongoing_rig)
        self.txt_area_ongoing_rig.setGeometry(QtCore.QRect(10, 60, 1050, 100))
        self.txt_area_ongoing_rig.setStyleSheet("QPlainTextEdit{\n"
        "\n"
        "\n"
        "background-color:#fff;\n"
        "border: 1px solid #8ec0af;\n"
        "border-radius: 6px\n"
        "}")
        self.txt_area_ongoing_rig.setPlaceholderText("")
        self.txt_area_ongoing_rig.setObjectName("txt_area_ongoing_rig")

        

        
        self.lbl_monitoring_coments = QtWidgets.QLabel(self.tab_ongoing_rig)
        self.lbl_monitoring_coments.setGeometry(QtCore.QRect(10, 220, 341, 31))
        font = QtGui.QFont("Corbel")
        font.setPointSize(11)
        self.lbl_monitoring_coments.setFont(font)
        self.lbl_monitoring_coments.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_monitoring_coments.setObjectName("lbl_monitoring_coments")
        
        self.lbl_ongoing_rig_activity = QtWidgets.QLabel(self.tab_ongoing_rig)
        self.lbl_ongoing_rig_activity.setGeometry(QtCore.QRect(10, 30, 170, 31))
        font = QtGui.QFont("Corbel")
        font.setPointSize(11)
        self.lbl_ongoing_rig_activity.setFont(font)
        self.lbl_ongoing_rig_activity.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_ongoing_rig_activity.setObjectName("lbl_ongoing_rig_activity")
        
        
        self.btn_next_fluid_information = QtWidgets.QPushButton(self.tab_ongoing_rig)
        self.btn_next_fluid_information.setGeometry(QtCore.QRect(10, 365, 491, 41))
        self.btn_next_fluid_information.setStyleSheet("\n"
        "\n"
        "QPushButton#btn_next_fluid_information{\n"
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
        "QPushButton#btn_next_fluid_information:hover{\n"
        " background-color: #044e42;\n"
        "border-radius: 6px;\n"
        "transition: background-color 0.5s ease;\n"
        "padding:10px;\n"
        "}\n"
        "\n"
        "QPushButton#btn_next_fluid_information:pressed {\n"
        " background-color: #044e42;\n"
        "border-radius: 6px;\n"
        "background-color: #033029;\n"
        "padding:10px;\n"
        " }\n"
        "")
        self.btn_next_fluid_information.setIcon(icon10)
        self.btn_next_fluid_information.setObjectName("btn_next_fluid_information")


        

        self.lbl_compliance_enginer = QtWidgets.QLabel(self.tab_audit_compliance_enginner)
        self.lbl_compliance_enginer.setObjectName("lbl_compliance_enginer")
        self.lbl_compliance_enginer.setText("Complience Engineer")
        self.lbl_compliance_enginer.setGeometry(QtCore.QRect(10,10,150,31))

        self.cbx_compliance_enginer = QtWidgets.QComboBox(self.tab_audit_compliance_enginner)
        self.cbx_compliance_enginer.setObjectName("cbx_compliance_enginer")
        self.cbx_compliance_enginer.setGeometry(QtCore.QRect(10,40,351,41))
        self.cbx_compliance_enginer.addItem("-- Select Compliance Enginner --")
        self.cbx_compliance_enginer.setStyleSheet("""
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

        self.lbl_shift = QtWidgets.QLabel(self.tab_audit_compliance_enginner)
        self.lbl_shift.setObjectName("lbl_shift")
        self.lbl_shift.setText("Shift")
        self.lbl_shift.setGeometry(QtCore.QRect(380,10,150,31))

        self.cbx_shift = QtWidgets.QComboBox(self.tab_audit_compliance_enginner)
        self.cbx_shift.setObjectName("cbx_shift")
        self.cbx_shift.setGeometry(QtCore.QRect(380,40,351,41))
        self.cbx_shift.addItem("-- Select Shift --")
        self.cbx_shift.addItems(["Days","Night"])
        self.cbx_shift.setStyleSheet("""
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

        self.btn_save_report = QtWidgets.QPushButton(self.tab_audit_compliance_enginner)
        self.btn_save_report.setGeometry(QtCore.QRect(735, 40, 347, 41))
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
        self.btn_save_report.setText("Next Step")
        
        self.lbl_monitoring_coments.raise_()
        self.lbl_ongoing_rig_activity.raise_()
        self.txt_area_monitoring_coments.raise_()
        self.txt_area_ongoing_rig.raise_()
        self.btn_next_fluid_information.raise_()
        
        self.tab_menus_compliance.addTab(self.tab_audit_questionary,"")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1400, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow,user_logado)
        self.tab_menus_compliance.setCurrentIndex(0)
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
        self.lbl_user_logado.setText(_translate("MainWindow", user_logado))
        self.lbl_form_tittle.setText(_translate("MainWindow", "A. M. Compliance - Add new Report"))
        self.lbl_form_text.setText(_translate("MainWindow", "Below are the fields to be filled in to generate a new report"))
        self.btn_list_report.setText(_translate("MainWindow", "List all report"))
        self.btn_list_report.clicked.connect(lambda:call_form_compliance_list())


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
        
        self.tab_menus_compliance.setTabText(self.tab_menus_compliance.indexOf(self.tab_report_information), _translate("MainWindow", "Report Information"))
        
        self.btn_next_step_driliing_properties.setText(_translate("MainWindow", "Next Step"))
        self.btn_next_step_driliing_properties.clicked.connect(lambda:save_fluid_information())

        self.lbl_mud_type.setText(_translate("MainWindow", "Mud Type"))
        self.lbl_rig_total_volume_type.setText(_translate("MainWindow", "Rig total volume (Unit)"))
        self.lbl_rig_volume.setText(_translate("MainWindow", "Rig total volume"))
        self.tab_menus_compliance.setTabText(self.tab_menus_compliance.indexOf(self.tab_fluid_information), _translate("MainWindow", "Fluid Information"))
        self.lbl_hole_size.setText(_translate("MainWindow", "Hole Size"))
        
        self.btn_next_step_drilling_information.setText(_translate("MainWindow", "Next Step"))
        self.btn_next_step_drilling_information.clicked.connect(lambda:drilling_information())

        self.lbl_total_depth.setText(_translate("MainWindow", "Total Depth (ft)"))
        self.lbl_feets_drilled.setText(_translate("MainWindow", "Feet Drilled"))
        self.txt_feets_drilled.setPlaceholderText(_translate("MainWindow", " Write here..."))
        self.lbl_average_rop.setText(_translate("MainWindow", "Average ROP"))
        self.txt_average_rop.setPlaceholderText(_translate("MainWindow", " Write here..."))
        self.tab_menus_compliance.setTabText(self.tab_menus_compliance.indexOf(self.tb_driling_information), _translate("MainWindow", "Drilling Information "))
        self.lbl_fluid_proprietes.setText(_translate("MainWindow", "Fluid Properties"))
        self.lbl_value_drilling_fluid.setText(_translate("MainWindow", "Value"))

        self.cbx_customer.textActivated.connect(lambda: carregar_poco(self.cbx_customer.currentText()))


        self.btn_next_drilling_fluid.setText(_translate("MainWindow", "Next Step"))
        self.btn_next_drilling_fluid.clicked.connect(lambda:validator_hse())
        
        self.btn_add_information_drilling_fluid.setText(_translate("MainWindow", "Add the filled information to report"))
        self.btn_add_information_drilling_fluid.clicked.connect(lambda:add_drilling_fluid())

        self.tab_menus_compliance.setTabText(self.tab_menus_compliance.indexOf(self.tab_drilling_fluid_information), _translate("MainWindow", "Drilling Fluid Proprieties"))
        self.lbl_depth.setText(_translate("MainWindow", "Depth Location"))
        self.lbl_sample_number.setText(_translate("MainWindow", "Sample Number"))
        self.lbl_sample_location.setText(_translate("MainWindow", "Sample Location"))
        self.btn_add_sample.setText(_translate("MainWindow", "Add Sample"))

        

        self.tab_menus_compliance.setTabText(self.tab_menus_compliance.indexOf(self.tab_add_sample), _translate("MainWindow", "Average OOC"))
        self.lbl_back.setText(_translate("MainWindow", "Back"))
        self.lbl_description_man_hour.setText(_translate("MainWindow", "Scalper"))
        self.lbl_front.setText(_translate("MainWindow", "Front"))
        self.lbl_Hours_run.setText(_translate("MainWindow", "Hours Run"))
        self.lbl_shalker_api.setText(_translate("MainWindow", "Shaker (Screen-API mesh)"))

        self.lbl_middle.setText(_translate("MainWindow", "Middle"))
        self.btn_next_step_solid_control_sample.setText(_translate("MainWindow", "Next Step"))
        self.btn_next_step_solid_control_sample.clicked.connect(lambda:validator_solid_control())

        self.tab_menus_compliance.setTabText(self.tab_menus_compliance.indexOf(self.tab_solid_control), _translate("MainWindow", "Solids Control "))
        
        self.btn_next_step_audit.setText(_translate("MainWindow", "Next Step"))
        self.btn_next_step_audit.clicked.connect(lambda:validator_imob_inventory())
        
        self.btn_add_information_solid_sample.setText(_translate("MainWindow", "Add the filled information to report"))
        self.btn_add_information_solid_sample.clicked.connect(lambda:add_sollid_control())

        self.btn_list_dril_flui_prop.clicked.connect(lambda:show_form_fluid_proprietes())
        
        self.lbl_flow.setText(_translate("MainWindow", "Flow"))
        self.lbl_weigth.setText(_translate("MainWindow", "Weight in"))
        self.lbl_bwl_speed.setText(_translate("MainWindow", "Bowl Speed (rpm )"))
        self.tab_menus_compliance.setTabText(self.tab_menus_compliance.indexOf(self.tab_solid_control_sample), _translate("MainWindow", "Solids Control"))
        self.lbl_monitoring_coments.setText(_translate("MainWindow", "Monitoring Comments"))
        self.lbl_ongoing_rig_activity.setText(_translate("MainWindow", "Ongoing Rig Activity"))
        
        
        self.btn_next_step_solid.clicked.connect(lambda:next_step_solid())
        self.btn_next_fluid_information.setText(_translate("MainWindow", "Next"))
        self.btn_next_fluid_information.clicked.connect(lambda:next_step_fluid_information())

        self.tab_menus_compliance.setTabText(self.tab_menus_compliance.indexOf(self.tab_ongoing_rig), _translate("MainWindow", "Inventory Mob"))

        self.btn_save_report.clicked.connect(lambda:save_report_header(self.cbx_customer.currentText()))

        self.tab_menus_compliance.setTabText(self.tab_menus_compliance.indexOf(self.tab_ongoing_rig), _translate("MainWindow", "Ongoing Rig Activity"))

        self.tab_menus_compliance.setTabText(self.tab_menus_compliance.indexOf(self.tab_audit_questionary), _translate("MainWindow","Audit Questionnaire"))

        self.tab_menus_compliance.setTabText(self.tab_menus_compliance.indexOf(self.tab_audit_compliance_enginner), _translate("MainWindow","Complience Engineer"))

        self.lbl_user_logado.setText(str(user_logado))

        self.btn_add_information_audit_questions.clicked.connect(lambda:add_auti_questionary())


        def carregar_poco(cliente):
            self.cbx_well_number.clear()
            lista_poco = controller.lista_well(cliente)
            for item in lista_poco:
                 self.cbx_well_number.addItem(str(item[1]))

        def carregar_cliente():
            lista_cliente = controller.buscar_cliente()
            for item in lista_cliente:
                self.cbx_customer.addItem(str(item[1]))


        def carregar_empregado():
            lista = controller.listar_employe()
            for item in lista:
                self.cbx_aproved_by.addItem(str(item[1]))
                self.cbx_compliance_enginer.addItem(str(item[1]))

        def carregar_mud_type():
             lista_mud = controller_mud.listar()
             for item in lista_mud:
                  self.cbx_mud_type.addItem(str(item[1]))

        def carregar_fluid_properties():
             lista_fluid_properties = controller_fluid.listar()
             for item in lista_fluid_properties:
                  self.cbx_fluid_proprieties.addItem(str(item[1])) 
        
        def carregar_sample_location_occ():
            lista_sample = controller_sample_location.listar()
            for item in lista_sample:
                self.cbx_sample_location_occ.addItem(str(item[1]))
                self.cbx_solids_sample_location.addItem(str(item[1]))

        def carregar_model_average():
             lista_model_average = controller_model_average.listar()
             for item in lista_model_average:
                  self.cbx_model_average.addItem(str(item[1]))
                  self.cbx_dryer.addItem(str(item[1]))

        def return_id(nome,lista):
            for item in lista:
                if item[1] == nome:
                    return item[0]
            return None

        carregar_cliente()
        carregar_empregado()
        carregar_mud_type()
        carregar_fluid_properties()
        carregar_sample_location_occ()
        carregar_model_average()

        
       
        def show_message_sucess():
            msg_error = QMessageBox()
            msg_error.setIcon(QMessageBox.Information)
            msg_error.setText('Data has been added successfully')
            msg_error.setWindowTitle('Adding data')
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("./img/sucess_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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

        def message_error_validation(text_input_error,tittle_windows):
            msg_error = QMessageBox()
            msg_error.setIcon(QMessageBox.Critical)
            msg_error.setText(str(text_input_error))
            msg_error.setWindowTitle(str(tittle_windows))
            msg_error.exec_()

        def validator_report_information():

            countVezes = False
            lista = controller.listar_employe()
            caracter_especial = '1234567890!#$%&/=?*+ªº^~-"'
            only_special_character = '!#$%&/=?*+ªº^~-"'

            # Text Rig Name
            txt_job_ref = str(self.txt_job_ref.text())
            txt_rig = str(self.txt_rig_name.text())
            txt_job_type = str(self.txt_job_type.text())
            txt_field_location = str(self.txt_field_location.text())
            cbx_aproved_by = str(self.cbx_aproved_by.currentText())
            txt_project_description = str(self.txt_project_description.text())

            id_empregado = return_id(self.cbx_aproved_by.currentText(),lista)
            

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
                self.tab_menus_compliance.setCurrentIndex(1)

        def next_step_fluid_information():
            self.tab_menus_compliance.setCurrentIndex(3)

        def save_fluid_information():

            try:
                lista_mud = controller_mud.listar()
                id_mud_type = return_id(self.cbx_mud_type.currentText(),lista_mud)
                rig_total = self.txt_rig_volume.text()
                density = self.txt_density.text()
                viscosity_pv = self.txt_viscosity_pv.text()
                viscosity_yp = self.txt_viscosity_yp.text()
                hole_volume = self.txt_hole_volume.text()
                tipo_density = self.cbx_density_type.currentText()
                tipo_rig_volume = self.cbx_rig_volume_type.currentText()
                hole_volume_type = self.cbx_hole_volume_type.currentText()
                id_last_report = controller.buscar_id_ultimo_report()

                fluid_information = controller_fluid_information.cadastrar(id_mud_type,tipo_rig_volume,tipo_density,hole_volume_type,rig_total,density,viscosity_pv,viscosity_yp,hole_volume,id_last_report)
                
                if fluid_information != 0:
                    message_error_validation(fluid_information,"Fluid Information")
                    
                else:
                    show_message_sucess()
                    self.tab_menus_compliance.setCurrentIndex(5)
            except Exception as e:
                message_error_validation(e,"Fluid Information")

            
                     

                

        def drilling_information():
            
            self.tab_menus_compliance.setCurrentIndex(2)
            #try:
            customer = self.cbx_customer.currentText()
            well = self.cbx_well_number.currentText()
            report_date = self.data_at_depth.text()
            approved_by = self.cbx_aproved_by.currentText()
                

        
        def add_drilling_fluid():
          
            try:
                lista_fluid_properties = controller_fluid.listar()
                id_fluid_properties = return_id(self.cbx_fluid_proprieties.currentText(),lista_fluid_properties)
                value_fluid_properties = self.txt_value.text()
                id_last_report = controller.buscar_id_ultimo_report()
                drilling_fluid = controller_drilling_fluid.cadastrar(id_fluid_properties,value_fluid_properties,id_last_report)
                if drilling_fluid != 0:
                    message_error_validation(drilling_fluid,"Drilling Fluid Properties")
                else:
                    show_message_sucess()
            except Exception as e:
               message_error_validation(e,"Drillin Fluid Properties")

           
        def next_step_solid():
            self.tab_menus_compliance.setCurrentIndex(7)

        def add_hse_to_report():
             
            
                show_message_sucess()

        def add_tank_information():
             
                show_message_sucess()
                   
                
       
             

        def add_produtive_man_to_report():
             
             only_special_character = '!#$%&/=?*+ªº^~-"'
             
             

             def has_special_characters(input_str, special_chars):
                for char in input_str:
                    if char in special_chars:
                        return True
                return False

             if has_special_characters(self.txt_scaper.text(), only_special_character) or (self.txt_scaper.text() == ""):
                message_error_validation("This field does not accept special characters or is empty", "Input Description Error")
            
             elif has_special_characters(self.cbx_dryer_screen_size.text(),only_special_character) or (self.cbx_dryer_screen_size.text() == ""):
                message_error_validation("This field does not accept special characters or is empty", "Field Location entry Error")
        
             elif has_special_characters(self.txt_middle.text(),only_special_character) or (self.txt_middle.text() == ""):
                message_error_validation("This field does not accept special characters or is empty", "Field Location entry Error")
             
             else:
                        

                show_message_sucess()

        def add_sollid_control():
            
            lista_sample_location = controller_sample_location.listar()
            lista_model_average = controller_model_average.listar()

            id_sample_location = return_id(self.cbx_sample_location_occ.currentText(),lista_sample_location)
            id_mode_avarage = return_id(self.cbx_model_average.currentText(),lista_model_average)

            id_last_report = controller.buscar_id_ultimo_report()
            save_solid_control = solid_controller.cadastrar(self.txt_shaker_api.text(),
            self.txt_scaper.text(),self.txt_back.text(),self.txt_middle.text(),self.txt_front.text(),self.txt_hour_run.text(),id_sample_location,self.txt_dryer_screen_size.text(),self.txt_bwl_speed.text(),self.txt_flow.text(),"15",self.txt_daily_occ.text(),id_last_report)

            show_message_sucess()

        
                  
        def validator_hse():

                self.tab_menus_compliance.setCurrentIndex(6)

        def validator_produtive_man_hour():

                self.tab_menus_compliance.setCurrentIndex(5)

        def validator_solid_control():

                self.tab_menus_compliance.setCurrentIndex(8)

        def validator_imob_inventory():

                self.tab_menus_compliance.setCurrentIndex(9)

        def report():
            show_message_sucess()


        def add_sample_average_dry_cutting(depth_location,sample_location,sample_number,dataTeste,timeTest,model,numberOfShake,numberOfCuttings):

            
            self.window = QtWidgets.QMainWindow()
            import compliance.compliance_sample as add
            self.ui = add.Ui_MainWindow()
            self.ui.setupUi(self.window,depth_location,sample_location,sample_number,dataTeste,timeTest,model,numberOfShake,numberOfCuttings)
            self.window.show()
            #MainWindow.close()


        def call_form_compliance_list():
            self.window = QtWidgets.QMainWindow()
            import compliance.compliance_view as listar
            self.ui = listar.Ui_MainWindow()
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

        def show_form_fluid_proprietes():
             self.window = QtWidgets.QMainWindow()
             import compliance.pack_fluid_proprieties.fluid_properties as view
             self.ui = view.Ui_MainWindow()
             self.ui.setupUi(self.window,self.lbl_user_logado.text())
             self.window.show()
             MainWindow.close()

        
        lista_model_average = controller_model_average.listar()
        lista_sample_location = controller_sample_location.listar()

        id_sample_location = return_id(self.cbx_sample_location_occ.currentText(),lista_sample_location)
        #id_mode_avarage = return_id(self.cbx_model_average.currentText(),lista_model_average)
        


        self.btn_add_sample.clicked.connect(lambda:add_sample_average_dry_cutting(self.txt_depth_location.text(),id_sample_location,self.txt_sample_number.text(),self.data_test.text(),self.time_test.text(),self.cbx_model_average.currentText(),self.txt_number_of_shakers.text(),self.txt_number_of_cutting.text()))



        #Funcao para Salvar
        def save_report_header(customer):

            lista_cliente = controller.buscar_cliente()
            lista_well = controller.lista_well(customer)
            lista_mud = controller_mud.listar()
            lista_empregado = controller.listar_employe()
            lista_fluid_properties = controller_fluid.listar()
            lista_sample_location = controller_sample_location.listar()
            lista_model_average = controller_model_average.listar()



            id_cliente = return_id(self.cbx_customer.currentText(),lista_cliente)
            id_well_number = return_id(self.cbx_well_number.currentText(),lista_well)
            id_mud_type = return_id(self.cbx_mud_type.currentText(),lista_mud)
            id_empregado = return_id(self.cbx_aproved_by.currentText(),lista_empregado)
            id_fluid_properties = return_id(self.cbx_fluid_proprieties.currentText(),lista_fluid_properties)
            id_sample_location = return_id(self.cbx_sample_location_occ.currentText(),lista_sample_location)
            id_mode_avarage = return_id(self.cbx_model_average.currentText(),lista_model_average)
            id_dryer = return_id(self.cbx_dryer.currentText(),lista_model_average)
            id_compliance_enginer = return_id(self.cbx_compliance_enginer.currentText(),lista_empregado)
            id_solids_sample_location = return_id(self.cbx_solids_sample_location.currentText(),lista_sample_location)
            id_user_logado = controller.buscar_id_user_logado(user_logado)


            #Salvar Report Information
            try:
                data = str(self.data_report.text())
                job_ref_number = str(self.txt_job_ref.text())
                rig_name = str(self.txt_rig_name.text())
                field_location = str(self.txt_field_location.text())
                job_type = str(self.txt_job_type.text())
                project_description = str(self.txt_project_description.text())
                hole_size = str(self.txt_hole_size.text())
                total_depth = str(self.txt_total_depth.text())
                feets_drilled = str(self.txt_feets_drilled.text())
                average_rop = str(self.txt_average_rop.text())
                time_at_depth = str(self.data_at_depth.text())
                shift = str(self.cbx_shift.currentText())
                ongoing_activity = str(self.txt_area_ongoing_rig.toPlainText())
                monitoring_comments = str(self.txt_area_monitoring_coments.toPlainText())

            except Exception as e:
                print(f"{e}")
            
            finally:
                
                save_report_information = controller.cadastrar(str(id_cliente),str(id_well_number),data,str(id_compliance_enginer),job_ref_number,rig_name,field_location,job_type,project_description,hole_size,total_depth,feets_drilled,average_rop,time_at_depth,id_user_logado,shift,ongoing_activity,monitoring_comments)
                id_last_report = controller.buscar_id_ultimo_report()
                svae_enginer = enginer_controller.cadastrar_enginer(shift,id_empregado,id_last_report)
                print(svae_enginer)
                if (save_report_information == 0) and (svae_enginer == 0):
                    
                    self.tab_menus_compliance.setCurrentIndex(3)
                else:
                    print("Não Salvou")
            show_message_sucess()
            self.tab_menus_compliance.setCurrentIndex(4)

        def add_auti_questionary():
            id_last_report = controller.buscar_id_ultimo_report()
            save_audit = audit_controller.cadastrar(self.cbx_finding.currentText(),self.radioYes.text(),self.txt_time.text(),self.txt_contrator.text(),id_last_report)
            print(save_audit)  

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
