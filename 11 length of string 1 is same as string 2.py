a = True
while a:
    try:
        string1 = input("enter string= ")
        string2 = input("enter string= ")
        if len(string1) == len(string2):
            a = False
        else:
            l=[0,1,2]
            print(l[4])

    except:
        print("enter same string")
