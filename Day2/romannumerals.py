class Solution:
    def numeralToInteger(self, s: str) -> int:
        """
        IDEATION
        1. create a hash table mapping strings to integer values
            create a counter that iterates through the string indices
            check the second value after a character if the character is I, X, or C
        """
        # intialize a value
        value = 0
        # index to iterate over the string
        index = 0
        # hash table mapping roman numeral strings to integer values
        table = {
            "I": 1, "IV": 4, "IX": 9,
            "V": 5,
            "X": 10, "XL": 40, "XC": 90,
            "L": 50,
            "C": 100, "CD": 400, "CM": 900,
            "D": 500, "M": 1000
        }
        while index < len(s):
            if s[index:index + 2] in table:
                value += table[s[index:index + 2]]
                index += 2
            else:
                value += table[s[index]]
                index += 1

        return value


test = Solution()

ex1 = "IX"
ex2 = "III"
ex3 = "XX"
ex4 = "XCLIV"
ex5 = "LVIII"
ex6 = "MCMXCIV"

print(test.numeralToInteger(ex1))
print(test.numeralToInteger(ex2))
print(test.numeralToInteger(ex3))
print(test.numeralToInteger(ex4))
print(test.numeralToInteger(ex5))
print(test.numeralToInteger(ex6))
