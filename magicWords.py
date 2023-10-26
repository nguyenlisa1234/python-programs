def magicWords(n):
    if n % 3 == 0 and n % 5 == 0:
        print("Alakazam")
    elif n % 3 == 0:
        print("Abra")
    elif n % 5 == 0:
        print("Kadabra")
    else:
        print(n)
for i in range(1,30):
    magicWords(i)