#!/usr/bin/env python2.7

import os
import re
import sys
import urllib
import random
import ConfigParser
from time import gmtime, strftime, sleep

class color:
    HEADER = '\033[95m'
    IMPORTANT = '\33[35m'
    NOTICE = '\033[33m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'
    LOGGING = '\33[34m'

installPath = os.path.dirname(os.path.abspath(__file__)) + '/'

random_color=[color.HEADER,color.IMPORTANT,color.NOTICE,color.BLUE,color.GREEN,color.WARNING,color.RED,color.END,color.UNDERLINE,color.LOGGING]
random.shuffle(random_color)

os.system("clear")
logo = random_color[0] + ''' 
        .d8888. 88"""Yb db      db 88888b.  88""Yb  .d8888.
        88'  YP 88   dP  `8b  d8'   8I  dY  88   db 88'  YP
        `8bo.   88___Yb   `8bd8'    8I   dY 88  db  `8bo.
          `Y8b. 88"""       88      8I   dY 88"Yb     `Y8b.
        db   8D 88          88      8I  dY  88  YP  db   8D
        `8888Y' 88          YP     88888b.  88   YI `8888Y'                               
     '''
menu = color.GREEN + '''
    {1}--Whois Lookup
    {2}--Traceroute
    {3}--DNS Lookup
    {4}--Reverse DNS Lookup
    {5}--GeoIP Lookup
    {6}--Port Scan(Nmap)
    {7}--Reverse IP Lookup
    {8}--Subdomain Finder
    {9}--Admin Panel Finder
    {10}-Upload File Finder
    {11}-Get server Info
    {12}-XssPy
    {99}-Exit                                                                                                                   
 '''

# find admin panels
def findAdminPanels():
	target = raw_input('Enter target: ')
        os.system("clear")
	print("""
  __  ___  _    _  ___  _   _     ___   __   _   _  ___  _
 /  \ |  \ |\  /| |_ _|| \ | |   |   \ /  \ | \ | || __/| |
/ () \||) || \/ |  | | |  \| |   | *_// () \|  \| || _/ | |_
|_/\_||__/ |_||_| |___|\_|\__/   |_|  |_/\_|\_|\__/|___/|___|
     
	  """)

	print "[~] Finding admin panels"
	adminList = ['admin/', 'site/admin', 'admin.php/', 'up/admin/', 'central/admin/', 'whm/admin/', 'whmcs/admin/', 'support/admin/', 'upload/admin/', 'video/admin/', 'shop/admin/', 'shoping/admin/', 'wp-admin/', 'wp/wp-admin/', 'blog/wp-admin/', 'admincp/', 'admincp.php/', 'vb/admincp/', 'forum/admincp/', 'up/admincp/', 'administrator/',
		     'administrator.php/', 'joomla/administrator/', 'jm/administrator/', 'site/administrator/', 'install/', 'vb/install/', 'dimcp/', 'clientes/', 'admin_cp/', 'login/', 'login.php', 'site/login', 'site/login.php', 'up/login/', 'up/login.php', 'cp.php', 'up/cp', 'cp', 'master', 'adm', 'member', 'control', 'webmaster', 'myadmin', 'admin_cp', 'admin_site', 'adminpanel/']
	for admin in adminList:
		try:
		    if urllib.urlopen(target + admin).getcode() == 200:
			print " [*] Found admin panel -> ", target + admin
		except IOError:
		    pass
        quit()

#get server info
def getServerInfo():
        target = raw_input('Enter Server IP: ')
        os.system("clear")
	print("""     
  ____                              ___         ____ 
 / ___| ___  ___  _ _  ___  ___    |_ _|______ | __/___
 \___ \| -_||  _|| | || -_||  _|    | | | | | \| _// _ \,
 |____/|___||_|   \_/ |___||_|     |___||_| |_||_| \___/

      """)

        try:
            s = 'http://' + target
            httpresponse = urllib.urlopen(s)
            print ' [*] Server header -> ', httpresponse.headers.getheader(
                'server')
        except:
            print('[*] Server header ->  Not Found')
        quit()

