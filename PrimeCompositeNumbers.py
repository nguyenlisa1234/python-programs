def primeComposite(start,end):
    for n in range(start,end+1):
        if n <= 2:
            print(f"{n} is prime since the only divisors are 1 and {n}.")
        for d in range(2,n):
            if n % d == 0:
                q = int(n / d)
                print(f"{n} is composite since we can write {n} = {d} * {q} and clearly 1 < {d} < {n}.")
                break
            elif d == n-1:
                print(f"{n} is prime since the only divisors are 1 and {n}.")

# other way is with boolean

def primeComposite(start,end):
    for n in range(start,end+1):
        prime = True
        for d in range(2,n):
            if n % d == 0:
                q = n / d
                print(f"{n} is composite since we can write {n} = {d} * {q} and clearly 1 < {d} < {n}.")
                prime = False
                break
        if prime:
            print(f"{n} is prime since the only divisors are 1 and {n}.")