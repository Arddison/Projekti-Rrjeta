from socket import *
import time
from random import randint
import math

print("UP-FIEK")
print("Rrjeta Kompjuterike")
print("UDP Server")
print("-----------------------\n")

serverPort = 9000
serverSocket = socket(AF_INET,SOCK_DGRAM)

serverSocket.bind(('',serverPort))



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

    if opcioni=="CELSIUSTOKELVIN":
        kelvin = 273.15 +numri
        return kelvin
    elif opcioni =="CELSIUSTOFAHRENHEIT":
        fahrenheit = 32 + (numri*9/5)
        return fahrenheit
    elif opcioni == "KELVINTOFAHRENHEIT":
        fahrenheit = (numri*9/5)-459.67
        return fahrenheit
    elif opcioni == "KELVINTOCELSIUS": 
          celsius = numri - 273.15
          return celsius
    elif opcioni == "FAHRENHEITTOCELSIUS":
        celsius = (numri -32)*5/9
        return celsius
    elif opcioni == "FAHRENHEITTOKELVIN":
        kelvin = (numri + 459.67) *5/9
        return kelvin
    elif opcioni == "POUNDTOKILOGRAM":
        kilogram = numri*0.45359237
        return kilogram
    elif opcioni == "KILOGRAMTOPOUND":
        pound = numri/0.45359237
        return pound
    
#funksioni per llogaritjen e faktorielit
def faktoriel(n):
    rez = 1
    while n>0:
        rez *= n
        n -= 1
    return rez

def eshteZanore(ch):
    return ch in "aeiouyAEIOUY"

def numriZanoreve(fjala):
    vlera = 0
    for ch in fjala:
        if eshteZanore(ch):
            vlera += 1
    return vlera

def BRISHTE(viti):
    intviti=int(viti)
    if intviti%4==0:
        if intviti%100==0:
            if intviti%400==0:
                return "Viti "+viti+" eshte i Brishte"
            else:
                return "Viti "+viti+" nuk eshte i Brishte"
        else:
            return "Viti "+viti+"  eshte i Brishte"
    else:
        return "Viti "+viti+" nuk eshte i Brishte"  

#Funksionet Ekstra Gjenerimi i numrave primar deri ne X:Ardi Rexhepi
def PRIMAR(max):
    import math
    import random
    maxint = int(max)
    def isPrime(n):
        if n == 2:
            return True
        if n % 2 == 0 or n <= 1:
            return False

        sqr = int(math.sqrt(n)) + 1

        for i in range(3, sqr, 2):
            if n % i == 0:
                return False
        return True

    lista = []
    if maxint <=1:
        return "Nuk ka numra primar ne kete interval"
    else:
        for i in range(2,maxint+1):
            if isPrime(i):
                lista.append(i)


        return random.choice(lista)
