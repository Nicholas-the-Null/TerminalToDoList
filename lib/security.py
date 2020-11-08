import tkinter as tk
from tkinter import messagebox
import random
from lib.password import password as passwordo





def get_capslock_state():
    """Check if you have capsloock!"""
    import ctypes
    hllDll = ctypes.WinDLL ("User32.dll")
    VK_CAPITAL = 0x14
    s=hllDll.GetKeyState(VK_CAPITAL)
    if s == 0:
        s=False
    else:
        s=True
    return s




check_Caps=get_capslock_state()

if check_Caps is True:
    messagebox.showwarning(":/","HAI IL BLOCCO MAIUSCOLE ATTIVO")

def disable_event():
        x=messagebox.askyesno("chiudere","uscire")
        if x is True:
            exit(1)
        else:
            pass
password=int(random.uniform(9999,1000)) #generate a 'secure' 2 step password 
class log(tk.Frame):
    '''
    The log object contains method for do a secure login
    Args 
    password
    Return 
    2 step password
    '''
    def __init__(self,master = None):
        """Log-in main!"""
        super().__init__(master)
        self.master.title("security token")
        self.master.geometry("200x200")
        self.master.protocol("WM_DELETE_WINDOW", disable_event)
        self.grid()
        self.crea_widgets()

    def crea_widgets(self):
        self.lblPasswords = tk.Label(self, text = "master-password")
        self.lblPasswords.grid(row = 1, column = 0, sticky = tk.W)
        self.vPasswords = tk.StringVar()
        self.txtPasswords = tk.Entry(self, textvariable = self.vPasswords,show="*")
        self.txtPasswords.grid(row = 1 , column = 1)
        
        


        self.btnInvio = tk.Button(self, text = "enter", command = self.invia)
        self.btnInvio.grid(row = 3, column = 1, columnspan = 2)


        
        
    def invia(self):
        Password_verificare = self.vPasswords.get()
        if Password_verificare == " " or Password_verificare == "":
            messagebox.showwarning(":/","per favore inserire i dati ")
        else:
            password_check=passwordo()
            if password_check == Password_verificare:
                messagebox.showinfo("ok","bentornato, ti sei loggato con successo inserisci questo codice di conferma " + str(password))
                self.master.destroy()
            else:
                messagebox.showerror("error","dati non coincidenti")

                




def sig():
    log()

def main() -> int:
    sig()
    return password


