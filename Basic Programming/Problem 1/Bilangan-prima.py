#input
#n = 3
#n = 7
n = 10

num_faktor = 0
for i in range(1, n+1):
    if n % i == 0:
        num_faktor += 1

if num_faktor == 2 :
    print(" Bilangan Prima ")

else:
    print(" Bukan Bilangan prima ")