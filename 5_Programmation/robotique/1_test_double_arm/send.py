import serial
import time
from gpiozero import *

ser = serial.Serial("/dev/ttyS0",baudrate=115200)

def send_uart(addr, angl = [], time = 0):
    '''
    Fonction for sending angle.
    @param1 : addr -> adresse
    @param2 : angl[] -> list 0f angle < 180
    @parma3 : time -> time of execution (default not send)
    Ex : !1&123+012+235$045Z;
    '''
    #send start bit
    send = b'!'
    #send the address (01 for cam)
    send = send + bytes(str(("{:02d}").format(addr)), encoding="ascii")
    send = send + b'&'
    
    nangl = len(angl)
    i = 0
    if nangl > 1:
        nangl = nangl - 1  
        while i is not nangl:
            #check under 180
            if angl[i] > 180 :
                angl[i] = 256
                
            #send angle (000 + 000 + ...)
            send = send + bytes(str(("{:03d}").format(angl[i])), encoding="ascii")
            #send + between
            send = send + b'+'
            i = i + 1
        i = len(angl)
        if angl[i-1] > 180 :
            angl[i-1] = 256
            
        #send last angle
        send = send + bytes(str(("{:03d}").format(angl[i-1])), encoding="ascii")
        send = send + b'$'
    else :
        #for 1 angle
        #check under 180
        if angl :
            if angl[i] > 180 :
                angl[i] = 256
            
            #send angle
            send = send + bytes(str(("{:03d}").format(angl[0])), encoding="ascii")
            send = send + b'$'
    #send time
    if time is not 0:
        send = send + bytes(str(("{:03d}").format(time)), encoding="ascii")
        send = send + b'Z'
    
    #send stop bit
    send = send + b';'
    
    #print(send)
    # SEND
    ser.write(send)
    
    #wait the ack
    while not verif_ack(addr):
        #send
        ser.write(send)
    

def read_commande_line(addr,ang = [], time = 0):
    '''
    Fonction for read and set the commande line to send UART.
    @param1 : addr -> adresse
    @param2 : angl[] -> list 0f angle < 180
    @parma3 : time -> time of execution (default not send)
    Ex : !1&123+012+235$045Z;
    '''
    ecrit = LED(23)
    lecture = Button(24)
    
    #si la ligne est a 0
    if lecture.is_pressed :
        print("can't write")
        
        return 0
    
    else :
        #bloquer la ligne
        ecrit.on()
        #envoie des info
        send_uart(addr,ang,time)
        #relacher la ligne
        ecrit.off()
        
        return 1

def read_uart():
    '''
    read the UART line.
    return (string): addr, angl, time
    '''
    
    time = ""
    addr = ""
    angl = ""
    
    receive = ser.read_until(b';')
    print(receive)
    receive = str(receive, 'utf-8')
    
    if receive[0] == '!' and ";" in receive:
        i = 1
        while receive[i] is not "&":
            addr = addr + receive[i]
            i += 1
        i += 1
        if "$" in receive:
            while receive[i] is not "$":
                if receive[i] is not "+":
                    angl = angl + receive[i]
                i += 1
            
        i += 1
        if "Z" in receive:
            while receive[i] is not "Z":
                time = time + receive[i]
                i += 1
    #print(addr)
    #print(angl)
    #print(time)
    return addr, angl, time
    
def poignee_main(addr):
    '''
    send addr for hand shake
    @param1 : addr to send
    '''
    start = time.time()
    
    read_commande_line(addr)
    
    #wait the ack
    while not verif_ack(addr):
        #send
        read_commande_line(addr)
        
    return 1
     
def verif_ack(addr):
    start = time.time()
    returnAddr = None
    
    while returnAddr is not addr:
        returnAddr, _, _ = read_uart()
        end = time.time()
        if (end - start) >= 0.03:
            return 0       
    return 1
     
if __name__ ==  "__main__":
    pass