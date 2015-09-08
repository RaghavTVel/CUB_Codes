import socket

host = 'localhost'
port = 8004
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
file1stringcontent="GET / HTTP/1.1"
file1asciicontent = file1stringcontent.encode('ascii')
s.send(file1asciicontent)
data = s.recv(size)
s.close()
datastringcontent = data.decode('ascii')
print ('Received: '+ datastringcontent)