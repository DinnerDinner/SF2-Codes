# # # # # # # # # # # # # # # # # # # # standings = {
# # # # # # # # # # # # # # # # # # # #  "Bruins": [28, 28, 8],
# # # # # # # # # # # # # # # # # # # #  "Canadiens": [30, 26 ,6],
# # # # # # # # # # # # # # # # # # # #  "Penguins": [24, 30, 10],
# # # # # # # # # # # # # # # # # # # #  "Predators": [23, 32, 7],
# # # # # # # # # # # # # # # # # # # #  "Jets": [43, 16, 4],
# # # # # # # # # # # # # # # # # # # #  "Oilers": [36, 22, 4]
# # # # # # # # # # # # # # # # # # # # }
# # # # # # # # # # # # # # # # # # # # ordered = []
# # # # # # # # # # # # # # # # # # # # for i in standings.keys():
# # # # # # # # # # # # # # # # # # # #     team = []
# # # # # # # # # # # # # # # # # # # #     team.append(i)
# # # # # # # # # # # # # # # # # # # #     team.append((standings[i][0]*2)+(standings[i][2]))
# # # # # # # # # # # # # # # # # # # #     ordered.append(team)
# # # # # # # # # # # # # # # # # # # # print(ordered)

# # # # # # # # # # # # # # # # # # # # import numpy as np
# # # # # # # # # # # # # # # # # # # import pandas as pd
# # # # # # # # # # # # # # # # # # # import matplotlib.pyplot as plt
# # # # # # # # # # # # # # # # # # # sales_df = pd.DataFrame({
# # # # # # # # # # # # # # # # # # #     "Months": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
# # # # # # # # # # # # # # # # # # #     "Electronics": [50, 55, 53, 60, 62, 65],
# # # # # # # # # # # # # # # # # # #     "Clothing": [20, 22, 21, 25, 27, 26],
# # # # # # # # # # # # # # # # # # #     "Furniture": [30, 28, 35, 40, 38, 42]
# # # # # # # # # # # # # # # # # # # })

# # # # # # # # # # # # # # # # # # # mean_sales = sales_df[["Electronics","Clothing","Furniture"]].mean()
# # # # # # # # # # # # # # # # # # # plt.plot(sales_df['Months'], sales_df['Electronics'], label = "Electronics")
# # # # # # # # # # # # # # # # # # # # plt.plot(sales_df['Months'], sales_df['Clothing'], label = "Clothing")
# # # # # # # # # # # # # # # # # # # # plt.plot(sales_df['Months'], sales_df['Furniture'], label = "Furniture")

# # # # # # # # # # # # # # # # # # # # plt.xlabel("Months")
# # # # # # # # # # # # # # # # # # # # plt.ylabel("Electronic Sales")
# # # # # # # # # # # # # # # # # # # # plt.title("Electronics Sales Over Months")

# # # # # # # # # # # # # # # # # # # # # plt.legend()
# # # # # # # # # # # # # # # # # # # # plt.show()
# # # # # # # # # # # # # # # # # # # # print(mean_sales)



# # # # # # # # # # # # # # # # # # # def countPeaks(lst):
# # # # # # # # # # # # # # # # # # #     countpeaks = 0
# # # # # # # # # # # # # # # # # # #     for i in range(len(lst)):
# # # # # # # # # # # # # # # # # # #         for j in range(len(lst[0])):
# # # # # # # # # # # # # # # # # # #             num = lst[i][j]
# # # # # # # # # # # # # # # # # # #             top = lst[i-1][j] if i > 0 else float('-inf')
# # # # # # # # # # # # # # # # # # #             bottom = lst[i+1][j] if i < len(lst)-1 else float('-inf')
# # # # # # # # # # # # # # # # # # #             right = lst[i][j+1] if j<len(lst[0])-1 else float('-inf')
# # # # # # # # # # # # # # # # # # #             left = lst[i][j-1] if j>0 else float('-inf')
# # # # # # # # # # # # # # # # # # #             if num>top and num>bottom and num>right and num>left:
# # # # # # # # # # # # # # # # # # #                 countpeaks+=1
# # # # # # # # # # # # # # # # # # #     return countpeaks

