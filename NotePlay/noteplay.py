from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from mido import MidiFile
import keyboard
import os


class Ui_MainWindow(object):
    # Вікно програми (створено за допомогою QT Designer)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 360)
        MainWindow.setStyleSheet("background-color: rgb(192, 147, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_file = QtWidgets.QFrame(self.centralwidget)
        self.frame_file.setGeometry(QtCore.QRect(10, 10, 285, 140))
        self.frame_file.setStyleSheet("background-color: rgb(219, 193, 255);\n"
                                      "border-radius: 10px;")
        self.frame_file.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_file.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_file.setObjectName("frame_file")
        self.label_file = QtWidgets.QLabel(self.frame_file)
        self.label_file.setGeometry(QtCore.QRect(0, 0, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_file.setFont(font)
        self.label_file.setAlignment(QtCore.Qt.AlignCenter)
        self.label_file.setWordWrap(False)
        self.label_file.setObjectName("label_file")
        self.btn_file = QtWidgets.QPushButton(self.frame_file)
        self.btn_file.setGeometry(QtCore.QRect(20, 60, 245, 50))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.btn_file.setFont(font)
        self.btn_file.setStyleSheet("QPushButton {\n"
                                    "    background-color: rgb(225, 210, 255);\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                    "     background-color:  rgb(235, 220, 255);\n"
                                    "}\n"
                                    "QPushButton:pressed {\n"
                                    "    background-color: rgb(192, 147, 255);\n"
                                    "}\n"
                                    "")
        self.btn_file.setObjectName("btn_file")
        self.btn_file_help = QtWidgets.QPushButton(self.frame_file)
        self.btn_file_help.setGeometry(QtCore.QRect(10, 10, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.btn_file_help.setFont(font)
        self.btn_file_help.setStyleSheet("QPushButton {\n"
                                         "    background-color: rgb(225, 210, 255);\n"
                                         "    border-radius: 15px;\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "     background-color:  rgb(235, 220, 255);\n"
                                         "}\n"
                                         "QPushButton:pressed {\n"
                                         "    background-color: rgb(192, 147, 255);\n"
                                         "}\n"
                                         "")
        self.btn_file_help.setObjectName("btn_file_help")
        self.frame_note = QtWidgets.QFrame(self.centralwidget)
        self.frame_note.setGeometry(QtCore.QRect(10, 160, 580, 190))
        self.frame_note.setStyleSheet("background-color: rgb(219, 193, 255);\n"
                                      "border-radius: 10px;")
        self.frame_note.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_note.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_note.setObjectName("frame_note")
        self.label_note = QtWidgets.QLabel(self.frame_note)
        self.label_note.setGeometry(QtCore.QRect(0, 0, 580, 50))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_note.setFont(font)
        self.label_note.setAlignment(QtCore.Qt.AlignCenter)
        self.label_note.setWordWrap(False)
        self.label_note.setObjectName("label_note")
        self.btn_note_help = QtWidgets.QPushButton(self.frame_note)
        self.btn_note_help.setGeometry(QtCore.QRect(10, 10, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.btn_note_help.setFont(font)
        self.btn_note_help.setStyleSheet("QPushButton {\n"
                                         "    background-color: rgb(225, 210, 255);\n"
                                         "    border-radius: 15px;\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "     background-color:  rgb(235, 220, 255);\n"
                                         "}\n"
                                         "QPushButton:pressed {\n"
                                         "    background-color: rgb(192, 147, 255);\n"
                                         "}\n"
                                         "")
        self.btn_note_help.setObjectName("btn_note_help")
        self.frame_note_item_0 = QtWidgets.QFrame(self.frame_note)
        self.frame_note_item_0.setGeometry(QtCore.QRect(33, 57, 40, 60))
        self.frame_note_item_0.setStyleSheet("background-color: rgb(168, 94, 155);\n"
                                             "border-radius: 10px;")
        self.frame_note_item_0.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_note_item_0.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_note_item_0.setObjectName("frame_note_item_0")
        self.label_note_0 = QtWidgets.QLabel(self.frame_note_item_0)
        self.label_note_0.setGeometry(QtCore.QRect(0, 0, 40, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_note_0.setFont(font)
        self.label_note_0.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_note_0.setScaledContents(False)
        self.label_note_0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_note_0.setWordWrap(False)
        self.label_note_0.setObjectName("label_note_0")
        self.btn_note_0 = QtWidgets.QPushButton(self.frame_note_item_0)
        self.btn_note_0.setGeometry(QtCore.QRect(3, 27, 34, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        self.btn_note_0.setFont(font)
        self.btn_note_0.setStyleSheet("QPushButton {\n"
                                      "    background-color: rgb(225, 210, 255);\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "     background-color:  rgb(235, 220, 255);\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color: rgb(219, 193, 255);\n"
                                      "}\n"
                                      "")
        self.btn_note_0.setObjectName("btn_note_0")
        self.frame_note_item_1 = QtWidgets.QFrame(self.frame_note)
        self.frame_note_item_1.setGeometry(QtCore.QRect(76, 57, 40, 60))
        self.frame_note_item_1.setStyleSheet("background-color: rgb(167, 94, 136);\n"
                                             "border-radius: 10px;")
        self.frame_note_item_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_note_item_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_note_item_1.setObjectName("frame_note_item_1")
        self.label_note_1 = QtWidgets.QLabel(self.frame_note_item_1)
        self.label_note_1.setGeometry(QtCore.QRect(0, 0, 40, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_note_1.setFont(font)
        self.label_note_1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_note_1.setScaledContents(False)
        self.label_note_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_note_1.setWordWrap(False)
        self.label_note_1.setObjectName("label_note_1")
        self.btn_note_1 = QtWidgets.QPushButton(self.frame_note_item_1)
        self.btn_note_1.setGeometry(QtCore.QRect(3, 27, 34, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        self.btn_note_1.setFont(font)
        self.btn_note_1.setStyleSheet("QPushButton {\n"
                                      "    background-color: rgb(225, 210, 255);\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "     background-color:  rgb(235, 220, 255);\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color: rgb(219, 193, 255);\n"
                                      "}\n"
                                      "")
        self.btn_note_1.setObjectName("btn_note_1")
        self.frame_note_item_2 = QtWidgets.QFrame(self.frame_note)
        self.frame_note_item_2.setGeometry(QtCore.QRect(119, 57, 40, 60))
        self.frame_note_item_2.setStyleSheet("background-color: rgb(167, 94, 118);\n"
                                             "border-radius: 10px;")
        self.frame_note_item_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_note_item_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_note_item_2.setObjectName("frame_note_item_2")
        self.label_note_2 = QtWidgets.QLabel(self.frame_note_item_2)
        self.label_note_2.setGeometry(QtCore.QRect(0, 0, 40, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_note_2.setFont(font)
        self.label_note_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_note_2.setScaledContents(False)
        self.label_note_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_note_2.setWordWrap(False)
        self.label_note_2.setObjectName("label_note_2")
        self.btn_note_2 = QtWidgets.QPushButton(self.frame_note_item_2)
        self.btn_note_2.setGeometry(QtCore.QRect(3, 27, 34, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        self.btn_note_2.setFont(font)
        self.btn_note_2.setStyleSheet("QPushButton {\n"
                                      "    background-color: rgb(225, 210, 255);\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "     background-color:  rgb(235, 220, 255);\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color: rgb(219, 193, 255);\n"
                                      "}\n"
                                      "")
        self.btn_note_2.setObjectName("btn_note_2")
        self.frame_note_item_3 = QtWidgets.QFrame(self.frame_note)
        self.frame_note_item_3.setGeometry(QtCore.QRect(162, 57, 40, 60))
        self.frame_note_item_3.setStyleSheet("background-color: rgb(167, 94, 100);\n"
                                             "border-radius: 10px;")
        self.frame_note_item_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_note_item_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_note_item_3.setObjectName("frame_note_item_3")
        self.label_note_3 = QtWidgets.QLabel(self.frame_note_item_3)
        self.label_note_3.setGeometry(QtCore.QRect(0, 0, 40, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_note_3.setFont(font)
        self.label_note_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_note_3.setScaledContents(False)
        self.label_note_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_note_3.setWordWrap(False)
        self.label_note_3.setObjectName("label_note_3")
        self.btn_note_3 = QtWidgets.QPushButton(self.frame_note_item_3)
        self.btn_note_3.setGeometry(QtCore.QRect(3, 27, 34, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        self.btn_note_3.setFont(font)
        self.btn_note_3.setStyleSheet("QPushButton {\n"
                                      "    background-color: rgb(225, 210, 255);\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "     background-color:  rgb(235, 220, 255);\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color: rgb(219, 193, 255);\n"
                                      "}\n"
                                      "")
        self.btn_note_3.setObjectName("btn_note_3")
        self.frame_note_item_4 = QtWidgets.QFrame(self.frame_note)
        self.frame_note_item_4.setGeometry(QtCore.QRect(205, 57, 40, 60))
        self.frame_note_item_4.setStyleSheet("background-color: rgb(167, 105, 94);\n"
                                             "border-radius: 10px;")
        self.frame_note_item_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_note_item_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_note_item_4.setObjectName("frame_note_item_4")
        self.label_note_4 = QtWidgets.QLabel(self.frame_note_item_4)
        self.label_note_4.setGeometry(QtCore.QRect(0, 0, 40, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_note_4.setFont(font)
        self.label_note_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_note_4.setScaledContents(False)
        self.label_note_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_note_4.setWordWrap(False)
        self.label_note_4.setObjectName("label_note_4")
        self.btn_note_4 = QtWidgets.QPushButton(self.frame_note_item_4)
        self.btn_note_4.setGeometry(QtCore.QRect(3, 27, 34, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        self.btn_note_4.setFont(font)
        self.btn_note_4.setStyleSheet("QPushButton {\n"
                                      "    background-color: rgb(225, 210, 255);\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "     background-color:  rgb(235, 220, 255);\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color: rgb(219, 193, 255);\n"
                                      "}\n"
                                      "")
        self.btn_note_4.setObjectName("btn_note_4")
        self.frame_note_item_5 = QtWidgets.QFrame(self.frame_note)
        self.frame_note_item_5.setGeometry(QtCore.QRect(248, 57, 40, 60))
        self.frame_note_item_5.setStyleSheet("background-color: rgb(167, 124, 94);\n"
                                             "border-radius: 10px;")
        self.frame_note_item_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_note_item_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_note_item_5.setObjectName("frame_note_item_5")
        self.label_note_5 = QtWidgets.QLabel(self.frame_note_item_5)
        self.label_note_5.setGeometry(QtCore.QRect(0, 0, 40, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_note_5.setFont(font)
        self.label_note_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_note_5.setScaledContents(False)
        self.label_note_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_note_5.setWordWrap(False)
        self.label_note_5.setObjectName("label_note_5")
        self.btn_note_5 = QtWidgets.QPushButton(self.frame_note_item_5)
        self.btn_note_5.setGeometry(QtCore.QRect(3, 27, 34, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        self.btn_note_5.setFont(font)
        self.btn_note_5.setStyleSheet("QPushButton {\n"
                                      "    background-color: rgb(225, 210, 255);\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "     background-color:  rgb(235, 220, 255);\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color: rgb(219, 193, 255);\n"
                                      "}\n"
                                      "")
        self.btn_note_5.setObjectName("btn_note_5")
        self.frame_note_item_6 = QtWidgets.QFrame(self.frame_note)
        self.frame_note_item_6.setGeometry(QtCore.QRect(291, 57, 40, 60))
        self.frame_note_item_6.setStyleSheet("background-color: rgb(167, 142, 94);\n"
                                             "border-radius: 10px;")
        self.frame_note_item_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_note_item_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_note_item_6.setObjectName("frame_note_item_6")
        self.label_note_6 = QtWidgets.QLabel(self.frame_note_item_6)
        self.label_note_6.setGeometry(QtCore.QRect(0, 0, 40, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_note_6.setFont(font)
        self.label_note_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_note_6.setScaledContents(False)
        self.label_note_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_note_6.setWordWrap(False)
        self.label_note_6.setObjectName("label_note_6")
        self.btn_note_6 = QtWidgets.QPushButton(self.frame_note_item_6)
        self.btn_note_6.setGeometry(QtCore.QRect(3, 27, 34, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        self.btn_note_6.setFont(font)
        self.btn_note_6.setStyleSheet("QPushButton {\n"
                                      "    background-color: rgb(225, 210, 255);\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "     background-color:  rgb(235, 220, 255);\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color: rgb(219, 193, 255);\n"
                                      "}\n"
                                      "")
        self.btn_note_6.setObjectName("btn_note_6")
        self.frame_note_item_7 = QtWidgets.QFrame(self.frame_note)
        self.frame_note_item_7.setGeometry(QtCore.QRect(334, 57, 40, 60))
        self.frame_note_item_7.setStyleSheet("background-color: rgb(167, 160, 94);\n"
                                             "border-radius: 10px;")
        self.frame_note_item_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_note_item_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_note_item_7.setObjectName("frame_note_item_7")
        self.label_note_7 = QtWidgets.QLabel(self.frame_note_item_7)
        self.label_note_7.setGeometry(QtCore.QRect(0, 0, 40, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_note_7.setFont(font)
        self.label_note_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_note_7.setScaledContents(False)
        self.label_note_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_note_7.setWordWrap(False)
        self.label_note_7.setObjectName("label_note_7")
        self.btn_note_7 = QtWidgets.QPushButton(self.frame_note_item_7)
        self.btn_note_7.setGeometry(QtCore.QRect(3, 27, 34, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        self.btn_note_7.setFont(font)
        self.btn_note_7.setStyleSheet("QPushButton {\n"
                                      "    background-color: rgb(225, 210, 255);\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "     background-color:  rgb(235, 220, 255);\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color: rgb(219, 193, 255);\n"
                                      "}\n"
                                      "")
        self.btn_note_7.setObjectName("btn_note_7")
        self.frame_note_item_8 = QtWidgets.QFrame(self.frame_note)
        self.frame_note_item_8.setGeometry(QtCore.QRect(377, 57, 40, 60))
        self.frame_note_item_8.setStyleSheet("background-color: rgb(155, 167, 94);\n"
                                             "border-radius: 10px;")
        self.frame_note_item_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_note_item_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_note_item_8.setObjectName("frame_note_item_8")
        self.label_note_8 = QtWidgets.QLabel(self.frame_note_item_8)
        self.label_note_8.setGeometry(QtCore.QRect(0, 0, 40, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_note_8.setFont(font)
        self.label_note_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_note_8.setScaledContents(False)
        self.label_note_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_note_8.setWordWrap(False)
        self.label_note_8.setObjectName("label_note_8")
        self.btn_note_8 = QtWidgets.QPushButton(self.frame_note_item_8)
        self.btn_note_8.setGeometry(QtCore.QRect(3, 27, 34, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        self.btn_note_8.setFont(font)
        self.btn_note_8.setStyleSheet("QPushButton {\n"
                                      "    background-color: rgb(225, 210, 255);\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "     background-color:  rgb(235, 220, 255);\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color: rgb(219, 193, 255);\n"
                                      "}\n"
                                      "")
        self.btn_note_8.setObjectName("btn_note_8")
        self.frame_note_item_9 = QtWidgets.QFrame(self.frame_note)
        self.frame_note_item_9.setGeometry(QtCore.QRect(420, 57, 40, 60))
        self.frame_note_item_9.setStyleSheet("background-color: rgb(136, 167, 94);\n"
                                             "border-radius: 10px;")
        self.frame_note_item_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_note_item_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_note_item_9.setObjectName("frame_note_item_9")
        self.label_note_9 = QtWidgets.QLabel(self.frame_note_item_9)
        self.label_note_9.setGeometry(QtCore.QRect(0, 0, 40, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_note_9.setFont(font)
        self.label_note_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_note_9.setScaledContents(False)
        self.label_note_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_note_9.setWordWrap(False)
        self.label_note_9.setObjectName("label_note_9")
        self.btn_note_9 = QtWidgets.QPushButton(self.frame_note_item_9)
        self.btn_note_9.setGeometry(QtCore.QRect(3, 27, 34, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        self.btn_note_9.setFont(font)
        self.btn_note_9.setStyleSheet("QPushButton {\n"
                                      "    background-color: rgb(225, 210, 255);\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "     background-color:  rgb(235, 220, 255);\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color: rgb(219, 193, 255);\n"
                                      "}\n"
                                      "")
        self.btn_note_9.setObjectName("btn_note_9")
        self.frame_note_item_10 = QtWidgets.QFrame(self.frame_note)
        self.frame_note_item_10.setGeometry(QtCore.QRect(463, 57, 40, 60))
        self.frame_note_item_10.setStyleSheet("background-color: rgb(118, 167, 94);\n"
                                              "border-radius: 10px;")
        self.frame_note_item_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_note_item_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_note_item_10.setObjectName("frame_note_item_10")
        self.label_note_10 = QtWidgets.QLabel(self.frame_note_item_10)
        self.label_note_10.setGeometry(QtCore.QRect(0, 0, 40, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_note_10.setFont(font)
        self.label_note_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_note_10.setScaledContents(False)
        self.label_note_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_note_10.setWordWrap(False)
        self.label_note_10.setObjectName("label_note_10")
        self.btn_note_10 = QtWidgets.QPushButton(self.frame_note_item_10)
        self.btn_note_10.setGeometry(QtCore.QRect(3, 27, 34, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        self.btn_note_10.setFont(font)
        self.btn_note_10.setStyleSheet("QPushButton {\n"
                                       "    background-color: rgb(225, 210, 255);\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "     background-color:  rgb(235, 220, 255);\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: rgb(219, 193, 255);\n"
                                       "}\n"
                                       "")
        self.btn_note_10.setObjectName("btn_note_10")
        self.frame_note_item_11 = QtWidgets.QFrame(self.frame_note)
        self.frame_note_item_11.setGeometry(QtCore.QRect(506, 57, 40, 60))
        self.frame_note_item_11.setStyleSheet("background-color: rgb(100, 167, 94);\n"
                                              "border-radius: 10px;")
        self.frame_note_item_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_note_item_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_note_item_11.setObjectName("frame_note_item_11")
        self.label_note_11 = QtWidgets.QLabel(self.frame_note_item_11)
        self.label_note_11.setGeometry(QtCore.QRect(0, 0, 40, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_note_11.setFont(font)
        self.label_note_11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_note_11.setScaledContents(False)
        self.label_note_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_note_11.setWordWrap(False)
        self.label_note_11.setObjectName("label_note_11")
        self.btn_note_11 = QtWidgets.QPushButton(self.frame_note_item_11)
        self.btn_note_11.setGeometry(QtCore.QRect(3, 27, 34, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        self.btn_note_11.setFont(font)
        self.btn_note_11.setStyleSheet("QPushButton {\n"
                                       "    background-color: rgb(225, 210, 255);\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "     background-color:  rgb(235, 220, 255);\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: rgb(219, 193, 255);\n"
                                       "}\n"
                                       "")
        self.btn_note_11.setObjectName("btn_note_11")
        self.frame_note_item_12 = QtWidgets.QFrame(self.frame_note)
        self.frame_note_item_12.setGeometry(QtCore.QRect(12, 120, 40, 60))
        self.frame_note_item_12.setStyleSheet("background-color: rgb(94, 167, 105);\n"
                                              "border-radius: 10px;")
        self.frame_note_item_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_note_item_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_note_item_12.setObjectName("frame_note_item_12")
        self.label_note_12 = QtWidgets.QLabel(self.frame_note_item_12)
        self.label_note_12.setGeometry(QtCore.QRect(0, 0, 40, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_note_12.setFont(font)
        self.label_note_12.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_note_12.setScaledContents(False)
        self.label_note_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_note_12.setWordWrap(False)
        self.label_note_12.setObjectName("label_note_12")
        self.btn_note_12 = QtWidgets.QPushButton(self.frame_note_item_12)
        self.btn_note_12.setGeometry(QtCore.QRect(3, 27, 34, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        self.btn_note_12.setFont(font)
        self.btn_note_12.setStyleSheet("QPushButton {\n"
                                       "    background-color: rgb(225, 210, 255);\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "     background-color:  rgb(235, 220, 255);\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: rgb(219, 193, 255);\n"
                                       "}\n"
                                       "")
        self.btn_note_12.setObjectName("btn_note_12")
        self.frame_note_item_13 = QtWidgets.QFrame(self.frame_note)
        self.frame_note_item_13.setGeometry(QtCore.QRect(55, 120, 40, 60))
        self.frame_note_item_13.setStyleSheet("background-color: rgb(94, 167, 124);\n"
                                              "border-radius: 10px;")
        self.frame_note_item_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_note_item_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_note_item_13.setObjectName("frame_note_item_13")
        self.label_note_13 = QtWidgets.QLabel(self.frame_note_item_13)
        self.label_note_13.setGeometry(QtCore.QRect(0, 0, 40, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_note_13.setFont(font)
        self.label_note_13.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_note_13.setScaledContents(False)
        self.label_note_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_note_13.setWordWrap(False)
        self.label_note_13.setObjectName("label_note_13")
        self.btn_note_13 = QtWidgets.QPushButton(self.frame_note_item_13)
        self.btn_note_13.setGeometry(QtCore.QRect(3, 27, 34, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        self.btn_note_13.setFont(font)
        self.btn_note_13.setStyleSheet("QPushButton {\n"
                                       "    background-color: rgb(225, 210, 255);\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "     background-color:  rgb(235, 220, 255);\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: rgb(219, 193, 255);\n"
                                       "}\n"
                                       "")
        self.btn_note_13.setObjectName("btn_note_13")
        self.frame_note_item_14 = QtWidgets.QFrame(self.frame_note)
        self.frame_note_item_14.setGeometry(QtCore.QRect(98, 120, 40, 60))
        self.frame_note_item_14.setStyleSheet("background-color: rgb(94, 167, 142);\n"
                                              "border-radius: 10px;")
        self.frame_note_item_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_note_item_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_note_item_14.setObjectName("frame_note_item_14")
        self.label_note_14 = QtWidgets.QLabel(self.frame_note_item_14)
        self.label_note_14.setGeometry(QtCore.QRect(0, 0, 40, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_note_14.setFont(font)
        self.label_note_14.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_note_14.setScaledContents(False)
        self.label_note_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_note_14.setWordWrap(False)
        self.label_note_14.setObjectName("label_note_14")
        self.btn_note_14 = QtWidgets.QPushButton(self.frame_note_item_14)
        self.btn_note_14.setGeometry(QtCore.QRect(3, 27, 34, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        self.btn_note_14.setFont(font)
        self.btn_note_14.setStyleSheet("QPushButton {\n"
                                       "    background-color: rgb(225, 210, 255);\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "     background-color:  rgb(235, 220, 255);\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: rgb(219, 193, 255);\n"
                                       "}\n"
                                       "")
        self.btn_note_14.setObjectName("btn_note_14")
        self.frame_note_item_15 = QtWidgets.QFrame(self.frame_note)
        self.frame_note_item_15.setGeometry(QtCore.QRect(141, 120, 40, 60))
        self.frame_note_item_15.setStyleSheet("background-color: rgb(94, 167, 160);\n"
                                              "border-radius: 10px;")
        self.frame_note_item_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_note_item_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_note_item_15.setObjectName("frame_note_item_15")
        self.label_note_15 = QtWidgets.QLabel(self.frame_note_item_15)
        self.label_note_15.setGeometry(QtCore.QRect(0, 0, 40, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_note_15.setFont(font)
        self.label_note_15.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_note_15.setScaledContents(False)
        self.label_note_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_note_15.setWordWrap(False)
        self.label_note_15.setObjectName("label_note_15")
        self.btn_note_15 = QtWidgets.QPushButton(self.frame_note_item_15)
        self.btn_note_15.setGeometry(QtCore.QRect(3, 27, 34, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        self.btn_note_15.setFont(font)
        self.btn_note_15.setStyleSheet("QPushButton {\n"
                                       "    background-color: rgb(225, 210, 255);\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "     background-color:  rgb(235, 220, 255);\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: rgb(219, 193, 255);\n"
                                       "}\n"
                                       "")
        self.btn_note_15.setObjectName("btn_note_15")
        self.frame_note_item_16 = QtWidgets.QFrame(self.frame_note)
        self.frame_note_item_16.setGeometry(QtCore.QRect(184, 120, 40, 60))
        self.frame_note_item_16.setStyleSheet("background-color: rgb(94, 155, 167);\n"
                                              "border-radius: 10px;")
        self.frame_note_item_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_note_item_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_note_item_16.setObjectName("frame_note_item_16")
        self.label_note_16 = QtWidgets.QLabel(self.frame_note_item_16)
        self.label_note_16.setGeometry(QtCore.QRect(0, 0, 40, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_note_16.setFont(font)
        self.label_note_16.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_note_16.setScaledContents(False)
        self.label_note_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_note_16.setWordWrap(False)
        self.label_note_16.setObjectName("label_note_16")
        self.btn_note_16 = QtWidgets.QPushButton(self.frame_note_item_16)
        self.btn_note_16.setGeometry(QtCore.QRect(3, 27, 34, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        self.btn_note_16.setFont(font)
        self.btn_note_16.setStyleSheet("QPushButton {\n"
                                       "    background-color: rgb(225, 210, 255);\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "     background-color:  rgb(235, 220, 255);\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: rgb(219, 193, 255);\n"
                                       "}\n"
                                       "")
        self.btn_note_16.setObjectName("btn_note_16")
        self.frame_note_item_17 = QtWidgets.QFrame(self.frame_note)
        self.frame_note_item_17.setGeometry(QtCore.QRect(227, 120, 40, 60))
        self.frame_note_item_17.setStyleSheet("background-color: rgb(94, 136, 167);\n"
                                              "border-radius: 10px;")
        self.frame_note_item_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_note_item_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_note_item_17.setObjectName("frame_note_item_17")
        self.label_note_17 = QtWidgets.QLabel(self.frame_note_item_17)
        self.label_note_17.setGeometry(QtCore.QRect(0, 0, 40, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_note_17.setFont(font)
        self.label_note_17.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_note_17.setScaledContents(False)
        self.label_note_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_note_17.setWordWrap(False)
        self.label_note_17.setObjectName("label_note_17")
        self.btn_note_17 = QtWidgets.QPushButton(self.frame_note_item_17)
        self.btn_note_17.setGeometry(QtCore.QRect(3, 27, 34, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        self.btn_note_17.setFont(font)
        self.btn_note_17.setStyleSheet("QPushButton {\n"
                                       "    background-color: rgb(225, 210, 255);\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "     background-color:  rgb(235, 220, 255);\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: rgb(219, 193, 255);\n"
                                       "}\n"
                                       "")
        self.btn_note_17.setObjectName("btn_note_17")
        self.frame_note_item_18 = QtWidgets.QFrame(self.frame_note)
        self.frame_note_item_18.setGeometry(QtCore.QRect(270, 120, 40, 60))
        self.frame_note_item_18.setStyleSheet("background-color: rgb(94, 118, 167);\n"
                                              "border-radius: 10px;")
        self.frame_note_item_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_note_item_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_note_item_18.setObjectName("frame_note_item_18")
        self.label_note_18 = QtWidgets.QLabel(self.frame_note_item_18)
        self.label_note_18.setGeometry(QtCore.QRect(0, 0, 40, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_note_18.setFont(font)
        self.label_note_18.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_note_18.setScaledContents(False)
        self.label_note_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_note_18.setWordWrap(False)
        self.label_note_18.setObjectName("label_note_18")
        self.btn_note_18 = QtWidgets.QPushButton(self.frame_note_item_18)
        self.btn_note_18.setGeometry(QtCore.QRect(3, 27, 34, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        self.btn_note_18.setFont(font)
        self.btn_note_18.setStyleSheet("QPushButton {\n"
                                       "    background-color: rgb(225, 210, 255);\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "     background-color:  rgb(235, 220, 255);\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: rgb(219, 193, 255);\n"
                                       "}\n"
                                       "")
        self.btn_note_18.setObjectName("btn_note_18")
        self.frame_note_item_19 = QtWidgets.QFrame(self.frame_note)
        self.frame_note_item_19.setGeometry(QtCore.QRect(313, 120, 40, 60))
        self.frame_note_item_19.setStyleSheet("background-color: rgb(94, 100, 167);\n"
                                              "border-radius: 10px;")
        self.frame_note_item_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_note_item_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_note_item_19.setObjectName("frame_note_item_19")
        self.label_note_19 = QtWidgets.QLabel(self.frame_note_item_19)
        self.label_note_19.setGeometry(QtCore.QRect(0, 0, 40, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_note_19.setFont(font)
        self.label_note_19.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_note_19.setScaledContents(False)
        self.label_note_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_note_19.setWordWrap(False)
        self.label_note_19.setObjectName("label_note_19")
        self.btn_note_19 = QtWidgets.QPushButton(self.frame_note_item_19)
        self.btn_note_19.setGeometry(QtCore.QRect(3, 27, 34, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        self.btn_note_19.setFont(font)
        self.btn_note_19.setStyleSheet("QPushButton {\n"
                                       "    background-color: rgb(225, 210, 255);\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "     background-color:  rgb(235, 220, 255);\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: rgb(219, 193, 255);\n"
                                       "}\n"
                                       "")
        self.btn_note_19.setObjectName("btn_note_19")
        self.frame_note_item_20 = QtWidgets.QFrame(self.frame_note)
        self.frame_note_item_20.setGeometry(QtCore.QRect(356, 120, 40, 60))
        self.frame_note_item_20.setStyleSheet("background-color: rgb(105, 94, 167);\n"
                                              "border-radius: 10px;")
        self.frame_note_item_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_note_item_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_note_item_20.setObjectName("frame_note_item_20")
        self.label_note_20 = QtWidgets.QLabel(self.frame_note_item_20)
        self.label_note_20.setGeometry(QtCore.QRect(0, 0, 40, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_note_20.setFont(font)
        self.label_note_20.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_note_20.setScaledContents(False)
        self.label_note_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_note_20.setWordWrap(False)
        self.label_note_20.setObjectName("label_note_20")
        self.btn_note_20 = QtWidgets.QPushButton(self.frame_note_item_20)
        self.btn_note_20.setGeometry(QtCore.QRect(3, 27, 34, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        self.btn_note_20.setFont(font)
        self.btn_note_20.setStyleSheet("QPushButton {\n"
                                       "    background-color: rgb(225, 210, 255);\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "     background-color:  rgb(235, 220, 255);\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: rgb(219, 193, 255);\n"
                                       "}\n"
                                       "")
        self.btn_note_20.setObjectName("btn_note_20")
        self.frame_note_item_21 = QtWidgets.QFrame(self.frame_note)
        self.frame_note_item_21.setGeometry(QtCore.QRect(399, 120, 40, 60))
        self.frame_note_item_21.setStyleSheet("background-color: rgb(124, 94, 167);\n"
                                              "border-radius: 10px;")
        self.frame_note_item_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_note_item_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_note_item_21.setObjectName("frame_note_item_21")
        self.label_note_21 = QtWidgets.QLabel(self.frame_note_item_21)
        self.label_note_21.setGeometry(QtCore.QRect(0, 0, 40, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_note_21.setFont(font)
        self.label_note_21.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_note_21.setScaledContents(False)
        self.label_note_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_note_21.setWordWrap(False)
        self.label_note_21.setObjectName("label_note_21")
        self.btn_note_21 = QtWidgets.QPushButton(self.frame_note_item_21)
        self.btn_note_21.setGeometry(QtCore.QRect(3, 27, 34, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        self.btn_note_21.setFont(font)
        self.btn_note_21.setStyleSheet("QPushButton {\n"
                                       "    background-color: rgb(225, 210, 255);\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "     background-color:  rgb(235, 220, 255);\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: rgb(219, 193, 255);\n"
                                       "}\n"
                                       "")
        self.btn_note_21.setObjectName("btn_note_21")
        self.frame_note_item_22 = QtWidgets.QFrame(self.frame_note)
        self.frame_note_item_22.setGeometry(QtCore.QRect(442, 120, 40, 60))
        self.frame_note_item_22.setStyleSheet("background-color: rgb(142, 94, 167);\n"
                                              "border-radius: 10px;")
        self.frame_note_item_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_note_item_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_note_item_22.setObjectName("frame_note_item_22")
        self.label_note_22 = QtWidgets.QLabel(self.frame_note_item_22)
        self.label_note_22.setGeometry(QtCore.QRect(0, 0, 40, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_note_22.setFont(font)
        self.label_note_22.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_note_22.setScaledContents(False)
        self.label_note_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_note_22.setWordWrap(False)
        self.label_note_22.setObjectName("label_note_22")
        self.btn_note_22 = QtWidgets.QPushButton(self.frame_note_item_22)
        self.btn_note_22.setGeometry(QtCore.QRect(3, 27, 34, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        self.btn_note_22.setFont(font)
        self.btn_note_22.setStyleSheet("QPushButton {\n"
                                       "    background-color: rgb(225, 210, 255);\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "     background-color:  rgb(235, 220, 255);\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: rgb(219, 193, 255);\n"
                                       "}\n"
                                       "")
        self.btn_note_22.setObjectName("btn_note_22")
        self.frame_note_item_23 = QtWidgets.QFrame(self.frame_note)
        self.frame_note_item_23.setGeometry(QtCore.QRect(485, 120, 40, 60))
        self.frame_note_item_23.setStyleSheet("background-color: rgb(160, 94, 167);\n"
                                              "border-radius: 10px;")
        self.frame_note_item_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_note_item_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_note_item_23.setObjectName("frame_note_item_23")
        self.label_note_23 = QtWidgets.QLabel(self.frame_note_item_23)
        self.label_note_23.setGeometry(QtCore.QRect(0, 0, 40, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_note_23.setFont(font)
        self.label_note_23.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_note_23.setScaledContents(False)
        self.label_note_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_note_23.setWordWrap(False)
        self.label_note_23.setObjectName("label_note_23")
        self.btn_note_23 = QtWidgets.QPushButton(self.frame_note_item_23)
        self.btn_note_23.setGeometry(QtCore.QRect(3, 27, 34, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        self.btn_note_23.setFont(font)
        self.btn_note_23.setStyleSheet("QPushButton {\n"
                                       "    background-color: rgb(225, 210, 255);\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "     background-color:  rgb(235, 220, 255);\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: rgb(219, 193, 255);\n"
                                       "}\n"
                                       "")
        self.btn_note_23.setObjectName("btn_note_23")
        self.frame_note_item_24 = QtWidgets.QFrame(self.frame_note)
        self.frame_note_item_24.setGeometry(QtCore.QRect(528, 120, 40, 60))
        self.frame_note_item_24.setStyleSheet("background-color: rgb(167, 94, 155);\n"
                                              "border-radius: 10px;")
        self.frame_note_item_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_note_item_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_note_item_24.setObjectName("frame_note_item_24")
        self.label_note_24 = QtWidgets.QLabel(self.frame_note_item_24)
        self.label_note_24.setGeometry(QtCore.QRect(0, 0, 40, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_note_24.setFont(font)
        self.label_note_24.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_note_24.setScaledContents(False)
        self.label_note_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_note_24.setWordWrap(False)
        self.label_note_24.setObjectName("label_note_24")
        self.btn_note_24 = QtWidgets.QPushButton(self.frame_note_item_24)
        self.btn_note_24.setGeometry(QtCore.QRect(3, 27, 34, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        self.btn_note_24.setFont(font)
        self.btn_note_24.setStyleSheet("QPushButton {\n"
                                       "    background-color: rgb(225, 210, 255);\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "     background-color:  rgb(235, 220, 255);\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: rgb(219, 193, 255);\n"
                                       "}\n"
                                       "")
        self.btn_note_24.setObjectName("btn_note_24")
        self.frame_control = QtWidgets.QFrame(self.centralwidget)
        self.frame_control.setGeometry(QtCore.QRect(305, 10, 285, 140))
        self.frame_control.setStyleSheet("background-color: rgb(219, 193, 255);\n"
                                         "border-radius: 10px;")
        self.frame_control.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_control.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_control.setObjectName("frame_control")
        self.label_control = QtWidgets.QLabel(self.frame_control)
        self.label_control.setGeometry(QtCore.QRect(0, 0, 285, 50))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_control.setFont(font)
        self.label_control.setAlignment(QtCore.Qt.AlignCenter)
        self.label_control.setWordWrap(False)
        self.label_control.setObjectName("label_control")
        self.btn_start = QtWidgets.QPushButton(self.frame_control)
        self.btn_start.setGeometry(QtCore.QRect(50, 50, 185, 40))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.btn_start.setFont(font)
        self.btn_start.setStyleSheet("QPushButton {\n"
                                     "    background-color: rgb(225, 210, 255);\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "     background-color:  rgb(235, 220, 255);\n"
                                     "}\n"
                                     "QPushButton:pressed {\n"
                                     "    background-color: rgb(192, 147, 255);\n"
                                     "}\n"
                                     "")
        self.btn_start.setObjectName("btn_start")
        self.label_stop = QtWidgets.QLabel(self.frame_control)
        self.label_stop.setGeometry(QtCore.QRect(20, 100, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.label_stop.setFont(font)
        self.label_stop.setObjectName("label_stop")
        self.btn_stop = QtWidgets.QPushButton(self.frame_control)
        self.btn_stop.setGeometry(QtCore.QRect(150, 95, 80, 35))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        self.btn_stop.setFont(font)
        self.btn_stop.setStyleSheet("QPushButton {\n"
                                    "    background-color: rgb(225, 210, 255);\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                    "     background-color:  rgb(235, 220, 255);\n"
                                    "}\n"
                                    "QPushButton:pressed {\n"
                                    "    background-color: rgb(192, 147, 255);\n"
                                    "}\n"
                                    "")
        self.btn_stop.setObjectName("btn_stop")
        self.btn_control_help = QtWidgets.QPushButton(self.frame_control)
        self.btn_control_help.setGeometry(QtCore.QRect(10, 10, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.btn_control_help.setFont(font)
        self.btn_control_help.setStyleSheet("QPushButton {\n"
                                            "    background-color: rgb(225, 210, 255);\n"
                                            "    border-radius: 15px;\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                            "     background-color:  rgb(235, 220, 255);\n"
                                            "}\n"
                                            "QPushButton:pressed {\n"
                                            "    background-color: rgb(192, 147, 255);\n"
                                            "}\n"
                                            "")
        self.btn_control_help.setObjectName("btn_control_help")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()

    # Перейменування об'єктів вінка (також створено за допомогою QT Designer)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NotePlay"))
        self.label_file.setText(_translate("MainWindow", "Файл"))
        self.btn_file.setText(_translate("MainWindow", "Вибрати файл"))
        self.btn_file_help.setText(_translate("MainWindow", "?"))
        self.label_note.setText(_translate("MainWindow", "Ноти"))
        self.btn_note_help.setText(_translate("MainWindow", "?"))
        self.label_note_0.setText(_translate("MainWindow", "F#"))
        self.btn_note_0.setText(_translate("MainWindow", "q"))
        self.label_note_1.setText(_translate("MainWindow", "G"))
        self.btn_note_1.setText(_translate("MainWindow", "w"))
        self.label_note_2.setText(_translate("MainWindow", "G#"))
        self.btn_note_2.setText(_translate("MainWindow", "e"))
        self.label_note_3.setText(_translate("MainWindow", "A"))
        self.btn_note_3.setText(_translate("MainWindow", "r"))
        self.label_note_4.setText(_translate("MainWindow", "A#"))
        self.btn_note_4.setText(_translate("MainWindow", "t"))
        self.label_note_5.setText(_translate("MainWindow", "B"))
        self.btn_note_5.setText(_translate("MainWindow", "y"))
        self.label_note_6.setText(_translate("MainWindow", "C"))
        self.btn_note_6.setText(_translate("MainWindow", "u"))
        self.label_note_7.setText(_translate("MainWindow", "C#"))
        self.btn_note_7.setText(_translate("MainWindow", "p"))
        self.label_note_8.setText(_translate("MainWindow", "D"))
        self.btn_note_8.setText(_translate("MainWindow", "a"))
        self.label_note_9.setText(_translate("MainWindow", "D#"))
        self.btn_note_9.setText(_translate("MainWindow", "s"))
        self.label_note_10.setText(_translate("MainWindow", "E"))
        self.btn_note_10.setText(_translate("MainWindow", "d"))
        self.label_note_11.setText(_translate("MainWindow", "F"))
        self.btn_note_11.setText(_translate("MainWindow", "f"))
        self.label_note_12.setText(_translate("MainWindow", "F#"))
        self.btn_note_12.setText(_translate("MainWindow", "g"))
        self.label_note_13.setText(_translate("MainWindow", "G"))
        self.btn_note_13.setText(_translate("MainWindow", "h"))
        self.label_note_14.setText(_translate("MainWindow", "G#"))
        self.btn_note_14.setText(_translate("MainWindow", "j"))
        self.label_note_15.setText(_translate("MainWindow", "A"))
        self.btn_note_15.setText(_translate("MainWindow", "k"))
        self.label_note_16.setText(_translate("MainWindow", "A#"))
        self.btn_note_16.setText(_translate("MainWindow", "l"))
        self.label_note_17.setText(_translate("MainWindow", "B"))
        self.btn_note_17.setText(_translate("MainWindow", "z"))
        self.label_note_18.setText(_translate("MainWindow", "C"))
        self.btn_note_18.setText(_translate("MainWindow", "x"))
        self.label_note_19.setText(_translate("MainWindow", "C#"))
        self.btn_note_19.setText(_translate("MainWindow", "c"))
        self.label_note_20.setText(_translate("MainWindow", "D"))
        self.btn_note_20.setText(_translate("MainWindow", "v"))
        self.label_note_21.setText(_translate("MainWindow", "D#"))
        self.btn_note_21.setText(_translate("MainWindow", "b"))
        self.label_note_22.setText(_translate("MainWindow", "E"))
        self.btn_note_22.setText(_translate("MainWindow", "n"))
        self.label_note_23.setText(_translate("MainWindow", "F"))
        self.btn_note_23.setText(_translate("MainWindow", "m"))
        self.label_note_24.setText(_translate("MainWindow", "F#"))
        self.btn_note_24.setText(_translate("MainWindow", "0"))
        self.label_control.setText(_translate("MainWindow", "Керування"))
        self.btn_start.setText(_translate("MainWindow", "Старт"))
        self.label_stop.setText(_translate("MainWindow", "Стоп кнопка:"))
        self.btn_stop.setText(_translate("MainWindow", "esc"))
        self.btn_control_help.setText(_translate("MainWindow", "?"))

    # Реалізація функціоналу програми
    def add_functions(self):
        self.btn_file.clicked.connect(self.choose_file)  # Вибір файла

        self.btn_start.clicked.connect(self.start)  # Запуск програвання мелодії
        self.btn_stop.clicked.connect(self.stop)  # Зміна стоп кнопки

        # Зміна клавіш керування нотами
        self.btn_note_0.clicked.connect(self.note_0)
        self.btn_note_1.clicked.connect(self.note_1)
        self.btn_note_2.clicked.connect(self.note_2)
        self.btn_note_3.clicked.connect(self.note_3)
        self.btn_note_4.clicked.connect(self.note_4)
        self.btn_note_5.clicked.connect(self.note_5)
        self.btn_note_6.clicked.connect(self.note_6)
        self.btn_note_7.clicked.connect(self.note_7)
        self.btn_note_8.clicked.connect(self.note_8)
        self.btn_note_9.clicked.connect(self.note_9)
        self.btn_note_10.clicked.connect(self.note_10)
        self.btn_note_11.clicked.connect(self.note_11)
        self.btn_note_12.clicked.connect(self.note_12)
        self.btn_note_13.clicked.connect(self.note_13)
        self.btn_note_14.clicked.connect(self.note_14)
        self.btn_note_15.clicked.connect(self.note_15)
        self.btn_note_16.clicked.connect(self.note_16)
        self.btn_note_17.clicked.connect(self.note_17)
        self.btn_note_18.clicked.connect(self.note_18)
        self.btn_note_19.clicked.connect(self.note_19)
        self.btn_note_20.clicked.connect(self.note_20)
        self.btn_note_21.clicked.connect(self.note_21)
        self.btn_note_22.clicked.connect(self.note_22)
        self.btn_note_23.clicked.connect(self.note_23)
        self.btn_note_24.clicked.connect(self.note_24)

        # Інструкції до інструментів
        self.btn_file_help.clicked.connect(self.file_help)
        self.btn_control_help.clicked.connect(self.control_help)
        self.btn_note_help.clicked.connect(self.note_help)

        self.fname = None  # Шлях до вибраного файлу

        self.start = False  # Індикатор запуску
        self.stop_key = False  # Індикатор зміни стоп кнопки

        # Індикатори зміни клавіш керування нотами
        self.note_0 = False
        self.note_1 = False
        self.note_2 = False
        self.note_3 = False
        self.note_4 = False
        self.note_5 = False
        self.note_6 = False
        self.note_7 = False
        self.note_8 = False
        self.note_9 = False
        self.note_10 = False
        self.note_11 = False
        self.note_12 = False
        self.note_13 = False
        self.note_14 = False
        self.note_15 = False
        self.note_16 = False
        self.note_17 = False
        self.note_18 = False
        self.note_19 = False
        self.note_20 = False
        self.note_21 = False
        self.note_22 = False
        self.note_23 = False
        self.note_24 = False

        keyboard.on_press(self.on_press)  # Обробка натискань клавіш

    # Вибір Midi файлу
    def choose_file(self):
        self.fname = QtWidgets.QFileDialog.getOpenFileName(None, 'Open File', None, 'Midi File (*.mid)')[0]
        if self.fname != '':
            self.btn_file.setText(os.path.basename(self.fname))
            font = QtGui.QFont()
            font.setFamily("Comic Sans MS")
            font.setPointSize(10)
            self.btn_file.setFont(font)

    # Запуск програми
    def start(self):
        # Стилі об'єктів
        frame_style = "background-color: rgb(219, 193, 255);border-radius: 10px;"
        btn_style = "QPushButton {background-color: rgb(225, 210, 255);}" \
                    "QPushButton:hover {background-color:  rgb(235, 220, 255);}" \
                    "QPushButton:pressed {background-color: rgb(192, 147, 255);}"

        # Стилі об'єктів при помилці
        frame_style_error = "background-color: rgb(255, 150, 150);border-radius: 10px;"
        btn_style_error = "QPushButton {background-color: rgb(255, 170, 170);}" \
                          "QPushButton:hover {background-color:  rgb(255, 180, 180);}" \
                          "QPushButton:pressed {background-color: rgb(255, 130, 130);}"

        # Перевірка файлу
        if self.fname is not None and self.fname != '':
            mid = MidiFile(self.fname, clip=True)

            self.frame_file.setStyleSheet(frame_style)
            self.btn_file.setStyleSheet(btn_style)
            self.btn_file_help.setStyleSheet(btn_style)
        else:
            self.frame_file.setStyleSheet(frame_style_error)
            self.btn_file.setStyleSheet(btn_style_error)
            self.btn_file_help.setStyleSheet(btn_style_error)
            return

        # Список клавіш для керування нотами в грі
        a = [self.btn_note_0.text(), self.btn_note_1.text(), self.btn_note_2.text(), self.btn_note_3.text(),
             self.btn_note_4.text(),
             self.btn_note_5.text(), self.btn_note_6.text(), self.btn_note_7.text(), self.btn_note_8.text(),
             self.btn_note_9.text(),
             self.btn_note_10.text(), self.btn_note_11.text(), self.btn_note_12.text(), self.btn_note_13.text(),
             self.btn_note_14.text(),
             self.btn_note_15.text(), self.btn_note_16.text(), self.btn_note_17.text(), self.btn_note_18.text(),
             self.btn_note_19.text(),
             self.btn_note_20.text(), self.btn_note_21.text(), self.btn_note_22.text(), self.btn_note_23.text(),
             self.btn_note_24.text()]

        self.start = True

        # Програвання музики
        for msg in mid.play():
            if self.start is False:  # Зупинка програвання при натиснутій стоп клавіші
                return

            # Перенос нот на октаву нижче чи вище (за потреби) та програвання їх у грі
            if msg.type == 'note_on' and msg.velocity != 0:
                if msg.note > 78:
                    keyboard.press_and_release(a[msg.note // 12 + 12])
                elif msg.note < 54:
                    keyboard.press_and_release(a[msg.note // 12])
                else:
                    keyboard.press_and_release(a[msg.note - 54])
                print(msg)

    # Зміна стоп кнопки
    def stop(self):
        self.stop_key = True

    # Зміна клавіш керування нотами
    def note_0(self):
        self.note_0 = True

    def note_1(self):
        self.note_1 = True

    def note_2(self):
        self.note_2 = True

    def note_3(self):
        self.note_3 = True

    def note_4(self):
        self.note_4 = True

    def note_5(self):
        self.note_5 = True

    def note_6(self):
        self.note_6 = True

    def note_7(self):
        self.note_7 = True

    def note_8(self):
        self.note_8 = True

    def note_9(self):
        self.note_9 = True

    def note_10(self):
        self.note_10 = True

    def note_11(self):
        self.note_11 = True

    def note_12(self):
        self.note_12 = True

    def note_13(self):
        self.note_13 = True

    def note_14(self):
        self.note_14 = True

    def note_15(self):
        self.note_15 = True

    def note_16(self):
        self.note_16 = True

    def note_17(self):
        self.note_17 = True

    def note_18(self):
        self.note_18 = True

    def note_19(self):
        self.note_19 = True

    def note_20(self):
        self.note_20 = True

    def note_21(self):
        self.note_21 = True

    def note_22(self):
        self.note_22 = True

    def note_23(self):
        self.note_23 = True

    def note_24(self):
        self.note_24 = True

    # Інструкція до вибору файла
    def file_help(self):
        # Створення віджету інструкції
        self.frame_file_help = QtWidgets.QFrame(self.centralwidget)
        self.frame_file_help.setGeometry(QtCore.QRect(10, 10, 580, 340))
        self.frame_file_help.setStyleSheet("background-color: rgb(219, 193, 255);\n"
                                           "border-radius: 10px;")
        self.frame_file_help.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_file_help.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_file_help.setObjectName("frame_file_help")

        # Заголовок інструкції
        self.label_file_help = QtWidgets.QLabel(self.frame_file_help)
        self.label_file_help.setGeometry(QtCore.QRect(0, 0, 580, 50))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_file_help.setFont(font)
        self.label_file_help.setAlignment(QtCore.Qt.AlignCenter)
        self.label_file_help.setWordWrap(False)
        self.label_file_help.setObjectName("label_file_help")
        self.label_file_help.setText("Файл")

        # Опис інтрукції
        self.label_file_help_description = QtWidgets.QLabel(self.frame_file_help)
        self.label_file_help_description.setGeometry(QtCore.QRect(10, 50, 560, 220))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_file_help_description.setFont(font)
        self.label_file_help_description.setAlignment(QtCore.Qt.AlignCenter)
        self.label_file_help_description.setWordWrap(True)
        self.label_file_help_description.setObjectName("label_file_help_description")
        self.label_file_help_description.setText(
            "Натиснувши кнопку «Вибрати файл», ви можете вибрати Midi файл, який хочете зіграти. "
            "Підтримується лише Midi (.mid) формат.")

        # Кнопка закриття інструкції
        self.btn_file_help_ok = QtWidgets.QPushButton(self.frame_file_help)
        self.btn_file_help_ok.setGeometry(QtCore.QRect(190, 280, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.btn_file_help_ok.setFont(font)
        self.btn_file_help_ok.setStyleSheet("QPushButton {\n"
                                            "    background-color: rgb(225, 210, 255);\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                            "     background-color:  rgb(235, 220, 255);\n"
                                            "}\n"
                                            "QPushButton:pressed {\n"
                                            "    background-color: rgb(192, 147, 255);\n"
                                            "}\n"
                                            "")
        self.btn_file_help_ok.setObjectName("btn_file_help_ok")
        self.btn_file_help_ok.setText("Зрозуміло")

        self.btn_file_help_ok.clicked.connect(self.file_help_ok)  # Обробка натискання кнопки закриття інструкції

        self.frame_file_help.show()  # Показ віджету інструкції

    # Закриття інструкції
    def file_help_ok(self):
        self.frame_file_help.hide()

    # Інструкція до панелі керування
    def control_help(self):
        # Створення віджету інструкції
        self.frame_control_help = QtWidgets.QFrame(self.centralwidget)
        self.frame_control_help.setGeometry(QtCore.QRect(10, 10, 580, 340))
        self.frame_control_help.setStyleSheet("background-color: rgb(219, 193, 255);\n"
                                              "border-radius: 10px;")
        self.frame_control_help.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_control_help.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_control_help.setObjectName("frame_control_help")

        # Заголовок інструкції
        self.label_control_help = QtWidgets.QLabel(self.frame_control_help)
        self.label_control_help.setGeometry(QtCore.QRect(0, 0, 580, 50))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_control_help.setFont(font)
        self.label_control_help.setAlignment(QtCore.Qt.AlignCenter)
        self.label_control_help.setWordWrap(False)
        self.label_control_help.setObjectName("label_control_help")
        self.label_control_help.setText("Управление")

        # Опис інтрукції
        self.label_control_help_description = QtWidgets.QLabel(self.frame_control_help)
        self.label_control_help_description.setGeometry(QtCore.QRect(10, 50, 560, 220))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_control_help_description.setFont(font)
        self.label_control_help_description.setAlignment(QtCore.Qt.AlignCenter)
        self.label_control_help_description.setWordWrap(True)
        self.label_control_help_description.setObjectName("label_control_help_description")
        self.label_control_help_description.setText(
            "Натиснувши кнопку «Старт» програма почне грати мелодію. Переконайтеся, що файл вибрано.\n"
            "Для коректної роботи змініть розкладку клавіатури на англійську.\n"
            "Щоб зупинити програму, натисніть на стоп кнопку. "
            "За замовчуванням це esc, але ви можете вибрати свою, "
            "натиснувши кнопку «esc» і потім натиснувши потрібну клавішу на клавіатурі.")

        # Кнопка закриття інструкції
        self.btn_control_help_ok = QtWidgets.QPushButton(self.frame_control_help)
        self.btn_control_help_ok.setGeometry(QtCore.QRect(190, 280, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.btn_control_help_ok.setFont(font)
        self.btn_control_help_ok.setStyleSheet("QPushButton {\n"
                                               "    background-color: rgb(225, 210, 255);\n"
                                               "}\n"
                                               "QPushButton:hover{\n"
                                               "     background-color:  rgb(235, 220, 255);\n"
                                               "}\n"
                                               "QPushButton:pressed {\n"
                                               "    background-color: rgb(192, 147, 255);\n"
                                               "}\n"
                                               "")
        self.btn_control_help_ok.setObjectName("btn_control_help_ok")
        self.btn_control_help_ok.setText("Зрозуміло")

        self.btn_control_help_ok.clicked.connect(self.control_help_ok)  # Обробка натискання кнопки закриття інструкції

        self.frame_control_help.show()  # Показ віджету інструкції

    # Закриття інструкції
    def control_help_ok(self):
        self.frame_control_help.hide()

    # Інструкція до панелі керування нотами
    def note_help(self):
        # Створення віджету інструкції
        self.frame_note_help = QtWidgets.QFrame(self.centralwidget)
        self.frame_note_help.setGeometry(QtCore.QRect(10, 10, 580, 340))
        self.frame_note_help.setStyleSheet("background-color: rgb(219, 193, 255);\n"
                                           "border-radius: 10px;")
        self.frame_note_help.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_note_help.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_note_help.setObjectName("frame_note_help")

        # Заголовок інструкції
        self.label_note_help = QtWidgets.QLabel(self.frame_note_help)
        self.label_note_help.setGeometry(QtCore.QRect(0, 0, 580, 50))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_note_help.setFont(font)
        self.label_note_help.setAlignment(QtCore.Qt.AlignCenter)
        self.label_note_help.setWordWrap(False)
        self.label_note_help.setObjectName("label_note_help")
        self.label_note_help.setText("Ноты")

        # Фото інтрукції
        self.photo_note_help = QtWidgets.QLabel(self.frame_note_help)
        self.photo_note_help.setGeometry(QtCore.QRect(10, 50, 560, 99))
        self.photo_note_help.setObjectName("photo_note_help")
        self.photo_note_help.setPixmap(QPixmap("note_help.png"))
        self.photo_note_help.setScaledContents(True)

        # Опис інтрукції
        self.label_note_help_description = QtWidgets.QLabel(self.frame_note_help)
        self.label_note_help_description.setGeometry(QtCore.QRect(20, 150, 540, 120))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_note_help_description.setFont(font)
        self.label_note_help_description.setAlignment(QtCore.Qt.AlignCenter)
        self.label_note_help_description.setWordWrap(True)
        self.label_note_help_description.setObjectName("label_note_help_description")
        self.label_note_help_description.setText(
            "Побудуйте «Піаніно» з 25 нот і на кожну ноту призначте клавіші, які вказані в програмі. "
            "Клавіші можна змінювати, клацнувши кнопку потрібної ноти в програмі і потім натиснувши "
            "клавішу на клавіатурі. Не забудьте також змінити її і в грі.")

        # Кнопка закриття інструкції
        self.btn_note_help_ok = QtWidgets.QPushButton(self.frame_note_help)
        self.btn_note_help_ok.setGeometry(QtCore.QRect(190, 280, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.btn_note_help_ok.setFont(font)
        self.btn_note_help_ok.setStyleSheet("QPushButton {\n"
                                            "    background-color: rgb(225, 210, 255);\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                            "     background-color:  rgb(235, 220, 255);\n"
                                            "}\n"
                                            "QPushButton:pressed {\n"
                                            "    background-color: rgb(192, 147, 255);\n"
                                            "}\n"
                                            "")
        self.btn_note_help_ok.setObjectName("btn_note_help_ok")
        self.btn_note_help_ok.setText("Зрозуміло")

        self.btn_note_help_ok.clicked.connect(self.note_help_ok)  # Обробка натискання кнопки закриття інструкції

        self.frame_note_help.show()  # Показ віджету інструкції

    # Закриття інструкції
    def note_help_ok(self):
        self.frame_note_help.hide()

    # Обробка натискань клавіш
    def on_press(self, key):
        # Зупинити якщо натиснута стоп кнопка
        if self.start is True:
            if key.name == self.btn_stop.text():
                self.start = False

        # Зміна стоп кнопки
        if self.stop_key is True:
            self.btn_stop.setText(key.name)
            self.stop_key = False

        # Зміна клавіш керування нотами
        if self.note_0 is True:
            self.btn_note_0.setText(key.name)
            self.note_0 = False

        if self.note_1 is True:
            self.btn_note_1.setText(key.name)
            self.note_1 = False

        if self.note_2 is True:
            self.btn_note_2.setText(key.name)
            self.note_2 = False

        if self.note_3 is True:
            self.btn_note_3.setText(key.name)
            self.note_3 = False

        if self.note_4 is True:
            self.btn_note_4.setText(key.name)
            self.note_4 = False

        if self.note_5 is True:
            self.btn_note_5.setText(key.name)
            self.note_5 = False

        if self.note_6 is True:
            self.btn_note_6.setText(key.name)
            self.note_6 = False

        if self.note_7 is True:
            self.btn_note_7.setText(key.name)
            self.note_7 = False

        if self.note_8 is True:
            self.btn_note_8.setText(key.name)
            self.note_8 = False

        if self.note_9 is True:
            self.btn_note_9.setText(key.name)
            self.note_9 = False

        if self.note_10 is True:
            self.btn_note_10.setText(key.name)
            self.note_10 = False

        if self.note_11 is True:
            self.btn_note_11.setText(key.name)
            self.note_11 = False

        if self.note_12 is True:
            self.btn_note_12.setText(key.name)
            self.note_12 = False

        if self.note_13 is True:
            self.btn_note_13.setText(key.name)
            self.note_13 = False

        if self.note_14 is True:
            self.btn_note_14.setText(key.name)
            self.note_14 = False

        if self.note_15 is True:
            self.btn_note_15.setText(key.name)
            self.note_15 = False

        if self.note_16 is True:
            self.btn_note_16.setText(key.name)
            self.note_16 = False

        if self.note_17 is True:
            self.btn_note_17.setText(key.name)
            self.note_17 = False

        if self.note_18 is True:
            self.btn_note_18.setText(key.name)
            self.note_18 = False

        if self.note_19 is True:
            self.btn_note_19.setText(key.name)
            self.note_19 = False

        if self.note_20 is True:
            self.btn_note_20.setText(key.name)
            self.note_20 = False

        if self.note_21 is True:
            self.btn_note_21.setText(key.name)
            self.note_21 = False

        if self.note_22 is True:
            self.btn_note_22.setText(key.name)
            self.note_22 = False

        if self.note_23 is True:
            self.btn_note_23.setText(key.name)
            self.note_23 = False

        if self.note_24 is True:
            self.btn_note_24.setText(key.name)
            self.note_24 = False


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # Зміна значка програми
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("NotePlay.ico"),
                   QtGui.QIcon.Selected, QtGui.QIcon.On)
    MainWindow.setWindowIcon(icon)

    MainWindow.show()
    sys.exit(app.exec_())
