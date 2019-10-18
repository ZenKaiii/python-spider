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
        response_template = '''HTTP/1.1 200 OK
     
<html_test>
    <head>
        <title>Web Server</title>
    </head>
    <body>
        Hello world!
    </body>
</html_test>

'''

        # input_data = input()
        sock.send(response_template.encode("utf8"))

while True:
    sock,addr = server.accept()
    client_thread = threading.Thread(target=handle_sock, args=(sock,addr))
    client_thread.start()


