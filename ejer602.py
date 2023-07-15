print( "\033[H\033[J")
from datos import *
def listarNombres(lista):
    nombres = []
    for i in range(len(lista)):
        nombres.append(lista[i][0])
    nombres.sort()
    
    print()
    print('Lista ordenada de nombres')
    for i in range(len(nombres)):
        print(nombres[i])
    print()
    return
############
def listarNombresYNotas(lista):
    for i in range(len(lista)-1): # 0-1
        for j in range(len(lista)-i-1): # 0-1
            if (lista[j][0] > lista[j+1][0]):
                auxN = lista[j].copy()
                lista[j] = lista[j+1].copy()
                lista[j+1] = auxN
    
    print()
    print('Lista ordenada de nombres y notas')
    for i in range(len(lista)):
        print(lista[i][0],lista[i][1])
    print()
    return
##############
def listarNombresYPromedios(lista):
    for i in range(len(lista)-1): # 0-1
        for j in range(len(lista)-i-1): # 0-1
            if (lista[j][0] > lista[j+1][0]):
                auxN = lista[j].copy()
                lista[j] = lista[j+1].copy()
                lista[j+1] = auxN
    print(" ")
    print('Lista ordenada de nombres y promedios')
    for i in range(len(lista)):
        print(lista[i][0]," ---- ",'Promedio:',sum(lista[i][1])/len(lista[i][1]))
    return
#############
def NotaMedia(lista):
    acum=0
    for i in range(len(lista)):
        a1=sum(lista[i][1])/len(lista[i][1])
        acum=acum+a1
        promgral=acum/len(lista)
    print("La nota media de todos los alumnos es: ",promgral)    
    return
##################
def NotaMediaApro(lista):
    acum=0
    conta=0
    for i in range(len(lista)):
        a1=sum(lista[i][1])/len(lista[i][1])
        if a1>=6:
            acum=acum+a1
            conta=conta+1
    promgral=acum/conta
    print("La nota media de los alumnos aprobados es: ",promgral)
    return
##################
def NotaMediaNoApro(lista):
    acum=0
    conta=0
    for i in range(len(lista)):
        a1=sum(lista[i][1])/len(lista[i][1])
        if a1<6:
            acum=acum+a1
            conta=conta+1
    promgral=acum/conta
    print("La nota media de los alumnos suspendidos es: ",promgral)
    return
##################
op="x"
while op!="g":
    print("             MENÚ PRINCIPAL    ")
    print("a) Mostrar la lista (alfabética) de alumnos.")
    print("b) Mostrar la lista (alfabética) de alumnos con sus notas.")
    print("c) Mostrar la lista (alfabética) de alumnos con sus promedios.")
    print("d) Mostrar la nota media de todos los alumnos.")
    print("e) Mostrar la nota media de los alumnos aprobados.")
    print("f) Mostrar la nota media de los alumnos suspendidos.")
    print("g) Salir del programa")
    op=input("Elija una opción: ")
    if op=="a":
        listarNombres(alumnos)
    if op=="b":
        listarNombresYNotas(alumnos)
    if op=="c":
        listarNombresYPromedios(alumnos)
    if op=="d":
        NotaMedia(alumnos)
    if op=="e":
        NotaMediaApro(alumnos)
    if op=="f":
        NotaMediaNoApro(alumnos)
    if op=="g":
        print("Usted a salido del menú")
        