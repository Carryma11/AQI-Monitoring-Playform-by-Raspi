#!/usr/bin/env python
# coding: utf-8
#Remote_UDP_Server
import socket
import sqlite3

database = 'AQI.db'
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 指定 IP:port
s.bind(('0.0.0.0', 9999))
print('listening to localport:9999')

db = sqlite3.connect(database)

def make_dicts(cursor,row):
    return dict((cursor.descriptrion[idx][0],value)
                for idx, value in enumerate(row))

db.row_factory = make_dicts
# 循环 每次有新的连接触发
while True:
    data, clientaddr = s.recvfrom(1024)
    print('Received from %s:%s' % clientaddr)
    data = data.decode()
    data = data.split(',')
    print('接收到数据：', data)
    if len(data) !=8:
        continue
    data_H=map(int, data[:-2])
    data_L=map(float,data[-2:])
    timestamp, co2, hcho, tvoc, pm2_5, pm_10 = data_H
    tem, hum = data_L
    creat_table = '''create table AQI( 
                              timestamp int(14),
                              co2 int(4),
                              hcho int(4),
                              tvoc int(4),
                              pm2_5 int(3),
                              pm_10 int(4),
                              tem float(100),
                              hum  fooat(100)
                                    )'''
    #id int(10)  primary key autoincrement,
    try:
        cur=db.cursor()
        cur.execute(creat_table)
    except:
        cur.execute('INSERT INTO AQI (timestamp, co2, hcho, tvoc, pm2_5, pm_10,tem ,hum) VALUES'
               ' (?, ?, ?, ?, ?, ? ,?, ?)', (timestamp, co2, hcho, tvoc, pm2_5, pm_10,tem ,hum))
        cur.close()
        db.commit()
    #send_data=('数据接收成功:'+data.decode())
    #s.sendto(send_data.encode(), clientaddr)
#s.close()