import socket

print('''

 /$$      /$$                       /$$                         /$$$$$$$  /$$                    
| $$$    /$$$                      | $$                        | $$__  $$|__/                    
| $$$$  /$$$$  /$$$$$$   /$$$$$$$ /$$$$$$    /$$$$$$   /$$$$$$ | $$  \ $$ /$$ /$$$$$$$   /$$$$$$ 
| $$ $$/$$ $$ |____  $$ /$$_____/|_  $$_/   /$$__  $$ /$$__  $$| $$$$$$$/| $$| $$__  $$ /$$__  $$
| $$  $$$| $$  /$$$$$$$|  $$$$$$   | $$    | $$$$$$$$| $$  \__/| $$____/ | $$| $$  \ $$| $$  \ $$
| $$\  $ | $$ /$$__  $$ \____  $$  | $$ /$$| $$_____/| $$      | $$      | $$| $$  | $$| $$  | $$
| $$ \/  | $$|  $$$$$$$ /$$$$$$$/  |  $$$$/|  $$$$$$$| $$      | $$      | $$| $$  | $$|  $$$$$$$
|__/     |__/ \_______/|_______/    \___/   \_______/|__/      |__/      |__/|__/  |__/ \____  $$
                                                                                        /$$  \ $$
                                                                                       |  $$$$$$/
                                                                                        \______/ 
[--------------------------Author: https://github.com/EliasPython/ Version:1--------------------]
''')

def client_program():
    host = '127.0.0.1'
    port = 1234

    client_socket = socket.socket()
    client_socket.connect((host, port))

    mode = input("Enter the mode (Normal, dos, opo): ")
    client_socket.send(mode.encode())

    if mode == 'dos':
        ip = input("Enter the target IP/Host: ")
        client_socket.send(ip.encode())
    elif mode == 'opo':
        ip = input("Enter the target IP/Host: ")
        client_socket.send(ip.encode())
    elif mode == 'normal':
        ip = input("Enter the target IP/Host: ")
        client_socket.send(ip.encode())

    client_socket.close()

if __name__ == '__main__':
    client_program()
