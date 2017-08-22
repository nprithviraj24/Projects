#fibonacci:  Using recursion, i.e calling it's own function.
#defining the function

#This program compatibe with python 2.x intrepreter only
def fib(num):
    if num == 0: 
        #print ("0")
        return 0
    elif num == 1:
        #print ("1")
        return 1
    else:
        num = num-1
        #print '%d +' % (num) ,   
        #print "{} + ".format(num),
        return fib(num)+fib(num-1)


#Then ask the number!
number = input("Enter the number: ")
type(number)

x = fib(number)
print '\n\nFibonacci sequence: %d ' %(x)