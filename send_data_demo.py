#!/usr/bin/env python
# coding: utf-8
#UDP_Client
import binascii
import time
import socket
n=bytes.fromhex('3C 01 01 0E 01 E2 00 05 00 24 00 2D 00 38 1E 05 40 06 B8')#把字符串转换为16进制比特流

data=n
print('origin_data:',data)
if n[3]==0x0E:
    print('返回采集数据个数正确，开始收集>>>')
#data= str(binascii.b2a_hex(n))[2:-1]#把16进制数转换为字符串
CO2=data[4]*256+data[5]#根据关系计算各参数实际值，这里运算计算机会直接帮我们转换为十进制
JQ=data[6]*256+data[7]
TVOC=data[8]*256+data[9]
PM2_5=data[10]*256+data[11]
PM_10=data[12]*256+data[13]
TEMPUTER=data[14]+data[15]*0.1
WET=data[16]+data[17]*0.1
print('CO2:%d ppm 甲醛:%d ug TVOC:%d ug PM2.5:%d ug PM10:%d ug 温度：%1.f℃ 湿度：%.1f%% '%(
                    CO2,JQ,TVOC,PM2_5,PM_10,TEMPUTER,WET))
#print('湿度:{:+.1f}%'.format(WET))
def GetTimeStamp():
    return time.strftime("%Y%m%d%H%M%S", time.localtime())

def sendtoudp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data_send=(GetTimeStamp()+','+str(CO2)+','+str(JQ)+','+str(TVOC)+','+str(PM2_5)+
                ','+str(PM_10)+','+str(TEMPUTER)+','+str(WET))
    s.sendto(data_send.encode(),('192.168.0.198', 9999))
    print('sending msg :',data_send)
    #recv_serdata,seraddr=s.recvfrom(1024)
    #if recv_serdata:
        #print('%s:%s'%seraddr,recv_serdata.decode())
    s.close()
while True:
    sendtoudp()
    time.sleep(1)
