# # # # # def endsWith(C, F):
# # # # #     try:
# # # # #         file = open(F, "r")
# # # # #     except FileNotFoundError:
# # # # #         return None
# # # # #     else: 
# # # # #         words = []
# # # # #         good = []
# # # # #         for line in file:
# # # # #             line = line.rstrip().split()
# # # # #             for word in line:
# # # # #                 words.append(word)
# # # # #         for word in words:
# # # # #             if word[-1] == C:
# # # # #                 good.append(word)
# # # # #         return list(set(good))
    

# # # # # print(endsWith("n", "words.txt"))


# # # # from __future__ import annotations
# # # # class Car:
# # # #     def __init__(self, brand="Toyota", year=2025, fuel=100):
# # # #         self.brand = brand
# # # #         self.year = year
# # # #         self.fuel = fuel

# # # #     def __repr__(self):
# # # #         return (f"The {self.brand} car, made in {self.year}, has a current fuel of {self.fuel}!")
    
# # # #     def refuel(self, newfuel:int):
# # # #         try:
# # # #             newfuel = int(newfuel)
# # # #         except ValueError:
# # # #             return("Enter an int for the refuel value")
# # # #         else:
# # # #             if self.fuel+newfuel<=100:
# # # #                 self.fuel+=newfuel
    
# # # #     def drive(self, d:int):
# # # #         if self.fuel-d>=0:
# # # #             self.fuel-=d
# # # #             return (self.fuel, d)
# # # #     def __lt__(self, other_year):
# # # #         try:
# # # #             self.year = int(self.year)
# # # #             other_year.year = int(other_year.year)
# # # #         except ValueError:
# # # #             print("Input integers")

# # # #         else:
# # # #             return isinstance(other_year, Car) and self.year<other_year.year
        

# # # # car1 = Car()
# # # # car2 = Car("Mazda", 2020, 90)
# # # # car2.drive(10)
# # # # print(f"{car1<car2}")
# # # # car2.refuel(11)
# # # # print(car1)
# # # # print(car2)


# # # d = {'a':{'b':{'c':42}}}

# # # d['a']['b']['c'] = set('Hello')

# # # print(d)



# # def compare(n):

# #     return len(n) != len(set(n))

# # print(compare([1, 2, 3, 4]))

# # print(compare([1, 2, 2, 3]))











# data = {

# "students": {

# "Alice": {"Math", "English"},

# "Bob": {"Math", "History"},

# "Charlie": {"History", "English"}

# }

# }


# data["students"]["Bob"].add("Science")


# data["students"]["Alice"].discard("English")


# all_subjects = set()

# for subjects in data["students"].values():

#     all_subjects.update(subjects)

# print(all_subjects)

# print(len(all_subjects))






























from __future__ import annotations
class person_info:
    def __init__(self, lst=["John", "Doe", 0]):
        self.f_name = lst[0]
        self.l_name = lst[1]
        self.money = int(lst[2])

    def add(self, money):
        self.money+=money
    def remove(self, money):
        self.money-=money
    def changename(self, name):
        try:
            name = str(name)
        except ValueError:
            print("str please as s name")
        else:
            name = name.split()
            self.f_name = name[0]
            self.l_name = name[1]

    def __repr__(self):
        return(f"first: {self.f_name}, last: {self.l_name}, money: {self.money}")

    def __lt__(self, other):
        return isinstance(other, person_info) and self.money<other.money
    

name1 = person_info()
name2 = person_info(["amy", "young", 12])
print(name2<name1)