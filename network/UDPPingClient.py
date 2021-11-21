from socket import *
import time
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)

for i in range(0, 10):
    sendTime = time.time()
    message = ('Ping %d %s' % (i + 1, sendTime)).encode()  # 生成数据报，编码为bytes以便发送
    try:
        clientSocket.sendto(message, (serverName, serverPort))  # 将信息发送到服务器
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)  # 从服务器接收信息，同时也能得到服务器地址
        rtt = time.time() - sendTime  # 计算往返时间
        print('Sequence %d: Reply from %s    RTT = %.3fs' % (i + 1, serverName, rtt))  # 显示信息
    except Exception as e:
        print('Sequence %d: Request timed out' % (i + 1))
        print(e)
clientSocket.close()