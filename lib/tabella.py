import datetime as dt
import os

def tabella(file):
    """print all line off file!"""
    ida=1
    os.system("cls")
    x=open(file,"r")
    y=x.readlines()
    for i in y:
        i=list(i.split())
        date_time_obj = dt.datetime.strptime(i[2],'%Y-%m-%d')
        date_time_obje = dt.datetime.strptime(i[3],'%Y-%m-%d')
        scadenza=date_time_obje-date_time_obj
        commento_non_modificato=i[4]
        commento=commento_non_modificato.replace("_"," ")
        print("Nome " + i[0]+"\n" + "punteggio " + i[1]+ "\n" +"Data creazione "+ i[2] + "\n" + "Deadline " + i[3] + "\nscadenza " + str(scadenza) + "\n" + "Commento " + commento + "\n" + "stato " + i [5]+"\nid " + str(ida)+"\n\n\n\n\n")
        ida+=1




def Return_id(file) -> int:
    """return number of id!"""
    ida=0
    x=open(file,"r")
    y=x.readlines()
    for i in y:
        i=list(i.split())
        ida+=1

    return ida