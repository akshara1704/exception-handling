import random

a = True
while a:
    try:
        num = int(input("enter number= "))
        if num % 4 == 0 and num % 6== 0:
            a = False
    except:
        l1 = ["sale", "bsdk", "chutiye", "gandu"]
        r = random.randrange(0, 4)
        print(l1[r], "number daal")
    finally:
        print("finally always run")

#note if try block raises an error amd except block will also raise and error
#then if there is an finally block the statement in the finally block
#will always run then after complete execution the error will be shown
#which are shown in the try and except block

