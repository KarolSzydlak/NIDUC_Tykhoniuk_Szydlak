import socket
class recipient:
    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 9090
    recipient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    recipient.bind((HOST,PORT))
    recipient.listen(1)
    print("dziala")
    while True:
        communication_socket, adress = recipient.accept()
        print(f"Connected to {adress}")
        message = communication_socket.recv(1024).decode('ascii')
        print(message)