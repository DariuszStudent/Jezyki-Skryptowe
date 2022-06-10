# =============================================
# M3Z01
import Helper as helper

while True:
    quantity = helper.userVariableINT("Podaj liczbę całkowitą n elementów listy: ")
    lista = helper.randomList(quantity)
    print(lista)
    howManyNextElement = helper.userVariableINT("Ile chcesz dodać kolejnych elementów?: ")
    lista = helper.userAddElementToList(howManyNextElement, lista)
    print(lista)
    pozycja = helper.userVariableINT("Podaj na którą pozycję listy chcesz dodać element: ")
    dodanyElement = helper.userVariableINT("Podaj wartość tej pozycji: ")
    lista.insert(pozycja, dodanyElement)
    print(lista)
    print("Pobranie ostatniego elementu z usunięciem: ")
    print(lista[-1])
    del lista[-1]
    print(lista)
    elementDoUsuniecia = helper.userVariableINT("Podaj element który chcesz usunąć: ")
    del lista[elementDoUsuniecia]
    print(lista)
    elementDoZliczenia = helper.userVariableINT("Podaj element listy który chcesz zliczyć: ")
    print(lista.count(elementDoZliczenia))
    lista.sort()
    print(lista)
    odIlu = helper.userVariableINT("Od jakiej pozycji chcesz wyświetlić listę?: ")
    doIlu = helper.userVariableINT("Do jakiej pozycji chcesz wyświetlić listę?: ")
    print(lista[odIlu:doIlu + 1])
    helper.exitProgram()

# =============================================
