import requests
from googlesearch import search 

banner = """
______           _      _____                                 
|  _  \         | |    /  ___|                                
| | | |___  _ __| | __ \ `--.  ___ __ _ _ __  _ __   ___ _ __ 
| | | / _ \| '__| |/ /  `--. \/ __/ _` | '_ \| '_ \ / _ \ '__|
| |/ / (_) | |  |   <  /\__/ / (_| (_| | | | | | | |  __/ |   
|___/ \___/|_|  |_|\_\ \____/ \___\__,_|_| |_|_| |_|\___|_|   
                    www.Xpykerz.com                                                    
"""
print(banner)

check = input("\033[0;31;40m\nWARNING....!..: The tools is on developing and this is BETA Version. Tool maybe miss behave sometimes. \n Do you want to continue (yes/no | Default:yes): ")

if check in ['n', 'N', 'No', 'no', 'NO']:
	quit()

query = input("\033[0;37;40m\nEnter Dork To Scan: ")

def vul_check(url):
    check = (requests.get(url + "'")).text
    error = ['at line','on line','mysql','MySQL']
    if  any(err in check for err in error):
        print ("\033[1;32;40m [+]Vulnerable \033[0;37;40m",url)
    
    else:
        print ("\033[1;31;40m [-]Vulnerability Can't Find \033[0;37;40m",url)

print("\033[1;34;40mScan Started ...")
for url in search(query):
    url = url.split('&')[0]
    try:
        vul_check(url)
    except :
        print("\033[1;31;40mYou Tried Too Many Requests Today, Please Use VPN To Scan More Or Use After Few Minutes Later")
        quit()
        
