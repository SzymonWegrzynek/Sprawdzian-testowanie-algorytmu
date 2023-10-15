def rozkladanieNaCzynnikiPierwsze(x):
    k = 2
    while x >= 2:
        while x % k == 0:
            print(x)
            x = int(x/k)
        k += 1
    print("1")

i = int(input("Podaj liczbę: "))
rozkladanieNaCzynnikiPierwsze(i)
