# =============================================
# M5Z05
sekundy = int(input("Podaj ilość sekund do obliczeń: "))

MM, SS = divmod(sekundy, 60)
GG, MM = divmod(MM, 60)

print('gdzin:', GG, ', minut:', MM, ', sekund:', SS,)
print('Czas ', GG, MM, SS, sep=':')

# =============================================