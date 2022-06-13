# =============================================
# M5Z02
import sys

plikwej = 'zajecia05-02.py'
plikwyj = 'zajecia05-02.py.out'

try:
    with open(plikwej, "rt") as wej:
        wiersze = wej.readlines()
        dl = len(wiersze)
        print(f"Ilość wierszy: {dl}")
        with open(plikwyj, "a") as wyj:
            wyj.writelines([plikwej, '\n', str(dl), '\n'])
except Exception as e:
    print(e)
    sys.exit(1)
finally:
    try:
        wej.close()
        wyj.close()
    except Exception as e:
        print(e)
        sys.exit(2)

# =============================================