# # # # # # # # # # # # # # # # # # # print(countPeaks([ [10, 2, 5], [3, 20, 4], [31, 2, 14] ] ))




# # # # # # # # # # # # # # # # # # # def count_digit_in_matrix(matrix, digit):
# # # # # # # # # # # # # # # # # # #     times = 0
# # # # # # # # # # # # # # # # # # def count_digit_in_matrix(matrix, digit):
# # # # # # # # # # # # # # # # # #     count = 0
# # # # # # # # # # # # # # # # # #     for row in matrix:
# # # # # # # # # # # # # # # # # #         for cell in row:
# # # # # # # # # # # # # # # # # #             count += str(cell).count(str(digit))  # Convert to string to check each digit
# # # # # # # # # # # # # # # # # #     return count



# # # # # # # # # # # # # # # # # # print(count_digit_in_matrix([['abc44444444444444'],['agv4'],['344afdfadaf']],44))
# # # # # # # # # # # # # # # # # import pandas as pd

# # # # # # # # # # # # # # # # # data = {
# # # # # # # # # # # # # # # # #     "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
# # # # # # # # # # # # # # # # #     "Age": [22, 25, 27, 21, 30],
# # # # # # # # # # # # # # # # #     "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
# # # # # # # # # # # # # # # # # }

# # # # # # # # # # # # # # # # # df = pd.DataFrame(data)
# # # # # # # # # # # # # # # # # filtered_df = df[df["Age"]>23]
# # # # # # # # # # # # # # # # # print(filtered_df)


# # # # # # # # # # # # # # # # lst = [ [1, 2, 3, 4], [5, 6, 7, 8], [8, 10, 11, 12] ]

# # # # # # # # # # # # # # # # for i in range(1, len(lst)):
# # # # # # # # # # # # # # # #     for j in range(len(lst[i]) - 1):  # Correcting the dash
# # # # # # # # # # # # # # # #         temp = lst[i][j]
# # # # # # # # # # # # # # # #         lst[i][j] = lst[i-1][j+1] * 2
        
# # # # # # # # # # # # # # # #         if lst[i][j] % 5 == 0 and lst[i][j] < 30:
# # # # # # # # # # # # # # # #             lst[i][j] = "multiple5"

# # # # # # # # # # # # # # # # for row in lst:
# # # # # # # # # # # # # # # #     print(row)



# # # # # # # # # # # # # # # def count_frequences(nums):
# # # # # # # # # # # # # # #     freq = {}
# # # # # # # # # # # # # # #     for num in nums:
# # # # # # # # # # # # # # #         if num not in freq:
# # # # # # # # # # # # # # #             freq[num] = 1
# # # # # # # # # # # # # # #         else:
# # # # # # # # # # # # # # #             freq[num] += 1
# # # # # # # # # # # # # # #     return freq

# # # # # # # # # # # # # # # print(count_frequences([1,2,2,3,3,3,4]))


# # # # # # # # # # # # # # # def process_tuples(tup1, tup2):
# # # # # # # # # # # # # # #     result = []
# # # # # # # # # # # # # # #     for i in range(len(tup1)):
# # # # # # # # # # # # # # #         result.append(tup1[i] + tup2[i])
# # # # # # # # # # # # # # #     return tuple(result)

# # # # # # # # # # # # # # # t1 = (1, 2, 3)
# # # # # # # # # # # # # # # t2 = (4, 5, 6)
# # # # # # # # # # # # # # # output = process_tuples(t1, t2)
# # # # # # # # # # # # # # # print(output)




# # # # # # # # # # # # # # import pandas as pd
# # # # # # # # # # # # # # import numpy as np
# # # # # # # # # # # # # # import matplotlib.pyplot as plt
# # # # # # # # # # # # # # data = {'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
# # # # # # # # # # # # # #  'Math': [85, 92, 78, 88, 95],
# # # # # # # # # # # # # #  'Science': [90, 87, 82, 84, 91],
# # # # # # # # # # # # # #  'English': [88, 91, 79, 85, 92]} 
# # # # # # # # # # # # # # df = pd.DataFrame(data) 

