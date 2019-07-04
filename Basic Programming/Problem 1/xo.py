#x = "xoxoxo"
#x = "oxooxo"
#x = "oxo"
#x = "xxxooo"
x = "xoxooxxo"


jumlah_x = 0
jumlah_o = 0

for i in range(0, len(x)):
    if x[i] == "x":
        jumlah_x += 1
    elif x[i] == "o":
        jumlah_o += 1
    
if jumlah_o == jumlah_x:
    print('true')
else:
    print('false')