'''
Question1:

Given a dictionary of keys that are strings and/or integers, 
values are lists, write a snippet of code that returns the total number
of elements of all lists that have keys as strings.  
'''


def list_counter(d):
    lst = []
    for key in d:
        if type(key) == str:
            for i in d[key]:
                lst.append(i)
    return len(lst)


print(list_counter({'a':[4], 3:[10], 'b':["hello", 'rahrah'], 'meow':[1,2,3,4]}))




'''
Question2:

Write a function wordTally that takes an integer argument 
n and reads n words from the user.  Note that the user
may enter the same word multiple times.  
Your function should tally up how many times each word
occurs that the user has entered and store it in a dictionary
where the keys are the words and the values are the number
of times each word occurs.  
Return this dictionary. 

You may only create one collection: one dictionary
'''

def wordTally(n):
    d = {}
    for i in range(n):
        user = input('> ')
        if user not in d:
            d[user]=1
        else:
            d[user] += 1
    return d

# print(wordTally(3))





'''
Quesiton3: 

write a function called invertDictionary that takes a 
dictionary d as an argument.  This function inverts the
provided dictionary.  That is, the keys become the values
(as lists) and the values become the keys. 

Note that d may have repetitive values, in which case in 
the inverted dictionary only one of these values
will be used as a key. For such a key, in the inverted
dictionary the value is a list of all such possible
keys from d

For example: 
d = {3: 5, 4: 5, 6: 1}
d_inverted = {5: [3, 4], 1: [6]}
'''

def invertDictionary(d):
    d_inverted ={}
    for key in d:
        num = d[key]
        d_inverted[num] = d_inverted.get(num, [])
        d_inverted[num].append(key)
    return d_inverted

print(invertDictionary({3: 5, 4: 5, 6: 1}))



'''
Question 4:

Given a sequence of m words and an integer k, find the
k-th most common words.  A word w is the k-th most 
common if exactly k-1 distinct words occur more
frequently than w. 
'''

def common(m, k):
    dct = {}
    for x in m.split():
        if x not in dct:
            dct[x] = 1
        else:
            dct[x]+=1
    print(dct)
    a = list(dct.keys())
    a.sort()
    return a

print(common("hello world blah blah blah blah", 4))