
# all  prime factors of a number.
#This code is compatible in python 3.x, works in 2.x as well but output formatting is different

number = input("Enter the number: ")

number = int(number)

def check_Prime(i):
    if i >=2:
        for  j in range(2,i):
            if not (i%j):
                return False
    else: 
        return False
    return True

print ("The prime factors are: ")
for i in range(2,number):
    if(number%i == 0):
        if(check_Prime(i)):
            string = repr(i)
            print(" ",string), 



