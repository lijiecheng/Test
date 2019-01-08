
#!/usr/bin/python

import socket

sk = socket.socket()   # 创建socket实例

ip_port = ("127.0.0.1", 8888) # 定义绑定ip和port

sk.bind(ip_port) # 绑定监听

sk.listen(5)  # 最大连接数

print("正在进行等待接受数据")

conn, address = sk.accept() # 接收数据
print(conn,address)

msg = "Hello World"

conn.send(msg.encode())

conn.close()

