# =============================================
# M5Z09
import string
import random

dlugosc = int(input("Podaj dlugosc hasla jakie chcesz wygenerowac : "))

liczba = string.digits
symbol = string.punctuation
male = string.ascii_lowercase
duze = string.ascii_uppercase


suma = liczba + symbol + male + duze

x = random.sample(suma,dlugosc)
haslo = "".join(x)



plik = open("Haslo1.txt","w+")
plik.write(haslo)

# =============================================
