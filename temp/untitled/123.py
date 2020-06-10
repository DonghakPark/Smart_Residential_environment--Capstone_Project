import sys
import urllib.request
import cv2
import time
import numpy as np
import threading
import pytesseract
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor
import PIL

import Face
import start
import Car_Number_Recog

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

form_class = uic.loadUiType("main.ui")[0]

class MainWindow(QMainWindow, form_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.facebtn.clicked.connect(self.facebtnFunction)
        self.carbtn.clicked.connect(self.carbtnFunction)

    def facebtnFunction(self):
        FaceMainClass(self)

    def carbtnFunction(self):
        CarMainClass(self)

class FaceMainClass(QDialog) :
    def __init__(self, parent) :
        super(FaceMainClass, self).__init__(parent)
        option_ui = "FaceMain.ui"
        uic.loadUi(option_ui, self)
        self.show()

        # 버튼에 기능을 연결하는 코드
        self.btn_1.clicked.connect(self.button1Function)
        self.btn_2.clicked.connect(self.button2Function)

        # btn_1이 눌리면 작동할 함수

    def button1Function(self):
        face1class(self)

        # btn_2가 눌리면 작동할 함수

    def button2Function(self):
        t_executor = ThreadPoolExecutor(1)
        t = t_executor.submit(Face.Face_reg)

        while True:
            if t.done():
                name = t.result()
                break

        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load("Face_result.jpg")
        self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(350)
        self.lbl_picture.setPixmap(self.qPixmapFileVar)
        self.lbl2_picture.setText(name)

f_name = []
f_home = []
class face1class(QDialog) :
    def __init__(self, parent):
        super(face1class, self).__init__(parent)
        option_ui = "face1.ui"
        uic.loadUi(option_ui, self)
        self.show()

        # 버튼에 기능을 할당하는 코드

        self.btn_Text.clicked.connect(self.btn_printTextFunction)     #이줄은 저장 버튼



    def btn_printTextFunction(self):      #저장버튼 함수

        # Lineedit의 글자를 배열에 저장
        f_name.append(self.lineedit_Test1.text())
        f_home.append(self.lineedit_Test2.text())
        print(f_name)
        print(f_home)


c_name = []
c_home = []
c_num = []
class car1Class(QDialog) :
    def __init__(self, parent) :
        super(car1Class, self).__init__(parent)
        option_ui = "car1.ui"
        uic.loadUi(option_ui, self)
        self.show()

        self.btn_Text.clicked.connect(self.btn_printTextFunction)  # 이줄은 저장 버튼

    def btn_printTextFunction(self):  # 저장버튼 함수

        # Lineedit의 글자를 배열에 저장
        c_name.append(self.lineedit_Test1.text())
        c_home.append(self.lineedit_Test2.text())
        c_num.append(self.lineedit_Test3.text())
        print(c_name)
        print(c_home)
        print(c_num)




#화면을 띄우는데 사용되는 Class 선언
class CarMainClass(QDialog) :
    def __init__(self, parent) :
        super(CarMainClass, self).__init__(parent)
        option_ui = "carmainTest.ui"
        uic.loadUi(option_ui, self)
        self.show()


        #버튼에 기능을 연결하는 코드
        self.btn_1.clicked.connect(self.button1Function)
        self.btn_2.clicked.connect(self.button2Function)


    def button1Function(self) :

        car1Class(self)


    def button2Function(self):

        t_executor1 = ThreadPoolExecutor(1)
        t1 = t_executor1.submit(start.start)

        show = ""
        while True:
            if t1.done():
                print("Recognition complete")
                show = t1.result()

                break
        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load("result.jpg")
        self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(350)
        self.lbl_picture.setPixmap(self.qPixmapFileVar)
        self.lbl2_picture.setText(show)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()
    app.exec_()