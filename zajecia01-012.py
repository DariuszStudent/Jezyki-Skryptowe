# =============================================
# M1Z12

import datetime

today = datetime.date.today()
endWorldWarII = datetime.date(1945, 5, 8)

print("Dzisiejsza data to:", today)
print("Data zakończenia drugiej wojny światowej:", endWorldWarII)
difference = today - endWorldWarII

print("Od drugiej wojny światowej minęło:", difference.days)

# =============================================