#Funksioni koha per sherbimin Transfero-Premtim Ramadani
def koha(opcioni,sasia,shpejtesia):
    if opcioni=="1":
        koha=float((sasia*8)/shpejtesia)
        if koha>=3600:
            dite=int(koha/3600)
            diteStr=str(dite)
            minuta=koha%3600
            minutaStr=str(minuta)
            sekonda=(koha%3600)*60
            sekondaStr=str(sekonda)
            return "Koha e nevojshme: "+diteStr+" dite "+minutaStr+" minuta "+sekondaStr+" sekonda"
        elif koha>=60:
            minuta=int(koha/60)
            minuta=str(minuta)
            sekonda=koha%60
            sekondaStr=str(sekonda)
            return "Koha e nevojshme: "+minutaStr+" minuta "+sekondaStr+" sekonda "
        else:
            kohaStr=str(koha)
            return "Koha e nevojshme: "+kohaStr+" sekonda"
    elif opcioni=="2":
        koha=(float((sasia*8)/(shpejtesia*1000)))*1000
        kohaStr=str(koha)
        mesazhi=kohaStr+" miliSekonda"
        return mesazhi
    elif opcioni=="3":
        koha=(float((sasia*8)/(shpejtesia*1000000)))*1000000
        kohaStr=str(koha)
        mesazhi=kohaStr+" mikroSekonda"
        return mesazhi
    elif opcioni=="4":
        koha=float(sasia*8000/shpejtesia)
        if koha>=3600:
            dite=int(koha/3600)
            diteStr=str(dite)
            minuta=koha%3600
            minutaStr=str(minuta)
            sekonda=(koha%3600)*60
            sekondaStr=str(sekonda)
            return "Koha e nevojshme: "+diteStr+" dite "+minutaStr+" minuta "+sekondaStr+" sekonda"
        elif koha>=60:
            minuta=int(koha/60)
            minuta=str(minuta)
            sekonda=koha%60
            sekondaStr=str(sekonda)
            return "Koha e nevojshme: "+minutaStr+" minuta "+sekondaStr+" sekonda "
        else:
            kohaStr=str(koha)
            return "Koha e nevojshme: "+sekonda+" sekonda"
    elif opcioni=="5":
        koha= float(sasia*8/shpejtesia)
        if koha>=3600:
            dite=int(koha/3600)
            diteStr=str(dite)
            minuta=koha%3600
            minutaStr=str(minuta)
            sekonda=(koha%3600)*60
            sekondaStr=str(sekonda)
            return "Koha e nevojshme: "+diteStr+" dite "+minutaStr+" minuta "+sekondaStr+" sekonda"
        elif koha>=60:
            minuta=int(koha/60)
            minuta=str(minuta)
            sekonda=koha%60
            sekondaStr=str(sekonda)
            return "Koha e nevojshme: "+minutaStr+" minuta "+sekondaStr+" sekonda "
        else:
            kohaStr=str(koha)
            return "Koha e nevojshme: "+kohaStr+" sekonda"
    elif opcioni=="6":
        koha=(float((sasia*8)/(shpejtesia*1000)))*1000
        kohaStr=str(koha)
        mesazhi=kohaStr+" miliSekonda"
        return mesazhi
    elif opcioni=="7":
        koha=float((sasia*8000000)/shpejtesia)
        if koha>=3600:
            dite=int(koha/3600)
            diteStr=str(dite)
            minuta=koha%3600
            minutaStr=str(minuta)
            sekonda=(koha%3600)*60
            sekondaStr=str(sekonda)
            return "Koha e nevojshme: "+diteStr+" dite "+minutaStr+" minuta "+sekondaStr+" sekonda"
        elif koha>=60:
            minuta=int(koha/60)
            minuta=str(minuta)
            sekonda=koha%60
            sekondaStr=str(sekonda)
            return "Koha e nevojshme: "+minutaStr+" minuta "+sekondaStr+" sekonda "
        else:
            kohaStr=str(koha)
            return "Koha e nevojshme: "+sekonda+" sekonda"
    elif opcioni=="8":
        koha=float((sasia*8000)/shpejtesia)
        if koha>=3600:
            dite=int(koha/3600)
            diteStr=str(dite)
            minuta=koha%3600
            minutaStr=str(minuta)
            sekonda=(koha%3600)*60
            sekondaStr=str(sekonda)
            return "Koha e nevojshme: "+diteStr+" dite "+minutaStr+" minuta "+sekondaStr+" sekonda"
        elif koha>=60:
            minuta=int(koha/60)
            minuta=str(minuta)
            sekonda=koha%60
            sekondaStr=str(sekonda)
            return "Koha e nevojshme: "+minutaStr+" minuta "+sekondaStr+" sekonda "
        else:
            kohaStr=str(koha)
            return "Koha e nevojshme: "+sekonda+" sekonda"
    elif opcioni=="9":
        koha=float((sasia*8/shpejtesia))
        if koha>=3600:
            dite=int(koha/3600)
            diteStr=str(dite)
            minuta=koha%3600
            minutaStr=str(minuta)
            sekonda=(koha%3600)*60
            sekondaStr=str(sekonda)
            return "Koha e nevojshme: "+diteStr+" dite "+minutaStr+" minuta "+sekondaStr+" sekonda"
        elif koha>=60:
            minuta=int(koha/60)
            minuta=str(minuta)
            sekonda=koha%60
            sekondaStr=str(sekonda)
            return "Koha e nevojshme: "+minutaStr+" minuta "+sekondaStr+" sekonda "
        else:
            kohaStr=str(koha)
            return "Koha e nevojshme: "+kohaStr+" sekonda"
