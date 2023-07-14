from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PIL import Image
from ahk import AHK

ahk = AHK(executable_path='AutoHotkey\AutoHotkey.exe')
import mouse
import keyboard
import os

import numpy as np
import cv2 as cv
import math


class Ui_MainWindow(object):
    # Вікно програми (створено за допомогою QT Designer)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(600, 400)
        MainWindow.setStyleSheet("background-color: rgb(192, 147, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_image = QtWidgets.QFrame(self.centralwidget)
        self.frame_image.setGeometry(QtCore.QRect(10, 10, 285, 185))
        self.frame_image.setStyleSheet("background-color: rgb(219, 193, 255);\n"
                                       "border-radius: 10px;")
        self.frame_image.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_image.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_image.setObjectName("frame_image")
        self.label_image = QtWidgets.QLabel(self.frame_image)
        self.label_image.setGeometry(QtCore.QRect(0, 0, 285, 50))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_image.setFont(font)
        self.label_image.setAlignment(QtCore.Qt.AlignCenter)
        self.label_image.setWordWrap(False)
        self.label_image.setObjectName("label_image")
        self.btn_image = QtWidgets.QPushButton(self.frame_image)
        self.btn_image.setGeometry(QtCore.QRect(20, 50, 245, 50))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.btn_image.setFont(font)
        self.btn_image.setStyleSheet("QPushButton {\n"
                                     "    background-color: rgb(225, 210, 255);\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "     background-color:  rgb(235, 220, 255);\n"
                                     "}\n"
                                     "QPushButton:pressed {\n"
                                     "    background-color: rgb(192, 147, 255);\n"
                                     "}\n"
                                     "")
        self.btn_image.setObjectName("btn_image")

        self.btn_image_resize = QtWidgets.QPushButton(self.frame_image)
        self.btn_image_resize.setGeometry(QtCore.QRect(20, 105, 245, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.btn_image_resize.setFont(font)
        self.btn_image_resize.setStyleSheet("QPushButton {\n"
                                            "    background-color: rgb(225, 210, 255);\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                            "     background-color:  rgb(235, 220, 255);\n"
                                            "}\n"
                                            "QPushButton:pressed {\n"
                                            "    background-color: rgb(192, 147, 255);\n"
                                            "}\n"
                                            "")
        self.btn_image_resize.setObjectName("btn_image_resize")

        self.btn_image_post = QtWidgets.QPushButton(self.frame_image)
        self.btn_image_post.setGeometry(QtCore.QRect(20, 140, 245, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.btn_image_post.setFont(font)
        self.btn_image_post.setStyleSheet("QPushButton {\n"
                                          "    background-color: rgb(225, 210, 255);\n"
                                          "}\n"
                                          "QPushButton:hover{\n"
                                          "     background-color:  rgb(235, 220, 255);\n"
                                          "}\n"
                                          "QPushButton:pressed {\n"
                                          "    background-color: rgb(192, 147, 255);\n"
                                          "}\n"
                                          "")
        self.btn_image_post.setObjectName("btn_image_post")

        self.btn_image_help = QtWidgets.QPushButton(self.frame_image)
        self.btn_image_help.setGeometry(QtCore.QRect(10, 10, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.btn_image_help.setFont(font)
        self.btn_image_help.setStyleSheet("QPushButton {\n"
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
        self.btn_image_help.setObjectName("btn_image_help")
        self.frame_canvas = QtWidgets.QFrame(self.centralwidget)
        self.frame_canvas.setGeometry(QtCore.QRect(305, 10, 285, 185))
        self.frame_canvas.setStyleSheet("background-color: rgb(219, 193, 255);\n"
                                        "border-radius: 10px;")
        self.frame_canvas.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_canvas.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_canvas.setObjectName("frame_canvas")
        self.label_canvas = QtWidgets.QLabel(self.frame_canvas)
        self.label_canvas.setGeometry(QtCore.QRect(0, 0, 285, 50))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_canvas.setFont(font)
        self.label_canvas.setAlignment(QtCore.Qt.AlignCenter)
        self.label_canvas.setWordWrap(False)
        self.label_canvas.setObjectName("label_canvas")
        self.label_size = QtWidgets.QLabel(self.frame_canvas)
        self.label_size.setGeometry(QtCore.QRect(10, 50, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.label_size.setFont(font)
        self.label_size.setObjectName("label_size")
        self.lineEdit_sizex = QtWidgets.QLineEdit(self.frame_canvas)
        self.lineEdit_sizex.setEnabled(True)
        self.lineEdit_sizex.setGeometry(QtCore.QRect(90, 50, 60, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.lineEdit_sizex.setFont(font)
        self.lineEdit_sizex.setStyleSheet("background-color: rgb(225, 210, 255);")
        self.lineEdit_sizex.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_sizex.setObjectName("lineEdit_sizex")
        self.lineEdit_sizey = QtWidgets.QLineEdit(self.frame_canvas)
        self.lineEdit_sizey.setEnabled(True)
        self.lineEdit_sizey.setGeometry(QtCore.QRect(160, 50, 60, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.lineEdit_sizey.setFont(font)
        self.lineEdit_sizey.setStyleSheet("background-color: rgb(225, 210, 255);")
        self.lineEdit_sizey.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_sizey.setObjectName("lineEdit_sizey")
        self.label_corners = QtWidgets.QLabel(self.frame_canvas)
        self.label_corners.setGeometry(QtCore.QRect(10, 90, 60, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.label_corners.setFont(font)
        self.label_corners.setObjectName("label_corners")
        self.btn_corner1 = QtWidgets.QPushButton(self.frame_canvas)
        self.btn_corner1.setGeometry(QtCore.QRect(70, 90, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.btn_corner1.setFont(font)
        self.btn_corner1.setStyleSheet("QPushButton {\n"
                                       "    background-color: rgb(225, 210, 255);\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "     background-color:  rgb(235, 220, 255);\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: rgb(192, 147, 255);\n"
                                       "}\n"
                                       "")
        self.btn_corner1.setObjectName("btn_corner1")
        self.btn_corner2 = QtWidgets.QPushButton(self.frame_canvas)
        self.btn_corner2.setGeometry(QtCore.QRect(160, 90, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.btn_corner2.setFont(font)
        self.btn_corner2.setStyleSheet("QPushButton {\n"
                                       "    background-color: rgb(225, 210, 255);\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "     background-color:  rgb(235, 220, 255);\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: rgb(192, 147, 255);\n"
                                       "}\n"
                                       "")
        self.btn_corner2.setObjectName("btn_corner2")
        self.btn_corner3 = QtWidgets.QPushButton(self.frame_canvas)
        self.btn_corner3.setGeometry(QtCore.QRect(70, 130, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.btn_corner3.setFont(font)
        self.btn_corner3.setStyleSheet("QPushButton {\n"
                                       "    background-color: rgb(225, 210, 255);\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "     background-color:  rgb(235, 220, 255);\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: rgb(192, 147, 255);\n"
                                       "}\n"
                                       "")
        self.btn_corner3.setObjectName("btn_corner3")
        self.btn_corner4 = QtWidgets.QPushButton(self.frame_canvas)
        self.btn_corner4.setGeometry(QtCore.QRect(160, 130, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.btn_corner4.setFont(font)
        self.btn_corner4.setStyleSheet("QPushButton {\n"
                                       "    background-color: rgb(225, 210, 255);\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "     background-color:  rgb(235, 220, 255);\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: rgb(192, 147, 255);\n"
                                       "}\n"
                                       "")
        self.btn_corner4.setObjectName("btn_corner4")
        self.btn_canvas_help = QtWidgets.QPushButton(self.frame_canvas)
        self.btn_canvas_help.setGeometry(QtCore.QRect(10, 10, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.btn_canvas_help.setFont(font)
        self.btn_canvas_help.setStyleSheet("QPushButton {\n"
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
        self.btn_canvas_help.setObjectName("btn_canvas_help")
        self.frame_color = QtWidgets.QFrame(self.centralwidget)
        self.frame_color.setGeometry(QtCore.QRect(10, 205, 285, 185))
        self.frame_color.setStyleSheet("background-color: rgb(219, 193, 255);\n"
                                       "border-radius: 10px;")
        self.frame_color.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_color.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_color.setObjectName("frame_color")
        self.label_color = QtWidgets.QLabel(self.frame_color)
        self.label_color.setGeometry(QtCore.QRect(0, 0, 285, 50))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_color.setFont(font)
        self.label_color.setAlignment(QtCore.Qt.AlignCenter)
        self.label_color.setWordWrap(False)
        self.label_color.setObjectName("label_color")
        self.label_red = QtWidgets.QLabel(self.frame_color)
        self.label_red.setGeometry(QtCore.QRect(10, 50, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.label_red.setFont(font)
        self.label_red.setObjectName("label_red")
        self.label_blue = QtWidgets.QLabel(self.frame_color)
        self.label_blue.setGeometry(QtCore.QRect(10, 110, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.label_blue.setFont(font)
        self.label_blue.setObjectName("label_blue")
        self.label_green = QtWidgets.QLabel(self.frame_color)
        self.label_green.setGeometry(QtCore.QRect(10, 80, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.label_green.setFont(font)
        self.label_green.setObjectName("label_green")
        self.btn_red1 = QtWidgets.QPushButton(self.frame_color)
        self.btn_red1.setGeometry(QtCore.QRect(110, 55, 70, 25))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.btn_red1.setFont(font)
        self.btn_red1.setStyleSheet("QPushButton {\n"
                                    "    background-color: rgb(225, 210, 255);\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                    "     background-color:  rgb(235, 220, 255);\n"
                                    "}\n"
                                    "QPushButton:pressed {\n"
                                    "    background-color: rgb(192, 147, 255);\n"
                                    "}\n"
                                    "")
        self.btn_red1.setObjectName("btn_red1")
        self.btn_red2 = QtWidgets.QPushButton(self.frame_color)
        self.btn_red2.setGeometry(QtCore.QRect(190, 55, 70, 25))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.btn_red2.setFont(font)
        self.btn_red2.setStyleSheet("QPushButton {\n"
                                    "    background-color: rgb(225, 210, 255);\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                    "     background-color:  rgb(235, 220, 255);\n"
                                    "}\n"
                                    "QPushButton:pressed {\n"
                                    "    background-color: rgb(192, 147, 255);\n"
                                    "}\n"
                                    "")
        self.btn_red2.setObjectName("btn_red2")
        self.btn_blue1 = QtWidgets.QPushButton(self.frame_color)
        self.btn_blue1.setGeometry(QtCore.QRect(110, 115, 70, 25))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.btn_blue1.setFont(font)
        self.btn_blue1.setStyleSheet("QPushButton {\n"
                                     "    background-color: rgb(225, 210, 255);\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "     background-color:  rgb(235, 220, 255);\n"
                                     "}\n"
                                     "QPushButton:pressed {\n"
                                     "    background-color: rgb(192, 147, 255);\n"
                                     "}\n"
                                     "")
        self.btn_blue1.setObjectName("btn_blue1")
        self.btn_green1 = QtWidgets.QPushButton(self.frame_color)
        self.btn_green1.setGeometry(QtCore.QRect(110, 85, 70, 25))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.btn_green1.setFont(font)
        self.btn_green1.setStyleSheet("QPushButton {\n"
                                      "    background-color: rgb(225, 210, 255);\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "     background-color:  rgb(235, 220, 255);\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color: rgb(192, 147, 255);\n"
                                      "}\n"
                                      "")
        self.btn_green1.setObjectName("btn_green1")
        self.btn_blue2 = QtWidgets.QPushButton(self.frame_color)
        self.btn_blue2.setGeometry(QtCore.QRect(190, 115, 70, 25))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.btn_blue2.setFont(font)
        self.btn_blue2.setStyleSheet("QPushButton {\n"
                                     "    background-color: rgb(225, 210, 255);\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "     background-color:  rgb(235, 220, 255);\n"
                                     "}\n"
                                     "QPushButton:pressed {\n"
                                     "    background-color: rgb(192, 147, 255);\n"
                                     "}\n"
                                     "")
        self.btn_blue2.setObjectName("btn_blue2")
        self.btn_green2 = QtWidgets.QPushButton(self.frame_color)
        self.btn_green2.setGeometry(QtCore.QRect(190, 85, 70, 25))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.btn_green2.setFont(font)
        self.btn_green2.setStyleSheet("QPushButton {\n"
                                      "    background-color: rgb(225, 210, 255);\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "     background-color:  rgb(235, 220, 255);\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color: rgb(192, 147, 255);\n"
                                      "}\n"
                                      "")
        self.btn_green2.setObjectName("btn_green2")
        self.btn_color_help = QtWidgets.QPushButton(self.frame_color)
        self.btn_color_help.setGeometry(QtCore.QRect(10, 10, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.btn_color_help.setFont(font)
        self.btn_color_help.setStyleSheet("QPushButton {\n"
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
        self.btn_color_help.setObjectName("btn_color_help")

        self.frame_control = QtWidgets.QFrame(self.centralwidget)
        self.frame_control.setGeometry(QtCore.QRect(305, 205, 285, 185))
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
        self.label_stop.setGeometry(QtCore.QRect(10, 100, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.label_stop.setFont(font)
        self.label_stop.setObjectName("label_stop")
        self.btn_stop = QtWidgets.QPushButton(self.frame_control)
        self.btn_stop.setGeometry(QtCore.QRect(140, 95, 80, 35))
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
        self.label_start_with = QtWidgets.QLabel(self.frame_control)
        self.label_start_with.setGeometry(QtCore.QRect(10, 135, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.label_start_with.setFont(font)
        self.label_start_with.setObjectName("label_start_with")
        self.lineEdit_startx = QtWidgets.QLineEdit(self.frame_control)
        self.lineEdit_startx.setEnabled(True)
        self.lineEdit_startx.setGeometry(QtCore.QRect(110, 135, 50, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.lineEdit_startx.setFont(font)
        self.lineEdit_startx.setStyleSheet("background-color: rgb(225, 210, 255);")
        self.lineEdit_startx.setInputMask("")
        self.lineEdit_startx.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_startx.setObjectName("lineEdit_startx")
        self.lineEdit_starty = QtWidgets.QLineEdit(self.frame_control)
        self.lineEdit_starty.setEnabled(True)
        self.lineEdit_starty.setGeometry(QtCore.QRect(170, 135, 50, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.lineEdit_starty.setFont(font)
        self.lineEdit_starty.setStyleSheet("background-color: rgb(225, 210, 255);")
        self.lineEdit_starty.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_starty.setObjectName("lineEdit_starty")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "PixelDraw"))
        self.label_image.setText(_translate("MainWindow", "Зображення"))
        self.btn_image.setText(_translate("MainWindow", "Вибрати зображення"))

        self.btn_image_resize.setText(_translate("MainWindow", "Змінити розмір"))
        self.btn_image_post.setText(_translate("MainWindow", "Постеризувати"))

        self.btn_image_help.setText(_translate("MainWindow", "?"))
        self.label_canvas.setText(_translate("MainWindow", "Полотно"))
        self.label_size.setText(_translate("MainWindow", "Розмір:"))
        self.label_corners.setText(_translate("MainWindow", "Кути:"))
        self.btn_corner1.setText(_translate("MainWindow", "1"))
        self.btn_corner2.setText(_translate("MainWindow", "2"))
        self.btn_corner3.setText(_translate("MainWindow", "3"))
        self.btn_corner4.setText(_translate("MainWindow", "4"))
        self.btn_canvas_help.setText(_translate("MainWindow", "?"))
        self.label_color.setText(_translate("MainWindow", "Вибір кольору"))
        self.label_red.setText(_translate("MainWindow", "Червоний:"))
        self.label_blue.setText(_translate("MainWindow", "Синій:"))
        self.label_green.setText(_translate("MainWindow", "Зелёний:"))
        self.btn_red1.setText(_translate("MainWindow", "1"))
        self.btn_red2.setText(_translate("MainWindow", "2"))
        self.btn_blue1.setText(_translate("MainWindow", "1"))
        self.btn_green1.setText(_translate("MainWindow", "1"))
        self.btn_blue2.setText(_translate("MainWindow", "2"))
        self.btn_green2.setText(_translate("MainWindow", "2"))
        self.btn_color_help.setText(_translate("MainWindow", "?"))
        self.label_control.setText(_translate("MainWindow", "Керування"))
        self.btn_start.setText(_translate("MainWindow", "Старт"))
        self.label_stop.setText(_translate("MainWindow", "Стоп кнопка:"))
        self.btn_stop.setText(_translate("MainWindow", "esc"))
        self.label_start_with.setText(_translate("MainWindow", "Почати з:"))
        self.lineEdit_startx.setText(_translate("MainWindow", "0"))
        self.lineEdit_starty.setText(_translate("MainWindow", "0"))
        self.btn_control_help.setText(_translate("MainWindow", "?"))

    # Реалізація функціоналу програми
    def add_functions(self):
        self.btn_image.clicked.connect(self.choose_file)  # Вибір файла
        self.btn_image_resize.clicked.connect(self.image_resize)  # Кнопка зміни розміру зображення
        self.btn_image_post.clicked.connect(self.image_post)  # Кнопка постеризації зображення

        # Координати кутів полотна
        self.btn_corner1.clicked.connect(self.corner1)
        self.btn_corner2.clicked.connect(self.corner2)
        self.btn_corner3.clicked.connect(self.corner3)
        self.btn_corner4.clicked.connect(self.corner4)

        # Координати палітри кольорів
        self.btn_red1.clicked.connect(self.red1)
        self.btn_red2.clicked.connect(self.red2)
        self.btn_green1.clicked.connect(self.green1)
        self.btn_green2.clicked.connect(self.green2)
        self.btn_blue1.clicked.connect(self.blue1)
        self.btn_blue2.clicked.connect(self.blue2)

        self.btn_start.clicked.connect(self.start)  # Запуск програми
        self.btn_stop.clicked.connect(self.stop)  # Зміна стоп кнопки

        # Інструкції до інструментів
        self.btn_image_help.clicked.connect(self.image_help)
        self.btn_canvas_help.clicked.connect(self.canvas_help)
        self.btn_color_help.clicked.connect(self.color_help)
        self.btn_control_help.clicked.connect(self.control_help)

        self.fname = None  # Шлях до вибраного файлу
        self.resize = False  # Індикатор зміни розміру зображення
        self.post = False  # Індикатор постеризації зображення

        self.img_error = False  # Індикатор помилки зображення

        # Індикатори зміни координат палітри
        self.r1 = None
        self.r2 = None
        self.g1 = None
        self.g2 = None
        self.b1 = None
        self.b2 = None

        self.start = False  # Індикатор запуску
        self.stop_key = False  # Індикатор зміни стоп кнопки

        keyboard.on_press(self.on_press)  # Обробка натискань клавіш

    # Вибір файлу
    def choose_file(self):
        self.fname = \
            QtWidgets.QFileDialog.getOpenFileName(None, 'Open File', None, 'JPG File (*.jpg);;PNG File (*.png)')[0]
        if self.fname != '':
            self.btn_image.setText(os.path.basename(self.fname))
            font = QtGui.QFont()
            font.setFamily("Comic Sans MS")
            font.setPointSize(10)
            self.btn_image.setFont(font)

    # Кнопка зміни розміру зображення
    def image_resize(self):
        if self.resize:
            if self.img_error is False:
                self.btn_image_resize.setStyleSheet("QPushButton {background-color: rgb(225, 210, 255);}"
                                                    "QPushButton:hover {background-color:  rgb(235, 220, 255);}"
                                                    "QPushButton:pressed {background-color: rgb(192, 147, 255);}")
            else:
                self.btn_image_resize.setStyleSheet("QPushButton {background-color: rgb(255, 170, 170);}"
                                                    "QPushButton:hover {background-color:  rgb(255, 180, 180);}"
                                                    "QPushButton:pressed {background-color: rgb(255, 130, 130);}")
            self.resize = False
        else:
            if self.img_error is False:
                self.btn_image_resize.setStyleSheet("QPushButton {background-color: rgb(192, 147, 255);}"
                                                    "QPushButton:pressed {background-color: rgb(225, 210, 255);}")
            else:
                self.btn_image_resize.setStyleSheet("QPushButton {background-color: rgb(255, 130, 130);}"
                                                    "QPushButton:pressed {background-color: rgb(255, 170, 170);}")
            self.resize = True

    # Кнопка постеризації зображення
    def image_post(self):
        if self.post:
            if self.img_error is False:
                self.btn_image_post.setStyleSheet("QPushButton {background-color: rgb(225, 210, 255);}"
                                                  "QPushButton:hover {background-color:  rgb(235, 220, 255);}"
                                                  "QPushButton:pressed {background-color: rgb(192, 147, 255);}")
            else:
                self.btn_image_post.setStyleSheet("QPushButton {background-color: rgb(255, 170, 170);}"
                                                  "QPushButton:hover {background-color:  rgb(255, 180, 180);}"
                                                  "QPushButton:pressed {background-color: rgb(255, 130, 130);}")

            self.btn_image_post.setGeometry(QtCore.QRect(20, 140, 245, 30))

            self.lineEdit_post_level.hide()

            self.post = False
        else:
            self.btn_image_post.setGeometry(QtCore.QRect(20, 140, 180, 30))

            self.lineEdit_post_level = QtWidgets.QLineEdit(self.frame_image)
            self.lineEdit_post_level.setEnabled(True)
            self.lineEdit_post_level.setGeometry(QtCore.QRect(205, 140, 60, 30))
            font = QtGui.QFont()
            font.setFamily("Comic Sans MS")
            font.setPointSize(15)
            self.lineEdit_post_level.setFont(font)
            self.lineEdit_post_level.setStyleSheet("background-color: rgb(225, 210, 255);")
            self.lineEdit_post_level.setAlignment(QtCore.Qt.AlignCenter)
            self.lineEdit_post_level.setObjectName("lineEdit_post_level")
            self.lineEdit_post_level.setText("10")

            if self.img_error is False:
                self.btn_image_post.setStyleSheet("QPushButton {background-color: rgb(192, 147, 255);}" \
                                                  "QPushButton:pressed {background-color: rgb(225, 210, 255);}")
                self.lineEdit_post_level.setStyleSheet("background-color: rgb(225, 210, 255);")
            else:
                self.btn_image_post.setStyleSheet("QPushButton {background-color: rgb(255, 130, 130);}" \
                                                  "QPushButton:pressed {background-color: rgb(255, 170, 170);}")
                self.lineEdit_post_level.setStyleSheet("background-color: rgb(255, 170, 170);")

            self.lineEdit_post_level.show()

            self.post = True

    # Кнопки зміни координат кутів полотна 
    def corner1(self):
        mouse.wait("left")
        print(ahk.mouse_position)
        self.btn_corner1.setText(str(ahk.mouse_position[0]) + ", " + str(ahk.mouse_position[1]))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.btn_corner1.setFont(font)

    def corner2(self):
        mouse.wait("left")
        print(ahk.mouse_position)
        self.btn_corner2.setText(str(ahk.mouse_position[0]) + ", " + str(ahk.mouse_position[1]))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.btn_corner2.setFont(font)

    def corner3(self):
        mouse.wait("left")
        print(ahk.mouse_position)
        self.btn_corner3.setText(str(ahk.mouse_position[0]) + ", " + str(ahk.mouse_position[1]))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.btn_corner3.setFont(font)

    def corner4(self):
        mouse.wait("left")
        print(ahk.mouse_position)
        self.btn_corner4.setText(str(ahk.mouse_position[0]) + ", " + str(ahk.mouse_position[1]))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.btn_corner4.setFont(font)

    # Кнопки зміни координат палітри
    def red1(self):
        mouse.wait("left")
        self.btn_red1.setText(str(ahk.mouse_position[0]) + ", " + str(ahk.mouse_position[1]))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.btn_red1.setFont(font)
        self.r1 = [ahk.mouse_position[0], ahk.mouse_position[1]]

    def red2(self):
        mouse.wait("left")
        self.btn_red2.setText(str(ahk.mouse_position[0]) + ", " + str(ahk.mouse_position[1]))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.btn_red2.setFont(font)
        self.r2 = [ahk.mouse_position[0], ahk.mouse_position[1]]

    def green1(self):
        mouse.wait("left")
        self.btn_green1.setText(str(ahk.mouse_position[0]) + ", " + str(ahk.mouse_position[1]))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.btn_green1.setFont(font)
        self.g1 = [ahk.mouse_position[0], ahk.mouse_position[1]]

        if self.r2 is not None:
            print(self.r2)
            self.btn_red1.setText(str(self.g1[0]) + ", " + str(self.r2[1]))
            font = QtGui.QFont()
            font.setFamily("Comic Sans MS")
            font.setPointSize(10)
            self.btn_red1.setFont(font)

            self.btn_green2.setText(str(self.r2[0]) + ", " + str(self.g1[1]))
            font = QtGui.QFont()
            font.setFamily("Comic Sans MS")
            font.setPointSize(10)
            self.btn_green2.setFont(font)

            self.btn_blue1.setText(str(self.g1[0]) + ", " + str(self.g1[1] + (self.g1[1] - self.r2[1])))
            font = QtGui.QFont()
            font.setFamily("Comic Sans MS")
            font.setPointSize(10)
            self.btn_blue1.setFont(font)

            self.btn_blue2.setText(str(self.r2[0]) + ", " + str(self.g1[1] + (self.g1[1] - self.r2[1])))
            font = QtGui.QFont()
            font.setFamily("Comic Sans MS")
            font.setPointSize(10)
            self.btn_blue2.setFont(font)

    def green2(self):
        mouse.wait("left")
        self.btn_green2.setText(str(ahk.mouse_position[0]) + ", " + str(ahk.mouse_position[1]))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.btn_green2.setFont(font)
        self.g2 = [ahk.mouse_position[0], ahk.mouse_position[1]]

    def blue1(self):
        mouse.wait("left")
        self.btn_blue1.setText(str(ahk.mouse_position[0]) + ", " + str(ahk.mouse_position[1]))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.btn_blue1.setFont(font)
        self.b1 = [ahk.mouse_position[0], ahk.mouse_position[1]]

    def blue2(self):
        mouse.wait("left")
        self.btn_blue2.setText(str(ahk.mouse_position[0]) + ", " + str(ahk.mouse_position[1]))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.btn_blue2.setFont(font)
        self.b2 = [ahk.mouse_position[0], ahk.mouse_position[1]]

    # Запуск програми
    def start(self):
        global size

        global n1n
        global n2n
        global n3n
        global n4n

        global r1
        global r2
        global g1
        global g2
        global b1
        global b2

        alright = True

        # Стилі об'єктів
        frame_style = "background-color: rgb(219, 193, 255);border-radius: 10px;"
        lineEdit_style = "background-color: rgb(225, 210, 255);"
        btn_style = "QPushButton {background-color: rgb(225, 210, 255);}" \
                    "QPushButton:hover {background-color:  rgb(235, 220, 255);}" \
                    "QPushButton:pressed {background-color: rgb(192, 147, 255);}"
        btn_on_style = "QPushButton {background-color: rgb(192, 147, 255);}" \
                       "QPushButton:pressed {background-color: rgb(225, 210, 255);}"

        # Стилі об'єктів при помилці
        frame_style_error = "background-color: rgb(255, 150, 150);border-radius: 10px;"
        lineEdit_style_error = "background-color: rgb(255, 170, 170);"
        btn_style_error = "QPushButton {background-color: rgb(255, 170, 170);}" \
                          "QPushButton:hover {background-color:  rgb(255, 180, 180);}" \
                          "QPushButton:pressed {background-color: rgb(255, 130, 130);}"
        btn_on_style_error = "QPushButton {background-color: rgb(255, 130, 130);}" \
                             "QPushButton:pressed {background-color: rgb(255, 170, 170);}"

        # Перевірка помилок та наявність всіх даних
        try:
            img = Image.open(self.fname).convert("RGBA")
            print(img.mode)

            if self.resize:
                self.btn_image_resize.setStyleSheet(btn_on_style)
            else:
                self.btn_image_resize.setStyleSheet(btn_style)

            if self.post:
                self.btn_image_post.setStyleSheet(btn_on_style)
                self.lineEdit_post_level.setStyleSheet(lineEdit_style)

                try:
                    post_level = int(self.lineEdit_post_level.text())
                except:
                    self.lineEdit_post_level.setStyleSheet(lineEdit_style_error)
                    alright = False
            else:
                self.btn_image_post.setStyleSheet(btn_style)

            self.frame_image.setStyleSheet(frame_style)
            self.btn_image.setStyleSheet(btn_style)
            self.btn_image_help.setStyleSheet(btn_style)

            self.img_error = False
        except:
            self.frame_image.setStyleSheet(frame_style_error)
            self.btn_image.setStyleSheet(btn_style_error)
            self.btn_image_help.setStyleSheet(btn_style_error)

            if self.resize:
                self.btn_image_resize.setStyleSheet(btn_on_style_error)
            else:
                self.btn_image_resize.setStyleSheet(btn_style_error)

            if self.post:
                self.btn_image_post.setStyleSheet(btn_on_style_error)
                self.lineEdit_post_level.setStyleSheet(lineEdit_style_error)
            else:
                self.btn_image_post.setStyleSheet(btn_style_error)

            self.img_error = True
            alright = False

        try:
            cor = [int(self.lineEdit_startx.text()), int(self.lineEdit_starty.text())]
            self.frame_control.setStyleSheet(frame_style)
            self.btn_start.setStyleSheet(btn_style)
            self.btn_stop.setStyleSheet(btn_style)
            self.lineEdit_startx.setStyleSheet(lineEdit_style)
            self.lineEdit_starty.setStyleSheet(lineEdit_style)
            self.btn_control_help.setStyleSheet(btn_style)
        except:
            self.frame_control.setStyleSheet(frame_style_error)
            self.btn_start.setStyleSheet(btn_style_error)
            self.btn_stop.setStyleSheet(btn_style_error)
            self.lineEdit_startx.setStyleSheet(lineEdit_style_error)
            self.lineEdit_starty.setStyleSheet(lineEdit_style_error)
            self.btn_control_help.setStyleSheet(btn_style_error)
            alright = False

        try:
            size = [int(self.lineEdit_sizex.text()) - 1, int(self.lineEdit_sizey.text()) - 1]
            n1n = [int(self.btn_corner1.text().split(", ")[0]), int(self.btn_corner1.text().split(", ")[1])]
            n2n = [int(self.btn_corner2.text().split(", ")[0]), int(self.btn_corner2.text().split(", ")[1])]
            n3n = [int(self.btn_corner3.text().split(", ")[0]), int(self.btn_corner3.text().split(", ")[1])]
            n4n = [int(self.btn_corner4.text().split(", ")[0]), int(self.btn_corner4.text().split(", ")[1])]
            self.frame_canvas.setStyleSheet(frame_style)
            self.lineEdit_sizex.setStyleSheet(lineEdit_style)
            self.lineEdit_sizey.setStyleSheet(lineEdit_style)
            self.btn_corner1.setStyleSheet(btn_style)
            self.btn_corner2.setStyleSheet(btn_style)
            self.btn_corner3.setStyleSheet(btn_style)
            self.btn_corner4.setStyleSheet(btn_style)
            self.btn_canvas_help.setStyleSheet(btn_style)
        except:
            self.frame_canvas.setStyleSheet(frame_style_error)
            self.lineEdit_sizex.setStyleSheet(lineEdit_style_error)
            self.lineEdit_sizey.setStyleSheet(lineEdit_style_error)
            self.btn_corner1.setStyleSheet(btn_style_error)
            self.btn_corner2.setStyleSheet(btn_style_error)
            self.btn_corner3.setStyleSheet(btn_style_error)
            self.btn_corner4.setStyleSheet(btn_style_error)
            self.btn_canvas_help.setStyleSheet(btn_style_error)
            alright = False

        try:
            r1 = [int(self.btn_red1.text().split(", ")[0]), int(self.btn_red1.text().split(", ")[1])]
            r2 = [int(self.btn_red2.text().split(", ")[0]), int(self.btn_red2.text().split(", ")[1])]
            g1 = [int(self.btn_green1.text().split(", ")[0]), int(self.btn_green1.text().split(", ")[1])]
            g2 = [int(self.btn_green2.text().split(", ")[0]), int(self.btn_green2.text().split(", ")[1])]
            b1 = [int(self.btn_blue1.text().split(", ")[0]), int(self.btn_blue1.text().split(", ")[1])]
            b2 = [int(self.btn_blue2.text().split(", ")[0]), int(self.btn_blue2.text().split(", ")[1])]
            self.frame_color.setStyleSheet(frame_style)
            self.btn_red1.setStyleSheet(btn_style)
            self.btn_red2.setStyleSheet(btn_style)
            self.btn_green1.setStyleSheet(btn_style)
            self.btn_green2.setStyleSheet(btn_style)
            self.btn_blue1.setStyleSheet(btn_style)
            self.btn_blue2.setStyleSheet(btn_style)
            self.btn_color_help.setStyleSheet(btn_style)
        except:
            self.frame_color.setStyleSheet(frame_style_error)
            self.btn_red1.setStyleSheet(btn_style_error)
            self.btn_red2.setStyleSheet(btn_style_error)
            self.btn_green1.setStyleSheet(btn_style_error)
            self.btn_green2.setStyleSheet(btn_style_error)
            self.btn_blue1.setStyleSheet(btn_style_error)
            self.btn_blue2.setStyleSheet(btn_style_error)
            self.btn_color_help.setStyleSheet(btn_style_error)
            alright = False

        if alright is False:
            return

        # Зміна розміру зображення за потреби
        if self.resize:
            img = img.reduce(math.floor(min(img.size[0] / size[0], img.size[1] / size[1])))

        # Постеризація зображення
        if self.post:
            img.save("image.png")
            img = cv.imread("image.png")
            Z = img.reshape((-1, 3))

            # convert to np.float32
            Z = np.float32(Z)

            # define criteria, number of clusters(K) and apply kmeans()
            criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
            K = post_level
            ret, label, center = cv.kmeans(Z, K, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)

            # Now convert back into uint8, and make original image
            center = np.uint8(center)
            res = center[label.flatten()]
            res2 = res.reshape((img.shape))

            cv.imwrite("image.png", res2)

            img = Image.open("image.png")

            r = -1
            g = -1
            b = -1

            # Створення списку всіх кольорів зображення
            colors = []
            for y in range(size[1] + 1):
                for x in range(size[0] + 1):
                    if y > cor[1] or (y == cor[1] and x >= cor[0]):
                        if img.getpixel((x, y)) not in colors:
                            colors.append(img.getpixel((x, y)))
            print(colors)

            self.start = True

            self.color(0, 0, 0)

            # Малювання зображення
            for color in colors:
                self.color(color[0], color[1], color[2])
                for y in range(size[1] + 1):
                    pixels_line = []
                    for x in range(size[0] + 1):
                        if y > cor[1] or (y == cor[1] and x >= cor[0]):
                            if img.getpixel((x, y)) == color:
                                pixels_line.append(x)

                    pixels = {}

                    for i in range(len(pixels_line)):
                        if i == 0:
                            pixels[pixels_line[i]] = "s"

                        elif pixels_line[i] - pixels_line[i - 1] == 1:
                            pixels[pixels_line[i]] = ""
                        else:
                            if pixels[pixels_line[i - 1]] == "s":
                                pixels[pixels_line[i - 1]] = "cl"
                            else:
                                pixels[pixels_line[i - 1]] = "f"
                            pixels[pixels_line[i]] = "s"

                        if i == len(pixels_line) - 1:
                            if pixels[pixels_line[i - 1]] == "f" or pixels[pixels_line[i - 1]] == "cl" or pixels[
                                pixels_line[i]] == "s":
                                pixels[pixels_line[i]] = "cl"
                            else:
                                pixels[pixels_line[i]] = "f"

                    print(pixels)

                    start = None
                    finish = None
                    for key, value in pixels.items():
                        if self.start is False:
                            return
                        if value == "cl":
                            self.click(key, y)
                        if value == "s":
                            start = key
                        if value == "f":
                            finish = key
                            print(start, ' ', y, ' ', finish, ' ', y)
                            self.drag(start, y, finish, y)
        else:
            a = cor[1] * (size[0] + 1) + cor[0]

            r = -1
            g = -1
            b = -1

            self.start = True

            self.color(0, 0, 0)

            while a < (size[0] + 1) * (size[1] + 1) and self.start is True:
                col = img.getpixel((cor[0], cor[1]))
                print(col)

                if os.path.splitext(self.fname)[1] == ".jpg" or col[3] == 255:
                    if r != col[0] or g != col[1] or b != col[2]:
                        self.color(col[0], col[1], col[2])
                    self.click(cor[0], cor[1])
                cor[0] = cor[0] + 1
                if cor[0] > size[0]:
                    cor[0] = 0
                    cor[1] = cor[1] + 1
                a = a + 1
                r = col[0]
                g = col[1]
                b = col[2]

    # Зміна стоп кнопки
    def stop(self):
        self.stop_key = True

    # Інструкція до панелі зображення
    def image_help(self):
        # Створення віджету інструкції
        self.frame_image_help = QtWidgets.QFrame(self.centralwidget)
        self.frame_image_help.setGeometry(QtCore.QRect(10, 10, 580, 380))
        self.frame_image_help.setStyleSheet("background-color: rgb(219, 193, 255);\n"
                                            "border-radius: 10px;")
        self.frame_image_help.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_image_help.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_image_help.setObjectName("frame_image_help")

        # Заголовок інструкції
        self.label_image_help = QtWidgets.QLabel(self.frame_image_help)
        self.label_image_help.setGeometry(QtCore.QRect(0, 0, 580, 50))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_image_help.setFont(font)
        self.label_image_help.setAlignment(QtCore.Qt.AlignCenter)
        self.label_image_help.setWordWrap(False)
        self.label_image_help.setObjectName("label_image_help")
        self.label_image_help.setText("Зображення")

        # Опис інтрукції
        self.label_image_help_description = QtWidgets.QLabel(self.frame_image_help)
        self.label_image_help_description.setGeometry(QtCore.QRect(10, 50, 560, 230))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_image_help_description.setFont(font)
        self.label_image_help_description.setAlignment(QtCore.Qt.AlignCenter)
        self.label_image_help_description.setWordWrap(True)
        self.label_image_help_description.setObjectName("label_image_help_description")
        self.label_image_help_description.setText(
            "Натиснувши кнопку «Вибрати зображення», ви можете вибрати файл, який хочете намалювати. "
            "Підтримуються лише JPG та PNG формати.\n"
            "Функція «Змінити розмір» робить розмір зображення, як у полотна.\n"
            "Функція «Постеризувати» обмежує кількість кольорів на зображенні до заданої кількості. "
            "Це дозволить прискорити процес малювання. Чим менше кольорів, тим швидше.")

        # Кнопка закриття інструкції
        self.btn_image_help_ok = QtWidgets.QPushButton(self.frame_image_help)
        self.btn_image_help_ok.setGeometry(QtCore.QRect(190, 320, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.btn_image_help_ok.setFont(font)
        self.btn_image_help_ok.setStyleSheet("QPushButton {\n"
                                             "    background-color: rgb(225, 210, 255);\n"
                                             "}\n"
                                             "QPushButton:hover{\n"
                                             "     background-color:  rgb(235, 220, 255);\n"
                                             "}\n"
                                             "QPushButton:pressed {\n"
                                             "    background-color: rgb(192, 147, 255);\n"
                                             "}\n"
                                             "")
        self.btn_image_help_ok.setObjectName("btn_image_help_ok")
        self.btn_image_help_ok.setText("Зрозуміло")

        self.btn_image_help_ok.clicked.connect(self.image_help_ok)  # Обробка натискання кнопки закриття інструкції

        self.frame_image_help.show()  # Показ віджету інструкції

    # Закриття інструкції
    def image_help_ok(self):
        self.frame_image_help.hide()

    # Інструкція до панелі полотна
    def canvas_help(self):
        # Створення віджету інструкції
        self.frame_canvas_help = QtWidgets.QFrame(self.centralwidget)
        self.frame_canvas_help.setGeometry(QtCore.QRect(10, 10, 580, 380))
        self.frame_canvas_help.setStyleSheet("background-color: rgb(219, 193, 255);\n"
                                             "border-radius: 10px;")
        self.frame_canvas_help.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_canvas_help.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_canvas_help.setObjectName("frame_canvas_help")

        # Заголовок інструкції
        self.label_canvas_help = QtWidgets.QLabel(self.frame_canvas_help)
        self.label_canvas_help.setGeometry(QtCore.QRect(0, 0, 580, 50))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_canvas_help.setFont(font)
        self.label_canvas_help.setAlignment(QtCore.Qt.AlignCenter)
        self.label_canvas_help.setWordWrap(False)
        self.label_canvas_help.setObjectName("label_canvas_help")
        self.label_canvas_help.setText("Полотно")

        # Фото інтрукції
        self.photo_canvas_help = QtWidgets.QLabel(self.frame_canvas_help)
        self.photo_canvas_help.setGeometry(QtCore.QRect(10, 60, 236, 221))
        self.photo_canvas_help.setObjectName("photo_canvas_help")
        self.photo_canvas_help.setPixmap(QPixmap("canvas_help.png"))
        self.photo_canvas_help.setScaledContents(True)

        # Опис інтрукції
        self.label_canvas_help_description = QtWidgets.QLabel(self.frame_canvas_help)
        self.label_canvas_help_description.setGeometry(QtCore.QRect(260, 50, 300, 240))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_canvas_help_description.setFont(font)
        self.label_canvas_help_description.setAlignment(QtCore.Qt.AlignCenter)
        self.label_canvas_help_description.setWordWrap(True)
        self.label_canvas_help_description.setObjectName("label_canvas_help_description")
        self.label_canvas_help_description.setText(
            "Вкажіть розмір полотна. У першому полі потрібно вписати кількість пікселів по горизонталі, "
            "у друге - по вертикалі.\nНатиснувши на кнопки з номерами і потім клацнувши по кутовому блоку полотна, "
            "з таким самим номером (як показано на картинці), ви вкажете координати кута полотна.")

        self.label_canvas_help_1 = QtWidgets.QLabel(self.frame_canvas_help)
        self.label_canvas_help_1.setGeometry(QtCore.QRect(20, 70, 50, 50))
        self.label_canvas_help_1.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_canvas_help_1.setFont(font)
        self.label_canvas_help_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_canvas_help_1.setWordWrap(False)
        self.label_canvas_help_1.setObjectName("label_canvas_help_1")
        self.label_canvas_help_1.setText("1")

        self.label_canvas_help_2 = QtWidgets.QLabel(self.frame_canvas_help)
        self.label_canvas_help_2.setGeometry(QtCore.QRect(190, 70, 50, 50))
        self.label_canvas_help_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_canvas_help_2.setFont(font)
        self.label_canvas_help_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_canvas_help_2.setWordWrap(False)
        self.label_canvas_help_2.setObjectName("label_canvas_help_2")
        self.label_canvas_help_2.setText("2")

        self.label_canvas_help_3 = QtWidgets.QLabel(self.frame_canvas_help)
        self.label_canvas_help_3.setGeometry(QtCore.QRect(10, 220, 50, 50))
        self.label_canvas_help_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_canvas_help_3.setFont(font)
        self.label_canvas_help_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_canvas_help_3.setWordWrap(False)
        self.label_canvas_help_3.setObjectName("label_canvas_help_3")
        self.label_canvas_help_3.setText("3")

        self.label_canvas_help_4 = QtWidgets.QLabel(self.frame_canvas_help)
        self.label_canvas_help_4.setGeometry(QtCore.QRect(200, 220, 50, 50))
        self.label_canvas_help_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_canvas_help_4.setFont(font)
        self.label_canvas_help_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_canvas_help_4.setWordWrap(False)
        self.label_canvas_help_4.setObjectName("label_canvas_help_4")
        self.label_canvas_help_4.setText("4")

        # Кнопка закриття інструкції
        self.btn_canvas_help_ok = QtWidgets.QPushButton(self.frame_canvas_help)
        self.btn_canvas_help_ok.setGeometry(QtCore.QRect(190, 320, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.btn_canvas_help_ok.setFont(font)
        self.btn_canvas_help_ok.setStyleSheet("QPushButton {\n"
                                              "    background-color: rgb(225, 210, 255);\n"
                                              "}\n"
                                              "QPushButton:hover{\n"
                                              "     background-color:  rgb(235, 220, 255);\n"
                                              "}\n"
                                              "QPushButton:pressed {\n"
                                              "    background-color: rgb(192, 147, 255);\n"
                                              "}\n"
                                              "")
        self.btn_canvas_help_ok.setObjectName("btn_canvas_help_ok")
        self.btn_canvas_help_ok.setText("Зрозуміло")

        self.btn_canvas_help_ok.clicked.connect(self.canvas_help_ok)  # Обробка натискання кнопки закриття інструкції

        self.frame_canvas_help.show() # Показ віджету інструкції

    # Закриття інструкції
    def canvas_help_ok(self):
        self.frame_canvas_help.hide()

    # Інструкція до панелі вибору кольорів
    def color_help(self):
        # Створення віджету інструкції
        self.frame_color_help = QtWidgets.QFrame(self.centralwidget)
        self.frame_color_help.setGeometry(QtCore.QRect(10, 10, 580, 380))
        self.frame_color_help.setStyleSheet("background-color: rgb(219, 193, 255);\n"
                                            "border-radius: 10px;")
        self.frame_color_help.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_color_help.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_color_help.setObjectName("frame_color_help")

        # Заголовок інструкції
        self.label_color_help = QtWidgets.QLabel(self.frame_color_help)
        self.label_color_help.setGeometry(QtCore.QRect(0, 0, 580, 50))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_color_help.setFont(font)
        self.label_color_help.setAlignment(QtCore.Qt.AlignCenter)
        self.label_color_help.setWordWrap(False)
        self.label_color_help.setObjectName("label_color_help")
        self.label_color_help.setText("Вибір кольору")

        # Фото інтрукції
        self.photo_color_help = QtWidgets.QLabel(self.frame_color_help)
        self.photo_color_help.setGeometry(QtCore.QRect(10, 60, 221, 225))
        self.photo_color_help.setObjectName("photo_color_help")
        self.photo_color_help.setPixmap(QPixmap("color_help.jpg"))
        self.photo_color_help.setScaledContents(True)

        # Опис інтрукції
        self.label_color_help_description = QtWidgets.QLabel(self.frame_color_help)
        self.label_color_help_description.setGeometry(QtCore.QRect(240, 50, 320, 240))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_color_help_description.setFont(font)
        self.label_color_help_description.setAlignment(QtCore.Qt.AlignCenter)
        self.label_color_help_description.setWordWrap(True)
        self.label_color_help_description.setObjectName("label_color_help_description")
        self.label_color_help_description.setText(
            "Натиснувши на кнопки з номерами і потім клацнувши по краю смуги вибору кольору з тим самим номером "
            "(як показано на малюнку), ви вкажете координати смуги для вибору кольору.\n"
            "P.S. Якщо вказати координати правого краю червоного кольору, а потім лівого краю зеленого, "
            "всі інші координати вкажуться автоматично.")

        self.label_color_help_red1 = QtWidgets.QLabel(self.frame_color_help)
        self.label_color_help_red1.setGeometry(QtCore.QRect(25, 160, 50, 50))
        self.label_color_help_red1.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_color_help_red1.setFont(font)
        self.label_color_help_red1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_color_help_red1.setWordWrap(False)
        self.label_color_help_red1.setObjectName("label_color_help_red1")
        self.label_color_help_red1.setText("1")

        self.label_color_help_red2 = QtWidgets.QLabel(self.frame_color_help)
        self.label_color_help_red2.setGeometry(QtCore.QRect(110, 160, 50, 50))
        self.label_color_help_red2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_color_help_red2.setFont(font)
        self.label_color_help_red2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_color_help_red2.setWordWrap(False)
        self.label_color_help_red2.setObjectName("label_color_help_red2")
        self.label_color_help_red2.setText("2")

        self.label_color_help_green1 = QtWidgets.QLabel(self.frame_color_help)
        self.label_color_help_green1.setGeometry(QtCore.QRect(25, 195, 50, 50))
        self.label_color_help_green1.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_color_help_green1.setFont(font)
        self.label_color_help_green1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_color_help_green1.setWordWrap(False)
        self.label_color_help_green1.setObjectName("label_color_help_green1")
        self.label_color_help_green1.setText("1")

        self.label_color_help_green2 = QtWidgets.QLabel(self.frame_color_help)
        self.label_color_help_green2.setGeometry(QtCore.QRect(110, 195, 50, 50))
        self.label_color_help_green2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_color_help_green2.setFont(font)
        self.label_color_help_green2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_color_help_green2.setWordWrap(False)
        self.label_color_help_green2.setObjectName("label_color_help_green2")
        self.label_color_help_green2.setText("2")

        self.label_color_help_blue1 = QtWidgets.QLabel(self.frame_color_help)
        self.label_color_help_blue1.setGeometry(QtCore.QRect(25, 230, 50, 50))
        self.label_color_help_blue1.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_color_help_blue1.setFont(font)
        self.label_color_help_blue1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_color_help_blue1.setWordWrap(False)
        self.label_color_help_blue1.setObjectName("label_color_help_blue1")
        self.label_color_help_blue1.setText("1")

        self.label_color_help_blue2 = QtWidgets.QLabel(self.frame_color_help)
        self.label_color_help_blue2.setGeometry(QtCore.QRect(110, 230, 50, 50))
        self.label_color_help_blue2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_color_help_blue2.setFont(font)
        self.label_color_help_blue2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_color_help_blue2.setWordWrap(False)
        self.label_color_help_blue2.setObjectName("label_color_help_blue2")
        self.label_color_help_blue2.setText("2")

        # Кнопка закриття інструкції
        self.btn_color_help_ok = QtWidgets.QPushButton(self.frame_color_help)
        self.btn_color_help_ok.setGeometry(QtCore.QRect(190, 320, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.btn_color_help_ok.setFont(font)
        self.btn_color_help_ok.setStyleSheet("QPushButton {\n"
                                             "    background-color: rgb(225, 210, 255);\n"
                                             "}\n"
                                             "QPushButton:hover{\n"
                                             "     background-color:  rgb(235, 220, 255);\n"
                                             "}\n"
                                             "QPushButton:pressed {\n"
                                             "    background-color: rgb(192, 147, 255);\n"
                                             "}\n"
                                             "")
        self.btn_color_help_ok.setObjectName("btn_color_help_ok")
        self.btn_color_help_ok.setText("Зрозуміло")

        self.btn_color_help_ok.clicked.connect(self.color_help_ok)  # Обробка натискання кнопки закриття інструкції

        self.frame_color_help.show()  # Показ віджету інструкції

    # Закриття інструкції
    def color_help_ok(self):
        self.frame_color_help.hide()

    # Інструкція до панелі керування
    def control_help(self):
        # Створення віджету інструкції
        self.frame_control_help = QtWidgets.QFrame(self.centralwidget)
        self.frame_control_help.setGeometry(QtCore.QRect(10, 10, 580, 380))
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
        self.label_control_help.setText("Керування")

        # Опис інтрукції
        self.label_control_help_description = QtWidgets.QLabel(self.frame_control_help)
        self.label_control_help_description.setGeometry(QtCore.QRect(10, 50, 560, 250))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_control_help_description.setFont(font)
        self.label_control_help_description.setAlignment(QtCore.Qt.AlignCenter)
        self.label_control_help_description.setWordWrap(True)
        self.label_control_help_description.setObjectName("label_control_help_description")
        self.label_control_help_description.setText(
            "Натиснувши кнопку «Старт» програма почне малювати зображення. "
            "Переконайтеся, що всі поля заповнені належним чином.\n"
            "Щоб зупинити програму, натисніть на стоп кнопку. За замовчуванням це esc, "
            "але ви можете вибрати свою, натиснувши кнопку «esc» і потім натиснувши потрібну клавішу на клавіатурі.\n"
            "Зображення починає малюватись із початку, тобто з верхнього лівого кута. "
            "Ви можете вписати свої координати, щоб почати малювати з вашої точки.\n"
            "P.S. Відлік координат починається з верхнього лівого кута (0, 0). "
            "Вправо – збільшення x (перше поле). Вниз – y (друге поле)")

        # Кнопка закриття інструкції
        self.btn_control_help_ok = QtWidgets.QPushButton(self.frame_control_help)
        self.btn_control_help_ok.setGeometry(QtCore.QRect(190, 320, 200, 40))
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

    # Натискання на потрібний піксель полотна
    def click(self, corx, cory):
        # Визначення координат пікселя по координатам кутів полотна
        n1 = [n1n[0] - (cory * ((n1n[0] - n3n[0]) / size[1])), n1n[1]]
        n2 = [n2n[0] + (cory * ((n4n[0] - n2n[0]) / size[1])), n2n[1]]
        x = n1[0] + (((n2[0] - n1[0]) / size[0]) * ((size[0] / size[1]) * cory))
        ay = (n4n[1] - n1n[1]) / (n4n[0] - n1n[0]) * x - (n1n[0] * (n4n[1] - n1n[1])) / (n4n[0] - n1n[0]) + n1n[1]
        n1 = [(n3n[0] - n1n[0]) / (n3n[1] - n1n[1]) * ay - (n1n[1] * (n3n[0] - n1n[0])) / (n3n[1] - n1n[1]) + n1n[0],
              n1n[1]]
        n2 = [(n4n[0] - n2n[0]) / (n4n[1] - n2n[1]) * ay - (n2n[1] * (n4n[0] - n2n[0])) / (n4n[1] - n2n[1]) + n2n[0],
              n2n[1]]
        ax = n1[0] + (((n2[0] - n1[0]) / size[0]) * corx)

        ahk.mouse_move(ax, ay, speed=2)  # Пересування миші
        ahk.click()  # Клік миші

    # Пересування миші по потрібним пікселям з зажатою кнопкою миші
    def drag(self, corx, cory, corx2, cory2):
        x1, y1 = self.coordinates(corx, cory)
        x2, y2 = self.coordinates(corx2, cory2)

        ahk.mouse_move(x1, y1, speed=2)
        mouse.press('left')

        while corx < corx2:
            corx += 1
            x1, y1 = self.coordinates(corx, cory)
            ahk.mouse_move(x1, y1, speed=2)

        mouse.release('left')

    # Визначення координат пікселя по координатам кутів полотна
    def coordinates(self, corx, cory):
        n1 = [n1n[0] - (cory * ((n1n[0] - n3n[0]) / size[1])), n1n[1]]
        n2 = [n2n[0] + (cory * ((n4n[0] - n2n[0]) / size[1])), n2n[1]]
        x = n1[0] + (((n2[0] - n1[0]) / size[0]) * ((size[0] / size[1]) * cory))
        ay = (n4n[1] - n1n[1]) / (n4n[0] - n1n[0]) * x - (n1n[0] * (n4n[1] - n1n[1])) / (n4n[0] - n1n[0]) + n1n[1]
        n1 = [(n3n[0] - n1n[0]) / (n3n[1] - n1n[1]) * ay - (n1n[1] * (n3n[0] - n1n[0])) / (n3n[1] - n1n[1]) + n1n[0],
              n1n[1]]
        n2 = [(n4n[0] - n2n[0]) / (n4n[1] - n2n[1]) * ay - (n2n[1] * (n4n[0] - n2n[0])) / (n4n[1] - n2n[1]) + n2n[0],
              n2n[1]]
        ax = n1[0] + (((n2[0] - n1[0]) / size[0]) * corx)
        return ax, ay

    # Вибір кольору
    def color(self, r, g, b):
        rx = r1[0] + (((r2[0] - r1[0]) / 254) * r)
        ahk.mouse_move(rx, r1[1], speed=2)
        ahk.click()
        gx = g1[0] + (((g2[0] - g1[0]) / 254) * g)
        ahk.mouse_move(gx, g1[1], speed=2)
        ahk.click()
        bx = b1[0] + (((b2[0] - b1[0]) / 254) * b)
        ahk.mouse_move(bx, b1[1], speed=2)
        ahk.click()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # Зміна значка програми
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("PixelDraw.ico"),
                   QtGui.QIcon.Selected, QtGui.QIcon.On)
    MainWindow.setWindowIcon(icon)

    MainWindow.show()
    sys.exit(app.exec_())
