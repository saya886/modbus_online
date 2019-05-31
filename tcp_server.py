import socket
import threading
import time
import os
import sys
import django
# 在脚本中使用django的orm
dir = os.path.dirname(os.path.abspath(__file__))
dir = os.path.join(dir, 'modbus_online')
sys.path.insert(0, dir)
settings_path = 'modbus_online.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_path)
django.setup()
from modbus_view.models import data_history,sensor_data

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 9998
# 监听端口:
s.bind(('0.0.0.0', port))

s.listen(5)
print('等待链接')

def tcplink(sock, addr):
    try:
        sensor_command = sensor_data.objects.get(id="1").data
        data = bytes.fromhex("".join(sensor_command.split(",")))
        print('连接建立完成  链接的地址 %s:%s...' % addr)
        sock.send(data)
        print("send data is  "+str(data))
        while True:
            print("--------------------------------------")
            recv_data = sock.recv(1024)
            try:
                data_history(value=int(recv_data.hex()[6:10],16)).save()
            except:
                pass
            try:
                print("from client data is >>> {}".format(recv_data))
            except:
                print("can not parser data content")
            #if recv_data == b'':
            #    break
            sock.send(recv_data)
            print("send data is >>> "+str(recv_data))
            time.sleep(10)
    except KeyboardInterrupt:
        sock.close()
        print('客户端 %s:%s 断开链接.' % addr)


while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
