# =============================================
# M5Z02a

def trojkat(l):
    for i in range(0, l):
        for j in range(0, i + 1):
            print("*", end="")
        print("\r")

liczba = int(input("Podaj liczę wierszy: "))
trojkat(liczba)

# =============================================
