import socket
import time
import urllib.request, urllib.parse, urllib.error

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mySocket.send(cmd)

while True:
    data = mySocket.recv(512)
    if len(data) < 1:
        break
    # print(data.decode(), end='')

mySocket.close()


# Retrieving images over HTTP

HOST = 'data.pr4e.org'
port = 80

imageSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
imageSocket.connect((HOST, port))
imageSocket.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
count = 0
picture = b""

while True:
    imgData = imageSocket.recv(5120)
    if len(imgData) < 1: break
    count = count + len(imgData)
    picture = picture + data

imageSocket.close()

# Look for the end of the header (2 CRLF)
# and delete the header from the content
pos = picture.find(b"\r\n\r\n")
print(picture[:pos].decode())

picture = picture[pos+4:]
fHand = open("stuff.jpg", "wb")
fHand.write(picture)
fHand.close()


# urllib - more feasible way to retrieve web pages in python
print('Retrieving data through urllib')
fileHandler = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fileHandler:
    print(line.decode().strip())

# retrieveing the file from server
# and counting the frequency of each word

count = dict()
wordCountHandler = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for currentLine in wordCountHandler:
    words = currentLine.decode().split()
    for word in words:
        count[word] = count.get(word, 0) + 1
print(count)

# reading image or video files using urllib
img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
imageHandler = open('cover3.jpg', 'wb')
size = 0
while True:
    info = img.read(1000000)
    if len(info) < 1: break
    size = size + len(info)
    imageHandler.write(info)

print(size, 'character copied')
imageHandler.close()




