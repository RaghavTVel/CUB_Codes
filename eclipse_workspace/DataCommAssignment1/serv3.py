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
    #print(data)
    datastring = data.decode('ascii')
    datastringlist = datastring.split('\r\n')
    #print(datastringlist)
    
    if data:
        
        if datastringlist[0]=='GET / HTTP/1.1':
            #print("In Index HTML")
            with open(root+"/index.html","rb") as file1:
                file1content = file1.read()
                response_header = "HTTP/1.1 200 OK\r\n"+"Content-Type: text/html; charset=UTF-8\r\n"+"Content-Length: 620\r\n"+"\r\n"
                response_header_binary = response_header.encode('ascii')
                file1asciicontent = response_header_binary+file1content
        
        if datastringlist[0]=='GET /html/nextpage.html HTTP/1.1':
            #print("In HTML")
            with open(root+"/html/nextpage.html","rb") as file1:
                file1content = file1.read()
                response_header = "HTTP/1.1 200 OK\r\n"+"Content-Type: text/html; charset=UTF-8\r\n"+"Content-Length: 300\r\n"+"\r\n"
                response_header_binary = response_header.encode('ascii')
                file1asciicontent = response_header_binary+file1content
        
        if datastringlist[0]=='GET /text/thankyou.txt HTTP/1.1':
            #print("In Text")
            with open(root+"/text/thankyou.txt","rb") as file1:
                file1content = file1.read()
                response_header = "HTTP/1.1 200 OK\r\n"+"Content-Type: text/plain\r\n"+"Content-Length: 60\r\n"+"\r\n"
                response_header_binary = response_header.encode('ascii')
                file1asciicontent = response_header_binary+file1content
        
        if datastringlist[0]=='GET /images/impact.gif HTTP/1.1':
            #print("In GIF")
            with open(root+"/images/impact.gif","rb") as file1:
                file1content = file1.read()
                response_header = "HTTP/1.1 200 OK\r\n"+"Content-Type: image/gif\r\n"+"Content-Length: 168998\r\n"+"\r\n"
                response_header_binary = response_header.encode('ascii')
                file1asciicontent = response_header_binary+file1content
        
        if datastringlist[0]=='GET /images/fractal.png HTTP/1.1':
            #print("In PNG")
            with open(root+"/images/fractal.png","rb") as file1:
                file1content = file1.read()
                response_header = "HTTP/1.1 200 OK\r\n"+"Content-Type: image/png\r\n"+"Content-Length: 131365\r\n"+"\r\n"
                response_header_binary = response_header.encode('ascii')
                file1asciicontent = response_header_binary+file1content
               
        conn.send(file1asciicontent)
    #print("Near Exit point")
    conn.close()