imiona = ["Jaga", "Agata", "Jas", "Malgosia"]
l1 = list()
l2 = []

print(imiona)
print(imiona[0])
print("\nod elementu do elementu co 2")


imiona.append("Janusz")
imiona.append("Grażyna")
imiona.append("Sławuś")
imiona.append("Szwagier")

print(imiona[1:6:2])
print(imiona[:6])
print(imiona[3:])

print("\n pętla")
for i in imiona:
    print(i, end=' ')

imiona.sort()
print("\n posortowana")
for i in imiona:
    print(i, end=' ')
imie = imiona.pop()
print(imie)
print(imiona)
imiona.insert(1, "Edzio")
print(imiona)
print(imiona.count("Jaga"))
imiona.remove("Jaga")

l1 = [1,2,3,4]
l2 = [100,200,300,400]
l3 = l1+l2
print(l3)

print(len(imiona))
del imiona[:2]
print(imiona)

#l1 = l2
#print(l1)
#print(l2)
#
#l2[0] = 133
#print(l1)
#print(l2)

l1 = l2[:]
print(l1)
print(l2)

l2[0] = 333
print(l1)
print(l2)

l4 = list(range(0, 100))
print(l4)

# ===================
k1 = ("Janusz", "Agata", [1, 2, 3])
print(k1)
print(k1[0])
print(k1.index("Agata"))

l2[1] = (1, 2, 3)
print(l2)

k1[2][0] = 20
print(k1)

k1[2].append(11)
print(k1)
k2 = (100,200,300)

# zbior
x = set()
x.add("janusz")
x.add("agata")
x.add("zbigniew")
x.add(1)
x.add(3)
x.add(1)
x.add(6)
print(x)
x.add(k2)
print(x)
print(x)
print(x)
#x.remove(500) #blad nie ma elementów
#x.discard(500) #brak błędó
x = {1, 2, 3, 4, 5}
y = {100, 200, 300, 400}
z = x.union(y)
print(z)

x = {1, 2, 3, 4, 5, 400}
y = {100, 200, 300, 400}
z = x.difference(y)
print(z)
z = x.intersection(y)
print(z)

l = [8, 9, 10]
l.append(z)
print(l)

l = [8, 9, 10]
l.extend(z)
print(l)