#definimi i funksionit exchange per sherbimin exchange (monedhave)-Premtim Ramadani
def exchange(opcioni, vlera):
    if opcioni == "EURO-DOLLAR":
        dollar=vlera*0.94
        return dollar
    if opcioni == "EURO-POUND":
        pound = vlera*0.85
        return pound
    if opcioni == "DOLLAR-EURO":
        euro = vlera/0.94
        return euro
    if opcioni == "DOLLAR-POUND":
        pound = vlera*0.8
        return pound
    if opcioni == "POUND-EURO":
        euro = vlera/0.85
        return euro
    if opcioni == "POUND-DOLLAR":
        dollar = vlera/0.8
        return dollar
    #funksionet ekstra: Arber Shumolli

def ekKuadratik(a,b,c):
   d = b*b-4*a*c
   if d<0:
       return ("Ky ekuacion nuk ka zgjidhje reale...")
     
   elif d==0:
       x1=(-b+math.sqrt(b**2-4*a*c))/2*a
       return ("Ekuacioni ka zgjidhje te barabarta : %.2f" %x1)
       
   else:
       x1 = (-b+math.sqrt(b**2-4*a*c))/2*a
       x2 = (-b-math.sqrt(b**2-4*a*c))/2*a
       return(" Zgjidhjet e ekuacionit jane : x1=%.2f x2=%.2f" %(x1, x2))

def getMesatare():
    shuma=0
    keno=[randint(0,1000) for i in range (0,20)]
    for n in range(20):
        shuma=shuma+keno[n]
    return shuma/20

#Metodat ekstra:Arsim Osmani     
def nxitimi(v,vf,t):
    a=(v-vf)/t
    if vf<v:
         a=(v-vf)/t
         return("Kemi pershpejtim: a=%.2f" %a)
    elif vf==0:
         a=v/t
         return("Nxitimi konstant: a=%.2f" %a)
    else:
         return("Nxitimi konstant")

#Metodat ekstra:Arsim Osmani

def reverse(text):
    if len(text)<=1:
        return text
    return reverse(text[1:])+text[0]
        
        
#funksioni kalkulo - Ardison Molliqaj
def kalkulo(opsioni, num1, num2):
    if (opsioni =="MBLEDH"):
        return num1 + num2
    elif (opsioni == "ZBRIT"):
        return num1 - num2
    elif (opsioni == "SHUMEZO"):
        return num1 * num2
    elif (opsioni == "PJESTO"):
        return num1 / num2

#funksioni per konstanta - Ardison Molliqaj
def konstantat(opsioni):
    if (opsioni == "PI"):
        return 3.1415
    elif (opsioni == "E"):
        return 2.71
    elif (opsioni == "G"):
        return 9.81

        

mesazhiIP =str(getIP())
mesazhiPORT = str(serverPort)
mesazhiHOST = str(getHOST())
mesazhinull = "Invalid"
mesazhiKoha=str(getTime())
mesazhiKeno=str(getKeno())





