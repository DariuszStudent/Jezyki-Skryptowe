# =============================================
# M3Z00c

# Zbiór (ang. set) to tablica, w których nie ma dwóch lub więcej identycznych elementów.
# Powiedzmy, że chcesz dostać zbiór wszystkich słów użytych w danym zdaniu:

print(set("jego imie to Eryk i Eryk jest jego imieniem".split()))

A = set(["Jake", "John", "Eric"])
B = set(["John", "Jill"])
print("\n", A)
print(B)
print("(część wspólna):")

print(A.intersection(B)) # set(['John'])
print(B.intersection(A)) # set(['John'])

print("\n(część różna):")
print(A.difference(B)) # set(['Jake', 'Eric']
print(B.difference(A)) # set(['Jill'])

print("\n(suma):")
print(A.union(B)) # set(['Jill', 'Jake', 'John', 'Eric'])

# =================================================================
l1 = [1,2,3,4]
l2 = [100,200,300,400]
l3 = l1+l2
print(l3)

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
#x.discard(500) #brak błędów
x = {1, 2, 3, 4, 5}
y = {100, 200, 300, 400}
z = x.union(y)
print(z)

l = [8, 9, 10]
l.append(z)
print(l)

l = [8, 9, 10]
l.extend(z)
print(l)

# ========================================================