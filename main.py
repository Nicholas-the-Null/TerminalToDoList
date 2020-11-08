#secure lib
import os
import datetime
from tkinter import messagebox
import getpass
import tkinter



original=os.getcwd()


def SaveEvent(event):
    """Log every event in html file"""
    current=os.getcwd()
    if current != original:
        os.chdir(original)
    ora=datetime.datetime.now()
    ora=ora.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    if os.path.exists("event.html") is False:
        x=open("event.html","w+")
        x.close()
    x=open("event.html","a")
    x.write(ora+ " " + event + "<br>")
    x.close()
    os.chdir(current)


#log error
def error_show(fix):
    root = tkinter.Tk()
    root.withdraw()
    messagebox.showerror("errore",fix)
    root.destroy()

def error_log(error):
    current=os.getcwd()
    if current != original:
        os.chdir(original)
    if os.path.exists("logga.txt") is False:
        x=open("logga.txt","w+")
        x.close()
    ora=datetime.datetime.now()
    ora=ora.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    x=open("logga.txt","a")
    x.write(ora + " "+ str(error) + "\n")
    x.close()
    os.chdir(current)






try:
    from lib.security import main as log_in
    import lib.Crittografia
    from lib.tabella import tabella as tb
    from lib.tabella import Return_id as Id_number
    import lib.punteggio as punteggio
    from lib.delete_line import delete as dt
    import lib.gestici as gestici
    
except ImportError as I:
    fix="non hai eseguito la procedura per lo installer o non hai installato il programma corettamente o è stato cancellato la directory che conteneva le lib"
    error_show(fix)
    error_log(I)




try:
    x=log_in()
except UnboundLocalError:
    error_show("errore 213 è richiesto il riavvio")
    exit()



while True:
    password=input()
    try:
        password=int(password)
    except:
        password=1
    if x==password:
        break
    else:
        print("inserisci la password furbetto")












#decripta i file
if os.path.exists("sec.txt") is True:
    vedi=lib.Crittografia.decrypt_file()
    if vedi!="successo":
        error_log(vedi)
    os.remove("sec.txt")




        
os.system("title Terminal ToDo V3")






SaveEvent("logIn")


