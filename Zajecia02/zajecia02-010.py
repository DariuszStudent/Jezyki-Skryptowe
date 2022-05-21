# =============================================
# M2Z10

wzrost = float(input("podaj wzrost w cm: "))
waga = float(input("podaj wage w kg: "))

bmi = waga / ((wzrost / 100) ** 2)
print(bmi)
if (bmi < 18.4):
    print('Niedowaga')
elif (bmi < 24.9):
    print("OK")
elif (bmi <= 29.9):
    print("nadwaga")
elif (bmi <= 34.9):
    print("Duża nadwaga")
elif (bmi <= 39.9):
    print("Bardzo duża nadwaga")
else:
    print("OJ!")


# =============================================