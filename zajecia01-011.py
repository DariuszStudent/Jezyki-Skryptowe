# =============================================
# M1Z11
from datetime import datetime, timedelta

today = datetime.now()
print("Aktualna data to:", today.year)
daysInput = int(input("Podaj ilość dni: "))
today = today + timedelta(days=daysInput)
print("Za", daysInput, "dni będzie rok", today.year)

# =============================================
