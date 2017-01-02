#!/usr/bin/python

import time

# returns True if the given number is a prime, False otherwise
def isPrime(num):
    for i in range(2,num):
        if  (num % i) == 0:
            print("{} isn't prime! It can be divided by {}! Off with his head!".format(num, num // i))
            return False
    return True

# prompts user for a prime number (very politely, of course!)
def askForPrime():
    noPrimeYet = True
    while noPrimeYet:
        num = int(input("Enter a prime number, Snivelling Little Rat-Faced Git! "))
        noPrimeYet = not isPrime(num)

# main, just call askForPrime()
askForPrime()
print("Well that was rather silly.")
time.sleep(2)
print("Ni!")




