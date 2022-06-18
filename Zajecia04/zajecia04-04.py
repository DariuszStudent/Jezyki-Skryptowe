# =============================================
# M4Z04
import Helper as helper


def ciag_fibonaciego(n):
   if n <= 1:
       return n
   else:
       return(ciag_fibonaciego(n-1) + ciag_fibonaciego(n-2))

dlugosc_ciagu = int(input("Jaka ma być długośc ciągu?: "))


if dlugosc_ciagu <= 0:
   print("Liczba musi być dodatnia")
else:
   print("Ciąg fibonaciego:")
   for i in range(dlugosc_ciagu):
       print(ciag_fibonaciego(i))


# =============================================