# # # # # # # # # # # # # # df['Average'] = df[['Math', 'Science', 'English']].mean(axis=1).round()
# # # # # # # # # # # # # # plt.plot(df['Student'], df['Average'])
# # # # # # # # # # # # # # plt.xlabel('Student')
# # # # # # # # # # # # # # plt.ylabel('Average')
# # # # # # # # # # # # # # plt.show()
# # # # # # # # # # # # # # print(df)



# # # # # # # # # # # # # d1= {3: 4, 5: 6, 7: 8}
# # # # # # # # # # # # # for i in range(len(d1)):
# # # # # # # # # # # # #  d1[i+2] = i+5 
# # # # # # # # # # # # # print(d1)

# # # # # # # # # # # # def tupler(d):
# # # # # # # # # # # #     for i in d:
# # # # # # # # # # # #         if sum(d[i][1]) != d[i][0]:
# # # # # # # # # # # #             d[i]= (d[i][0], [d[i][0], 0])
# # # # # # # # # # # #     a = []
# # # # # # # # # # # #     for value in d.values():
# # # # # # # # # # # #         a.append(value[1])
# # # # # # # # # # # #     return sorted(a)
        
# # # # # # # # # # # # print(tupler( {1: (5, [2, 3]), 2: (4, [4, 5]), 3: (6, [1, 4])}))



# # # # # # # # # # # products = {'laptop': 800, 'phone': 600, 'tablet': 400, 'headphones': 150}
# # # # # # # # # # # discounts = {'laptop': 10, 'phone': 5, 'tablet': 20}
# # # # # # # # # # # for product in discounts ():
# # # # # # # # # # #     if product in products:
# # # # # # # # # # #         products[product] = products[product] * (1 - discount/100)


# # # # # # # # # # tuple = (10, 20, 30 , 40)
# # # # # # # # # # lst = list(tuple)
# # # # # # # # # # lst[1] = "“Hello”"
# # # # # # # # # # print(tuple)
# # # # # # # # # # print(lst) 


# # # # # # # # # import pandas as pd
# # # # # # # # # import matplotlib.pyplot as plt

# # # # # # # # # # Create the DataFrame with sales and expenses
# # # # # # # # # data = {
# # # # # # # # #     'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
# # # # # # # # #     'Sales': [1500, 1800, 1200, 2000, 2500, 2200],
# # # # # # # # #     'Expenses': [1200, 1300, 1100, 1500, 1600, 1400]
# # # # # # # # # }

# # # # # # # # # df = pd.DataFrame(data)
# # # # # # # # # df['Profit'] = df['Sales'] - df['Expenses']
# # # # # # # # # plt.plot(df['Month'], df['Profit'])
# # # # # # # # # plt.show()
# # # # # # # # # print(df['Month'][df['Profit'].idxmax()])

# # # # # # # # # Given list of tuples: (Month, Revenue, Items Sold)
# # # # # # # # data = [
# # # # # # # #     ('Jan', 1000, 500),
# # # # # # # #     ('Feb', 1200, 600),
# # # # # # # #     ('Mar', 800, 400),
# # # # # # # #     ('Apr', 1500, 700),
# # # # # # # #     ('May', 2000, 800),
# # # # # # # #     ('Jun', 1800, 750)
# # # # # # # # ]
# # # # # # # # max_revenue = 100000000
# # # # # # # # max_revenue_month = ""
# # # # # # # # for month, revenue, items in data:
# # # # # # # #     if revenue-items < max_revenue:
# # # # # # # #         max_revenue = revenue-items
# # # # # # # #         max_revenue_month = month
# # # # # # # # print(max_revenue_month, max_revenue)


# # # # # # # def lolipop_wrap(matrix):
# # # # # # #     result = []
    
# # # # # # #     if not matrix:
# # # # # # #         return result
    
# # # # # # #     top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
    
# # # # # # #     while top <= bottom and left <= right:
# # # # # # #         # Traverse from left to right along the top row
# # # # # # #         for i in range(left, right + 1):
# # # # # # #             result.append(matrix[top][i])
# # # # # # #         top += 1  # Move down the top boundary
        
