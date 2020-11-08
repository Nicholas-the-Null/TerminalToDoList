from tkinter import messagebox
import tkinter
from cryptography.fernet import Fernet
import os
import subprocess
import getpass
import string
import random


user=getpass.getuser()

def write_key(nome="key"):
    """
    Generates a key and save it into a file!
    """
    key = Fernet.generate_key()
    with open(nome+".key", "wb") as key_file:
        key_file.write(key)

def load_key(nome="key"):
    try:
        x=open(nome+".key", "rb").read()
        return x

    except Exception as e:
        root = tkinter.Tk()
        root.withdraw()
        messagebox.showerror("error","errore nella lettura del file.key probabilmente è stato cancellato "+
        "impossibile decriptare i file ci dispiace")
        root.destroy()
        return e

        
def encrypt(key,filename=None):
    try:
        f = Fernet(key)
        if filename is None:
            pass
        if os.path.exists(filename) is False:
            return "file non trovato"
        else:
            with open(filename, "rb") as file:
                file_data = file.read()
            encrypted_data = f.encrypt(file_data)
            with open(filename, "wb") as file:
                file.write(encrypted_data)

    except Exception as e:
        root = tkinter.Tk()
        root.withdraw()
        messagebox.showerror("error","errore nella funzione di base del encrypt errore= " + e +" ci scusiamo")
        root.destroy()

def decrypt(key,filename=None,):
    try:
        f = Fernet(key)
        if filename is None:
            pass
        if os.path.exists(filename) is False:
            return "file non trovato"
        else:
            with open(filename, "rb") as file:
                encrypted_data = file.read()
            decrypted_data = f.decrypt(encrypted_data)
            with open(filename, "wb") as file:
                file.write(decrypted_data)
    except Exception as e:
        root = tkinter.Tk()
        root.withdraw()
        messagebox.showerror("error","errore nella funzione di base del decrypt errore= " + e +" ci scusiamo")
        root.destroy()
        
    



def get_random_string(length):
    """generate a name for file!"""
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def RandomDirectory():
    """save in a file the name of key file!"""
    original=os.getcwd()
    nomee_file=get_random_string(42)
    user=getpass.getuser()
    directory="C:\\Users\\"+user+"\\Desktop"
    os.chdir(directory)
    write_key(nomee_file)
    subprocess.check_call(["attrib","+H",nomee_file+".key"])
    os.chdir(original)
    x=open("sec.txt","w+")
    x.write(nomee_file)
    x.close()
    subprocess.check_call(["attrib","+H","sec.txt"])




def decrypt_file():
    logga=""
    original=os.getcwd()
    x=open("sec.txt","r")
    nome=x.readline()
    x.close()
    directory="C:\\Users\\"+user+"\\Desktop"
    os.chdir(directory)
    apri_chiave=open(nome+".key","r")
    chiave=apri_chiave.readline()
    apri_chiave.close()
    os.system("attrib -h "+nome+".key")
    os.remove(nome+".key")
    os.chdir(original)
    for x in os.listdir():
        if x=="main.py" or x=="logga.txt" or x=="lib" or x=="sec.txt":
            pass
        else:
            if os.path.isdir(x) is True :
                os.chdir(os.getcwd()+"\\"+x)
                for y in os.listdir():
                    if os.path.isfile(y) is True:
                        try:
                            decrypt(chiave,y)
                        except Exception as e:
                            root = tkinter.Tk()
                            root.withdraw()
                            messagebox.showerror("error","Il file " + x +" non è stato decriptato corretamente ci scusiamo")
                            root.destroy()
                            logga+=str(e)
                os.chdir(original)

            else:
                try:
                    decrypt(chiave,x)
                except Exception as e:
                    root = tkinter.Tk()
                    root.withdraw()
                    messagebox.showerror("error","Il file " + x +" non è stato decriptato corretamente ci scusiamo")
                    root.destroy()
                    logga+=str(e)

    if logga=="":
        logga="successo"

    return logga
    

def encrypt_file():
    logga=""
    original=os.getcwd()
    x=open("sec.txt","r")
    nome=x.readline()
    x.close()
    nome_completo=nome+".key"
    directory="C:\\Users\\"+user+"\\Desktop"
    os.chdir(directory)
    apri_chiave=open(nome_completo,"r")
    chiave=apri_chiave.readline()
    apri_chiave.close()
    os.chdir(original)
    for x in os.listdir():
        if x=="main.py" or x=="logga.txt" or x=="lib" or x=="sec.txt":
            pass
        else:
            if os.path.isdir(x) is True :
                os.chdir(os.getcwd()+"\\"+x)
                for y in os.listdir():
                    if os.path.isfile(y) is True:
                        try:
                            encrypt(chiave,y)
                        except Exception as e:
                            root = tkinter.Tk()
                            root.withdraw()
                            messagebox.showerror("error","Il file " + x +" non è stato decriptato corretamente ci scusiamo")
                            root.destroy()
                            logga+=str(e)
                os.chdir(original)
                

            else:
                try:
                    encrypt(chiave,x)
                except Exception as e:
                    root = tkinter.Tk()
                    root.withdraw()
                    messagebox.showerror("error","Il file " + x +" non è stato decriptato corretamente ci scusiamo")
                    root.destroy()
                    logga+=str(e)

    if logga=="":
        logga="successo"

    return logga
