# grades = open("grades.txt", "r")
# students  = []
# for line in grades:
#     data = line.strip().split(',')
#     student = {
#         'firstname': data[0],
#         'lastname': data[1],
#         'exam1grade': float(data[2]),
#         'exam2grade': float(data[3]),
#         'exam3grade': float(data[4])
#         }
        
#     students.append(student)

# for student in students:
#     exams = [student['exam1grade'], student['exam2grade'], student['exam3grade']]
#     print(min(exams))


# grades.close()



# # input_file = open('grades.txt', 'w')
# # for _ in range(10):
# #     student_info = input("Enter student information (firstname, lastname, exam1grade, exam2grade, exam3grade): ")
# #     input_file.write(student_info + "\n")
        
# # input_file.close()

# # students = []

# # file = open("grades.txt", "r") 

# # for line in file:
# #     data = line.strip().split(',')

# #     student = {
# #         'firstname': data[0],
# #         'lastname': data[1],
# #         'exam1grade': float(data[2]),
# #         'exam2grade': float(data[3]),
# #         'exam3grade': float(data[4])
# #         }
        
# #     students.append(student)


# (a) Read story file
with open("story.txt", "r") as f:
    story = f.read()

# (a) Print story
print("STORY:\n")
print(story)

# (b) Total number of words
words = story.lower().split()
print("\nTotal words:", len(words))

# (c) Frequency
word_freq = {}
for word in words:
    word = word.strip(".,!?;:-()[]{}\"'")  # Clean punctuation
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# Sort by frequency (highest to lowest)
sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

# Print results
print("\nWord Frequencies:")
for word, freq in sorted_words:
    print(f"{word}: {freq}")



#_------------------




# (a) With error messages
filenames = ["cats.txt", "dogs.txt"]
for file in filenames:
    try:
        f = open(file, 'r')
        print(f"\nContents of {file}:")
        for line in f:
            print(line)
    except FileNotFoundError:
        print(f"Oops! Could not find the file: {file}")

# (b) Fail silently
for file in filenames:
    try:
        with open(file, "r") as f:
            print(f"\nContents of {file}:")
            print(f.read())
    except FileNotFoundError:
        pass  # Fail silently



# -------------------

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    total = num1 + num2
    print("Result:", total)
except ValueError:
    print("ERROR: Please enter valid numbers only.")





# -------------


import json

# Sample student data
gradebook_dict = {
    "students": [
        {
            "first_name": "Alice",
            "last_name": "Smith",
            "exam1": 85,
            "exam2": 90,
            "exam3": 80
        },
        {
            "first_name": "Bob",
            "last_name": "Johnson",
            "exam1": 78,
            "exam2": 88,
            "exam3": 82
        },
        {
            "first_name": "Charlie",
            "last_name": "Lee",
            "exam1": 92,
            "exam2": 89,
            "exam3": 95
        }
    ]
}

# Write to JSON
with open("grades.json", "w") as f:
    json.dump(gradebook_dict, f, indent=4)


# ---------------


import json

# Read grades.json
with open("grades.json", "r") as f:
    data = json.load(f)

students = data["students"]

# Print header
print("{:<10} {:<10} {:<7} {:<7} {:<7} {:<7}".format(
    "First", "Last", "Exam1", "Exam2", "Exam3", "Average"
))

# Store sums for class average
sum1 = sum2 = sum3 = 0

# Print each student and compute individual average
for s in students:
    avg = (s["exam1"] + s["exam2"] + s["exam3"]) / 3
    sum1 += s["exam1"]
    sum2 += s["exam2"]
    sum3 += s["exam3"]
    print("{:<10} {:<10} {:<7} {:<7} {:<7} {:.2f}".format(
        s["first_name"], s["last_name"],
        s["exam1"], s["exam2"], s["exam3"], avg
    ))

# Class averages
count = len(students)
print("\nClass Averages:")
print(f"Exam1: {sum1 / count:.2f}")
print(f"Exam2: {sum2 / count:.2f}")
print(f"Exam3: {sum3 / count:.2f}")
# ----------------------
