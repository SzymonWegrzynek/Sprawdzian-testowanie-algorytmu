import math


def czynnikiPierwsze(n):
    czynniki = []

    if n <= 1:
        return

    while n % 2 == 0:
        czynniki.append(2)
        n = n // 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            czynniki.append(i)
            n = n // i

    if n > 2:
        czynniki.append(n)

    return czynniki


n = int(input("Podaj liczbę całkowitą: "))
wynik = czynnikiPierwsze(n)
print(wynik)
