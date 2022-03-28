# =============================================
# M1Z6
# Typy danych:
# - numeryczne (liczbowe): int, float, complex
# - tekstowe: str
# - sekwencji: list, tuple
# - odwzorowania (mapping type): dict
# - zestawów (set types): set, frozenset
# - logiczne: bool
# - binarne: bytes, bytearray
#
# Typ danych ustawiamy przypisując daną wartość do zmiennej. Nie deklarujemy jakiego typu ma być zmienna.
# Przyjmuje ona taki typ, jaki jest w przypisanej do niej wartości.

a = 3
print('-a jest to zmienna "a = 3": ', type(a))
b = 3.5
print('-b jest to zmienna "b = 3.5": ', type(b))
c = "ala ma kota"
print('-c jest to zmienna "c = ala ma kota": ', type(c))
# d = d + 1 #niepoprawne

e = 5*2.0
print('-wynik działania: "e = 5*2.0" to: ', e)
print('-e jest to zmienna typu: ', type(e))
print('-konwertujemy zmienną typu float to int: "int(round(e))\n'
      'round przy okazji zaokrągla ', int(round(e)))

# =============================================
