#x = 63
#x = 124
#x = 53
#x = 88
x = 120

y = x % 60

if x >= 60 and y < 10:
    print(str(int(x/60))+":0"+str(x%60))

elif x >= 60 and y >= 10:
    print(str(int(x/60))+":"+str(x%60))

elif x < 60:
    print("0:"+str(x))
