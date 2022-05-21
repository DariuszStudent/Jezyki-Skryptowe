tablica = [
    ["A", "B", "C"],
    ["D", "E", "F"],
    ["G", "H", "I"],
]

print(tablica)

for w in tablica:
    for k in w:
        print(k, " ", end="")
    print()