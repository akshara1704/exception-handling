#we use else block in exception handling if try does not raise an error then else block will also run

try:
    l1=[6,7,9,0,9]
    print(l1[0])
except:
    print("index out of range")
else:
    print("try main error nahi aya")