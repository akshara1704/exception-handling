#EXCEPTION HANDLING
'''
we use exception handling to bypass the error so we can run our desired program with different cases

SYNTAX -
try:
    #indented block
except:
    #indented block

#note if try runs then except block will not run and except will only run
      when try block raises an error
'''
try:
    print("error ayega neeche")
    l=[2,4,5,6]
    print(l[6]) #ye nahi chalega kyunki error hai
except:
    print("this runs because try raises an error")