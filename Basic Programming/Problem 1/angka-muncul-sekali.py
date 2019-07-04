#x = "1234123"
#x = "76523752"
x = "112723335"

list_temp = []

for i in range(0, len(x)):
    count_temp = 0
    for j in range(0, len(x)):
        if x[i] == x[j]:
            count_temp += 1
    if count_temp == 1:
        list_temp.append(int(x[i]))

print(list_temp)