while 1:
    inputi, address = serverSocket.recvfrom(2048)
    inputi= inputi.decode("ASCII").upper().split(' ')
    if(inputi[0].upper() == "IP"):
        serverSocket.sendto(mesazhiIP.encode('ASCII'),address)
    elif (inputi[0].upper() == "PORT"):
        serverSocket.sendto(mesazhiPORT.encode('ASCII'),address)
    elif (inputi[0].upper() == "HOST"):
        serverSocket.sendto(mesazhiHOST.encode('ASCII'),address)
    elif (inputi[0].upper()=="KOHA"):
        serverSocket.sendto(mesazhiKoha.encode('ASCII'),address)
    elif (inputi[0].upper()=="KENO"):
        serverSocket.sendto(mesazhiKeno.encode('ASCII'),address)
    #pjesa per faktoriel
    elif (inputi[0].upper() == "FAKTORIEL"):
        serverSocket.sendto(str(faktoriel(int(inputi[1]))).encode("ASCII"),address)
    #pjesa per konverto
    elif (inputi[0].upper() == "KONVERTO"):
        if (inputi[1] == "?"):
            paraqitja=str("-----------------------\nCelsiusToKelvin\nCelsiusToFahrenheit\nKelvinToFahrenheit\nKelvinToCelsius\nFahrenheitToCelsius\nFahrenheitToKelvin\nPoundToKilogram\nKilogramToPound\n-----------------------\n")
            serverSocket.sendto(paraqitja.encode('ASCII'),address)
            continue
        pergjigjaServerit = konverto(inputi[1],  int(inputi[2]))
        serverSocket.sendto(str(pergjigjaServerit).encode("ASCII"),address)
    elif (inputi[0].upper() == "ZANORE"):
        pergjigjaServerit = numriZanoreve(inputi[1])
        serverSocket.sendto(str(pergjigjaServerit).encode("ASCII"),address)
    elif (inputi[0].upper() == "PRINTO"):
        serverSocket.sendto(inputi[1].encode("ASCII"),address)
    elif (inputi[0].upper() == "PRIMAR"):
        serverSocket.sendto(str(PRIMAR(inputi[1])).encode("ASCII"),address)
    elif (inputi[0].upper() == "BRISHTE"):
        serverSocket.sendto(BRISHTE(inputi[1]).encode("ASCII"),address)
    elif (inputi[0].upper() == "TRANSFERIMI"):
        if (inputi[1] == "?"):
           serverSocket.sendto(("-----------------------\nZgjedhni njerin nga opcionet(shkruani numrin):\n1.KB-Kb/s\n2.KB-Mb/s\n3.KB-Gb/s\n4.MB-Kb/s\n5.MB-Mb/s\n6.MB-Gb/s\n7.GB-Kb/s\n8.GB-Mb/s\n9.Gb-Gb/s-----------------------\nPastaj jepni dy vlera (e para per sasine e te dhenave kurse e dyta per shpejtesine e transferimit)").encode('ASCII'),address)
           continue
        serverSocket.sendto(koha(inputi[1], int(inputi[2]), int(inputi[3])).encode("ASCII"),address)
    elif (inputi[0].upper() == "EXCHANGE"):
        if (inputi[1] == "?"):
            serverSocket.sendto(("-----------------------\nEuro-Dollar\nEuro-Pound\nDollar-Euro\nDollar-Pound\nPound-Euro\nPound-Dollar\n-----------------------\n").encode('ASCII'),address)
            continue
        serverSocket.sendto(str(exchange(inputi[1], int(inputi[2]))).encode("ASCII"),address)
    elif (inputi[0].upper() == "KUADRATIK"): 
        serverSocket.sendto(ekKuadratik(int(inputi[1]), int(inputi[2]), int(inputi[3])).encode("ASCII"),address)
    elif (inputi[0].upper()=="MESATARJAKENO"):
        strMesazhi=str("Mesatarja e numrave te rendomte "+str(getMesatare()))
        serverSocket.sendto(strMesazhi.encode("ASCII"),address)
    elif inputi[0] == "HELP":
        helpi="Shembuj per inpute\n-----------------------\n ip\n port\n zanore fjala-fjalia\n host\n time\n keno\n faktoriel numri\n konverto njesia1TOnjesia2 numri (konverto CelsiusToKelvin 12)\n exchange valuta1-valuta2 sasia (exchange dollar-euro 100)\n transferimi opcioni(1-9) sasia shpejtesia (transferimi 1 20 20)\n Brishte Viti \n Primar Vlera maksiale \n Kuadratik a b c (ax^2+bx+c=0)\n MesatarjaKeno \n Nxitimi num1 num2 num3 \n Reverse teksti \n Kalkulo operacioni num1 num2 \n Konstantja emri\n----------------------\n"
        serverSocket.sendto(helpi.encode("ASCII"),address)
    elif (inputi[0].upper()=="NXITIMI"):
         serverSocket.sendto(nxitimi(int(inputi[1]), int(inputi[2]), int(inputi[3])).encode("ASCII"),address)
    elif (inputi[0].upper()=="REVERSE"):
         serverSocket.sendto(reverse(inputi[1]).encode("ASCII"),address)
    elif (inputi[0].upper() == "KALKULO"):
         serverSocket.sendto(str(kalkulo(inputi[1], int(inputi[2]), int(inputi[3]))).encode("ASCII"), address)
    elif (inputi[0].upper() == "KONSTANTA"):
         if (inputi[1] == "?"):
             serverSocket.sendto(("Zgjidhni nje nga konstantat me poshte: \n PI \n e \n G \n").encode("ASCII"), address)
             continue
         serverSocket.sendto(str(konstantat(inputi[1])).encode("ASCII"), address)
    else: 
        serverSocket.sendto(mesazhinull.encode('ASCII'),address)
