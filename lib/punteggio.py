import os
from tkinter import messagebox as mb
import pathlib as Path
import tkinter



def ordina(file=None):
    """order points in a file """
    if file == "\n" or file == "" or file == " " or os.path.exists(file) is False or os.path.isfile(file) is False:
        root = tkinter.Tk()
        root.withdraw()
        mb.showerror("errore","il file richiesto non è esistente o non ha l'estensione .txt correggere l'errore e riprovare")
        root.destroy()
    else:
        ordina=open(file)
        classifica=[]
        punteggio=[]
        for i, line in enumerate(ordina):
            aggiungi=line.split()
            classifica.append(aggiungi)
        for i,line in enumerate(classifica):
            punteggio.append(line[1])
        new_punteggio=[]
        for n in punteggio:
            new_punteggio.append(int(n))
        new_punteggio.sort()
        pulisci_file=open(file,"w")
        pulisci_file.write("")
        pulisci_file.close()
        for i,line in enumerate(new_punteggio):
            vb=str(new_punteggio[i])
            res = next((i for i, (Nome,punteggio,Data_creazione,DeadLine,commento,stato ) in enumerate(classifica) if punteggio == vb), None) ###add element after ele for the number of word in file
            riscrivi=open(file,"a")
            ar=" ".join(classifica[res])
            riscrivi.write(str(ar)+"\n")
            kmj=ar.split()
            classifica.remove(kmj)
            riscrivi.close()



def Calcola():
    """Calcolate point of task"""
    esci=False
    while esci is False:
        try:
            check=False
            while check is False:
                DeadLine=input("inserisci la deadline in giorni ")
                try:
                    DeadLine = int(DeadLine)
                    check=True
                except ValueError:
                    root = tkinter.Tk()
                    root.withdraw()
                    mb.showerror("errore","errore non è stato inserito un numero")
                    root.destroy()

            check=False
            while check is False:
                livello=input("Livello(da 1-10 secondo la gravità del problema) ")
                try:
                    livello = int(livello)
                    if livello<1 or livello>10:
                        root = tkinter.Tk()
                        root.withdraw()
                        mb.showerror("errore","errore il valore inserito non è valido")
                        root.destroy()
                    else:
                        check=True
                except ValueError:
                    root = tkinter.Tk()
                    root.withdraw()
                    mb.showerror("errore","errore non è stato inserito un numero")
                    root.destroy()


            check=False
            while check is False:
                difficolta=input("inserire il livello di difficolta stimato da 1-10 ")
                try:
                    difficolta = int(difficolta)
                    if difficolta<1 or difficolta>10:
                        root = tkinter.Tk()
                        root.withdraw()
                        mb.showerror("errore","errore il valore inserito non è valido")
                        root.destroy()
                    else:
                        check=True
                        esci=True
                except ValueError:
                    root = tkinter.Tk()
                    root.withdraw()
                    mb.showerror("errore","errore non è stato inserito un numero")
                    root.destroy()

        except KeyboardInterrupt:
            root = tkinter.Tk()
            root.withdraw()
            mb.showerror("errore","non puoi uscire")
            root.destroy()

    punteggio=250-DeadLine-livello-difficolta
    return punteggio
            

