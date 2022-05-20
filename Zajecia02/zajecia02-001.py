# =============================================
# M2Z01

print("Podaj swój wiek, program sprawdzi ile brakuje ci do 100 lat i czy jesteś pełnoletni")
userNumber = input("Podaj swój wiek: ")
try:
    userNumber = int(userNumber)
    missingYears = 100 - userNumber
    if missingYears > 0:
        print("Do 100 lat brakuje Ci: {}".format(missingYears))
    elif missingYears == 0:
        print("Masz równo 100 lat")
    else:
        print("Masz ponad 100 lat czyli: {}".format(userNumber))
    if userNumber >= 18:
        print("PEŁNOLETNI")
    else:
        print("MŁODOCIANY")
except:
    print("Nie podałeś liczby całkowitej, tylko: {}"
          "\n Koniec programu".format(userNumber))

# =============================================
