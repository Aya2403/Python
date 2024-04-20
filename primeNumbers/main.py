# This is a sample Python script.
import math


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def is_prime(n):
    #The Sieve of Eratosthenes math concept
    prime_divsor = math.floor(math.sqrt(n))
    if n==1 or n==0:
        return False
    if n%2==0:     #if num is even and not 2 -> not prime
        return False
    else:
        for i in range(3,prime_divsor+1,2):#the rest are odd numbers to check.
            if n%i==0:
                return False
            else:
                    continue
        return True
#Task2 : calc the num of primes between 100-151 inclusive
x=0 #to calculate the number of primes
for i in range(100,152): #added one to include 151
    if is_prime(i):
        x+=1
# print(x)
# print(is_prime(3))







