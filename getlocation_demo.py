from urllib.request import urlopen
my_ip = urlopen('http://ip.42.pl/raw').read()

import requests
import IPy

def get_location(ip):
    url =  'https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?co=&resource_id=6006&t=1529895387942&ie=utf8&oe=gbk&cb=op_aladdin_callback&format=json&tn=baidu&cb=jQuery110203920624944751099_1529894588086&_=1529894588088&query=%s'%ip
    # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    html = r.text
    c1 = html.split('location":"')[1]
    c2 = c1.split('","')[0]
    return c2[:6]

def check_ip(ip):
    try:
        IPy.IP(ip)
        return True
    except Exception as e:
        print(e)
        return False


if __name__ == '__main__':
    ip = str(my_ip).strip('b')
    ip=eval(ip)
    print(ip)

    if check_ip(ip):
        print('IP位置为：',get_location(ip))
