# This is a sample Python script.
import math


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def is_prime(n):
#The Sieve of Eratosthenes math concept
    prime_divisor = math.isqrt(n) + 1  # Using isqrt for integer square root instead of sqrt and floor
    # +1 for the upper limit for the loop.
    if n == 2:
        return True
    if n < 2 or n % 2 == 0: #if num is even and not 2 -> not prime , also numbers less than 2
        return False
    for i in range(3,prime_divisor,2):#the rest are odd numbers to check.
        if n%i==0:
            return False
    return True
#Task2 : calc the num of primes between 100-151 inclusive
x=0 #to calculate the number of primes
for i in range(100,152): #added one to include 151
    if is_prime(i):
        x+=1
# print(x)
# print(is_prime(3))







