# =============================================
# M2Z03

for i in range(1, 101):
    print(i, end=",")

print("\n o dwa")

for i in range(1, 31, 2):
    print(i, end=",")

print("\npodzielne przez 3")

for i in range(1, 50):
    if (i % 3 == 0):
        print(i, end=",")

print("\n lista")
lista = [1,2,3,6,3,7,9,2]

for i in lista:
    print(i, end=',')

print("\n -1 skok")
lista = [1, 2, 3, 6, 3, 7, 9, 2]

for i in range(20, -1, -1):
    print(i, end=',')

# =============================================
