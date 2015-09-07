import socket
import configparser

size=1024
config = configparser.ConfigParser()
config.read('ws.conf')
port = config['DEFAULT']['port']
root = config['DEFAULT']['root']

print("Port: "+port)
print("Root: "+root)

port = int(port)

soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

soc.bind(('',port))
soc.listen(1)

while True:
    conn, addr = soc.accept()
    data = conn.recv(size)
    print(data)
    if data:
        with open(root+"/index.html","r") as file1:
            file1stringcontent = file1.read()
        print(file1stringcontent)
        file1asciicontent = file1stringcontent.encode('ascii')
        conn.send(file1asciicontent)
    print("Just In")
    conn.close()