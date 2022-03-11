import os
from msvcrt import*
import colorama
from colorama import Fore, Back, Style
os.system("cls=clear")
colorama.init()
print(Fore.RED)
print("""
                    Yapımcı:Aytlogo_Luxer""")
print("""
Devam Etmek İçin Bir Tuşa Basın...""")
getch()
os.system("cls=clear")
os.system("""netsh wlan show profile name=\"*\" key=clear > wifi.txt""")
os.system("cls=clear")
print(Fore.GREEN)
print("wifi'ler wifi.txt dosyasına oluşturuldu")
print("""Kapatmak İçin Bir Tuşa Basın...""")
getch()
os.system("exit")
