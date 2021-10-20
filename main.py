def citireLista():
    #aceasta functie citeste numarul de elemente si apoi elementele de la tastatura
    lista = []
    numarElemente=int(input("Numar elemente lista:"))
    for i in range (0,numarElemente):
        element=float(input("Valoare:"))
        lista.append(element)
    return lista
def citireInterval(i,a,b):
    #aceasta functie verifica daca un element dat i apartine sau nu intervalului deschis citit de la tastatura(capetele fiind considerate
    #elementele a si b citite de la tastatura apeland functia 3 a meniului)
    if i > a and i < b:
        return True
    else:
        return False

def eDivizibil(a,b):
    #aceasta functie verifica daca nr a e divizil cu nr. b,returnand True sau False,dupa caz
    if a % b == 0:
        return True
    else:
        return False
def printMenu():
    #am definit meniul cu toate functiile sale de apel,incluzand si o functie de exit ,spre incheierea programului
    print('0.Exit')
    print('1.Citire lista')
    print('2.Lista numere intregi')
    print('3. verificare aparteneta la un interval')
    print('4.Afisarea tuturor numerelor a caror parte intreaga e divizor al partii fractionare')
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
        if numar == 4:
            for elem in listaCitita:
                parteintreagaelem=int(elem)
                stringelem=str(elem)
                pozitiePunct=stringelem.find('.')
                partefractionarastring=stringelem[pozitiePunct+1:]
                partefractionaraelem=int(partefractionarastring)
                if eDivizibil(partefractionaraelem,parteintreagaelem):
                    print(elem, "are partea intreaga divizor al partii sale fractionare")
        printMenu()
        numar = int(input("Insert option:"))


