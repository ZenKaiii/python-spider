import socket

client = socket.socket()
client.connect(('172.22.19.235',8000))

#  以#结尾提交完成
# server_data = client.recv(1024)
# print("server response {}".format(server_data.decode('utf-8')))
while True:
    input_data = input()
    client.send(input_data.encode("utf-8"))
    server_data = client.recv(1024)
    print("server response: {}".format(server_data.decode('utf-8')))