import socket

host = 'www.google.com'
port = 80
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
file1stringcontent="GET / HTTP/1.1\r"
file1asciicontent = file1stringcontent.encode('ascii')
s.send(file1asciicontent)
data = s.recv(size)
s.close()
datastringcontent = data.decode('ascii')
print ('Received: '+ datastringcontent)