def findUploadFile():
        target = raw_input('Enter target: ')
        os.system("clear")
	print("""     
                                        
  _   _  ___  _     ___    __   ___      ___  ___  _    ___      ___  ___  _   _  __   ___  ___
 | | | ||   \| |   /   \  /  \  |  \    | __/|_ _|| |  | __/    | __/|_ _|| \ | ||  \ | __/|   )
 | \_/ || *_/| |_ | ( ) |/ () \ ||) |   | _/  | | | |_ | _/     | _/  | | |  \| |||) || _/ | * \  
  \___/	|_|  |___| \___/ |_/\_| |__/    |_|  |___||___||___/    |_|  |___|\_|\__/|__/ |___/|_|\|
 
      """)
        
        upList = ['up.php', 'up1.php', 'up/up.php', 'site/up.php', 'vb/up.php', 'forum/up.php', 'blog/up.php', 'upload.php',
                  'upload1.php', 'upload2.php', 'vb/upload.php', 'forum/upload.php', 'blog/upload.php', 'site/upload.php', 'download.php']
        print "[~] Finding Upload"
	for up in upList:
	    try:
		if (urllib.urlopen(target + up).getcode() == 200):
		    html = urllib.urlopen(target + up).readlines()
		    for line in html:
		        if re.findall('type=file', line):
		            print " [*] Found upload -> ", target + up
	    except IOError:
	        pass
        quit()

class XssPy:
    def __init__(self):
        self.installPath = installPath + "XssPy"
        self.gitRepo = "https://github.com/faizann24/XssPy.git"

        if not self.installed():
            self.install()
        target = raw_input("Enter Target: ")
        os.system("clear")
        print("""

   __  ______ ____ _____  _    _
   \ \/ / ___/ ___|| '_ \| \  / |
    \  /\___ \___ \| ,__/ \ \/ /
    /  \ ___) |__) | |     \  / 
   /_/\_\____/____/|_|     \_/ 

          """)
        self.run(target)

    def installed(self):
        return (os.path.isdir(self.installPath))

    def install(self):
        os.system("git clone --depth=1 %s %s" %
                  (self.gitRepo, self.installPath))

    def run(self, target):
        try:
            os.system("python %s/XssPy.py -u %s" %
                      (self.installPath, target))
        except KeyboardInterrupt:
            pass
        quit()

print logo
print menu

def quit():
            con = raw_input('Continue [Y/n] -> ')
            if con[0].upper() == 'N':
                exit()
            else:
                os.system("clear")
                print logo
                print menu
                select()

           
