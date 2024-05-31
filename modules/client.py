import socket

HOST = "192.168.1.53"
PORT = 42069
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
        s.connect((HOST, PORT))
        x = input("Message: ")
        s.send(bytes(x, 'utf-8'))
    

