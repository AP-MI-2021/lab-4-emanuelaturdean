def citireLista():
    lista = []
    numarElemente=int(input("Numar elemente lista:"))
    for i in range (0,numarElemente):
        element=float(input("Valoare:"))
        lista.append(element)
    return lista
def citireInterval(i,a,b):
    if i > a and i < b:
        return True
    else:
        return False


def printMenu():
    print ('0.Exit')
    print('1.Citire lista')
    print('2.Lista numere intregi')
    print('3. verificare aparteneta la un interval')

listaCitita= []
if __name__ == '__main__':
    printMenu()
    numar=int(input("Insert option:"))
    while(numar != 0):
        if numar == 1:
            listaCitita=citireLista()
            print(listaCitita)
        if numar == 2:
            print(listaCitita)
            listaNmereIntregi = []
            for element in listaCitita:
                if int(element) == element:
                    listaNumereIntregi.append(int(element))
            print(listaNumereIntregi)
        if numar == 3:
            capatstang = int(input("scrie capatul stang al intervalului:"))
            capatdrept = int(input("scrie capatul drept al intervalului:"))
            for elem in listaCitita:
                if citireInterval(elem,capatstang,capatdrept):
                    print(elem, "apartine intervalului dat")
        printMenu()
        numar = int(input("Insert option:"))


