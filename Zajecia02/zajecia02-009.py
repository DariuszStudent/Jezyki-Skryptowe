# =============================================
# M2Z09

odp = 't'

while (odp == 't'):
    a, b, c, = input("Podaj trzy zmienne oddzielone spacjami.").split(' ')
    print("Podano:", a, b, c)
    odp = input("Czy kontynuowac? [t/n]? ")
    odp = odp.lower()

# =============================================