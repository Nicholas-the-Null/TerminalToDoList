import os
import hashlib
from tkinter import messagebox
import tkinter




def auto_elimina_progetti_vuoti():
    """Delete empty file in a directory!"""
    logga=""
    number_element=0
    elementi=[]
    for y in os.listdir():
        if os.path.isfile(y) is True:
            apri=open(y,"r")
            leggi=apri.readline()
            apri.close()
            if leggi=="" or leggi=="\n":
                elementi.append(y)
            else:
                pass
        else:
            pass

    if len(elementi) == 0:
        root = tkinter.Tk()
        root.withdraw()
        messagebox.showinfo("avviso","non ci sono file")
        root.destroy()

    else:
        print("ci sono " + str(len(elementi))+" elementi da eliminare")

        while  True:

            try:
                scelta=int(input("1-eliminare tutti\n2-non eliminare\n3-scegli\n4-lista\n"))

            except ValueError:
                root = tkinter.Tk()
                root.withdraw()
                messagebox.showwarning("avviso","hai selezionato una stringa o qualche valore strano che non sia "+
                "un numero ergo di default verrà visualizzata la lista")
                root.destroy()
                scelta=4

            if scelta == 1:
                for x in elementi:
                    try:
                        os.remove(x)
                        number_element+=1
                    except Exception:
                        logga="error"
                        root = tkinter.Tk()
                        root.withdraw()
                        messagebox.showwarning("avviso","il file risulta gia eliminato/cambiato nome o posizione")
                        root.destroy()
                break

            if scelta == 2:
                break

            if scelta == 3:
                for x in elementi:
                    scelta=input("vuoi eliminare " + str(x) + " y/n ")
                    if scelta == "y":
                        try:
                            os.remove(x)
                            number_element+=1
                        except Exception:
                            logga="error"
                            root = tkinter.Tk()
                            root.withdraw()
                            messagebox.showwarning("avviso","il file risulta gia eliminato/cambiato nome o posizione")
                            root.destroy()
                    else:
                        pass
                break

            if scelta == 4:
                for x in elementi:
                    print(x+"\n")
                scelta=input("vuoi uscire da questa funzione y/n").lower().strip()
                if scelta!="y":
                    break
            else:
                print("numero non valido")
    if number_element == 0 and logga=="":
        logga="non ci sono elementi da eliminare"
    if logga=="" and number_element!=0:
        
        logga="eliminati con successo tutti i "+str(number_element)  
    else:
        logga="error "+str(len(elementi)-number_element) + " file non eliminati"

    return logga

                    
def Elimina_File_Duplicate():
    """Delete duplicate file in a directory!"""
    logga=""
    hasha=[]
    number_element=0
    totale=len(os.listdir())
    root = tkinter.Tk()
    root.withdraw()
    sicurezza=messagebox.askyesno("eliminare","procedere con l'auto eliminazione dei file duplicati " +
    "i file verrano eliminati per md5")
    root.destroy()

    if sicurezza is True:
        for x in os.listdir():
            md5 = hashlib.md5()
            with open(x, "rb") as thefile:
                buf = thefile.read()
                md5.update(buf)
            sha=md5.hexdigest()
            if sha in hasha:
                try:
                    os.remove(x)
                    number_element+=1
                except Exception as e:
                    logga="error"
                    root = tkinter.Tk()
                    root.withdraw()
                    messagebox.showerror("error",e)
                    root.destroy()
            else:
                hasha.append(sha)
        
        if number_element==0 and logga=="":

            logga="non ci sono file da eliminare"

        elif logga=="" and number_element!=0:

            logga="tutti i file sono stati eliminati con successo"
        
        else:

            logga="error "+str(totale-number_element)+ " possibili file non sono stati eliminati"
            
    else: 
        logga="nessun file eliminato operazione annulata"
    return logga

             





def Elimina_pattern(file,Pattern="Completo") -> str:
    """Delete lines by pattern in a file!"""
    logga=""
    ida=0
    numero_righe_eliminate=0
    pos=[]
    try:
        x=open(file,"r")
        y=x.readlines()
        x.close()
        for i in y:
            i=list(i.split())
            if i[5] == Pattern:
                pos.append(ida)
            ida+=1
        ida=0
        for x in pos:
            a_file = open(file, "r")
            lines = a_file.readlines()
            a_file.close()
            del lines[x-ida]
            numero_righe_eliminate+=1
            ida+=1
            new_file = open(file, "w+")
            for line in lines:
                new_file.write(line)
            new_file.close()

    except Exception:
        logga="error file not found"

    if logga!="error":
        logga="Sono stai eliminati correttamente tutte le "+ str(numero_righe_eliminate) + " righe"

    return logga
            

            
