from PyQt5.QtCore import QThread, pyqtSignal
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('0.0.0.0', 9999))


# 关键：继承QThread
class Server_RunThread(QThread):
    data_signal = pyqtSignal(list)  #设置发送信号类型
    def __init__(self,parent = None):
        super(Server_RunThread).__init__(parent)
    def run(self):
        while True:
            data, client_addr = s.recvfrom(1024)
            data = data.decode()
            data = data.split(',')
            print('接收到数据：', data)
            if len(data) !=7:
                continue
            #s.sendto(data.upper(), client_addr)
            self.data_signal.emit(data)

"""
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore
from PyQTUI.mainwindow import Ui_MainWindow
import sys
from PyQt5.QtCore import *
import time


# 继承QThread
class Runthread(QtCore.QThread):
    # python3,pyqt5与之前的版本有些不一样
    #  通过类成员对象定义信号对象
    _signal = pyqtSignal(str)

    def __init__(self, parent=None):
        super(Runthread, self).__init__()

    def __del__(self):
        self.wait()

    def run(self):
        pass
    # 处理你要做的业务逻辑，这里是通过一个回调来处理数据，这里的逻辑处理写自己的方法
    # wechat.start_auto(self.callback)
    # self._signal.emit(msg);  可以在这里写信号焕发

    def callback(self, msg):
        self._signal.emit(msg)



# 信号焕发，我是通过我封装类的回调来发起的



class mywindow(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.Button_start.clicked.connect(self.start_login)

    def start_login(self):
        # 创建线程
        self.thread = Runthread()
        # 连接信号
        self.thread._signal.connect(self.callbacklog)
        # 开始线程
        self.thread.start()

    def callbacklog(self, msg):
        # 将回调数据输出到文本框
        self.textEdit_log.setText(self.textEdit_log.toPlainText() + "\n" + msg + "   " +
                                  time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()));

if __name__ == "__main__":
    # 创建线程
    serverThread = Server_RunThread()
    serverThread._signal.connect('lcd(data)')    #填入线程执行的方法
"""
