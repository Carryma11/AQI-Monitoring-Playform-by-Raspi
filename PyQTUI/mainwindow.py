# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys
import time
from PyQTUI import UdpThread, getlocation
from PyQt5.QtGui import QPalette, QPixmap, QColor




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1024, 600))
        palette = QtGui.QPalette()  # 调色板类
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        MainWindow.setStatusTip("")
        MainWindow.setStyleSheet("")
        MainWindow.setIconSize(QtCore.QSize(0, 0))
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label_raw = QtWidgets.QLabel(self.centralWidget)
        self.label_raw.setGeometry(QtCore.QRect(0, 570, 631, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_raw.setFont(font)
        self.label_raw.setObjectName("label_raw")
        self.label_title_pm25 = QtWidgets.QLabel(self.centralWidget)
        self.label_title_pm25.setGeometry(QtCore.QRect(40, 50, 121, 51))
        self.label_title_pm25.setObjectName("label_title_pm25")

        self.label_title_tem = QtWidgets.QLabel(self.centralWidget)
        self.label_title_tem.setGeometry(QtCore.QRect(50, 225, 101, 51))
        self.label_title_tem.setObjectName("label_title_tem")

        self.label_cate_img = QtWidgets.QLabel(self.centralWidget)
        self.label_cate_img.setGeometry(QtCore.QRect(710, 385, 321, 225))
        self.label_cate_img.setText("")
        self.label_cate_img.setPixmap(QtGui.QPixmap('img/a.png'))# 打开顶部位图
        self.label_cate_img.setScaledContents(True)
        self.label_cate_img.setWordWrap(False)
        self.label_cate_img.setObjectName("label_cate_img")

        self.label_time = QtWidgets.QLabel(self.centralWidget)
        self.label_time.setGeometry(QtCore.QRect(770, 170, 251, 161))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label_time.setFont(font)
        self.label_time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time.setWordWrap(False)
        self.label_time.setObjectName("label_time")

        self.label_title = QtWidgets.QLabel(self.centralWidget)
        self.label_title.setGeometry(QtCore.QRect(0, 0, 1024, 51))
        self.label_title.setObjectName("label_title")

        self.label_img_logo = QtWidgets.QLabel(self.centralWidget)
        self.label_img_logo.setGeometry(QtCore.QRect(800, 20, 191, 121))
        self.label_img_logo.setObjectName("label_img_logo")

        self.label_title_pm10 = QtWidgets.QLabel(self.centralWidget)
        self.label_title_pm10.setGeometry(QtCore.QRect(310, 50, 121, 51))
        self.label_title_pm10.setObjectName("label_title_pm10")

        self.label_title_wet = QtWidgets.QLabel(self.centralWidget)
        self.label_title_wet.setGeometry(QtCore.QRect(320, 225, 101, 51))
        self.label_title_wet.setObjectName("label_title_wet")

        self.label_title_co2 = QtWidgets.QLabel(self.centralWidget)
        self.label_title_co2.setGeometry(QtCore.QRect(590, 50, 91, 41))
        self.label_title_co2.setObjectName("label_title_co2")

        self.label_title_hcho = QtWidgets.QLabel(self.centralWidget)
        self.label_title_hcho.setGeometry(QtCore.QRect(580, 225, 131, 50))
        self.label_title_hcho.setObjectName("label_title_hcho")

        self.label_title_tvoc = QtWidgets.QLabel(self.centralWidget)
        self.label_title_tvoc.setGeometry(QtCore.QRect(50, 395, 81, 61))
        self.label_title_tvoc.setObjectName("label_title_tvoc")

        self.label_warning = QtWidgets.QLabel(self.centralWidget)
        self.label_warning.setGeometry(QtCore.QRect(370, 540, 271, 31))
        self.label_warning.setObjectName("label_warning")

        self.label_title_location = QtWidgets.QLabel(self.centralWidget)
        self.label_title_location.setGeometry(QtCore.QRect(380, 440, 251, 101))
        self.label_title_location.setText("")
        self.label_title_location.setObjectName("label_title_location")

        palette.setBrush(QPalette.Background, QtGui.QBrush(QtGui.QColor(0, 228, 0)))  # 设置初始背景颜色
        self.lcd_pm25 = QtWidgets.QLCDNumber(self.centralWidget)
        self.lcd_pm25.setGeometry(QtCore.QRect(10, 90, 190, 120))
        self.lcd_pm25.setAutoFillBackground(True)
        self.lcd_pm25.setDigitCount(3)
        self.lcd_pm25.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd_pm25.setObjectName("lcd_pm25")

        self.lcd_pm10 = QtWidgets.QLCDNumber(self.centralWidget)
        self.lcd_pm10.setGeometry(QtCore.QRect(270, 90, 190, 120))
        self.lcd_pm10.setAutoFillBackground(True)
        self.lcd_pm10.setDigitCount(3)
        self.lcd_pm10.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd_pm10.setObjectName("lcd_pm10")

        self.lcd_hcho = QtWidgets.QLCDNumber(self.centralWidget)
        self.lcd_hcho.setGeometry(QtCore.QRect(530, 270, 190, 120))
        self.lcd_hcho.setAutoFillBackground(True)
        self.lcd_hcho.setDigitCount(4)
        self.lcd_hcho.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd_hcho.setObjectName("lcd_hcho")

        self.lcd_tem = QtWidgets.QLCDNumber(self.centralWidget)
        self.lcd_tem.setGeometry(QtCore.QRect(10, 270, 190, 120))
        self.lcd_tem.setAutoFillBackground(True)
        self.lcd_tem.setDigitCount(3)
        self.lcd_tem.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd_tem.setObjectName("lcd_tem")

        self.lcd_wet = QtWidgets.QLCDNumber(self.centralWidget)
        self.lcd_wet.setGeometry(QtCore.QRect(270, 270, 190, 120))
        self.lcd_wet.setAutoFillBackground(True)
        self.lcd_wet.setDigitCount(3)
        self.lcd_wet.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcd_wet.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd_wet.setProperty("value", 0.0)
        self.lcd_wet.setObjectName("lcd_wet")

        self.lcd_tvoc = QtWidgets.QLCDNumber(self.centralWidget)
        self.lcd_tvoc.setGeometry(QtCore.QRect(10, 440, 190, 120))
        self.lcd_tvoc.setAutoFillBackground(True)
        self.lcd_tvoc.setDigitCount(4)
        self.lcd_tvoc.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd_tvoc.setObjectName("lcd_tvoc")

        self.lcd_co2 = QtWidgets.QLCDNumber(self.centralWidget)
        self.lcd_co2.setGeometry(QtCore.QRect(530, 90, 190, 120))
        self.lcd_co2.setAutoFillBackground(True)
        self.lcd_co2.setDigitCount(4)
        self.lcd_co2.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd_co2.setObjectName("lcd_co2")

        self.lcd_co2.setPalette(palette)  # 为控件设置对应的调色板即可
        self.lcd_pm25.setPalette(palette)
        self.lcd_pm10.setPalette(palette)
        self.lcd_tem.setPalette(palette)
        self.lcd_wet.setPalette(palette)
        self.lcd_hcho.setPalette(palette)
        self.lcd_tvoc.setPalette(palette)


        #以下是单位标签
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(455, 180, 70, 40))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(195, 180, 70, 40))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        self.label_6.setGeometry(QtCore.QRect(200, 360, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralWidget)
        self.label_7.setGeometry(QtCore.QRect(725, 180, 50, 40))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_11 = QtWidgets.QLabel(self.centralWidget)
        self.label_11.setGeometry(QtCore.QRect(465, 360, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralWidget)
        self.label_12.setGeometry(QtCore.QRect(195, 530, 70, 40))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_10 = QtWidgets.QLabel(self.centralWidget)
        self.label_10.setGeometry(QtCore.QRect(715, 360, 70, 40))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        self.label_time.raise_()
        self.label_raw.raise_()
        self.label_title_pm25.raise_()
        self.lcd_tem.raise_()
        self.label_title_tem.raise_()
        self.label_7.raise_()
        self.label_cate_img.raise_()
        self.lcd_pm10.raise_()
        self.lcd_hcho.raise_()
        self.lcd_pm25.raise_()
        self.label_title.raise_()
        self.label_6.raise_()
        self.label_4.raise_()
        self.label_img_logo.raise_()
        self.label_title_pm10.raise_()
        self.label_title_wet.raise_()
        self.label_title_co2.raise_()
        self.label_title_hcho.raise_()
        self.label_title_tvoc.raise_()
        self.lcd_wet.raise_()
        self.lcd_tvoc.raise_()
        self.lcd_co2.raise_()
        self.label_5.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_10.raise_()
        self.label_warning.raise_()
        self.label_title_location.raise_()
        MainWindow.setCentralWidget(self.centralWidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    data_signal = pyqtSignal(list)
    def run_udp_thread(self):
        self.udp_thread = UdpThread.Server_runThread()
        self.udp_thread.data_singal.connect(self.refreshlcd())
        self.udp_thread.start()


    def refreshlcd(self, data, color_table=QtGui.QColor(255,255,255)):
        data = map(float,data[:])
        co2, hcho, tvoc, pm25, pm10, tem, wet = data
        color_table[0] = QtGui.QColor(0, 228, 0)
        color_table[1] = QtGui.QColor(255, 255, 0)
        color_table[2] = QtGui.QColor(225, 126, 0)
        color_table[3] = QtGui.QColor(225, 0, 0)
        color_table[4] = QtGui.QColor(153, 0, 76)
        color_table[5] = QtGui.QColor(126, 0, 35)
        color_table[6] = QtGui.QColor(128, 255, 128)
        palette = QPalette()
        if pm25 <= 35:
            level = 0
        elif pm25 <= 75:
            level = 1
        elif pm25 <= 115:
            level = 2
        elif pm25 <= 150:
            level = 3
        elif pm25 <= 250:
            level = 4
        else:
            level = 5
        palette.setBrush(QPalette.Background, QtGui.QBrush(color_table[level]))
        self.lcd_co2.setPalette(palette)
        co2, hcho, tvoc, pm25, pm10, tem, wet = [2000,1000,500,150,190,30,75]
        self.lcd_co2.setProperty("value", co2)
        self.lcd_hcho.setProperty("value", hcho)
        self.lcd_tvoc.setProperty("value", tvoc)
        self.lcd_pm25.setProperty("value", pm25)
        self.lcd_pm10.setProperty("value", pm10)
        self.lcd_tem.setProperty("value", tem)
        self.lcd_wet.setProperty("value", wet)

        self.lcd_pm25.raise_()
        self.lcd_pm10.raise_()
        self.lcd_wet.raise_()
        self.lcd_tvoc.raise_()
        self.lcd_wet.raise_()
        self.lcd_tem.raise_()
        self.lcd_hcho.raise_()





    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AQI Indoor"))
        self.label_raw.setText(_translate("MainWindow", "Raw: PM2.5: 0, PM10: 0, CO2: 0，tem：0，humidity：0，CH2O：0，TVOC：0"))
        self.label_title_pm25.setText(_translate("MainWindow", "PM2.5"))
        self.label_title_tem.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:35pt;\">温度</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">μg/m</span><span style=\" font-size:18pt; vertical-align:super;\">3</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">℃</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">ppm</span></p></body></html>"))
        self.label_time.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Time</p><p align=\"center\">Time</p></body></html>"))
        self.label_title.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:25pt;\">室内空气质量监测系统</span></p></body></html>"))
        self.label_img_logo.setText(_translate("MainWindow", "logo"))
        self.label_title_pm10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:35pt;\">PM10</span></p></body></html>"))
        self.label_title_wet.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:35pt;\">湿度</span></p></body></html>"))
        self.label_title_co2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:35pt;\">CO2</span></p></body></html>"))
        self.label_title_hcho.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:35pt;\">甲醛</span></p></body></html>"))
        self.label_title_tvoc.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:30pt;\">TVOC</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">μg/m</span><span style=\" font-size:18pt; vertical-align:super;\">3</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">%</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">μg/m</span><span style=\" font-size:18pt; vertical-align:super;\">3</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">μg/m</span><span style=\" font-size:18pt; vertical-align:super;\">3</span></p></body></html>"))
        self.label_warning.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">注：CO2，CH2O，TVOC需要预热2分钟才可显示</span></p></body></html>"))
        ip_text=getlocation.get_location()
        self.label_title_location.setText(ip_text)

def get_time():
    timestr = time.strftime("%Y-%m-%d\n%H:%M:%S", time.localtime())
    return timestr




def show_MainWindow():
    app = QtWidgets.QApplication(sys.argv)  # 首先必须实例化QApplication类，作为GUI主程序入口
    MainWindow = QtWidgets.QMainWindow()  # 实例化QtWidgets.QMainWindow类，创建自带menu的窗体类型QMainWindow
    ui = Ui_MainWindow()  # 实例UI类
    ui.setupUi(MainWindow)  # 设置窗体UI
    MainWindow.show()  # 显示窗体
    sys.exit(app.exec_())  # 当来自操作系统的分发事件指派调用窗口时，
    # 应用程序开启主循环（mainloop）过程，
    # 当窗口创建完成，需要结束主循环过程，
    # 这时候呼叫sys.exit（）方法来，结束主循环过程退出，
    # 并且释放内存。为什么用app.exec_()而不是app.exec()？
    # 因为exec是python系统默认关键字，为了以示区别，所以写成exec_

