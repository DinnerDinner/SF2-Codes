'''
Implement a custom iterator class to generate 
even numbers in the interval [start, end]
'''

class Even:
    def __init__(self, start=0, end =10):
        self.start = start
        if start %2!=0:
            self.start+=1
        self.end = end
    def _advance(self):
        self.start+=2

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        else:
            answer = self.start
            self._advance()
            return answer
            
if __name__ == "__main__":
    even = Even(3, 10)
    for num in even:
        print(num)




'''
Implement a custom iterable class for the Fibonacci
numbers.  This class constructor should take n, 
representing the first n terms of the Fibonacci 
sequence
'''

class Fibonacci:
    def __init__(self, n):
        self.__count = 0
        self.n = n
        self.a = 0
        self.b = 1


    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__count >= self.n:
            raise StopIteration
        else:
            self.__count+=1
            self.a, self.b = self.b, self.b+self.a
            return self.a
    

if __name__ == "__main__":
    fibo = Fibonacci(5)
    for num in fibo:
        print(num)
    print("\n\n")






'''
Draw the recursion tree for the computation of 
recSum(10)
'''


'''
write a recursive function that determines the
minimum element in a given list of integers. 
# '''
# def find_min_recursive(lst, min=0):
   
    # rest_min = find_min_recursive(lst[1:])
    # return lst[0] if lst[0] < rest_min else rest_min
#     if not lst:
#         return min
#     candidate=lst.pop(0)
#     if candidate<min:
#         return find_min_recursive(lst, min)
#     return find_min_recursive(lst, candidate)
    

# numbers = [3, 1, 4, 1, 5, 9, -2, 6]
# print("Minimum element:", find_min_recursive(numbers))




'''
write a recursive function that converts a string of integers
into its integer counterpart
'''




'''
write a recursive function to determine if a given string
is a palindrome
'''
def is_palindrome(s):
    s = list(s)
    print(s)
    if len(s) <= 1:
        return True
    a = s.pop(0)
    b = s.pop(-1)  
    if a!=b:
        return False
    
    return is_palindrome(s[1:-1])


'''
Write a recursive function to count number of vowels in a string
'''
def vowels(string, total=0):
    vowels = 'aeiou'
    string = list(string)
    current = string.pop(0)
    print(current)
    if current in vowels:
        total+=1
        vowels(string, total)
    return total
print(vowels("james"))


'''
use recursion to determine if a string has more vowels than consonants. 
'''