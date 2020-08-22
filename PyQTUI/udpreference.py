from PyQt5.QtNetwork import QUdpSocket, QHostAddress

def networkInit(self):
    self.udpSocket = QUdpSocket(self)
    self.port = 9999
    self.udpSocket.bind(self.port, QUdpSocket.ShareAddress | QUdpSocket.ReuseAddressHint)
    self.udpSocket.readyRead.connect(self.processPendingDatagrams)
"""使用此类的最常用方法是使用bind()绑定到地址和端口，然后调用writeDatagram()和readDatagram()/ receiveDatagram()来传输数据。
如果要使用标准QIODevice函数read()，readLine()，write()等，则必须首先通过调用connectToHost()将套接字直接连接到对等方。
每次将数据报写入网络时，套接字都会发出bytesWritten()信号。如果您只想发送数据报，则无需调用bind()。
只要数据报到达，就会发出readyRead()信号。在这种情况下，hasPendingDatagrams()返回True。调用pendingDatagramSize()以获取第一个挂起数据报的大小，并调用readDatagram()或receiveDatagram()来读取它。
注意：收到readyRead()信号时应读取输入数据报，否则不会为下一个数据报发出此信号。"""

def initSocket(self):
    self.udpSocket = QUdpSocket(self)
    self.udpSocket.bind(QHostAddress.LocalHost, 9999)
    self.udpSocket.readyRead.connect(self.readPendingDatagrams)

def readPendingDatagrams(self):

    while self.udpSocket.hasPendingDatagrams():
        datagram = self.udpSocket.receiveDatagram()
        self.processTheDatagram(datagram)
"""QUdpSocket还支持UDP多播。使用joinMulticastGroup()和leaveMulticastGroup()来控制组成员资格，
使用QAbstractSocket. MulticastTtlOption和QAbstractSocket. MulticastLoopbackOption来设置TTL和loopback套接字选项。
使用setMulticastInterface()控制组播数据报的传出接口，使用multicastInterface()查询它。
使用QUdpSocket，您还可以使用connectToHost()建立到UDP服务器的虚拟连接，然后使用read()和write()交换数据报，而无需为每个数据报指定接收器。"""


