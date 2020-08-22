 # -*- coding: utf-8 -*
import serial
import time
import threading
# 打开串口
ser = serial.Serial("/dev/ttyAMA0", 9600)
ser.flushInput()
def read_data():
    count=ser.inWaiting()
    if count:
        recv=ser.read(count)
        data=int(str(binascii.b2a_hex(s.read(n))))
        print('recv data:',recv)

def write_data():
    write = ser.write(bytes.fromhex('3C010000'))
def main():
    while True:


        time.sleep(1)
   
if __name__ == '__main__':
    t1= threading.Timer(1, write_data)  # 进行周期性采集，那个2证明间隔两秒采集一次
    t1.start()
    t2= threading.Timer(2, timerDelay)  # 进行周期性采集，那个2证明间隔两秒采集一次
    t2.start()
    try:
        main()
    except KeyboardInterrupt:
        if ser != None:
            ser.close()