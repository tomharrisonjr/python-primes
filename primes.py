import time

def prime(num):
    isPrime = True
    for i in range(2,num):
        if  (num % i) == 0:
            isPrime = False
            print("{} isn't prime! It can be divided by {}! Off with his head!".format(num, num // i))
            break
    return isPrime

noPrimeYet = True
while noPrimeYet:
    num = int(input("Enter a prime number, Snivelling Little Rat-Faced Git! "))
    noPrimeYet = prime(num)

print("Well that was rather silly.")
time.sleep(2)
print("Ni!")




