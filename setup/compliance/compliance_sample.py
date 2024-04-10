
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from compliance.pack_model_average import average_modelController as controller
from compliance.pack_sample_cp import sample_cpController as sample_controller
from compliance.pack_average_ooc_cp import average_oocController as average_controller
from compliance.pacote_report_information import report_informationController as controller_report

class Ui_MainWindow(object):
    def setupUi(self, MainWindow,depth_location,sample_location,sample_number,dataTeste,timeTest,model,numberOfShake,numberOfCuttings):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1050, 870)
        MainWindow.setMinimumSize(QtCore.QSize(1050, 870))
        MainWindow.setMaximumSize(QtCore.QSize(1050, 870))
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
        self.lbl_syntetic_sg = QtWidgets.QLabel(self.frame)
        self.lbl_syntetic_sg.setGeometry(QtCore.QRect(10, 100, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_syntetic_sg.setFont(font)
        self.lbl_syntetic_sg.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_syntetic_sg.setObjectName("lbl_syntetic_sg")
        self.txt_synthetic_sg = QtWidgets.QLineEdit(self.frame)
        self.txt_synthetic_sg.setGeometry(QtCore.QRect(10, 130, 321, 41))
        self.txt_synthetic_sg.setStyleSheet("QLineEdit{\n"
"\n"
"\n"
"background-color:#fff;\n"
"border: 1px solid #8ec0af;\n"
"border-radius: 6px\n"
"}")
        self.txt_synthetic_sg.setPlaceholderText("")
        self.txt_synthetic_sg.setObjectName("txt_synthetic_sg")
        self.txt_rop_at_time = QtWidgets.QLineEdit(self.frame)
        self.txt_rop_at_time.setGeometry(QtCore.QRect(340, 130, 321, 41))
        self.txt_rop_at_time.setStyleSheet("QLineEdit{\n"
"\n"
"\n"
"background-color:#fff;\n"
"border: 1px solid #8ec0af;\n"
"border-radius: 6px\n"
"}")
        self.txt_rop_at_time.setPlaceholderText("")
        self.txt_rop_at_time.setObjectName("txt_rop_at_time")
        self.lbl_rop_at_time = QtWidgets.QLabel(self.frame)
        self.lbl_rop_at_time.setGeometry(QtCore.QRect(340, 100, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_rop_at_time.setFont(font)
        self.lbl_rop_at_time.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_rop_at_time.setObjectName("lbl_rop_at_time")
        self.lbl_wercb = QtWidgets.QLabel(self.frame)
        self.lbl_wercb.setGeometry(QtCore.QRect(670, 100, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_wercb.setFont(font)
        self.lbl_wercb.setStyleSheet("color: black;")
        self.lbl_wercb.setObjectName("lbl_wercb")
        self.txt_wercb = QtWidgets.QLineEdit(self.frame)
        self.txt_wercb.setGeometry(QtCore.QRect(670, 130, 351, 41))
        self.txt_wercb.setStyleSheet("QLineEdit{\n"
        "\n"
        "\n"
        "background-color:#fff;\n"
        "border: 1px solid #8ec0af;\n"
        "border-radius: 6px\n"
        "}")
        self.txt_wercb.setPlaceholderText("")
        self.txt_wercb.setObjectName("txt_wercb")
        self.txt_wfrcbsg = QtWidgets.QLineEdit(self.frame)
        self.txt_wfrcbsg.setGeometry(QtCore.QRect(10, 210, 321, 41))
        self.txt_wfrcbsg.setStyleSheet("QLineEdit{\n"
        "\n"
        "\n"
        "background-color:#fff;\n"
        "border: 1px solid #8ec0af;\n"
        "border-radius: 6px\n"
        "}")
        self.txt_wfrcbsg.setPlaceholderText("")
        self.txt_wfrcbsg.setObjectName("txt_wfrcbsg")
        self.lbl_wfrcbsg = QtWidgets.QLabel(self.frame)
        self.lbl_wfrcbsg.setGeometry(QtCore.QRect(10, 180, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_wfrcbsg.setFont(font)
        self.lbl_wfrcbsg.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_wfrcbsg.setObjectName("lbl_wfrcbsg")
        self.txt_wfgcbswg = QtWidgets.QLineEdit(self.frame)
        self.txt_wfgcbswg.setGeometry(QtCore.QRect(340, 210, 371, 41))
        self.txt_wfgcbswg.setStyleSheet("QLineEdit{\n"
"\n"
"\n"
"background-color:#fff;\n"
"border: 1px solid #8ec0af;\n"
"border-radius: 6px\n"
"}")
        self.txt_wfgcbswg.setPlaceholderText("")
        self.txt_wfgcbswg.setObjectName("txt_wfgcbswg")
        self.lbl_wfrcbswg = QtWidgets.QLabel(self.frame)
        self.lbl_wfrcbswg.setGeometry(QtCore.QRect(340, 180, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_wfrcbswg.setFont(font)
        self.lbl_wfrcbswg.setStyleSheet("color: black;")
        self.lbl_wfrcbswg.setObjectName("lbl_wfrcbswg")
        self.txt_wgceg = QtWidgets.QLineEdit(self.frame)
        self.txt_wgceg.setGeometry(QtCore.QRect(720, 210, 301, 41))
        self.txt_wgceg.setStyleSheet("QLineEdit{\n"
"\n"
"\n"
"background-color:#fff;\n"
"border: 1px solid #8ec0af;\n"
"border-radius: 6px\n"
"}")
        self.txt_wgceg.setPlaceholderText("")
        self.txt_wgceg.setObjectName("txt_wgceg")
        self.lbl_gceg = QtWidgets.QLabel(self.frame)
        self.lbl_gceg.setGeometry(QtCore.QRect(720, 180, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_gceg.setFont(font)
        self.lbl_gceg.setStyleSheet("color: black;")
        self.lbl_gceg.setObjectName("lbl_gceg")
        self.txt_wgccg = QtWidgets.QLineEdit(self.frame)
        self.txt_wgccg.setGeometry(QtCore.QRect(10, 290, 321, 41))
        self.txt_wgccg.setStyleSheet("QLineEdit{\n"
"\n"
"\n"
"background-color:#fff;\n"
"border: 1px solid #8ec0af;\n"
"border-radius: 6px\n"
"}")
        self.txt_wgccg.setPlaceholderText("")
        self.txt_wgccg.setObjectName("txt_wgccg")
        self.txt_vwgcm = QtWidgets.QLineEdit(self.frame)
        self.txt_vwgcm.setGeometry(QtCore.QRect(340, 290, 331, 41))
        self.txt_vwgcm.setStyleSheet("QLineEdit{\n"
"\n"
"\n"
"background-color:#fff;\n"
"border: 1px solid #8ec0af;\n"
"border-radius: 6px\n"
"}")
        self.txt_vwgcm.setPlaceholderText("")
        self.txt_vwgcm.setObjectName("txt_vwgcm")
        self.txt_wrccarcg = QtWidgets.QLineEdit(self.frame)
        self.txt_wrccarcg.setGeometry(QtCore.QRect(680, 290, 341, 41))
        self.txt_wrccarcg.setStyleSheet("QLineEdit{\n"
"\n"
"\n"
"background-color:#fff;\n"
"border: 1px solid #8ec0af;\n"
"border-radius: 6px\n"
"}")
        self.txt_wrccarcg.setPlaceholderText("")
        self.txt_wrccarcg.setObjectName("txt_wrccarcg")
        self.lbl_wgccg = QtWidgets.QLabel(self.frame)
        self.lbl_wgccg.setGeometry(QtCore.QRect(10, 260, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_wgccg.setFont(font)
        self.lbl_wgccg.setStyleSheet("color: black;")
        self.lbl_wgccg.setObjectName("lbl_wgccg")
        self.lbl_vwgcm = QtWidgets.QLabel(self.frame)
        self.lbl_vwgcm.setGeometry(QtCore.QRect(340, 260, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_vwgcm.setFont(font)
        self.lbl_vwgcm.setStyleSheet("color: black;")
        self.lbl_vwgcm.setObjectName("lbl_vwgcm")
        self.lbl_wrccarcg = QtWidgets.QLabel(self.frame)
        self.lbl_wrccarcg.setGeometry(QtCore.QRect(680, 260, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_wrccarcg.setFont(font)
        self.lbl_wrccarcg.setStyleSheet("color: black;")
        self.lbl_wrccarcg.setObjectName("lbl_wrccarcg")
        self.txt_wsg = QtWidgets.QLineEdit(self.frame)
        self.txt_wsg.setGeometry(QtCore.QRect(10, 370, 211, 41))
        self.txt_wsg.setStyleSheet("QLineEdit{\n"
"\n"
"\n"
"background-color:#fff;\n"
"border: 1px solid #8ec0af;\n"
"border-radius: 6px\n"
"}")
        self.txt_wsg.setPlaceholderText("")
        self.txt_wsg.setObjectName("txt_wsg")
        self.txt_wsg.setEnabled(False)
        self.lbl_wsg = QtWidgets.QLabel(self.frame)
        self.lbl_wsg.setGeometry(QtCore.QRect(10, 340, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_wsg.setFont(font)
        self.lbl_wsg.setStyleSheet("color: red;")
        self.lbl_wsg.setObjectName("lbl_wsg")
        self.lbl_wwag = QtWidgets.QLabel(self.frame)
        self.lbl_wwag.setGeometry(QtCore.QRect(230, 340, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_wwag.setFont(font)
        self.lbl_wwag.setStyleSheet("color: red;")
        self.lbl_wwag.setObjectName("lbl_wwag")
        self.txt_wwag = QtWidgets.QLineEdit(self.frame)
        self.txt_wwag.setGeometry(QtCore.QRect(230, 370, 221, 41))
        self.txt_wwag.setStyleSheet("QLineEdit{\n"
"\n"
"\n"
"background-color:#fff;\n"
"border: 1px solid #8ec0af;\n"
"border-radius: 6px\n"
"}")
        self.txt_wwag.setPlaceholderText("")
        self.txt_wwag.setObjectName("txt_wwag")
        self.txt_wwag.setEnabled(False)
        self.btn_calculate_sample = QtWidgets.QPushButton(self.frame)
        self.btn_calculate_sample.setGeometry(QtCore.QRect(400, 770, 271, 41))
        self.btn_calculate_sample.setStyleSheet("\n"
"\n"
"QPushButton#btn_calculate_sample{\n"
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
"QPushButton#btn_calculate_sample:hover{\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_calculate_sample:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"background-color: #033029;\n"
"padding:10px;\n"
" }\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\../../../../../../img/check-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_calculate_sample.setIcon(icon1)
        self.btn_calculate_sample.setObjectName("btn_calculate_sample")
        self.txt_vsm = QtWidgets.QLineEdit(self.frame)
        self.txt_vsm.setEnabled(False)
        self.txt_vsm.setGeometry(QtCore.QRect(460, 370, 211, 41))
        self.txt_vsm.setStyleSheet("QLineEdit{\n"
"\n"
"\n"
"background-color:#fff;\n"
"border: 1px solid #8ec0af;\n"
"border-radius: 6px\n"
"}")
        self.txt_vsm.setPlaceholderText("")
        self.txt_vsm.setObjectName("txt_vsm")
        self.lbl_vsm = QtWidgets.QLabel(self.frame)
        self.lbl_vsm.setGeometry(QtCore.QRect(460, 340, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_vsm.setFont(font)
        self.lbl_vsm.setStyleSheet("color: red;")
        self.lbl_vsm.setObjectName("lbl_vsm")
        self.txt_wocg = QtWidgets.QLineEdit(self.frame)
        self.txt_wocg.setEnabled(False)
        self.txt_wocg.setGeometry(QtCore.QRect(230, 450, 221, 41))
        self.txt_wocg.setStyleSheet("QLineEdit{\n"
"\n"
"\n"
"background-color:#fff;\n"
"border: 1px solid #8ec0af;\n"
"border-radius: 6px\n"
"}")
        self.txt_wocg.setPlaceholderText("")
        self.txt_wocg.setObjectName("txt_wocg")
        self.txt_wcg = QtWidgets.QLineEdit(self.frame)
        self.txt_wcg.setEnabled(False)
        self.txt_wcg.setGeometry(QtCore.QRect(10, 450, 211, 41))
        self.txt_wcg.setStyleSheet("QLineEdit{\n"
"\n"
"\n"
"background-color:#fff;\n"
"border: 1px solid #8ec0af;\n"
"border-radius: 6px\n"
"}")
        self.txt_wcg.setPlaceholderText("")
        self.txt_wcg.setObjectName("txt_wcg")
        self.txt_dss = QtWidgets.QLineEdit(self.frame)
        self.txt_dss.setEnabled(False)
        self.txt_dss.setGeometry(QtCore.QRect(680, 370, 341, 41))
        self.txt_dss.setStyleSheet("QLineEdit{\n"
"\n"
"\n"
"background-color:#fff;\n"
"border: 1px solid #8ec0af;\n"
"border-radius: 6px\n"
"}")
        self.txt_dss.setPlaceholderText("")
        self.txt_dss.setObjectName("txt_dss")
        self.lbl_wocg = QtWidgets.QLabel(self.frame)
        self.lbl_wocg.setGeometry(QtCore.QRect(230, 420, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_wocg.setFont(font)
        self.lbl_wocg.setStyleSheet("color: red;")
        self.lbl_wocg.setObjectName("lbl_wocg")
        self.lbl_dss = QtWidgets.QLabel(self.frame)
        self.lbl_dss.setGeometry(QtCore.QRect(680, 340, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_dss.setFont(font)
        self.lbl_dss.setStyleSheet("color: red;")
        self.lbl_dss.setObjectName("lbl_dss")
        self.lbl_wcg = QtWidgets.QLabel(self.frame)
        self.lbl_wcg.setGeometry(QtCore.QRect(10, 420, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_wcg.setFont(font)
        self.lbl_wcg.setStyleSheet("color: red;")
        self.lbl_wcg.setObjectName("lbl_wcg")
        self.txt_vom = QtWidgets.QLineEdit(self.frame)
        self.txt_vom.setEnabled(False)
        self.txt_vom.setGeometry(QtCore.QRect(460, 450, 211, 41))
        self.txt_vom.setStyleSheet("QLineEdit{\n"
"\n"
"\n"
"background-color:#fff;\n"
"border: 1px solid #8ec0af;\n"
"border-radius: 6px\n"
"}")
        self.txt_vom.setPlaceholderText("")
        self.txt_vom.setObjectName("txt_vom")
        self.txt_wwsg = QtWidgets.QLineEdit(self.frame)
        self.txt_wwsg.setEnabled(False)
        self.txt_wwsg.setGeometry(QtCore.QRect(680, 450, 341, 41))
        self.txt_wwsg.setStyleSheet("QLineEdit{\n"
"\n"
"\n"
"background-color:#fff;\n"
"border: 1px solid #8ec0af;\n"
"border-radius: 6px\n"
"}")
        self.txt_wwsg.setPlaceholderText("")
        self.txt_wwsg.setObjectName("txt_wwsg")
        self.txt_wdscg = QtWidgets.QLineEdit(self.frame)
        self.txt_wdscg.setEnabled(False)
        self.txt_wdscg.setGeometry(QtCore.QRect(680, 530, 341, 41))
        self.txt_wdscg.setStyleSheet("QLineEdit{\n"
"\n"
"\n"
"background-color:#fff;\n"
"border: 1px solid #8ec0af;\n"
"border-radius: 6px\n"
"}")
        self.txt_wdscg.setPlaceholderText("")
        self.txt_wdscg.setObjectName("txt_wdscg")
        self.lbl_obv = QtWidgets.QLabel(self.frame)
        self.lbl_obv.setGeometry(QtCore.QRect(230, 500, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_obv.setFont(font)
        self.lbl_obv.setStyleSheet("color: red;")
        self.lbl_obv.setObjectName("lbl_obv")
        self.lbl_wdscg = QtWidgets.QLabel(self.frame)
        self.lbl_wdscg.setGeometry(QtCore.QRect(680, 500, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_wdscg.setFont(font)
        self.lbl_wdscg.setStyleSheet("color: red;")
        self.lbl_wdscg.setObjectName("lbl_wdscg")
        self.txt_wbv = QtWidgets.QLineEdit(self.frame)
        self.txt_wbv.setEnabled(False)
        self.txt_wbv.setGeometry(QtCore.QRect(460, 530, 211, 41))
        self.txt_wbv.setStyleSheet("QLineEdit{\n"
"\n"
"\n"
"background-color:#fff;\n"
"border: 1px solid #8ec0af;\n"
"border-radius: 6px\n"
"}")
        self.txt_wbv.setPlaceholderText("")
        self.txt_wbv.setObjectName("txt_wbv")
        self.lbl_wbv = QtWidgets.QLabel(self.frame)
        self.lbl_wbv.setGeometry(QtCore.QRect(460, 500, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_wbv.setFont(font)
        self.lbl_wbv.setStyleSheet("color: red;")
        self.lbl_wbv.setObjectName("lbl_wbv")
        self.txt_obv = QtWidgets.QLineEdit(self.frame)
        self.txt_obv.setEnabled(False)
        self.txt_obv.setGeometry(QtCore.QRect(230, 530, 221, 41))
        self.txt_obv.setStyleSheet("QLineEdit{\n"
"\n"
"\n"
"background-color:#fff;\n"
"border: 1px solid #8ec0af;\n"
"border-radius: 6px\n"
"}")
        self.txt_obv.setPlaceholderText("")
        self.txt_obv.setObjectName("txt_obv")
        self.lbl_vom = QtWidgets.QLabel(self.frame)
        self.lbl_vom.setGeometry(QtCore.QRect(460, 420, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_vom.setFont(font)
        self.lbl_vom.setStyleSheet("color: red;")
        self.lbl_vom.setObjectName("lbl_vom")
        self.lbl_wdsag = QtWidgets.QLabel(self.frame)
        self.lbl_wdsag.setGeometry(QtCore.QRect(10, 500, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_wdsag.setFont(font)
        self.lbl_wdsag.setStyleSheet("color: red;")
        self.lbl_wdsag.setObjectName("lbl_wdsag")
        self.lbl_wwsg = QtWidgets.QLabel(self.frame)
        self.lbl_wwsg.setGeometry(QtCore.QRect(680, 420, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_wwsg.setFont(font)
        self.lbl_wwsg.setStyleSheet("color: red;")
        self.lbl_wwsg.setObjectName("lbl_wwsg")
        self.txt_wdsag = QtWidgets.QLineEdit(self.frame)
        self.txt_wdsag.setEnabled(False)
        self.txt_wdsag.setGeometry(QtCore.QRect(10, 530, 211, 41))
        self.txt_wdsag.setStyleSheet("QLineEdit{\n"
"\n"
"\n"
"background-color:#fff;\n"
"border: 1px solid #8ec0af;\n"
"border-radius: 6px\n"
"}")
        self.txt_wdsag.setPlaceholderText("")
        self.txt_wdsag.setObjectName("txt_wdsag")
        self.lbl_sbv = QtWidgets.QLabel(self.frame)
        self.lbl_sbv.setGeometry(QtCore.QRect(10, 580, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_sbv.setFont(font)
        self.lbl_sbv.setStyleSheet("color: red;")
        self.lbl_sbv.setObjectName("lbl_sbv")
        self.txt_sbv = QtWidgets.QLineEdit(self.frame)
        self.txt_sbv.setEnabled(False)
        self.txt_sbv.setGeometry(QtCore.QRect(10, 610, 211, 41))
        self.txt_sbv.setStyleSheet("QLineEdit{\n"
"\n"
"\n"
"background-color:#fff;\n"
"border: 1px solid #8ec0af;\n"
"border-radius: 6px\n"
"}")
        self.txt_sbv.setPlaceholderText("")
        self.txt_sbv.setObjectName("txt_sbv")
        self.txt_obw = QtWidgets.QLineEdit(self.frame)
        self.txt_obw.setEnabled(False)
        self.txt_obw.setGeometry(QtCore.QRect(230, 610, 221, 41))
        self.txt_obw.setStyleSheet("QLineEdit{\n"
"\n"
"\n"
"background-color:#fff;\n"
"border: 1px solid #8ec0af;\n"
"border-radius: 6px\n"
"}")
        self.txt_obw.setPlaceholderText("")
        self.txt_obw.setObjectName("txt_obw")
        self.lbl_obw = QtWidgets.QLabel(self.frame)
        self.lbl_obw.setGeometry(QtCore.QRect(230, 580, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_obw.setFont(font)
        self.lbl_obw.setStyleSheet("color: red;")
        self.lbl_obw.setObjectName("lbl_obw")
        self.txt_wbw = QtWidgets.QLineEdit(self.frame)
        self.txt_wbw.setEnabled(False)
        self.txt_wbw.setGeometry(QtCore.QRect(460, 610, 211, 41))
        self.txt_wbw.setStyleSheet("QLineEdit{\n"
"\n"
"\n"
"background-color:#fff;\n"
"border: 1px solid #8ec0af;\n"
"border-radius: 6px\n"
"}")
        self.txt_wbw.setPlaceholderText("")
        self.txt_wbw.setObjectName("txt_wbw")
        self.lbl_wbw = QtWidgets.QLabel(self.frame)
        self.lbl_wbw.setGeometry(QtCore.QRect(460, 580, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_wbw.setFont(font)
        self.lbl_wbw.setStyleSheet("color: red;")
        self.lbl_wbw.setObjectName("lbl_wbw")
        self.lbl_sbw = QtWidgets.QLabel(self.frame)
        self.lbl_sbw.setGeometry(QtCore.QRect(680, 580, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_sbw.setFont(font)
        self.lbl_sbw.setStyleSheet("color: red;")
        self.lbl_sbw.setObjectName("lbl_sbw")
        self.txt_sbw = QtWidgets.QLineEdit(self.frame)
        self.txt_sbw.setEnabled(False)
        self.txt_sbw.setGeometry(QtCore.QRect(680, 610, 341, 41))
        self.txt_sbw.setStyleSheet("QLineEdit{\n"
"\n"
"\n"
"background-color:#fff;\n"
"border: 1px solid #8ec0af;\n"
"border-radius: 6px\n"
"}")
        self.txt_sbw.setPlaceholderText("")
        self.txt_sbw.setObjectName("txt_sbw")
        self.txt_wowcg = QtWidgets.QLineEdit(self.frame)
        self.txt_wowcg.setEnabled(False)
        self.txt_wowcg.setGeometry(QtCore.QRect(350, 690, 321, 41))
        self.txt_wowcg.setStyleSheet("QLineEdit{\n"
"\n"
"\n"
"background-color:#fff;\n"
"border: 1px solid #8ec0af;\n"
"border-radius: 6px\n"
"}")
        self.txt_wowcg.setPlaceholderText("")
        self.txt_wowcg.setObjectName("txt_wowcg")
        self.lbl_wsdcg = QtWidgets.QLabel(self.frame)
        self.lbl_wsdcg.setGeometry(QtCore.QRect(10, 660, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_wsdcg.setFont(font)
        self.lbl_wsdcg.setStyleSheet("color: red;")
        self.lbl_wsdcg.setObjectName("lbl_wsdcg")
        self.txt_wsdcg = QtWidgets.QLineEdit(self.frame)
        self.txt_wsdcg.setEnabled(False)
        self.txt_wsdcg.setGeometry(QtCore.QRect(10, 690, 321, 41))
        self.txt_wsdcg.setStyleSheet("QLineEdit{\n"
"\n"
"\n"
"background-color:#fff;\n"
"border: 1px solid #8ec0af;\n"
"border-radius: 6px\n"
"}")
        self.txt_wsdcg.setPlaceholderText("")
        self.txt_wsdcg.setObjectName("txt_wsdcg")
        self.lbl_wowc = QtWidgets.QLabel(self.frame)
        self.lbl_wowc.setGeometry(QtCore.QRect(350, 660, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_wowc.setFont(font)
        self.lbl_wowc.setStyleSheet("color: red;")
        self.lbl_wowc.setObjectName("lbl_wowc")
        self.txt_mwp = QtWidgets.QLineEdit(self.frame)
        self.txt_mwp.setEnabled(False)
        self.txt_mwp.setGeometry(QtCore.QRect(690, 690, 331, 41))
        self.txt_mwp.setStyleSheet("QLineEdit{\n"
"\n"
"\n"
"background-color:#fff;\n"
"border: 1px solid #8ec0af;\n"
"border-radius: 6px\n"
"}")
        self.txt_mwp.setPlaceholderText("")
        self.txt_mwp.setObjectName("txt_mwp")
        self.lbl_mwp = QtWidgets.QLabel(self.frame)
        self.lbl_mwp.setGeometry(QtCore.QRect(690, 660, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_mwp.setFont(font)
        self.lbl_mwp.setStyleSheet("color: red;")
        self.lbl_mwp.setObjectName("lbl_mwp")
        self.lbl_ac = QtWidgets.QLabel(self.frame)
        self.lbl_ac.setGeometry(QtCore.QRect(10, 740, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_ac.setFont(font)
        self.lbl_ac.setStyleSheet("color: red;")
        self.lbl_ac.setObjectName("lbl_ac")
        self.txt_ac = QtWidgets.QLineEdit(self.frame)
        self.txt_ac.setEnabled(False)
        self.txt_ac.setGeometry(QtCore.QRect(10, 770, 381, 41))
        self.txt_ac.setStyleSheet("QLineEdit{\n"
"\n"
"\n"
"background-color:#fff;\n"
"border: 1px solid #8ec0af;\n"
"border-radius: 6px\n"
"}")
        self.txt_ac.setPlaceholderText("")
        self.txt_ac.setObjectName("txt_ac")
        self.btn_add_sample = QtWidgets.QPushButton(self.frame)
        self.btn_add_sample.setGeometry(QtCore.QRect(690, 770, 331, 41))
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
        self.btn_add_sample.setIcon(icon1)
        self.btn_add_sample.setObjectName("btn_add_sample")
        self.lbl_mwp.raise_()
        self.lbl_wowc.raise_()
        self.lbl_wbw.raise_()
        self.lbl_obw.raise_()
        self.lbl_obv.raise_()
        self.lbl_wbv.raise_()
        self.lbl_vom.raise_()
        self.lbl_wdsag.raise_()
        self.lbl_wwsg.raise_()
        self.lbl_wdscg.raise_()
        self.lbl_wocg.raise_()
        self.lbl_wcg.raise_()
        self.lbl_dss.raise_()
        self.lbl_vsm.raise_()
        self.lbl_wsg.raise_()
        self.lbl_wrccarcg.raise_()
        self.lbl_vwgcm.raise_()
        self.lbl_wgccg.raise_()
        self.lbl_gceg.raise_()
        self.lbl_wfrcbswg.raise_()
        self.lbl_wfrcbsg.raise_()
        self.lbl_wercb.raise_()
        self.lbl_rop_at_time.raise_()
        self.frame_2.raise_()
        self.frame_3.raise_()
        self.frame_9.raise_()
        self.line_2.raise_()
        self.lbl_syntetic_sg.raise_()
        self.txt_synthetic_sg.raise_()
        self.txt_rop_at_time.raise_()
        self.txt_wercb.raise_()
        self.txt_wfrcbsg.raise_()
        self.txt_wfgcbswg.raise_()
        self.txt_wgceg.raise_()
        self.txt_wgccg.raise_()
        self.txt_vwgcm.raise_()
        self.txt_wrccarcg.raise_()
        self.txt_wsg.raise_()
        self.lbl_wwag.raise_()
        self.txt_wwag.raise_()
        self.btn_calculate_sample.raise_()
        self.txt_vsm.raise_()
        self.txt_wocg.raise_()
        self.txt_wcg.raise_()
        self.txt_dss.raise_()
        self.txt_vom.raise_()
        self.txt_wwsg.raise_()
        self.txt_wdscg.raise_()
        self.txt_wbv.raise_()
        self.txt_obv.raise_()
        self.txt_wdsag.raise_()
        self.lbl_sbv.raise_()
        self.txt_sbv.raise_()
        self.txt_obw.raise_()
        self.txt_wbw.raise_()
        self.lbl_sbw.raise_()
        self.txt_sbw.raise_()
        self.txt_wowcg.raise_()
        self.lbl_wsdcg.raise_()
        self.txt_wsdcg.raise_()
        self.txt_mwp.raise_()
        self.lbl_ac.raise_()
        self.txt_ac.raise_()
        self.btn_add_sample.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1050, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow,depth_location,sample_location,sample_number,dataTeste,timeTest,model,numberOfShake,numberOfCuttings)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
            

    def retranslateUi(self, MainWindow,depth_location,sample_location,sample_number,dataTeste,timeTest,model,numberOfShake,numberOfCuttings):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dashboard"))
        self.lbl_form_tittle.setText(_translate("MainWindow", "Samples"))
        self.lbl_form_text.setText(_translate("MainWindow", "Fill in the fields to obtain the sample results"))
        self.lbl_syntetic_sg.setText(_translate("MainWindow", "Synthetic SG"))
        self.lbl_rop_at_time.setText(_translate("MainWindow", "ROP At Time Of Sample"))
        self.lbl_wercb.setText(_translate("MainWindow", "Weight Empty Retort Cell + Body"))
        self.lbl_wfrcbsg.setText(_translate("MainWindow", "Weight Filled Retort Cell + Body + Sample gms"))
        self.lbl_wfrcbswg.setText(_translate("MainWindow", "Weight Filled Retort Cell + Body + Sample + water gms"))
        self.lbl_gceg.setText(_translate("MainWindow", "Weight Graduated Cylinder - Empty gms"))
        self.lbl_wgccg.setText(_translate("MainWindow", "Weight Graduated Cylinder + Condensate gms"))
        self.lbl_vwgcm.setText(_translate("MainWindow", "Volume of Water in graduated cylinder mls"))
        self.lbl_wrccarcg.setText(_translate("MainWindow", "Weight Retort Cell complete after retort cooled gms"))
        self.lbl_wsg.setText(_translate("MainWindow", "Weight of Sample gms"))
        self.lbl_wwag.setText(_translate("MainWindow", "Weight of water added gms"))
        self.btn_calculate_sample.setText(_translate("MainWindow", "Generate sample results"))
        self.btn_calculate_sample.clicked.connect(lambda:calculate_weigth_of_sample_gms())
        self.btn_calculate_sample.clicked.connect(lambda:calcultae_weight_of_water_added_gms())
        self.btn_calculate_sample.clicked.connect(lambda:calcultae_volume_of_sample())
        self.btn_calculate_sample.clicked.connect(lambda:calculate_density_sample_sg())
        self.btn_calculate_sample.clicked.connect(lambda:calculate_weight_condensate_gms())
        self.btn_calculate_sample.clicked.connect(lambda:calculate_weigth_oil())
        self.btn_calculate_sample.clicked.connect(lambda:calcultae_vol_oil_mls())
        self.btn_calculate_sample.clicked.connect(lambda:calculate_weigth_wather_in_sample())
        self.btn_calculate_sample.clicked.connect(lambda:calculate_weigth_dry_solid())
        self.btn_calculate_sample.clicked.connect(lambda:calculate_weigth_dry_solid_actual())
        self.btn_calculate_sample.clicked.connect(lambda:calcultae_oil_by_volume())
        self.btn_calculate_sample.clicked.connect(lambda:calcultae_wather_by_volume())
        self.btn_calculate_sample.clicked.connect(lambda:calcultae_solid_by_volume())
        self.btn_calculate_sample.clicked.connect(lambda:calculate_oil_by_weight())
        self.btn_calculate_sample.clicked.connect(lambda:calculate_water_by_weight())
        self.btn_calculate_sample.clicked.connect(lambda:calculate_solid_by_weigth())
        self.btn_calculate_sample.clicked.connect(lambda:calculate_soc_weigth_synt_dry_cutting())
        self.btn_calculate_sample.clicked.connect(lambda:calculate_occ_weigth_wet_cutting())
        self.btn_calculate_sample.clicked.connect(lambda:calcultae_mud())
        self.btn_calculate_sample.clicked.connect(lambda:calculate_accurency())
        self.lbl_vsm.setText(_translate("MainWindow", "Volume of Sample mls"))
        self.lbl_wocg.setText(_translate("MainWindow", "Weight Oil - calc gms"))
        self.lbl_dss.setText(_translate("MainWindow", "Density Sample SG"))
        self.lbl_wcg.setText(_translate("MainWindow", "Weight Condensate gms"))
        self.lbl_obv.setText(_translate("MainWindow", "% Oil by volume"))
        self.lbl_wdscg.setText(_translate("MainWindow", "Weight Dry Solids - calculated gms"))
        self.lbl_wbv.setText(_translate("MainWindow", "% Water by volume "))
        self.lbl_vom.setText(_translate("MainWindow", "VOL Oil mls"))
        self.lbl_wdsag.setText(_translate("MainWindow", "Weight Dry Solids - actual gms"))
        self.lbl_wwsg.setText(_translate("MainWindow", "Weight Water In Sample gms"))
        self.lbl_sbv.setText(_translate("MainWindow", "% Solids by volume"))
        self.lbl_obw.setText(_translate("MainWindow", "% Oil by weight"))
        self.lbl_wbw.setText(_translate("MainWindow", "% Water by weight "))
        self.lbl_sbw.setText(_translate("MainWindow", "% Solids by weight"))
        self.lbl_wsdcg.setText(_translate("MainWindow", "SOC, Weight of Synthetic on Dry Cuttings gms/kg"))
        self.lbl_wowc.setText(_translate("MainWindow", "OOC, Weight of Oil on Wet Cuttings gms/kg"))
        self.lbl_mwp.setText(_translate("MainWindow", "Mud Weight PPG  "))
        self.lbl_ac.setText(_translate("MainWindow", "Accuracy check ( If outside 95 to 105 range re-run retort)"))
        self.btn_add_sample.setText(_translate("MainWindow", " Add Sample"))
        self.btn_add_sample.clicked.connect(lambda:save_sample())

        

        def error_message(title,message):
             msg = QMessageBox()
             msg.setIcon(QMessageBox.Critical)
             msg.setText(title)
             msg.setInformativeText(str(message))
             msg.setWindowTitle("Error")
             msg.exec_()

        def success_message(title,message):
             msg = QMessageBox()
             msg.setIcon(QMessageBox.Information)
             msg.setText(title)
             msg.setInformativeText(str(message))
             msg.setWindowTitle("Error")
             msg.exec_()

        def calculate_weigth_of_sample_gms():
            try:
                wercb = float(self.txt_wercb.text())
                wfrcbsg = float(self.txt_wfrcbsg.text())
                result_weight_sample = round(wfrcbsg - wercb,2)
                self.txt_wsg.setText(str(result_weight_sample))
            except Exception as e:
               error_message("Error adding Weight of Sample gms ",e)

        def calcultae_weight_of_water_added_gms():
           try:
                wfrcbswg = float(self.txt_wfgcbswg.text())
                wfrcbsg = float(self.txt_wfrcbsg.text())
                result = wfrcbswg - wfrcbsg
                self.txt_wwag.setText(str(result))
           except Exception as e:
               error_message("Error adding Weight of water added gms",e)

        def calcultae_volume_of_sample():
            try:
                wwag = float(self.txt_wwag.text())
                result = 50 - wwag
                self.txt_vsm.setText(str(result))
            except Exception as e:
               error_message("Error adding Volume of Sample mls",e)

        def calculate_density_sample_sg():
            try:
                wsg = float(self.txt_wsg.text())
                vsm = float(self.txt_vsm.text())
                result = wsg/vsm
                self.txt_dss.setText(str(result))
            except (ValueError,TypeError) as e:
                error_message("Error adding Density Sample SG",e)

        def calculate_weight_condensate_gms():
            try:
                wgccg = float(self.txt_wgccg.text())
                wgceg = float(self.txt_wgceg.text())
                wwag = float(self.txt_wwag.text())
                result = wgccg - wgceg - wwag
                self.txt_wcg.setText(str(result))
            except Exception as e:
                error_message("Error adding Weight Condensate gms",e)

        def calculate_weigth_oil():
            try:
                wgccg = float(self.txt_wgccg.text())
                wgceg = float(self.txt_wgceg.text())
                vwgcm = float(self.txt_vwgcm.text())
                result = round(wgccg - wgceg - vwgcm,2)
                self.txt_wocg.setText(str(result))
            except Exception as e:
                error_message("Error adding Weight Oil - calc gms",e)

        def calcultae_vol_oil_mls():
             try:
                wfrcbsg = float(self.txt_wfrcbsg.text())
                wocg = float(self.txt_wocg.text())
                syntentic_sg = float(self.txt_synthetic_sg.text())

                if wfrcbsg == 0:
                        self.txt_vom.setText(str("0"))
                else:
                        result = wocg / syntentic_sg
                        result_str = "{:.2f}".format(result)
                        self.txt_vom.setText(str(result_str))
             except Exception as e:
                error_message("Error adding VOL Oil mls",e)

        def calculate_weigth_wather_in_sample():
            try:
                vwgcm = float(self.txt_vwgcm.text())
                wwag = float(self.txt_wwag.text())
                result = vwgcm - wwag
                self.txt_wwsg.setText(str(result))
            except (ValueError,TypeError) as e:
                error_message("Error adding Weight Water In Sample gms",e) 

        def calculate_weigth_dry_solid():
            try:
               wsg = float(self.txt_wsg.text())     
               wwsg = float(self.txt_wwsg.text())
               vwgcm = float(self.txt_wocg.text())
               result = wsg - wwsg - vwgcm
               self.txt_wdscg.setText(str(result))
            except (ValueError,TypeError) as e:
                error_message(" Error adding Weight Dry Solids - calculated gms",e)

        def calculate_weigth_dry_solid_actual():
            try:
                wrccarcg = float(self.txt_wrccarcg.text())
                wercb = float(self.txt_wercb.text())
                result = wrccarcg - wercb
                self.txt_wdsag.setText(str(result))
            except (ValueError,TypeError) as e:
                error_message(" Error adding Weight Dry Solids - actual gms",e)

        def calcultae_oil_by_volume():
            try:
                vom = float(self.txt_vom.text())
                vsm = float(self.txt_vsm.text())
                result = (vom/vsm)*100
                result_str = "{:.2f}".format(result)
                self.txt_obv.setText(str(result_str))
            except Exception as e:
                error_message(" Error adding % Oil by volume ",e)

        def calcultae_wather_by_volume():
            try:
                wwsg = float(self.txt_wwsg.text())
                vsm = float(self.txt_vsm.text())
                result = (wwsg/vsm)*100
                result_str = "{:.2f}".format(result)
                self.txt_wbv.setText(str(result_str))
            except Exception as e:
                error_message("Error adding % Water by volume ",e)

        def calcultae_solid_by_volume():
             try:
                wercb = float(self.txt_wercb.text())
                obv = float(self.txt_obv.text())
                wbv = float(self.txt_wbv.text())

                if wercb == 0:
                        self.txt_sbv.setText(str("0"))
                else:
                        result = 100 - obv - wbv
                        result_str = "{:.2f}".format(result)
                        self.txt_sbv.setText(str(result_str))
             except Exception as e:
                error_message("Error adding % Solids by volume  ",e)

        def calculate_oil_by_weight():
             try:
                wdscg = float(self.txt_wdscg.text())
                wocg = float(self.txt_wocg.text())
                wsg = float(self.txt_wsg.text())

                if wdscg == 0:
                        self.txt_obw.setText(str("0"))
                else:
                        result = (wocg * 100)/wsg
                        result_str = "{:.2f}".format(result)
                        self.txt_obw.setText(str(result_str))
             except Exception as e:
                error_message("Error adding % Oil by weight",e)

        def calculate_water_by_weight():
             try:
                wdscg = float(self.txt_wdscg.text())
                wwsg = float(self.txt_wwsg.text())
                wsg = float(self.txt_wsg.text())

                if wdscg == 0:
                        self.txt_wbw.setText(str("0"))
                else:
                        result = (wwsg * 100)/wsg
                        result_str = "{:.2f}".format(result)
                        self.txt_wbw.setText(str(result_str))
             except Exception as e:
                error_message("Error adding % Water by weight",e)

        def calculate_solid_by_weigth():
             try:
                wdscg = float(self.txt_wdscg.text())
                obw = float(self.txt_obw.text())
                wbw = float(self.txt_wbw.text())

                if wdscg == 0:
                        self.txt_sbw.setText(str("0"))
                else:
                        result = 100 - obw - wbw
                        result_str = "{:.2f}".format(result)
                        self.txt_sbw.setText(str(result_str))
             except Exception as e:
                error_message("Error adding % Solids by weight",e)


        def calculate_soc_weigth_synt_dry_cutting():
             try:
                wdscg = float(self.txt_wdscg.text())
                wocg = float(self.txt_wocg.text())
                wdsag = float(self.txt_wdsag.text())

                if wdscg == 0:
                        self.txt_wsdcg.setText(str("0"))
                else:
                        result = (wocg/wdsag)*1000
                        result_str = "{:.2f}".format(result)
                        self.txt_wsdcg.setText(str(result_str))
             except Exception as e:
                error_message(" Error adding SOC, Weight of Synthetic on Dry Cuttings gms/kg",e)

        def calculate_occ_weigth_wet_cutting():
             try:
                wsg = float(self.txt_wsg.text())
                wocg = float(self.txt_wocg.text())

                if wsg == 0:
                        self.txt_wowcg.setText(str("0"))
                else:
                        result = (wocg/wsg)*1000
                        result_str = "{:.2f}".format(result)
                        self.txt_wowcg.setText(str(result_str))
             except Exception as e:
                error_message("Error adding OOC, Weight of Oil on Wet Cuttings gms/kg",e)

        def calcultae_mud():
            try:
                dss = float(self.txt_dss.text())
                
                result = dss * 8.34
                result_str = "{:.2f}".format(result)
                self.txt_mwp.setText(str(result_str))
            except Exception as e:
                error_message("Error adding Mud Weight PPG  ",e)

        def calculate_accurency():
             try:
                wsg = float(self.txt_wsg.text())
                wcg = float(self.txt_wcg.text())
                wwag = float(self.txt_wwag.text())
                syntentic = float(self.txt_synthetic_sg.text())
                wdsag = float(self.txt_wdsag.text())
                wrccarcg = float(self.txt_wrccarcg.text())

                if wrccarcg == 0:
                        self.txt_ac.setText(str("0"))
                else:
                        result = ((wcg - (wwag * syntentic) + wdsag) / wsg) * 100
                        result_str = "{:.2f}".format(result)
                        self.txt_ac.setText(str(result_str))
             except (TypeError,ValueError,ZeroDivisionError) as e:
                error_message("Error Check Accuracy",e)

        id_model = controller.return_id_by_name(model)
        if id_model is None:
             error_message("Error to Select Model","Model was not selected")
        else:
             pass

        def save_sample():
             syntenct_sg = self.txt_synthetic_sg.text()
             rop_at_time = self.txt_rop_at_time.text()
             weight_empty = self.txt_wercb.text()
             weight_filled_body_sample = self.txt_wfrcbsg.text()
             weight_filled_body_sample_water = self.txt_wfgcbswg.text()
             weight_graduated_cyinder = self.txt_wgceg.text()
             weight_graduated_cyinder_condensate = self.txt_wgccg.text()
             volume_of_water_in_graduate = self.txt_vwgcm.text()
             weight_retort_cell = self.txt_wrccarcg.text()
             weight_of_sample = self.txt_wsg.text()
             weight_of_water = self.txt_wwag.text()
             volume_of_sample = self.txt_vsm.text()
             weight_oil = self.txt_wocg.text()
             weight_condensate_gms = self.txt_wcg.text()
             density_sample_sg = self.txt_dss.text()
             vol_oil = self.txt_vom.text()
             weigth_water = self.txt_wwsg.text()
             weight_dry_solids_calculated = self.txt_wdscg.text()
             perc_water_by_volume = self.txt_wbv.text()
             perc_oil_by_volume = self.txt_obv.text()
             weight_dry_solids_actual = self.txt_wdsag.text()
             perc_solids_by_volume = self.txt_sbv.text()
             perc_oil_by_weight = self.txt_obw.text()
             perc_water_by_weight = self.txt_wbw.text()    
             perc_solids_by_weight = self.txt_sbw.text()
             ooc = self.txt_wowcg.text()
             soc = self.txt_wsdcg.text()
             mud_weight = self.txt_mwp.text()
             acuracy_check = self.txt_ac.text()

             try:
                save_sample = sample_controller.cadastrar(syntenct_sg,rop_at_time,
                weight_empty,weight_filled_body_sample,weight_filled_body_sample_water,
                weight_graduated_cyinder,weight_graduated_cyinder_condensate,
                volume_of_water_in_graduate,weight_retort_cell,weight_of_sample,weight_of_water,volume_of_sample,
                weight_oil,weight_condensate_gms,density_sample_sg,vol_oil,weigth_water,
                weight_dry_solids_calculated,perc_water_by_volume,perc_oil_by_volume,weight_dry_solids_actual,
                perc_solids_by_volume,perc_oil_by_weight,perc_water_by_weight,perc_solids_by_weight,ooc,soc,mud_weight,acuracy_check)

                id_report = controller_report.buscar_id_ultimo_report()

                save_average = average_controller.cadastrar_average(id_model,depth_location,sample_number,
                dataTeste,timeTest,numberOfShake,numberOfCuttings,sample_location,
                weight_dry_solids_calculated,ooc,weight_of_sample,acuracy_check,weight_oil,weight_dry_solids_actual,id_report)

                print(id_report)

                if save_sample != 0:
                        error_message("Adding Sample",save_sample)
                else:
                        success_message(" Adding Success","Data Add Sucessful")
             except Exception as e:
                error_message("Addinf Sample",e)

                




    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
