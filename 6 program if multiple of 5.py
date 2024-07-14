import random
a=True
while a:
    try:
        num=int(input("enter number= "))
        if num % 5==0:
            a=False
    except:
        l1=["sale","bsdk","chutiye","gandu"]
        r=random.randrange(0,4)
        print(l1[r],"number daal")
        