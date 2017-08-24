import time  #Importing time module.

#function to check if the number is prime or not!
def check_prime(num):
    if(num>2):
        for i in range(2,num):
            if(num%i == 0):
                return False
    else:
        return False
    return True

#function to run the loop until there is any keyboard interruption(Ctrl+C for interruption)
def sleeper(num):
    i = 1
    #input = raw_input('')
    print('Running infinite loop printing all the prime numbers until inteprrupted. Ctrl+C')
    try:        
        while True:
            time.sleep(num)
            if check_prime(i):
                print(repr(i))
            i = i+1
    except KeyboardInterrupt:
        print('Interrupted.')


#Actual control logic starts from: 
try:
    num = input("Interruption between each sections: ")
    try: 
        num = float(num)
    except ValueError:
        print("Enter only number.")
    sleeper(num)
except KeyboardInterrupt:
    print('\n\nKeyboard exception received. Exiting.')
    exit()