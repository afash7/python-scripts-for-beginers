import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connection.connect(("ip", 80))

print("connected :)")

connection.send("GET /index.html/ HTTP/1.0 \n\n")

data = connection.recv(1234)

print (data)

connection.close()
