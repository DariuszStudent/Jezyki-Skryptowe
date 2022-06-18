# =============================================
# M5Z02

#Otwarcie pliku
plik = open('dane.txt')
plik = open('dane.txt', encoding='utf-8')

#Odczyt pliku
pl = open('dane.txt', encoding='utf-8')
linie = pl.read()
plik.close()
print(linie)
print(type(linie))

pl=open('dane.txt', encoding='utf-8')
linie=pl.readlines()
pl.close()
print(linie)
print(type(linie))

with open('dane.txt',encoding='utf-8') as f:
 for l in f:
    print(l)
f.close()

# Funkcja "seek" przesuwa kursor do wskazanej pozycji - numer znaku w pliku.
plik = open('dane.txt', encoding='utf-8')
linie = plik.readlines()
print(linie)
linie = plik.readlines()
print(linie)
plik.close()

#Jak widzisz ponowny odczyt funkcją "readlines" zwraca nam pustą listę. Wynika to z faktu, że po
#pierwszym odczycie kursor został przesunięty na koniec pliku
plik = open('dane.txt',encoding='utf-8')
linie = plik.readlines()
print(linie)
plik.seek(0)
linie = plik.readlines()
print(linie)
plik.close()


# Jeśli chcemy nadpisać ewentualną zawartość stosujemy przełącznik "w":
plik=open('nowy.txt',encoding='utf-8',mode='w')
#aby dopisywać używamy "a":
plik=open('nowy.txt',encoding='utf-8',mode='a')


#. Jeśli chcemy jednocześnie pisać i czytać używamy "r+":
plik=open('nowy.txt',encoding='utf-8',mode='r+')

# Najprostszy sposób pisania do plików:
plik=open('nowy.txt',encoding='utf-8',mode='w')
for x in range(10):
    plik.write(str(x))
plik.close()


#Jeśli chcesz zapisać kolejne wartości w kolejnych liniach, wystarczy dodać znacznik "\n":
plik=open('nowy.txt',encoding='utf-8',mode='w')
for x in range(10):
    plik.write(str(x)+"\n")
plik.close()

#Python umożliwia też zapis do pliku od razu całej listy elementów. Obrazuje to poniższy przykład
plik=open('nowy.txt',encoding='utf-8',mode='w')
linie=[]
for x in range(10):
    linie.append("linia numer {} \n".format(x))
plik.writelines(linie) # to nas interesuje
plik.close()

# =============================================