# 服务端
import socket
import threading

server = socket.socket()
server.bind(('0.0.0.0',8000))
server.listen()

def handle_sock(sock,addr):
    while True:
        # recv是阻塞的
        tmp_data = sock.recv(1024)
        print(tmp_data.decode('utf-8'))
        input_data = input()
        sock.send(input_data.encode("utf-8"))

while True:
    sock,addr = server.accept()
    client_thread = threading.Thread(target=handle_sock, args=(sock,addr))
    client_thread.start()



# data = ''


    # if tmp_data:
    #     data += tmp_data.decode('utf-8')
    #     if tmp_data.decode('utf-8').endswith('#'):
    #         break
    # else:
    #     break

# print(data)
# sock.close()