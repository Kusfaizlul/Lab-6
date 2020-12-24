import socket 
import sys

Client = socket.socket()
host = '192.168.14.10'
port = 4848

try:
    Client.connect((host,port))
    print (' Successfull Connect! ')
except socket.error as e:
    print ( str(e) )

loop = True

while loop:
    print ('\n Welcome to math calculator python ')
    print (' 1. Logarithmic expression ')
    print (' 2. Square Root ')
    print (' 3. Exponential expression ')
    print (' 9. Exit ')
    
    ans = input ('\n Enter your choice : ' )
    Client.send(ans.encode())

    if ans == '1':
        #log
        print ('\n [+] Logarithmic Function ')
        numb = input ('\n Enter Number : ')
        Client.send(numb.encode())
        tot = Client.recv(1024)

        print ( ' Answer for log( '+ numb +' ) : ' + str(tot.decode()))
    elif ans == '2':
        root = True
        While root:
            #Suare Root   
            print ('\n [+] Square Root Function ')
            numb = input ('\n Enter Number : ')
            if int(numb) > -1 :
                root = False
                Client.send(numb.encode())
                tot = Client.recv(1024)
            else
                print ('\n Square Root Cant Be Negative Number !! ')

        print ( ' Answer for sqrt( ' + numb +' ): ' + str(tot.decode()))


    elif ans == '3':
        #exponen
        print ('\n [+] Exponential Function ')
        numb = input ('\n Enter Number : ')
        Client.send(numb.encode())
        tot = Client.recv(1024)

        print ( ' Answer for exp( ' + numb + ' ): ' + str(tot.decode()))


    elif ans == '9':
        #exit
        Client.close()
        sys.exit()
    else:
        print ('\n Invalid input please try again !')

    input ( '\n Press Enter to Continue .. ')
