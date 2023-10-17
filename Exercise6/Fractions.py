import math

class Fractions:
    def __init__(self):
        pass

    def printFraction(self, numerator, denominator):
        return f"{numerator}/{denominator}"

    def reduceToLowestTerm(self, numerator, denominator):
        d = math.gcd(numerator, denominator)
 
        num = numerator // d
        denom = denominator // d
    
        return self.printFraction(num, denom)

    def multiply(self, numerator1, denominator1, numerator2, denominator2):
        prodNumerator = numerator1 * numerator2
        prodDenominator = denominator1 * denominator2

        return self.reduceToLowestTerm(prodNumerator, prodDenominator)

    def compare(self, fraction1, fraction2):
        if (fraction1 == fraction2):
            return True
        else: 
            return False