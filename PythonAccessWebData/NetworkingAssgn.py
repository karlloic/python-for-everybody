# Parsing HTTP Header
import socket

connector = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connector.connect(("www.pythonlearn.com", 80))
connector.send("GET http://www.pythonlearn.com/codes/intro-short.txt HTTP/1.0\n\n")

while True:
    data = connector.recv(512)
    if len(data) < 1:
        break
    print(data)
