# =============================================
# M2Z11

znak = ' . '

for i in range(0, 10):
    for j in range(0, 10):
        if (i == j):
            print(' 0 ', end='')
        else:
            print(znak, end='')
    print()

print()

for i in range(0, 10):
    for j in range(0, 10):
        if (j + i == 9):
            print(' 0 ', end='')
        else:
            print(znak, end='')
    print()


# =============================================