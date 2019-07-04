def FinePrime(start, end):
    for i in range(start, end+1):
        if prime(i) == True:
            return i
    else:
        return "Tidak ada bilangan prima"

def prime(bilangan):
    for i in range(2, bilangan):
        if bilangan % i == 0:
            return False
    return True

print(FinePrime(4000, 7000))