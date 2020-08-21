# 读写UART数据
# Auther MYH

import serial  # 导入串口包
import time  # 导入时间包
import threading  # 导入线程包
import socket

global data_ser, cmd, buf_L, buf_R, update

# 发送读取指令,每秒采集一次
def send_cmd():
    while True:
        data_ser.write(cmd)
        time.sleep(1)


def get_data():
    while True:
        data_count = data_ser.inWaiting()
        data = data_ser.read(data_count)
        co2 = data[4] * 256 + data[5]  # 根据关系计算各参数实际值，这里运算计算机会直接帮我们转换为十进制
        hcho = data[6] * 256 + data[7]
        tvoc = data[8] * 256 + data[9]
        pm2_5 = data[10] * 256 + data[11]
        pm_10 = data[12] * 256 + data[13]
        tem = data[14] + data[15] * 0.1
        wet = data[16] + data[17] * 0.1
        if data[3] == 0x0E:
            # data_count= str(binascii.b2a_hex(s.read(data_count)))[2:-1]

            buf_R = (str(co2)+','+str(hcho)+','+str(tvoc)+','+str(pm2_5)+
                   ','+str(pm_10)+','+str(tem)+','+str(wet))
            buf_L = buf_R
            """
            buf_L = ('co2:' + str(co2) + '甲醛:' + str(co2) + 'tvoc:' + str(tvoc) + 'PM2.5:' + str(pm2_5) +
                     'pm_10:' + str(pm_10) + '温度' + str(tem) + '湿度' + str(wet))
            """
            update = 1
            """
        elif data[3] ==0x0A:
            buf_R = (str(co2) + ',' + str(hcho) + ',' + str(tvoc) + ',' + str(pm2_5) +
                     ',' + str(pm_10) + ',' + str(tem) + ',' + str(wet))
            """

        time.sleep(.5)


def GetTimeStamp():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# UDP_Client
def UdpConnect():
    global s_R,s_L
    s_R= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s_L= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def sendtoudp_Local():  # 发送给本地
    data_send_Local = buf_L
    s_L.sendto(data_send_Local.encode(), ('127.0.0.1', 9999))
    # print(s.recv(1024).decode())

def sendtoudp_Remote():  # 发送给远端
    data_send_Remote = (GetTimeStamp()+','+buf_R)
    s_R.sendto(data_send_Remote.encode(), ('192.168.0.198', 9999))
    # print(s.recv(1024).decode())

def main():
    data_ser = serial.Serial(
        port='/dev/ttyAMA0',
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=5
    )
    # 清空缓冲区
    data_ser.flushInput()
    cmd = bytes.fromhex('3C 01 00 00')
    update = 0
    if not data_ser.isOpen():
        raise ("Serial is not oepn,please check the port")
    else:
        UdpConnect()
        while True:
            if update == 1:
                update = 0
                sendtoudp_Local()
                sendtoudp_Remote()
                print(buf_L)
                print(buf_R)




if __name__ == '__main__':
    main()
    t1 = threading.Thread(target=send_cmd)
    t2 = threading.Thread(target=get_data)
    t1.start()
    t2.start()
