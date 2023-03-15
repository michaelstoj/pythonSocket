# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 18:11:58 2022

@author: mikes
"""
#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
serverPort = 9999
serverSocket.bind(("127.0.0.1",serverPort))
serverSocket.listen(1)
#Fill in end
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode() #Fill in start          #Fill in end               
        filename = message.split()[1]                 
        f = open(filename[1:])                        
        outputdata = f.read()#Fill in start       #Fill in end                   
        #Send one HTTP header line into socket
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
        #Fill in start
        #Fill in end                
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):           
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        connectionSocket.send('\n404 File Not Found\n'.encode())
        #Fill in start        
        #Fill in end
        #Close client socket
        connectionSocket.close()
        #Fill in start
        #Fill in end            
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data  