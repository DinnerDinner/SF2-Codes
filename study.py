# # # # # # # inputfile = open('words.txt', 'r')
# # # # # # # x= 0
# # # # # # # outputfile = open('words_updated.txt', 'w')
# # # # # # # for line in inputfile:
# # # # # # #     line = line.strip()
# # # # # # #     if line and line == line[::-1]:
# # # # # # #         outputfile.write(line+'\n')
# # # # # # #     elif line==line[::-1] and not line:
# # # # # # #         x+=1
# # # # # # # outputfile.close()
# # # # # # # inputfile.close()
# # # # # # # print(x)


# # # # # # print('You are to enter two numebers, which I will divide for you ')
# # # # # # print('Enter \'q\' anytime to quit.')
# # # # # # while True:
# # # # # #     n = input("1> ")
# # # # # #     if n == "q":
# # # # # #         break
# # # # # #     m = input("2> ")
# # # # # #     if m == "q":
# # # # # #         break

# # # # # #     try: 
# # # # # #         result = int(n)/int(m)
# # # # # #     except ValueError:
# # # # # #         print("enter an integer")
# # # # # #     except ZeroDivisionError:
# # # # # #         print("cant divide by 0")
# # # # # #     else:
# # # # # #         print(F" Result : {result}")
# # # # # #     finally:
# # # # # #         print('FFJFJFJFJ')

# # # # # import json

# # # # # # convert from JSON to Python
# # # # # student_record = '{"name": "Lucy", "year": 1, "college": "Dawson"}' # some .json file
# # # # # parsed_record = json.loads(student_record)
# # # # # print(parsed_record) # prints a dictionnary (notice the single quotations)

# # # # # # convert from Python to JSON
# # # # # student_dict = {'name': 'Lucy', 'year': 1, 'college': 'Dawson'} # some dictionnary
# # # # # student_record_json = json.dumps(student_dict)
# # # # # print(student_record_json) # prints json file (with the double quotations)

# # # # # print('\n\n')
# # # # # print(json.dumps({'name': 'Lucy', 'year': 1})) # dict -> JSON object
# # # # # print(json.dumps(['red', 'green', 'blue', 1])) # list -> array
# # # # # print(json.dumps(('apple', [1, 2, 3]))) # tuple -> array
# # # # # print(json.dumps('hello world')) # string -> string
# # # # # print(json.dumps(12)) # int -> number
# # # # # print(json.dumps(12.02)) # float -> number
# # # # # print(json.dumps(True)) # True -> true
# # # # # print(json.dumps(False)) # False -> false
# # # # # print(json.dumps(None)) # None -> null




# # # # lines= open('book.txt', 'r')
# # # # freq = {}
# # # # for line in lines:
# # # #     line = line.rstrip().split()
# # # #     for word in line:
# # # #         if word not in freq:
# # # #             freq[word] = 1
# # # #         else:
# # # #             freq[word]+=1
    
# # # # for w in sorted(freq, key=freq.get, reverse=True):
# # # #     print(w, freq[w])
# # # #     break
    





# # # import json

# # # # Sample student data
# # # student1 = {
# # #     'first_name': 'Alice',
# # #     'last_name': 'Smith',
# # #     'exam1': 85,
# # #     'exam2': 90,
# # #     'exam3': 78
# # # }

# # # student2 = {
# # #     'first_name': 'Bob',
# # #     'last_name': 'Johnson',
# # #     'exam1': 92,
# # #     'exam2': 88,
# # #     'exam3': 84
# # # }

# # # student3 = {
# # #     'first_name': 'Charlie',
# # #     'last_name': 'Brown',
# # #     'exam1': 76,
# # #     'exam2': 81,
# # #     'exam3': 69
# # # }

# # # # Create the gradebook dictionary
# # # gradebook_dict = {
# # #     'students': [student1, student2, student3]
# # # }

# # # # Open the file and write JSON data without using 'with'
# # # json_file = open('grades.json', 'w')
# # # json.dump(gradebook_dict, json_file, indent=4)
# # # json_file.close()

# # # print("Student data has been written to grades.json")

# # # import json

# # # # Open the grades.json file and load the data
# # # file = open('grades.json', 'r')
# # # gradebook_dict = json.load(file)
# # # file.close()

# # # # Extract student list
# # # students = gradebook_dict['students']

# # # # Header for the table
# # # print(f"{'First Name':<12} {'Last Name':<12} {'Exam1':<8} {'Exam2':<8} {'Exam3':<8} {'Average':<8}")

# # # # Variables to hold totals for class averages
# # # total_exam1 = 0
# # # total_exam2 = 0
# # # total_exam3 = 0
# # # num_students = len(students)

# # # # Print each student's data with average
# # # for student in students:
# # #     exam1 = student['exam1']
# # #     exam2 = student['exam2']
# # #     exam3 = student['exam3']
# # #     avg = (exam1 + exam2 + exam3) / 3

# # #     print(f"{student['first_name']:<12} {student['last_name']:<12} {exam1:<8} {exam2:<8} {exam3:<8} {avg:<8.2f}")

# # #     # Add to totals
# # #     total_exam1 += exam1
# # #     total_exam2 += exam2
# # #     total_exam3 += exam3

# # # # Calculate class averages
# # # class_avg1 = total_exam1 / num_students
# # # class_avg2 = total_exam2 / num_students
# # # class_avg3 = total_exam3 / num_students

# # # # Print class averages row
# # # print(f"{'CLASS AVG':<24} {class_avg1:<8.2f} {class_avg2:<8.2f} {class_avg3:<8.2f}")














# # from __future__ import annotations
# # class Amount:
# #     def __init__(self, gold):
# #         self.gold = gold
# #     def addGold(self, amount):
# #         self.gold+= amount
# #     def zeroGold(self):
# #         self.gold = 0
# #     def doubleGold(self):
# #         self.gold = self.gold*2
# #     def __lt__(self, other):
# #         return isinstance(other, Amount) and self.gold < other.gold
    
# #     def __eq__(self, other):
# #         return isinstance(other,Amount) and self.gold == other.gold
    
# # a1 = Amount(4)
# # a2 = Amount(43)
# # a3 = Amount(13221)
# # a4  = Amount(12)
# # value = 500
# # print(a4<a3)


# class Point:
#     def __init__(self):
#         self.x = 0
#         self.y = 0

# p1 = Point()
# print(f"{p1.x}, {p1.y}")

import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def translate(self, dx, dy):
        self.x +=dx
        self.y+=dy
    def distance(self, other_point):
        a  = (other_point.x-self.x) ** 2
        b = (other_point.y-self.y)**2
        return math.sqrt(a+b)
    def __repr__(self):
        return f"{self.x}, {self.y}"

    def __lt__(self, other_point):
        return isinstance(other_point, Point) and self.x< other_point.x and self.y < other_point.y
    
p1 = Point(2,3)
print(f'{p1.x}, {p1.y}')
p1.translate(2, 4)
print(f'{p1.x}, {p1.y}')
p2 = Point(4,4)
print(p1.distance(p2))
print(p1.__repr__())
print(p1.__lt__(p2))
print(p1<p2)