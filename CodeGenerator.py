import hashlib
import json
import os
import platform
import random
import threading
import time
from os import path
from queue import Queue

import requests
from bs4 import BeautifulSoup
from colorama import Fore, init
from flask import Flask, request

gened = 0
codelist = ""

intro = """
 ######   #######  ########  ########  ######   ######## ##    ## 
##    ## ##     ## ##     ## ##       ##    ##  ##       ###   ## 
##       ##     ## ##     ## ##       ##        ##       ####  ## 
##       ##     ## ##     ## ######   ##   #### ######   ## ## ## 
##       ##     ## ##     ## ##       ##    ##  ##       ##  #### 
##    ## ##     ## ##     ## ##       ##    ##  ##       ##   ### 
 ######   #######  ########  ########  ######   ######## ##    ## 

Made by KinauJr and Exploit.

"""
os.system("cls")
print(Fore.LIGHTCYAN_EX + intro + Fore.LIGHTMAGENTA_EX)

if os.path.exists('./config.txt'):
    n_auth = json.loads(open("config.txt","r").read())["auth-key"]
else:
    n_auth = input("Auth Key? \n")

hasher = hashlib.md5()
hasher.update(n_auth.encode())
r = requests.get('https://www.nulled.to/misc.php?action=validateKey&authKey=' + hasher.hexdigest())
try:
    if json.loads(r.text)["status"] == "success":
        if json.loads(r.text)["auth"]:
            code = {}
            code["auth-key"] = n_auth
            open("config.txt","w+").write(json.dumps(code))
        else:
            print("Bad key, closing")
            time.sleep(5)
            exit()
    else:
        print('Bad key , closing')
        time.sleep(5)
        exit()
except:
    print("The Auth Request got blocked from Cloudflare. Skipping Auth :c")
    time.sleep(5)

os.system("cls")
print(Fore.LIGHTCYAN_EX + intro + Fore.LIGHTMAGENTA_EX)
threads = int(input("How many threads? \n"))

os.system("cls")
print(Fore.LIGHTCYAN_EX + intro + Fore.LIGHTMAGENTA_EX)
wanted = int(input("How many codes? \n"))

class yeetus(object):
    def __init__(self):
        self.Writeing = Queue()
        self.printing = []
        self.done = 0
        self.currentlyplaying = 0
        self.notactive = 0
        self.proccessing = 0
        self.failed = 0
        self.gened = 0
        
    def writethisshit(self):
        while not gened > wanted:
            write = self.Writeing.get()
            if write[1] == "Owner":
                open("FamilyOwner.txt","a+").write(write[0])
            if write[1] == "Premium":
                open("Premium.txt","a+").write(write[0])
            if write[1] == "Free":
                open("Free.txt","a+").write(write[0])
            if write[1] == "Code":
                open("AppleCodes.txt","a+").write(write[0])
            if write[1] == "CodeTaiwan":
                open("AppleCodes(Taiwan).txt","a+").write(write[0])
                
    def printservice(self):
        # Made by Kinau
        while not gened > wanted:
            if len(self.printing) != 0:
                os.system("cls")
                print(Fore.LIGHTCYAN_EX + intro + Fore.LIGHTMAGENTA_EX)
                print(Fore.LIGHTCYAN_EX + f"Codes generated: {self.gened}")
                for i in range(len(self.printing) - 17, len(self.printing)):
                    try:
                        print(self.printing[i])
                    except (ValueError, Exception):
                        pass
                time.sleep(0.5)

a = yeetus()
proxys = [""]
def ProxyUpdate():
    global proxys
    while True:
        resp = requests.get("https://api.proxyscrape.com/?request=getproxies&proxytype=http&ssl=yes").text
        buf = resp.split("\r\n")
        proxys = buf
        buf = []
        time.sleep(300)


threading.Thread(target=ProxyUpdate).start()
def yeet():
    global gened
    global codelist
    global wanted
    global proxys
    while gened < wanted:
        urls = ["https://redeem.itunes.apple.com/site/bMkG6A/Se87Rg/button?at=","https://redeem.itunes.apple.com/site/1Ue5Fw/rfHS0w/button?at=","https://redeem.itunes.apple.com/site/HaCZBQ/UTGQWQ/button?at="]
        for url in urls:
            try:
                proxy = random.choice(proxys)
                #url = "https://redeem.itunes.apple.com/site/bMkG6A/Se87Rg/button?at="
                csrf = requests.get(url).text.split('<meta name="csrf-token" content="')[1].split('" />')[0]
                resp = requests.post(url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0","X-CSRF-Token":csrf,"X-Item-Token":csrf},proxies={"https":proxy}).text
                if True:
                    ### JSON
                    resp2 = json.loads(resp)
                    #print(resp)
                    codelist = codelist + resp2["code"] + "\n" 
                    gened += 1
                    a.gened += 1
                    a.printing.append(resp2["code"])
                    a.Writeing.put([resp2["code"] + "\n","Code"])
            except:
                pass
        try:
            proxy = random.choice(proxys)
            url = "https://redeem.itunes.apple.com/site/Otd9qA/gpIs9w/button?at="
            csrf = requests.get("https://redeem.itunes.apple.com/site/Otd9qA/gpIs9w/button?at=").text.split('<meta name="csrf-token" content="')[1].split('" />')[0]
            resp = requests.get("https://redeem.itunes.apple.com/site/Otd9qA/gpIs9w/button?at=",headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0","X-CSRF-Token":csrf,"X-Item-Token":csrf},proxies={"https":proxy}).text
            if True:
                ### JSON
                resp2 = {}
                #print(resp) 
                gened += 1
                a.gened += 1
                resp2["code"] = resp.split("<span class='code-number'>")[1].split("</span>")[0]
                a.printing.append(resp2["code"])
                a.Writeing.put([resp2["code"] + "\n","CodeTaiwan"])
        except Exception as E:
            #print(E)
            pass
            
        
        


    
threading.Thread(target=a.writethisshit).start()
threading.Thread(target=a.printservice).start()



for i in range(0,threads):
    threading.Thread(target=yeet).start()
    time.sleep(0.001)
