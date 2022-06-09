# =============================================
# M3Z00c

def nextList(user):
    licznik = user - 10
    listaNext = []
    while licznik != user:
        listaNext.append(licznik)
        licznik += 1
    return listaNext


lista01 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista01)
print(lista01[1:6])
print(lista01[::2])
print(lista01[-2])

lista02 = []
word = "python"
for i in word:
    lista02 += i
print(lista02)

lista001 = nextList(10)
lista002 = nextList(20)
lista003 = nextList(30)
lista004 = nextList(40)
lista005 = nextList(50)
lista006 = nextList(60)
lista007 = nextList(70)
lista008 = nextList(80)
lista009 = nextList(90)
lista010 = nextList(100)

listaDwyWymiar = [lista001, lista002, lista003, lista004, lista005,
                  lista006, lista007, lista008, lista009, lista010]

for i in listaDwyWymiar:
    for j in i:
        print("{:>5}".format(j), end="")
    print()

print(listaDwyWymiar[1])


# =============================================
