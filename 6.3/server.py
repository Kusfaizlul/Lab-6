import socket 
import math 
import erno 

Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 4848

try:
    Server.Socket.bind((host,port))
except socket.error as e:
    print (str(e))

Server.listen(5)

while True:
    s = Server.accept()
    print ('\n Sucessfully Connected !! ')

    get = s.recv(1)
    number = s.recv(1024)

    if get.decode() == '1':
        #log calculation
        calc = math.log(float(number.decode()))

    elif get.decode() == '2':
        #SquareRoot calculation
        calc = math.sqrt(float(number.decode()))

    elif get.decode() == '3':
        #exponential Calculation
        calc = math.exp(float(number.decode()))
    elif get.decode() == '9':
        s.close()

    s.send(str(calc).decode())
