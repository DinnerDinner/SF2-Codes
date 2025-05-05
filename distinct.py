# # def isDistinct(year):
# #     s = str(year)
# #     digits_used = []

# #     for chat in s:
# #         if chat in digits_used:
# #             return False
# #         digits_used.append(chat)
# #     print(digits_used)
# #     return True

# # year = int(input())
# # year = year + 1

# # while not isDistinct(year):
# #     year += 1

# # print(year)



# from __future__ import annotations

# def validation(lst_songs):
#     valid_songs = []
#     for i in lst_songs:
#         try:
#             if "." not in i:
#                 raise ValueError
#         except ValueError:
#             print(f"Missing Extension: {i}")
#         else:
#             j = i.split('.')
#             # print(i)
#             good = ["mp3", "wav","ogg"]
#             if j[-1] in good:
#                 valid_songs.append(i)
#             else:
#                 print(f"Incorrect file extension: {i}")
#     return valid_songs


# lst_songs = ["track1.mp3", "track2.wav", "track3.txt", "track4", "track5.ogg"]
# print(validation(lst_songs))





'''
You are create a Fraction class that defines a rational number with common arithmetic
operations.

1) Define a constructor with default values (that is, if nothing provided by the user)
for numerator and denominator are 0 and 1 respectively.

in all other cases, make sure to check for the following:
-> if denominator is 0, raise a ZeroDivisionError with the message "Denominator cannot be zero"
-> if numerator is 0, then numberator and denominator attributes of object is 0 and 1 respectively
-> determine the sign of the fraction (positive or negative)
-> make sure to store fraction in reduced form
'''

class Fraction:
    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero")
        elif numerator == 0:
            self.numerator = 0
            self.denominator = 1
        else:
            self.numerator = numerator
            self.denominator = denominator
            self.reduce()

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def reduce(self):
        gcd = self.gcd(abs(self.numerator), abs(self.denominator))
        self.numerator //= gcd
        self.denominator //= gcd

        # Ensure the denominator is positive
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        else:
            return f"{self.numerator}/{self.denominator}"
        
    def __truediv__(self, other_fraction):
        num= self.numerator * other_fraction.denominator
        den = self.denominator * other_fraction.numerator
        return Fraction(num, den) 

    def __add__(self, other_fraction):
        
        new_numerator = self.numerator * other_fraction.denominator + other_fraction.numerator * self.denominator
        new_denominator = self.denominator * other_fraction.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other_fraction):
        new_numerator = self.numerator * other_fraction.denominator - other_fraction.numerator * self.denominator
        new_denominator = self.denominator * other_fraction.denominator
        return Fraction(new_numerator, new_denominator)

    '''
    4) Define __eq__, __ne__, __gt__, __ge__, __repr__ functions. When __repr__ is called, the display should be num/denom. Note that when checking for
    equality 3/4 and 6/8 should reutrn True.
    '''
    def __eq__(self, other_fraction):
        return self.numerator * other_fraction.denominator == other_fraction.numerator * self.denominator

    def __ne__(self, other_fraction):
        return not self.__eq__(other_fraction)

    def __gt__(self, other_fraction):
        return self.numerator * other_fraction.denominator > other_fraction.numerator * self.denominator

    def __ge__(self, other_fraction):
        return self.numerator * other_fraction.denominator >= other_fraction.numerator * self.denominator

    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"



f1 = Fraction(1,2)
f2 = Fraction(5,6)
a = f1/f2
print(a)
'''
5) Define __lt__, __le__, __float__ functions. Note that the __float__ function should return the float value of the fraction.
6) Create a list of Fraction objects and sort this list in descending order.
'''