def  select():
  try:
    choice = input("spydrs~# ")
    if choice == 1:
      target = raw_input('Enter IP Or Domain : ')
      os.system("clear")
      print("""
 _       ____  ______  _________
| |     / / / / / __ \/  _/ ___/
| | /| / / /_/ / / / // / \__ \ 
| |/ |/ / __  / /_/ _/ / ___/ / 
|__/|__/_/ /_/\____/___//____/                                  
      """)
      os.system("curl http://api.hackertarget.com/whois/?q=" + target)
      print("")
      quit()
    elif choice == 2:
      target = raw_input('Enter IP Or Domain : ')
      os.system("clear")
      print("""
 _____  ___    __    __  ___  ___   ___   _   _  _____  ___
|_   _||   )  /  \  /  \| __/|   ) /   \ | | | ||_   _|| __/
  | |  | * \ / () \| (| | _/ | * \| ( ) || \_/ |  | |  | _/
  |_|  |_|\| |_/\_| \__/|___/|_|\| \___/  \___/   |_|  |___/
  

""")
      os.system("curl https://api.hackertarget.com/mtr/?q=" + target )
      print("")
      quit()
    elif choice == 3:
      target = raw_input('Enter Domain : ')
      os.system("clear")
      print("""
______ _   _ _____   _                 _                
|  _  | \ | /  ___| | |               | |               
| | | |  \| \ `--.  | |     ___   ___ | | ___   _ _ __  
| | | | . ` |`--. \ | |    / _ \ / _ \| |/ | | | | '_ \ 
| |/ /| |\  /\__/ / | |___| (_) | (_) |   <| |_| | |_) |
|___/ \_| \_\____/  \_____/\___/ \___/|_|\_\\__,_| .__ / 
                                                 | |    
                                                 |_|     
""")
      os.system("curl http://api.hackertarget.com/dnslookup/?q=" + target )
      print("")
      quit()    
    elif choice == 4:
	  target = raw_input('Enter IP Address - IP Range Or Domain  : ')
	  os.system("clear")
	  print("""
 _____                            ____  _____ _____ 
| __  |___ _ _ ___ ___ ___ ___   |    \|   | |   __|
|    -| -_| | | -_|  _|_ -| -_|  |  |  | | | |__   |
|__|__|___|\_/|___|_| |___|___|  |____/|_|___|_____|
                                                    
	  """)
	  os.system("curl https://api.hackertarget.com/reversedns/?q=" + target )
	  print("")
	  quit()
    elif choice == 5:
	  target = raw_input('Enter IP Or Domain : ')
	  os.system("clear")
	  print("""
   _____           _____ _____  
  / ____|         |_   _|  __ \ 
 | |  __  ___  ___  | | | |__) |
 | | |_ |/ _ \/ _ \ | | |  ___/ 
 | |__| |  __| (_) _| |_| |     
  \_____|\___|\___|_____|_|     
                                	
	""")
	  os.system("curl http://api.hackertarget.com/geoip/?q=" + target )
	  print("")
	  quit()
    elif choice == 6:
      target = raw_input('Enter IP Or Domain : ')
      os.system("clear")
      print("""
     __                         __                 
  /\ \ \_ __ ___   __ _ _ __   / _\ ___ __ _ _ __  
 /  \/ | '_ ` _ \ / _` | '_ \  \ \ / __/ _` | '_ \ 
/ /\  /| | | | | | (_| | |_) | _\ | (_| (_| | | | |
\_\ \/ |_| |_| |_|\__,_| .__/  \__/\___\__,_|_| |_|
                       |_|                         
      """)
      os.system("curl http://api.hackertarget.com/nmap/?q=" + target )
      print("")
      quit()
    elif choice == 7:
	  target = raw_input('Enter IP Or Domain : ')
	  os.system("clear")
	  print("""
 ___ ___    _                         
|_ _| _ \  | |   ___ ___|          _____ 
 | ||  _/  | |__/ _ / _ |_/ / | || | '_ \ 
|___|_|    |____\___\___|_\_\ \_,_ | .__/  
                                   |_|     
	  """)
	  os.system("curl http://api.hackertarget.com/reverseiplookup/?q=" + target )
	  print("")
	  quit()
    elif choice == 8:
          target = raw_input('Entre Domain: ')
          os.system("clear")
          print("""
                                                  _
  ____        _    _____                         (_|
 / ___| _   _| |__ |  _ \  ____  _ __ ___   __ _  _  _ ___
 \___ \| | | | '_ \| | | |/ __ \| '_ ` _ \ / _` || || | | \ 
 |____/ \__,_|_.__/|____/ \____/|_| |_| |_|\__,_||_||_| |_|

        """) 
          os.system('python2 sub.py -t %s -l fr ' % target)
          print("") 
          quit()
    elif choice == 9:
          findAdminPanels()
    elif choice == 10:
          findUploadFile()
    elif choice == 11:
          getServerInfo()
    elif choice == 12:
          XssPy()
  except(KeyboardInterrupt):
    print ""
select()
