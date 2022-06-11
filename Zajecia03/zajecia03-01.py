# =============================================
# M3Z01
import Helper as helper

while True:
    quantity = helper.userVariableINTnumber("Podaj liczbę całkowitą n elementów listy: ")
    lista = helper.randomList(quantity)
    print(lista)
    howManyNextElement = helper.userVariableINTnumber("Ile chcesz dodać kolejnych elementów?: ")
    lista = helper.userAddElementToList(howManyNextElement, lista)
    print(lista)
    pozycja = helper.userVariableINTnumber("Podaj na którą pozycję listy chcesz dodać element: ")
    dodanyElement = helper.userVariableINTnumber("Podaj wartość tej pozycji: ")
    lista.insert(pozycja, dodanyElement)
    print(lista)
    print("Pobranie ostatniego elementu z usunięciem: ")
    print(lista[-1])
    del lista[-1]
    print(lista)
    elementDoUsuniecia = helper.userVariableINTnumber("Podaj element który chcesz usunąć: ")
    del lista[elementDoUsuniecia]
    print(lista)
    elementDoZliczenia = helper.userVariableINTnumber("Podaj element listy który chcesz zliczyć: ")
    print(lista.count(elementDoZliczenia))
    lista.sort()
    print(lista)
    odIlu = helper.userVariableINTnumber("Od jakiej pozycji chcesz wyświetlić listę?: ")
    doIlu = helper.userVariableINTnumber("Do jakiej pozycji chcesz wyświetlić listę?: ")
    print(lista[odIlu:doIlu + 1])
    helper.exitProgram()

# =============================================
