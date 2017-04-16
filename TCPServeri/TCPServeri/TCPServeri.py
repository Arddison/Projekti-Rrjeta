from socket import *
import time
from random import randint

print("UP-FIEK")
print("Rrjeta Kompjuterike")
print("TCP Server")
print("-----------------------\n")

serverPort = 9000
serverSocket = socket(AF_INET,SOCK_STREAM)

serverSocket.bind(('',serverPort))
serverSocket.listen(1)


print("Serveri eshte gati per pranim te dhenave...")


def getIP():
    ip = gethostbyname(gethostname()) 
    return ip
def getHOST():
    host = gethostname()
    return host
 
def getTime():
  koha= time.ctime()
  return koha

def getKeno():
    keno=[randint(0,80) for i in range (0,20)]
    for n in range(20):
        return keno
        
#funksioni per opcionin konverto 
def konverto(opcioni,numri):
    if opcioni==b"CelsiusToKelvin":
        kelvin = 273.15 +numri
        return kelvin
    elif opcioni == b"CelsiusToFahrenheit":
        fahrenheit = 32 + (numri*9/5)
        return fahrenheit
    elif opcioni == b"KelvinToFahrenheit":
        fahrenheit = (numri*9/5)-459.67
        return fahrenheit
    elif opcioni == b"KelvinToCelsius": 
          celsius = numri - 273.15
          return celsius
    elif opcioni == b"FahrenheitToCelsius":
        celsius = (numri -32)*5/9
        return celsius
    elif opcioni == b"FahrenheitToKelvin":
        kelvin = (numri + 459.67) *5/9
        return kelvin
    elif opcioni == b"PoundToKilogram":
        kilogram = numri*0.45359237
        return kilogram
    elif opcioni == b"KilogramToPound":
        pound = numri/0.45359237
        return pound
    
#funksioni per llogaritjen e faktorielit
def faktoriel(n):
    rez = 1
    while n>0:
        rez *= n
        n -= 1
    return rez
         
mesazhiIP =str(getIP())
mesazhiPORT = str(serverPort)
mesazhiHOST = str(getHOST())
mesazhinull = "Invalid"
mesazhiKoha=str(getTime())
mesazhiKeno=str(getKeno())





while 1:
    connectionSocket, addr = serverSocket.accept()
    opcioni = connectionSocket.recv(1024).decode("ASCII")
    capitalizedOpcioni = opcioni.upper()
    if(opcioni == "IP"):
        connectionSocket.send(mesazhiIP.encode('ASCII'))
    elif (opcioni == "PORT"):
        connectionSocket.send(mesazhiPORT.encode('ASCII'))
    elif (opcioni == "HOST"):
        connectionSocket.send(mesazhiHOST.encode('ASCII'))
    elif (opcioni=="KOHA"):
        connectionSocket.send(mesazhiKoha.encode('ASCII'))
    elif (opcioni=="KENO"):
        connectionSocket.send(mesazhiKeno.encode('ASCII'))
    #pjesa per faktoriel
    elif (opcioni == "FAKTORIEL"):
        connectionSocket.send("Jep numrin: ".encode("ASCII"))
        n = connectionSocket.recv(1024).decode("ASCII")
        connectionSocket.send(str(faktoriel(int(n))).encode("ASCII"))
    #pjesa per konverto
    elif "TO" in capitalizedOpcioni:
        opcioni,numri=opcioni.split(' ') 
        numri1=int(numri)
        mesazhiKONVERTO=str(konverto(opcioni,numri1))
        connectionSocket.send(mesazhiKONVERTO.encode('ASCII'))
    else:
        connectionSocket.send(mesazhinull.encode('ASCII'))
    connectionSocket.close()
