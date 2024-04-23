


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget,QMessageBox
import modulo_wbco.wbcoController
import modulo_wbco.report_wbco_download
import modulo_wbco.sizeController


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

        self.gerador_report = modulo_wbco.report_wbco_download.GerarReport()

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
        icon_employee = QtGui.QIcon()
        icon_employee.addPixmap(QtGui.QPixmap("img/users-group.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/house-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        icon_view_pdf = QtGui.QIcon()
        icon_view_pdf.addPixmap(QtGui.QPixmap("img/print.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        icon_download = QtGui.QIcon()
        icon_download.addPixmap(QtGui.QPixmap("img/download-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)


        icon_edit = QtGui.QIcon()
        icon_edit.addPixmap(QtGui.QPixmap("img/edit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
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
        font = QtGui.QFont("Corbel")
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
        self.lbl_user_logado.setText(user_name)
        self.img_user_login = QtWidgets.QPushButton(self.frame_2)
        self.img_user_login.setGeometry(QtCore.QRect(980, 10, 31, 31))
        self.img_user_login.setStyleSheet("background-color: #fff;\n"
"border-radius:30px;\n"
"width:30px;\n"
"height:30px;")
        self.img_user_login.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("img/user_dark.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.img_user_login.setIcon(icon8)
        self.img_user_login.setIconSize(QtCore.QSize(25, 25))
        self.img_user_login.setObjectName("img_user_login")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(0, 50, 1151, 151))
        self.frame_3.setStyleSheet("background-color:#2d6b56;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_titulo_form = QtWidgets.QLabel(self.frame_3)
        self.label_titulo_form.setGeometry(QtCore.QRect(40, 50, 281, 31))
        self.label_titulo_form.setStyleSheet("font-size: 30px;\n"
"color:#fff;")
        self.label_titulo_form.setObjectName("label_titulo_form")
        self.line = QtWidgets.QFrame(self.frame_3)
        self.line.setGeometry(QtCore.QRect(-10, 0, 21, 151))
        self.line.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.lbl_text_form = QtWidgets.QLabel(self.frame_3)
        self.lbl_text_form.setGeometry(QtCore.QRect(40, 90, 621, 21))
        self.lbl_text_form.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 9pt \"MS Shell Dlg 2\";")
        self.lbl_text_form.setObjectName("lbl_text_form")
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
        self.line_3.setGeometry(QtCore.QRect(20, 270, 1091, 20))
        self.line_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.btn_add_report = QtWidgets.QPushButton(self.frame)
        self.btn_add_report.setGeometry(QtCore.QRect(920, 240, 191, 33))
        self.btn_add_report.setStyleSheet("\n"
"\n"
"QPushButton#btn_add_report{\n"
"\n"
"border:none;\n"
"background-color:#044e42;\n"
"color:white;\n"
"font-size:12px;\n"
"border-radius: 6px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"text-align:rigth;\n"
"}\n"
"\n"
"QPushButton#btn_add_report:hover{\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_add_report:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"background-color: #033029;\n"
"padding:10px;\n"
" }\n"
"")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("img/file-lines-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add_report.setIcon(icon9)
        self.btn_add_report.setObjectName("btn_add_report")

#---------------------BOtao para listar os Sizes-----------------------------------------
        self.btn_list_size = QtWidgets.QPushButton(self.frame)
        self.btn_list_size.setGeometry(QtCore.QRect(720, 240, 191, 33))
        self.btn_list_size.setStyleSheet("\n"
"\n"
"QPushButton#btn_list_size{\n"
"\n"
"border:none;\n"
"background-color:#044e42;\n"
"color:white;\n"
"font-size:12px;\n"
"border-radius: 6px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"text-align:rigth;\n"
"}\n"
"\n"
"QPushButton#btn_list_size:hover{\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_list_size:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"background-color: #033029;\n"
"padding:10px;\n"
" }\n"
"")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("img/file-lines-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_list_size.setIcon(icon9)
        self.btn_list_size.setObjectName("btn_list_size")


#---------------------------------------------------------------------------------------- 
        
#---------------------BOtao para listar Threads-----------------------------------------
        self.btn_list_thread = QtWidgets.QPushButton(self.frame)
        self.btn_list_thread.setGeometry(QtCore.QRect(520, 240, 191, 33))
        self.btn_list_thread.setStyleSheet("\n"
"\n"
"QPushButton#btn_list_thread{\n"
"\n"
"border:none;\n"
"background-color:#044e42;\n"
"color:white;\n"
"font-size:12px;\n"
"border-radius: 6px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"text-align:rigth;\n"
"}\n"
"\n"
"QPushButton#btn_list_thread:hover{\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_list_thread:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"background-color: #033029;\n"
"padding:10px;\n"
" }\n"
"")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("img/file-lines-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_list_thread.setIcon(icon9)
        self.btn_list_thread.setObjectName("btn_list_thread")


#----------------------------------------------------------------------------------------         
        
 #---------------------BOtao para listar Engineer WBCO-----------------------------------------
        self.btn_list_wbco_engineer = QtWidgets.QPushButton(self.frame)
        self.btn_list_wbco_engineer.setGeometry(QtCore.QRect(320, 240, 191, 33))
        self.btn_list_wbco_engineer.setStyleSheet("\n"
"\n"
"QPushButton#btn_list_wbco_engineer{\n"
"\n"
"border:none;\n"
"background-color:#044e42;\n"
"color:white;\n"
"font-size:12px;\n"
"border-radius: 6px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"text-align:rigth;\n"
"}\n"
"\n"
"QPushButton#btn_list_wbco_engineer:hover{\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_list_wbco_engineer:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"background-color: #033029;\n"
"padding:10px;\n"
" }\n"
"")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("img/file-lines-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_list_wbco_engineer.setIcon(icon_employee)
        self.btn_list_wbco_engineer.setObjectName("btn_list_wbco_engineer")


#----------------------------------------------------------------------------------------              

        self.table_wbco_report = QtWidgets.QTableWidget(self.frame)
        self.table_wbco_report.setGeometry(QtCore.QRect(20, 290, 1091, 421))
        self.table_wbco_report.setAutoFillBackground(True)
        self.table_wbco_report.setStyleSheet("QTableWidget{\n"
"\n"
"\n"
"border:none;\n"
"selection-color:green;\n"
"selection-background-color:red;\n"
"\n"
"}\n"
"\n"
"QTableWidget::item:selected{\n"
"color:white;\n"
"background-color:#044e42;\n"
"\n"
"\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"\n"
"background-color:#044e42;\n"
"color:#fff;\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"}\n"
"QTableWidget::item{ padding:2px;}"
"\n"
"\n"
"\n"
"")
        self.table_wbco_report.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.table_wbco_report.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.table_wbco_report.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table_wbco_report.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_wbco_report.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.table_wbco_report.setShowGrid(False)
        self.table_wbco_report.setGridStyle(QtCore.Qt.NoPen)
        self.table_wbco_report.setCornerButtonEnabled(False)
        self.table_wbco_report.setObjectName("table_wbco_report")
        self.table_wbco_report.setColumnCount(6)
        self.table_wbco_report.setHorizontalHeaderLabels(["Customer Name","Job. Ref. Number","Prepared by","Date Report","",""])
        self.table_wbco_report.horizontalHeaderItem(0).setTextAlignment(0x0001)
        self.table_wbco_report.horizontalHeaderItem(1).setTextAlignment(0x0001)
        self.table_wbco_report.horizontalHeaderItem(2).setTextAlignment(0x0001)
        self.table_wbco_report.horizontalHeaderItem(3).setTextAlignment(0x0001)
        self.table_wbco_report.horizontalHeaderItem(4).setTextAlignment(0x0001)

        list_report = modulo_wbco.wbcoController.listar_report()
        self.table_wbco_report.setRowCount(30)
        tablerow = 0

        for row in list_report:
            
            self.button_view_report = QtWidgets.QPushButton("View")
            self.button_view_report.setStyleSheet("\n" "\n" "QPushButton#button_view_report{\n" "\n" "border:none;\n" "background-color:#044e42;\n" "color:white;\n" "font-size:13px;\n" "border-radius: 3px;\n" "transition: background-color 0.5s ease;\n" "padding:5px;\n" "text-align:rigth;\n" "}\n" "\n" "QPushButton#button_view_report:hover{\n" " background-color: #044e42;\n" "border-radius: 3px;\n" "transition: background-color 0.5s ease;\n" "padding:5px;\n" "}\n" "\n" "QPushButton#button_view_report:pressed {\n" " background-color: #044e42;\n" "border-radius: 0px;\n" "background-color: #033029;\n" "padding:5px;\n" " }\n" "")
            self.button_view_report.setIcon(icon_view_pdf)
            self.button_view_report.setObjectName("button_view_report")

            self.button_download_report = QtWidgets.QPushButton("Download")
            self.button_download_report.setStyleSheet("\n" "\n" "QPushButton#button_download_report{\n" "\n" "border:none;\n" "background-color:#044e42;\n" "color:white;\n" "font-size:13px;\n" "border-radius: 3px;\n" "transition: background-color 0.5s ease;\n" "padding:5px;\n" "text-align:rigth;\n" "}\n" "\n" "QPushButton#button_download_report:hover{\n" " background-color: #044e42;\n" "border-radius: 3px;\n" "transition: background-color 0.5s ease;\n" "padding:5px;\n" "}\n" "\n" "QPushButton#button_download_report:pressed {\n" " background-color: #044e42;\n" "border-radius: 0px;\n" "background-color: #033029;\n" "padding:5px;\n" " }\n" "")
            self.button_download_report.setIcon(icon_download)
            self.button_download_report.setObjectName("button_download_report")

            self.button_edit_report = QtWidgets.QPushButton("Edit")
            self.button_edit_report.setStyleSheet("\n" "\n" "QPushButton#button_edit_report{\n" "\n" "border:none;\n" "background-color:#044e42;\n" "color:white;\n" "font-size:13px;\n" "border-radius: 3px;\n" "transition: background-color 0.5s ease;\n" "padding:5px;\n" "text-align:rigth;\n" "}\n" "\n" "QPushButton#button_edit_report:hover{\n" " background-color: #044e42;\n" "border-radius: 3px;\n" "transition: background-color 0.5s ease;\n" "padding:5px;\n" "}\n" "\n" "QPushButton#button_edit_report:pressed {\n" " background-color: #044e42;\n" "border-radius: 0px;\n" "background-color: #033029;\n" "padding:5px;\n" " }\n" "")
            self.button_edit_report.setIcon(icon_edit)
            self.button_edit_report.setObjectName("button_edit_report")

            self.table_wbco_report.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
            self.table_wbco_report.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.table_wbco_report.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[3]))
            self.table_wbco_report.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[4]))
            self.table_wbco_report.setCellWidget(tablerow,4,self.button_download_report)
            self.table_wbco_report.setCellWidget(tablerow,5,self.button_view_report)

            tablerow+=1

            self.button_download_report.clicked.connect(lambda:buttnon_download_report())
            self.button_view_report.clicked.connect(lambda:view_report())
            #self.button_edit_report.clicked.connect(lambda:editar_report())



        def show_wbco_report_edit(job_ref):
            self.window = QtWidgets.QMainWindow()
            import modulo_wbco.wbco_report_edit
            self.ui = modulo_wbco.wbco_report_edit.Ui_MainWindow()
            self.ui.setupUi(self.window,self.lbl_user_logado.text(),job_ref)
            self.window.show()
            MainWindow.close()

        def show_message_sucess():
            msg_error = QMessageBox()
            msg_error.setIcon(QMessageBox.Information)
            msg_error.setText('Report was generated successfully')
            msg_error.setWindowTitle('Report generation')
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("img/sucess_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg_error.setWindowIcon(icon)
            msg_error.exec_()

        def buttnon_download_report():
            self.button_download_report = self.button_download_report.sender()
            if isinstance(self.button_download_report, QtWidgets.QPushButton):

                index = self.table_wbco_report.indexAt(self.button_download_report.pos())
                row = index.row()
                col = index.column()

                #Pegar a coluna Identify Card
                col = col - 3
                
                item = self.table_wbco_report.item(row,col)
                if item is not None:
                    
                    job_ref = item.text()

                    report_cabecalho = modulo_wbco.wbcoController.carregar_info_report_cabecalho_por_job_ref(job_ref)
                    well_information = modulo_wbco.wbcoController.carregar_well_information_por_job_ref(job_ref)
                    wbco_primary = modulo_wbco.wbcoController.carregar_wbco_primary_by_job_ref(job_ref)
                    wbco_back_up = modulo_wbco.wbcoController.carregar_wbco_back_up_by_job_ref(job_ref)
                    employe = modulo_wbco.wbcoController.carregar_empregado_by_job_ref(job_ref)

                    filemane = "Daily_Report_"+str(well_information[7])+"_WBCO_Tools_Service.pdf"
                    self.gerador_report.gerar_pdf(filemane,report_cabecalho,well_information,wbco_primary,wbco_back_up,employe)
                    show_message_sucess()

                    #show_form_edit_personeel(id_card) 

        def view_report():
            self.button_view_report = self.button_view_report.sender()
            if isinstance(self.button_view_report, QtWidgets.QPushButton):

                index = self.table_wbco_report.indexAt(self.button_view_report.pos())
                row = index.row()
                col = index.column()

                #Pegar a coluna Identify Card
                col = col - 4
                
                item = self.table_wbco_report.item(row,col)
                if item is not None:
                    
                    job_ref = item.text()

                    report_cabecalho = modulo_wbco.wbcoController.carregar_info_report_cabecalho_por_job_ref(job_ref)
                    well_information = modulo_wbco.wbcoController.carregar_well_information_por_job_ref(job_ref)
                    wbco_primary = modulo_wbco.wbcoController.carregar_wbco_primary_by_job_ref(job_ref)
                    wbco_back_up = modulo_wbco.wbcoController.carregar_wbco_back_up_by_job_ref(job_ref)
                    employe = modulo_wbco.wbcoController.carregar_empregado_by_job_ref(job_ref)

                    filemane = "Daily_Report_"+str(well_information[8])+"_WBCO_Tools_Service.pdf"

                    self.gerador_report.gerar_pdf(filemane,report_cabecalho,well_information,wbco_primary,wbco_back_up,employe)

                    def show_form_dashboard():
                        self.window = QtWidgets.QMainWindow()
                        import modulo_wbco.view_report
                        self.viewer = modulo_wbco.view_report.PDFViewer(filemane)
                        self.viewer.show()
                        

                    show_form_dashboard()

                    #show_form_edit_personeel(id_card) 
            
        #def editar_report():
        #    self.button_edit_report = self.button_edit_report.sender()
        #    if isinstance(self.button_edit_report, QtWidgets.QPushButton):
        #
        #        index = self.table_wbco_report.indexAt(self.button_edit_report.pos())
        #        row = index.row()
        #        col = index.column()
        #
        #        #Pegar a coluna Identify Card
        #        col = col - 5
        #        
        #        item = self.table_wbco_report.item(row,col)
        #        if item is not None:
        #            
        #            job_ref = item.text()
        #            show_wbco_report_edit(job_ref)



        self.table_wbco_report.horizontalHeader().setDefaultSectionSize(217)
        self.table_wbco_report.horizontalHeader().setHighlightSections(False)
        self.table_wbco_report.verticalHeader().setVisible(False)
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
        self.btn_filtration.setText(_translate("MainWindow", " Filtration"))
        self.btn_tank_cleaning.setText(_translate("MainWindow", " Tank Cleaning"))
        self.btn_user_profile.setText(_translate("MainWindow", "User Profile"))
        self.btn_logout.setText(_translate("MainWindow", "Logout"))
        self.btn_logout.clicked.connect(lambda:logout())
        self.btn_user.setText(_translate("MainWindow", " Personnel"))
        self.btn_user.clicked.connect(lambda:call_form_user())
        self.btn_customer.setText(_translate("MainWindow", "Customers"))
        self.btn_customer.clicked.connect(lambda:call_form_client())
        self.label_titulo_form.setText(_translate("MainWindow", "WBCO Tools Service"))
        self.lbl_text_form.setText(_translate("MainWindow", "Below are all the reports generated in the system regarding the WBCO Tools Service"))

        self.btn_add_report.setText(_translate("MainWindow", " Add new Report"))
        self.btn_add_report.clicked.connect(lambda: show_form_add_wbco_report())

        self.btn_list_size.setText(_translate("MainWindow", "  Size"))
        self.btn_list_size.clicked.connect(lambda: show_form_list_size())

        self.btn_list_thread.setText(_translate("MainWindow"," Thread Connections"))
        self.btn_list_thread.clicked.connect(lambda:show_form_list_thread())

        self.btn_list_wbco_engineer.setText(_translate("MainWindow"," WBCO Personnel"))
        self.btn_list_wbco_engineer.clicked.connect(lambda:show_form_list_enginer())

        self.table_wbco_report.setSortingEnabled(False)

        self.btn_compliance.clicked.connect(lambda:show_form_compliance())
        self.btn_wbco.clicked.connect(lambda:call_form_wbco())
        self.btn_logout.clicked.connect(lambda: logout())
        self.btn_customer.clicked.connect(lambda: call_form_client())
        self.btn_filtration.clicked.connect(lambda:show_add_filtration())
        self.btn_tank_cleaning.clicked.connect(lambda:show_add_tank_cleaning())
        self.btn_user_profile.clicked.connect(lambda:show_perfil_user())


        def show_form_list_size():
            self.window = QtWidgets.QMainWindow()
            import modulo_wbco.size
            self.ui = modulo_wbco.size.Ui_MainWindow()
            self.ui.setupUi(self.window,self.lbl_user_logado.text())
            self.window.show()
            MainWindow.close()

        def show_form_list_thread():
            self.window = QtWidgets.QMainWindow()
            import modulo_wbco.thread
            self.ui = modulo_wbco.thread.Ui_MainWindow()
            self.ui.setupUi(self.window,self.lbl_user_logado.text())
            self.window.show()
            MainWindow.close()

        def show_form_list_enginer():
            self.window = QtWidgets.QMainWindow()
            import modulo_wbco.wbco_enginer
            self.ui = modulo_wbco.wbco_enginer.Ui_MainWindow()
            self.ui.setupUi(self.window,self.lbl_user_logado.text())
            self.window.show()
            MainWindow.close()
        
        def report():

            value_well_information = modulo_wbco.wbcoController.carregar_well_information()
            filemane = "Daily_Report_"+str(value_well_information[8])+"_WBCO_Tools_Service.pdf"
            
            
            self.gerador_report.gerar_pdf(filemane)
            #show_message_sucess()
            print("Arquivo Gerado Com Sucesso")

        def show_form_add_wbco_report():
            self.window = QtWidgets.QMainWindow()
            import modulo_wbco.wbco_report_add
            self.ui = modulo_wbco.wbco_report_add.Ui_MainWindow()
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