while True:
    menu = None
    print("""
___________                  .__              .__    ___________   ________           ____   ____________  
\__    ___/__________  _____ |__| ____ _____  |  |   \__    ___/___\______ \   ____   \   \ /   /\_____  \ 
  |    |_/ __ \_  __ \/     \|  |/    \\\\__  \ |  |     |    | /  _ \|    |  \ /  _ \   \   Y   /   _(__  < 
  |    |\  ___/|  | \/  Y Y  \  |   |  \/ __ \|  |__   |    |(  <_> )    `   (  <_> )   \     /   /       \\
  |____| \___  >__|  |__|_|  /__|___|  (____  /____/   |____| \____/_______  /\____/     \___/   /______  /
             \/            \/        \/     \/                             \/                           \/ 
""")

    lista_prog=""
    print("Good morning " + str(getpass.getuser()) + " sei nella home della ToDo List V3 \ndirectory= " 
    +str( os.getcwd() ) )

    try:
        
        menu=int(input("1-creare un progetto,\n2 apri un progetto\n3-exit,\n4-faq,\n5elimina progetto\n"))
        

    except ValueError as V:

        error_show("hai inserito un valore che non è un numero")
        error_log(V)
        SaveEvent("errore")
    

    

    
    if menu==1:
        nome=input("inserisci il nome del progetto ")

        try:

            os.mkdir(nome)
            SaveEvent("creazione nuovo progetto nome "+ nome)

        except Exception as e:

            error_show("errore rilevato nella creazione della cartella  " + nome)
            error_log(e)

    
    if menu==3:
        SaveEvent("exit")
        break

    if menu == 4:

        SaveEvent("faq")
        print("benvenuto nella Terminal ToDo list V3 con questa potrai creare un agenda per ogni tuo lavoro "+
        "potrai assegnare ha ogni task un punteggio e ordinarli per punteggio, puoi eliminare automaticamente "+
        "i file duplicati o finiti inoltre potrai eliminare per Pattern ogni Task")

        os.system("pause")

    if menu==5:
        nome=input("nome del progetto ")
        if os.path.exists(nome) is True:
            os.rmdir(nome)
        
    if menu==2:

        lista_progetti=[]

        for x in os.listdir():

            if (x=="main.py" or x=="lib" or x=="sec.txt" or  
            x =="logga.txt" or x =="event.html" or x=="setup.py") or os.path.isdir(x) is False:
                pass

            else:
                informazioni=" il peso è " + str(os.path.getsize(x)//1024) + "kb " + " numero di file " + str(len(os.listdir(x)))
                lista_prog=lista_prog+"\n"+ x + informazioni
                lista_progetti.append(x)

        print("i tuoi progetti esistenti "+ lista_prog)



        while True:
            selezionare=input("seleziona il progetto ")

            if selezionare in lista_progetti:
                break

            else:
                error_show("cartella inesistente")

        lista_prog=""
        lista_progetti=[]

        SaveEvent("apperto sotto-menu per gestire progetti [" + selezionare+"]")
        
        try:

            os.chdir(selezionare)

            file=True

            while file is True:

                os.system("cls")

                try:
                    menu=int(input("1-vedi file\n2-apri file\n33-torna indietro"+
                    "\n4-gestici file vuoti\n5-elimina file duplicati\n"))

                except ValueError as V:
                    fix="hai inserito un valore che non è un numero"
                    error_show(fix)
                    error_log(V)
                    SaveEvent("errore")


                if menu == 1:
                    SaveEvent("vedi lista file")

                    for x in os.listdir():
                        if os.path.isdir(x) is False:
                            print(x+"\n")

                    input()

                if menu==33:
                    SaveEvent("torna indietro")
                    os.chdir(original)
                    file=False
                    

                if menu == 4:
                    SaveEvent("eliminati file vuoti")
                    do = gestici.auto_elimina_progetti_vuoti()

                    if do[0:5] == "error":
                        error_log(do)
                    
                    else:
                        root = tkinter.Tk()
                        root.withdraw()
                        messagebox.showinfo("info",do)
                        root.destroy()


                    
                
                if menu==5:
                    SaveEvent("eliminati file duplicati")
                    do = gestici.Elimina_File_Duplicate()

                    if do[0:5] == "error":
                        error_log(do)
                    
                    else:
                        root = tkinter.Tk()
                        root.withdraw()
                        messagebox.showinfo("info",do)
                        root.destroy()




                    



                
                    
                if menu == 2:
                    SaveEvent("apperto sottomeno per gestire un singolo progetto")

                    gestici_file=True

                    while gestici_file is True:

                        os.system("cls")
                        print(os.getcwd())

                        try:
                            menu=int(input("1-leggi,\n2-scrivi,\n3-rimuovi,\n4 ordina riga"+
                            "\n5-elimina pattern\n333-torna indietro\n"))

                        except ValueError as V:
                            fix="hai inserito un valore che non è un numero"
                            error_show(fix)
                            error_log(V)
                            SaveEvent("errore")


                        if menu == 1:
                            nome=input("inserisci il nome del file ")
                            SaveEvent("leggi file ["+nome+"]")

                            try:
                                tb(nome)
                                input()

                            except Exception as e:
                                fix="errore rilevato per leggere il file " + nome 
                                error_show(fix)
                                error_log(e)

                        
                                
                        if menu == 2:
                            nome=input("inserisci il nome del file con l'estensione ")
                            SaveEvent("creazione riga del file ["+nome+"]")

                            f=open(nome,"a")
                            nome=input("inserisci un nome ")

                            if nome=="" or nome == " " or nome =="\n":
                                pass

                            else:
                                punti=punteggio.Calcola() 
                                punti=str(punti)
                                Data_creazione=input("data creazione qualsiasi formato in questo formato (yyyy-mm-dd) ")
                                
                                if (Data_creazione == "" or Data_creazione == " " or Data_creazione == "\n") or len(Data_creazione) !=10:
                                    pass

                                else:
                                    Deadline=input("data deadline in questo formato (yyyy-mm-dd) ") 

                                    if len(Deadline) !=10:
                                        pass

                                    else:
                                        Commento=input("Commento")
                                        Commento=Commento.replace(" ","_")
                                        stato=input("stato  ps(Consiglio di mettere o fix o Completo) visto che c'è  "
                                        +"il comando per eliminare le righe in base al pattern di questo attributo")
                                        scrittura=nome + " " + punti + " " + Data_creazione + " " + Deadline + " " + Commento + " " + stato 
                                        f.write(scrittura+"\n")
                                        
                            f.close()
                            os.system("cls")
                            
                        if menu == 3:
                            nome=input("nome del file ")

                            if os.path.exists(nome) is True:

                                try:
                                    max_id=Id_number(nome)
                                    linea=int(input("inserisci linea tra un massimo di 0 e {max_id} da eliminare "))
                                    if linea >= max_id:

                                        error_show("nome del file inesistente")
                                        error_log("nome del file inesistente")
                                    else:    
                                        dt(nome,linea)
                                        SaveEvent("eliminazione della riga ["+str(linea)+"] del file ["+nome+"]")

                                except ValueError as V:
                                    error_show("hai inserito un valore che non è un numero")
                                    error_log(V)
                                    SaveEvent("errore")
                                

                            else:
                                error_show("nome del file inesistente")
                                error_log("nome del file inesistente")
                                

                        if menu == 5:
                            root = tkinter.Tk()
                            root.withdraw()                        
                            sicuro=messagebox.askyesno("sicuro?","stai per eliminare in base al pattern dello stato le righe di un determinato file sicuro (y/altro)")
                            root.destroy()
                            if sicuro is True:
                                file=input("dammi il file ")
                                if os.path.exists(file) is True:
                                    Pattern=input("dammi il pattern ")
                                    do=gestici.Elimina_pattern(file,Pattern)
                                    if do[0:5] == "error":
                                        
                                        pass
                                    else:
                                        root = tkinter.Tk()
                                        root.withdraw()
                                        messagebox.showinfo("info",do)
                                        root.destroy()
                                        SaveEvent("file ["+file+"]"+" il pattern ["+Pattern+"]")
                                else:
                                    root = tkinter.Tk()
                                    root.withdraw()
                                    messagebox.showinfo("info","file non trovato")
                                    root.destroy()
                            else:
                                pass
                                
                        if menu == 4:
                            file=input("inserisci il nome ")
                            SaveEvent("ordina file file ["+file+"]")

                            try:
                                punteggio.ordina(file)

                            except Exception as e:
                                fix="errore rilevato leggere il file " + file
                                error_show(fix)
                                error_log(e)

                        if menu == 333:
                            SaveEvent("torna indietro alla gestione del progetto")
                            gestici_file= False
                        
                        else:
                            pass
                else:
                    pass

        except:
            pass

    else:
        pass
        
    os.system("cls")








try:
    lib.Crittografia.RandomDirectory()
    vedi=lib.Crittografia.encrypt_file()


    if vedi!="successo":
        error_log(vedi)

except Exception as E:
    error_show("errore nella fase di criptazione ti chiediamo scusa")
    error_log(E)