# # # # # # #         # Traverse from top to bottom along the right column
# # # # # # #         for i in range(top, bottom + 1):
# # # # # # #             result.append(matrix[i][right])
# # # # # # #         right -= 1  # Move left the right boundary
        
# # # # # # #         if top <= bottom:
# # # # # # #             # Traverse from right to left along the bottom row
# # # # # # #             for i in range(right, left - 1, -1):
# # # # # # #                 result.append(matrix[bottom][i])
# # # # # # #             bottom -= 1  # Move up the bottom boundary
        
# # # # # # #         if left <= right:
# # # # # # #             # Traverse from bottom to top along the left column
# # # # # # #             for i in range(bottom, top - 1, -1):
# # # # # # #                 result.append(matrix[i][left])
# # # # # # #             left += 1  # Move right the left boundary
    
# # # # # # #     return result

# # # # # # # # Example usage:
# # # # # # # matrix = [
# # # # # # #     [1, 2, 3, 4],
# # # # # # #     [5, 6, 7, 8],
# # # # # # #     [9, 10, 11, 12]
# # # # # # # ]

# # # # # # # print(lolipop_wrap(matrix))

# # # # # # def al(n):
# # # # # #     return chr(65 + n)

# # # # # # k = {}
# # # # # # for i in range(26):
# # # # # #     k[i] = al(i)  # Assign a key-value pair where the key is 'i' and the value is the alphabet character corresponding to 'i'
# # # # # #     k[al(i)] = al(i + 1)  # Assign a key-value pair where the key is the alphabet letter corresponding to 'i' and the value is the next letter in the alphabet
# # # # # #     # print(k)
# # # # # #     if i > 0:
# # # # # #         k[i - 1] = al(i + 2)  # For 'i > 0', assign a new value to the key 'i - 1'
# # # # # #     # print(k)
# # # # # # print(k[12])  # Print the value of the key 12
# # # # # lst_of_keys = [3, None, "a", False, 16.0]
# # # # # lst = [[3, 5, 16], ["r", "i", "E", "c"], 145, "Computers", None, 1600.45, "yay!"]
# # # # # def listToDict(lst_of_keys, lst):
# # # # #     temp_dict = {}
# # # # #     for _ in range(len(lst_of_keys)):
# # # # #         temp_dict[lst_of_keys[_]] = lst[_]
# # # # #     return temp_dict

# # # # # print(listToDict(lst_of_keys, lst))

# # # # d = {'a': 10, 'b': 20, 'c': 30}
# # # # d['d'] = d.get('e', 40)
# # # # print(d)


# # # students = {
# # #     'Alice': [85, 90, 78],
# # #     'Bob': [92, 88, 95],
# # #     'Charlie': [70, 80, 65],
# # #     'David': [100, 98, 95]
# # # }

# # # highest_avg = 0
# # # top_student = ""
# # # for student, grades in students.items():
# # #     total = 0
# # #     for grade in grades:
# # #         total += grade
# # #     average = total / len(grades)
# # #     if average > highest_avg:
# # #         highest_avg = average
# # #         top_student = student

# # # print(f"The student with the highest average is {top_student} with an \
# # # average of {highest_avg}.")

# # butterflies = {
# #     "name": "Monarch",  # Fixed the missing comma
# #     "count": 10,
# #     "Location": ["forest", "lake"]
# # }

# # butterflies["count"] = butterflies.get("count", 0) + 1  # Increment the count by 1

# # if "colour" not in butterflies.keys():  # Fixed the if condition
# #     butterflies["colour"] = "orange"
# #     butterflies.get("Location", []).append("meadow")  # Append "meadow" to Location


# # for key in butterflies:  # Iterate through the dictionary
# #     print(f"{key}: {butterflies[key]}")  # Print the key and value


# lst = [1,2,3]
# letter = 'A'
# num1 = [42]
# num2 = 2
# letter.append('B')
# print(lst + letter) 



def transform_tuple(data):
 a, (b, c) = data
 b = list(b)
 for i in range(len(b)):
    b[i] += c[i]
 new_tuple = (sum(b) * a, tuple(b), c[::-1])
 return new_tuple
data = (3, ((4, 6, 8), (5, 7, 9)))
result = transform_tuple(data)
print(data)
print(result) 