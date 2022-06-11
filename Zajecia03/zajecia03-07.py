# =============================================
# M3Z07


id00001 = ('Dariusz', 'Kowalski')
id00002 = ('Daz', 'Wiak')
id00003 = ('Darsz', 'Wiak')
id00004 = ('iusz', 'Wak')
id00005 = ('WRDSDz', 'Wdf')
id00006 = ('dsfsdf', 'Wr')
id00007 = ('aaaaa', 'k')
id00008 = ('bbbbb', 'Franek')

listaOsob = {id00001: 'kierownik', id00002: 'pracownik', id00002: 'pracownik', id00004: 'pracownik'}
listaOsob[id00005] = 'kierownik'
listaOsob[id00006] = 'ksiegowa'
listaOsob[id00007] = 'sprzataczka'
listaOsob[id00008] = 'pracownik'

print(listaOsob)

for i in listaOsob:
    for j in i:
        print('{:>15}'.format(j), end=' ')
    print()

# =============================================
