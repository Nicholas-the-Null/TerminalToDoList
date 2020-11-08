import os
import  subprocess
import tkinter as tk


class Inputbox():
    '''password'''
    def __init__(self, text=""):
        self.root = tk.Tk()
        self.get = ""
        self.root.geometry("300x100")
        self.root.title("Inputbox")
        self.label_file_name = tk.Label(self.root, text=text)
        self.label_file_name.pack()
        self.entry = tk.Entry(self.root,show="*")
        self.entry.pack()
        self.entry.focus()
        self.entry.bind("<Return>", lambda x: self.getinput(self.entry.get()))
        self.root.mainloop()
 
    def getinput(self, value):
        self.get = value
        self.root.destroy()
 
 


try:
    from cryptography.fernet import Fernet
    print("ok lib Fernet is alredy install")

except ImportError:
    os.system("pip install cryptography")
    input("open again")
    exit()


if os.path.exists("lib\\security.py") is False or os.path.exists("lib\\Crittografia.py") is False:
    input("directory lib non trovato")
    exit()

if os.path.exists("lib\\tabella.py") is False or os.path.exists("lib\\punteggio.py") is False:
    input("directory lib non trovato")
    exit()

if os.path.exists("lib\\delete_line .py") is False or os.path.exists("lib\\gestici.py") is False:
    input("directory lib non trovato")
    exit()


print("ok")
    


password=Inputbox("insert master password")

os.chdir("lib")
posizione=os.getcwd()
scrivi=open("password.py","w+")
scrivi.write("""
def password():
    password='"""+password.get+"""'"""
    +"""\n    return password""")
scrivi.close()
os.system("python -m compileall -b password.py")
os.remove("password.py")

os.system("cls")


subprocess.Popen("python -c \"import os, time; time.sleep(1); os.remove('{}');\"".format("setup.py"))


input("premi un tasto per finire")
