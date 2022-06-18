# =============================================
# M4Z07
tekst = input("Podaj tekst do zakodowania: \n")
klucz = int(input("Jaki ma być klucz kodu?: \n"))

def szyfr_cezara(tekst, klucz):
    wynik = ""

    for i in range(len(tekst)):
        litera = tekst[i]
        if (litera.isupper()):
            wynik += chr((ord(litera) + klucz - 64) % 26 + 64)
        else:
            wynik += chr((ord(litera) + klucz - 96) % 26 + 96)
    return wynik


print("Tekst : ", tekst)
print("Klucz : ", str(klucz))
print("Kod zezara: ", szyfr_cezara(tekst, klucz))

# =============================================