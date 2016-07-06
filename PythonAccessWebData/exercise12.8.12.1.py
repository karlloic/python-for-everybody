# Chapter 12.8 Exercise 12.1
import socket
# import logging

url = 'http://www.pythonlearn.com'
urlParts = url.split('/')

connector = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    hostname = urlParts[2]
    connector.connect((hostname, 80))
except:
    print('Enter a valid URL')
    exit()

connector.send('GET ' + url + 'HTTP/1.0\n\n')
size = 0
content = ''
while True:
    data = connector.recv(512)
    if len(data) < 1:
        break
    content += data;
    size += len(data)

print(content[:3000])
