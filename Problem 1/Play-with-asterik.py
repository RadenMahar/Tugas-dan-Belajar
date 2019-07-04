n = 5

#pattern satu
for i in range(1, n+1):
    print('* '*i)
print("\n")

#pattern dua
for i in range(0, n):
    print(" "*(int((n+1/2))-i)+"* "*(i+1)+" "*(int((n+1/2))-i))

#pattern tiga
print('\n')
for i in range(1, n+1):
    for j in range(1, i+1):
        print(str(j), end = ' ')
    print(" ")
    
#pattern empat
temp = [0]
print('\n')
for i in range(1, n+2):
    for j in range(1+temp[-1], temp[-1]+i):
        temp.append(j)
        print(str(j), end = ' ')
    print(" ")

print('\n')
#pattern 5
for i in range(1, n+1):
    print(" "*((n+1)-i)+"*"*i)