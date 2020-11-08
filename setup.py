import os
import subprocess
from tkinter import messagebox
import tkinter as tk


 
class Inputbox():
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
 
 



root = tkinter.Tk()
root.withdraw()
scelta=messagebox.askyesno("installer","do you want continue to install?")
root.destroy()



if scelta is False:
    exit()


try:
    from cryptography.fernet import Fernet
    print("ok lib Fernet is alredy install")

except ImportError:
    os.system("pip install cryptography")
    input("open again")
    exit()

try:
    import lib.security
except Exception:
    pass

try: 
    import lib.Crittografia
    from lib.tabella import tabella as tb
    import lib.punteggio as punteggio
    from lib.delete_line import delete as dt
    import lib.gestici as gestici 
    print("ok")
    
except Exception as e:
    input("error = " + str(e))

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


#subprocess.Popen("python -c \"import os, time; time.sleep(1); os.remove('{}');\"".format(sys.argv[0]))


input("premi un tasto per finire")
