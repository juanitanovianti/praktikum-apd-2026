import os

def bersihkan_layar():
    if os.name == "nt":         
        os.system("cls")         
    else:         
        os.system("clear")