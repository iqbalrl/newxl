# -*- coding: utf-8 -*-
import os
import sys
import platform
import time
from xlpy import *
import base64

g = "\033[32;1m"
gt = "\033[0;32m"
bt = "\033[34;1m"
b = "\033[36;1m"
m = "\033[31;1m"
c = "\033[0m"
p = "\033[37;1m"
u = "\033[35;1m"
M = "\033[3;1m"
k = "\033[33;1m"
kt = "\033[0;33m"
a = "\033[30;1m"

W = '\x1b[0m'
R = '\x1b[31m'
G = '\x1b[1;32m'
O = '\x1b[33m'
B = '\x1b[34m'
P = '\x1b[35m'
C = '\x1b[36m'
GR = '\x1b[37m'



def slowprints(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1.0/90)
def lodprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(7.0/90)

semut=(gt+"""
""")
l="Harap tunggu.."

def main_menu():
    clear()
    slowprints(semut)
    print(p+
        "   Tembak Xl Mode Otp" +
        "\nPilih Salah Satu:"
        "\n  [1] Menu Beli Paket" + 
        "\n  [2] Minta Otp Code" +
        "\n  [3] Menu utama"
    )
    choice = str(input(" ex:1👉 "))
    exec_menu(choice)
    return

def exec_menu(choice):
    clear()
    if(choice == ''):
        menu_actions['main']()
    else:
        try:
            menu_actions[choice]()
        except KeyError:
            print("Invalid selection, please try again.\n")
            menu_actions['main']()
    return

def menu_1():
    lodprint(l)
    clear()
    print(semut)
    print(p+"Menu Beli Paket Xl")
    msisdn = str(input("Masukan No 62xx 👉 "))
    clear()
    print(semut)
    po = str(input(p+"Masukan Kode Otp 👉 "))
    clear()
    print(semut)
    print (p+" 1.Xtra combo lite 5GB/29.900")
    print (p+" 2.Xtra combo lite 9GB/49.900")
    print (p+" 3.Xtra combo lite 17GB/79.900")
    print (p+" 4.Xtra combo lite 25GB/99.900")
    print (p+" 5.Manual service id")
    pkt = str(input("Pilih Sesuai Keinginan >> "))
    
    if pkt == '1':
        i = '8210883'
    elif pkt == '2':
        i = '8210884'
    elif pkt == '3':
        i = '8210885'
    elif pkt == '4':
        i = '8210886'
    elif pkt == '5':
        i = str(input("Service ID Paket👉"))
    else:
        print("Pilihan gak tercantum")
    lodprint(l)
    serviceid = i
    xl = XL(msisdn)
    r = xl.loginWithOTP(po)
    if(r != False):
        print(xl.purchasePackage(serviceid)['message'])
        decision = str(input(p+"Ulangi Proses [Y/N]? 👉 "))
        menu_actions['main']() if(decision in ['N','n']) else menu_actions['1']()
        
def menu_2():
    lodprint(l)
    clear()
    print(semut)
    print(p+"Minta Kode Otp")
    msisdn = str(input("Masukan Nomor 62xx👉"))
    lodprint(l)
    xl = XL(msisdn)
    print(xl.reqOTP()['message'])
    decision = str(input(p+"Ulangi Proses[Y/N]? 👉 "))
    menu_actions['main']() if(decision in ['N','n']) else menu_2()

def menu_4():
    clear()
    print(".::Password Menu::.")
    msisdn = str(input("Input your MSISDN >> "))
    xl = XL(msisdn)
    print(xl.reqPassword()['message'])
    decision = str(input("Want to repeat the process [Y/N]? >> "))
    menu_actions['main']() if(decision in ['N','n']) else menu_actions['3']()
    return

def menu_3():
     lodprint(l)
     os.system('cd ..;python dor.py')


def exit():
    sys.exit()

def clear():
    return os.system("cls") if (platform.system() == 'Windows') else os.system("clear")

menu_actions = {
    "main" : main_menu,
    "1" : menu_1,
    "2" : menu_2,
    "3" : menu_3,
    "0" : exit
}


if __name__ == "__main__":
    main_menu()
