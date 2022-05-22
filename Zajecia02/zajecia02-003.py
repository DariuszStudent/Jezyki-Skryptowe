# =============================================
# M2Z03
print("Liczby od jednego do 100")
for i in range(1, 101):
    print(i, end=",")

print("\n\nNieparzyste")

for i in range(1, 31, 2):
    print(i, end=",")

print("\n\nPodzielne przez 3")

for i in range(1, 50):
    if i % 3 == 0:
        print(i, end=",")

print("\n\nLista")
lista = [1, 2, 3, 6, 3, 7, 9, 2]
print(lista)

print("\nFor przez liste")
for i in lista:
    print(i, end=',')

print("\n\n -1 skok <20:0>")
lista = [1, 2, 3, 6, 3, 7, 9, 2]
for i in range(20, -1, -1):
    print(i, end=',')

# =============================================
