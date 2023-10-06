# Import math module
import math

def divisors(num):
    # Empty set
    divs = set()
    for i in range(1, math.isqrt(num) + 1):
        if num % i == 0:
            divs.add(i)
            divs.add(num//i)

    return divs

def divisorOfTen(divisors):
    # Empty set
    divsOfTen = set()
    for divs in divisors:
        t = divs
        while t % 5 == 0:
            t //= 5
        while t % 2 == 0:
            t //= 2
        if t == 1:
            divsOfTen.add(divs)

    return divsOfTen

num = int(input("Enter the number: "))
divs = divisors(num)
divsOfTen = divisorOfTen(divs)

# Prints out the results
print(len(divsOfTen))
for divisor in sorted(divsOfTen):
    print(divisor)