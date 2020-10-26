import os
import hashlib



def auto_elimina_progetti_vuoti():
    """delete empty file in a directory"""
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
        input("non ci sono file da eliminare")
        pass
    else:
        print("ci sono " + str(len(elementi))+" elementi da eliminare")
        scelta=int(input("1-eliminare tutti\n2-non eliminare\n3-scegli\n4-lista\n"))
        while  True:
            if scelta == 1:
                for x in elementi:
                    os.remove(x)
                break
            if scelta == 2:
                break
            if scelta == 3:
                for x in elementi:
                    scelta=input("vuoi eliminare " + str(x) + " y/n ")
                    if scelta == "y":
                        os.remove(x)
                    else:
                        pass
                break
            if scelta == 4:
                for x in elementi:
                    print(x+"\n")
                pass
            
                
            else:
                print("numero non valido")

            scelta=int(input("1-eliminare tutti\n2-non eliminare\n3-scegli\n4-lista-\n"))

                    
def Elimina_File_Duplicate():
    """delete duplicate file in a directory"""
    hasha=[]
    print("cercando duplicati")
    for x in os.listdir():
        md5 = hashlib.md5()
        with open(x, "rb") as thefile:
            buf = thefile.read()
            md5.update(buf)
        sha=md5.hexdigest()
        if sha in hasha:
            os.remove(x)
        else:
            hasha.append(sha)
    return "Successo"            

def Elimina_pattern(file,Pattern="Completo") -> str:
    """delete lines by pattern in a file"""
    posizione=5
    ida=0
    pos=[]
    x=open(file,"r")
    y=x.readlines()
    x.close()
    for i in y:
        i=list(i.split())
        if i[posizione] == Pattern:
            pos.append(ida)
        ida+=1
    ida=0
    for x in pos:
        a_file = open(file, "r")
        lines = a_file.readlines()
        a_file.close()
        del lines[x-ida]
        ida+=1
        new_file = open(file, "w+")
        for line in lines:
            new_file.write(line)
        new_file.close()
    return "successo" 

            

            
