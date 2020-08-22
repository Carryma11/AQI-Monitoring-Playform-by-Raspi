#!/usr/bin/env python
# coding: utf-8

# In[4]:


#!/usr/bin/env python
# coding: utf-8 
import serial
import sys
import os
import time
import threading 
import serial.tools.list_ports

global MAX_LOOP_NUM,MAX_TRY
 
MAX_LOOP_NUM = 50
MAX_TRY=5
def get_data(s):
    maxloopNum = 0
 
    while True:
 
        data = s.read(s.inWaiting())      #读取串口缓冲区数据
        maxloopNum = maxloopNum + 1         #累加读取次数
        try:
            #data= str(binascii.b2a_hex(s.read(n)))[2:-1]
            if data[3]==0x0E:
                print('返回采集数据个数正确，开始收集>>>')
                CO2=data[4]*256+data[5]#根据关系计算各参数实际值，这里运算计算机会直接帮我们转换为十进制
                JQ=data[6]*256+data[7]
                TVOC=data[8]*256+data[9]
                PM2_5=data[10]*256+data[11]
                PM_10H=data[12]*256+data[13]
                TEMPUTER=data[14]+data[15]*0.1
                WET=data[16]+data[17]*0.1
                print('甲醛:%d ug TVOC:%d ug PM2.5:%d ug PM10:%d ug 温度：%1.f℃ 湿度：%.1f%'%(
                    JQ,TVOC,PM2_5,PM_10,TEMPUTER,WET))                        #输出
                cmd_get=bytes.fromhex('3C 01 01 00') #这是发送的命令，传感器接收到后会返还温湿度信息。
                s.write(cmd)
            if data[2]==0x02:
                address=str(binascii.b2a_hex(data))[2:-1]
                print('监测器地址为：',address[2:4])
        except:
                print(data)
                print('没有读取到有效数据，请检查查询地址是否正确\n'
                     '根据查询地址的返回值：00，01，10，11,修改查询指令的前两位\n'
                     '如返回地址结果为10，则输入1001\n')
                main()
        if (maxloopNum > MAX_LOOP_NUM):
                s.close()
                main()
                
        s.flushInput()
        time.sleep(1)
 
 
def send_cmd(ser, cmdstr):
    if cmdstr in( '0101','0100', '0110' , '0111'):
        cmd='3C'+cmdstr+'00'
        cmd=bytes.fromhex(cmdstr)
    elif cmdstr=='0002':
        cmd='3C'+cmdstr+'00'
        cmd=bytes.fromhex(cmdstr)
    elif cmdstr=='exit':
        sys.exit()  
    else :
        print('输入指令错误，请重新输入：')
        main()
    ser.write(cmd)   # 发送读取指令
    get_data(ser)




def main():
    plist = list(serial.tools.list_ports.comports())
    if len(plist) <= 0:
        print("没有发现端口,正在检测...")
        time.sleep(1)
    else :
        plist_0 = list(plist[0])
        serialName = plist_0[0]       #先自动检测串口， 检测到可用串口，取出串口名
        ser = serial.Serial(serialName, 9600, timeout=30)  # timeout=30 30s
        print("正在连接>>>", ser.name)
        cmd = input('请输入查询指令：\n 1.查询数据:0101\n 2.查询地址:0002\n 3.exit\n')
        send_cmd(ser,cmd)
        
                          
                      
                        
                
if __name__ == '__main__':
    for i in range(MAX_TRY+1):
        if i==MAX_TRY:
            print('重连达到最大次数，请检查连接')
            break
        else:
            try:
                main()
            except KeyboardInterrupt:
                if ser != None:
                    ser.close()
            
        





