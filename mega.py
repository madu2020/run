import time
import urllib
import sys
import os

os.system('clear')

barg = "\033[1;36;40m\n▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓\n"
barr = "\033[1;31;40m\n▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓\n"
barp = "\033[1;35;40m\n▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓\n"
print(barp);name = """    
\033[1;34;40m  ▓ ▓   ▓ ▓  ▓▓▓▓ ▓ ▓   ▓ ▓    ▓ ▓     ▓▓▓▓▓▓ 
\033[1;36;40m  ▓  ▓▓   ▓  ▓  ▓ ▓  ▓▓   ▓   ▓   ▓    ▓    ▓
\033[1;36;40m  ▓       ▓  ▓ ▓  ▓       ▓  ▓  ▓  ▓   ▓    ▓      
\033[1;36;40m  ▓       ▓  ▓  ▓ ▓       ▓ ▓       ▓  ▓▓▓▓▓▓     
"""
print(name, "");print(barp)
import time,sys
b="/-*1234»"
n=" CODE BY MADU\n"

for y in range(4):
    for o in range(len(b)):
        time.sleep(1/20)
        sys.stdout.write("\r"+"\033[1;36m"+b[o])


for p in range(len(n)): 
    
    time.sleep(.1)
    sys.stdout.write("\033[1;35;40m"+n[p])
    sys.stdout.flush() 


try:
    f = open("auth.txt", "r")
    auth = f.read()
    f.close 
except:
    wr = str(input("\033[1;0;40mPaste Your Auth here :- "))
    f = open("auth.txt", "w")
    f.write(wr)
    f.close
    f = open("auth.txt", "r")
    auth = f.read()
    f.close

try:
    f = open("url.txt", "r")
    f = open("url.txt", "r")
    url1 = f.read()
    f.close
except:
    wr = str(input("Paste Your URL here :- "))
    f = open("url.txt", "w")
    f.write(wr)
    f.close
    f = open("url.txt", "r")
    url1 = f.read()
    f.close

try:
    import requests


except ImportError:
    print('%s Requests isn\'t installed, installing now.')
    os.system('pip3 install requests')
    print('%s Requests has been installed.')
    os.system('clear')
    import requests


def main():
    os.system("clear")
    print(barg);print(name);print(barg)
    s = int(input("\033[1;0;40mEnter Amount - "))
    header = {"Host": "megarun.dialog.lk",
              "Authorization": auth, "X-Unity-Version": "2018.3.0f2"}
    url = url1
    
    ss = 0
    while s > ss:
        os.system("clear")
        print(name)
        size = 0
        res = requests.get(url, headers=header)
        resp = str(res)
        if resp == '<Response [204]>':
            print(barr)
            print("\n\033[1;36;40m [+] No Data ... [+]")
            print(barr)  
        elif resp == '<Response [200]>':
            print(barg)
            print("\n\033[1;32;40m [+] You Won Check Balance ... [+]")
            print(barg)
        else:
            print(barr)
            print("\n\033[1;31;40m [+] Check Again, I think You are Blocked User.../or network error [+]")
            print(barr)
        

        ss+=1
        print("\033[1;0;40m\n",str(ss), "Please Wait For Next request",end="")
        lo=""
        for i in range(180):
            lo=lo+"|"
            pr = i/180*100
            print("\033[1;36;40m\n>>> [+]",str(int(pr)) +"% ",end="")
            print(lo,end="")
            
            time.sleep(0.5)
            sys.stdout.write("\033[F")
        
    os.system('figlet FINISHED')
    again()


def again():
    again = input('\033[1;0;40m\nDo You want use again (y/n) - ')
    if again == "y" or again == "Y":
        main()
    elif again == "n" or again == "N":
        quit()
    else:
        print('\033[1;31;40mEnter valid letter')
        again()


if __name__ == "__main__":
    main()
                
