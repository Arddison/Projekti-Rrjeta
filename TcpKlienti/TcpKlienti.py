from socket import *
import sys
import time


print("UP-FIEK")
print("Rrjeta Kompjuterike")
print("TCP Klienti")
print("-----------------------\n")

serverName = "127.0.0.1"
serverPort = 9000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

print("Zgjedh nje opcion :  \n IP \n PORT \n HOST \n KOHA  \n KENO  \n KONVERTO \n FAKTORIEL \n")
print("-----------------------\n")
opcioni=input()
#me ba case insensitive, e kthejm cdo input nshkronja tmdhaja
opcioniUP=str(opcioni).upper()
#funksioni i cili dergon te dhenat ne server dhe merr nga ai pergjigjien
def konvertoServer():
    clientSocket.send(konvertimi.encode('ASCII'))
    pergjigjiaServerit = clientSocket.recv(1024)
    opcioni,numri=konvertimi.split(' ')
    print("KONVERTO",opcioni,numri,"kthen pergjigjie",
    pergjigjiaServerit.decode('ASCII'))
                
if opcioniUP=="IP":
    clientSocket.send(opcioniUP.encode('ASCII'))
    modifiedOpcioni = clientSocket.recv(1024)
    print("From Server:", modifiedOpcioni.decode('ASCII'))
    clientSocket.close()
elif opcioniUP=="PORT":
    clientSocket.send(opcioniUP.encode('ASCII'))
    modifiedOpcioni = clientSocket.recv(1024)
    print("From Server:", modifiedOpcioni.decode('ASCII'))
    clientSocket.close()

elif opcioniUP=="HOST":
    clientSocket.send(opcioniUP.encode('ASCII'))
    modifiedOpcioni = clientSocket.recv(1024)
    print("From Server:", modifiedOpcioni.decode('ASCII'))
    clientSocket.close()

elif opcioniUP=="KOHA":
    clientSocket.send(opcioniUP.encode('ASCII'))
    modifiedOpcioni = clientSocket.recv(1024)
    print("From Server:", modifiedOpcioni.decode('ASCII'))
    clientSocket.close()

elif opcioniUP=="KENO":
    clientSocket.send(opcioniUP.encode('ASCII'))
    modifiedOpcioni = clientSocket.recv(1024)
    print("From Server:", modifiedOpcioni.decode('ASCII'))
elif opcioniUP == "FAKTORIEL":
    clientSocket.send(opcioniUP.encode("ASCII"))
    print ( clientSocket.recv(1024).decode("ASCII"))
    numri = input()
    clientSocket.send(numri.encode("ASCII"))
    print ("Rezultati: " + str(numri) + "! = " + clientSocket.recv(1024).decode("ASCII"))
elif opcioniUP=="KONVERTO":
    konvertimi = input("KONVERTO ")
    if konvertimi=="?":
        print("-----------------------\n")
        print("CelsiusToKelvin\n","CelsiusToFahrenheit\n","KelvinToFahrenheit\n",
            "KelvinToCelsius\n","FahrenheitToCelsius\n","FahrenheitToKelvin\n",
            "PoundToKilogram\n","KilogramToPound\n")
        print("-----------------------\n")
        konvertimi = input("KONVERTO ")
        #thirrja e funksionit per dergim dhe pranim te te dhenave me serverin 
        konvertoServer()
    else:
        konvertoServer()



clientSocket.close()
