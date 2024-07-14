import random
try:
    num=int(input("enter number= "))
except:
    l1=["sale","bsdk","chutiye","gandu"]
    r=random.randrange(0,4)
    print(l1[r],"number daal")
finally:
    print("this is finally block")