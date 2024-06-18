
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtGui


def show_message_sucess():
        msg_error = QMessageBox()
        msg_error.setIcon(QMessageBox.Information)
        msg_error.setText('User added successfully')
        msg_error.setWindowTitle('Adding User')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/sucess_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg_error.setWindowIcon(icon)
        msg_error.exec_()

def show_message_user_not_allow():
        msg_error = QMessageBox()
        msg_error.setIcon(QMessageBox.Warning)
        msg_error.setText('Permission denied')
        msg_error.setWindowTitle('Permission denied')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/sucess_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg_error.setWindowIcon(icon)
        msg_error.exec_()