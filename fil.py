"""
Olvasd be a mellékelt file (film.txt) tartalmát, majd 
add meg az adatok sorainak a számát (az első sor nélkül)!
Melyik a legrövidebb film címe?
Hány darab legalább 110 perces film van?
Kérd be egy színész nevét, és ajánlj egy pár filmet a készletből, 
    ha tudsz (film címét íratjuk ki, ha van ilyen)! 
    Ha nincs ilyen nevű színész, akkor azt is tudasd!
A 4-es feladat eredményét írasd ki fájlba is!
"""
from Film import Film
def beolvas():
    fajl=open("film.txt", "r", encoding="utf-8")
    fajl.readline()
    nyers_lista=fajl.readlines()
    fajl.close()

    lista=[]
    for i in range(0,len(nyers_lista),1):
        sorok=nyers_lista[i]
        sor_tag=sorok.strip().split(";")
        cim=sor_tag[0]
        rendezo=sor_tag[1]
        foszereplo=sor_tag[2]
        ev=int(sor_tag[3])
        perc=int(sor_tag[4])
        film=Film(cim, rendezo, foszereplo, ev, perc)
        lista.append(film)
    return lista

def sorok(lista):
    print(f"A filmek szama: {len(lista)}")

def l_rovidebb(lista):
    lr_index=0
    for i in range(0,len(lista),1):
        if lista[lr_index].perc>lista[i].perc:
            lr_index=i
    return lr_index
    
def x_perces(lista):
    szamlalo=0
    for i in range(0,len(lista),1):
        if lista[i].perc >=110:
            szamlalo+=1
    return szamlalo

def beker(lista):
    kereses:str=str(input("Szinesz neve: "))
    for i in range(0,len(lista),1):
        if lista[i].foszereplo == kereses:
            eredmeny= print(f"A szinesz a kovetkezo filmben szerepel: {lista[i].cim}")
        elif lista[i].foszereplo != kereses:
            print("Nincs ilyen szinesz a listaban.")
            kereses:str=str(input("Szinesz neve: "))
        return eredmeny

def kiir(eredmeny):
    fajl=open("valasz.txt", "w", encoding="utf-8")
    fajl.write(f"A szinesz a kovetkezo filmben szerepel: {eredmeny}")
    fajl.close()