# Kian Candelario
import math

def cubeRoot(num):
    # Formula x^1/3
    cubeRoot = num ** (1/3)
    return round(cubeRoot, 2) # Round off two decimal places

number = int(input("Enter the number: "))
print(f"Cube root: {cubeRoot(number)}")