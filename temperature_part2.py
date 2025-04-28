<<<<<<< HEAD
# Pranjwal Singh - 2436027

def toCelsius(temp):
    celsius = (temp - 32)*(5/9)
    return round(celsius, 2)

inputfile = open('data.txt', 'r')
temp_dict = {}
for line in inputfile:
    if line[0][0] == '1': # you said ok
        line = line.strip().split()
        values = list(map(float, line[1:]))
        temp_dict[int(line[0])] = list(map(toCelsius, values))

def avgTempYear(d1, year):
    try: 
        yearly = d1[year]
    except KeyError:
        print(f"The {year} isn't part of the given dictionary")
    else:
        values = sum(yearly)
        return round(values/len(yearly), 2)

def topThreeYears(d1):
    averages = set()
    keys = list(d1.keys())
    for key in keys:
        averages.add(avgTempYear(d1, key))

    topthree = []
    for i in range(3):
        topthree.append(max(averages))
        averages.remove(max(averages))
    return topthree

def avgTempMonth(d1, month):
    month_dict = {'JAN':1, 'FEB':2, 'MAR':3, 'APR':4, 'MAY':5, 'JUN':6, 'JUL':7, 'AUG':8, 'SEP':9, 'OCT':10, 'NOV':11, 'DEC':12}
    total_month = []
    for year in d1:
        total_month.append(d1[year][month_dict[month]-1])
    return round(sum(total_month)/len(total_month), 2)

def belowFreezing(d1):
    months = set()
    month_dict_inverted = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    for year in d1:
        for i in d1[year]:
            if i < 0:
                months.add(month_dict_inverted[d1[year].index(i)+1])
    return months
# print(avgTempMonth(temp_dict, 'JAN'))
# print(topThreeYears(temp_dict))
print(belowFreezing(temp_dict))


outputfile = open('data_celsius.txt', 'w')
inputfile = open('data.txt', 'r')

for line in inputfile:
    line = line.rstrip()  
    if line and line[0] == '1':
        pass
    else:  
        outputfile.write(line + '\n')  

for year in temp_dict:
    line = ""
    line += str(year)
    for i in temp_dict[year]:
        if len(str(i))<6:
            num = 6-len(str(i))
            i = str(i)+' '*num
        line += '\t' + str(i)
    outputfile.write(line + '\n') 


outputfile.close()
inputfile.close()
=======
# Pranjwal Singh - 2436027

def toCelsius(temp):
    celsius = (temp - 32)*(5/9)
    return round(celsius, 2)

inputfile = open('data.txt', 'r')
temp_dict = {}
for line in inputfile:
    if line[0][0] == '1': # you said ok
        line = line.strip().split()
        values = list(map(float, line[1:]))
        temp_dict[int(line[0])] = list(map(toCelsius, values))

def avgTempYear(d1, year):
    try: 
        yearly = d1[year]
    except KeyError:
        print(f"The {year} isn't part of the given dictionary")
    else:
        values = sum(yearly)
        return round(values/len(yearly), 2)

def topThreeYears(d1):
    averages = set()
    keys = list(d1.keys())
    for key in keys:
        averages.add(avgTempYear(d1, key))

    topthree = []
    for i in range(3):
        topthree.append(max(averages))
        averages.remove(max(averages))
    return topthree

def avgTempMonth(d1, month):
    month_dict = {'JAN':1, 'FEB':2, 'MAR':3, 'APR':4, 'MAY':5, 'JUN':6, 'JUL':7, 'AUG':8, 'SEP':9, 'OCT':10, 'NOV':11, 'DEC':12}
    total_month = []
    for year in d1:
        total_month.append(d1[year][month_dict[month]-1])
    return round(sum(total_month)/len(total_month), 2)

def belowFreezing(d1):
    months = set()
    month_dict_inverted = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    for year in d1:
        for i in d1[year]:
            if i < 0:
                months.add(month_dict_inverted[d1[year].index(i)+1])
    return months
# print(avgTempMonth(temp_dict, 'JAN'))
# print(topThreeYears(temp_dict))
# print(belowFreezing(temp_dict))


outputfile = open('data_celsius.txt', 'w')
inputfile = open('data.txt', 'r')

for line in inputfile:
    line = line.rstrip()  
    if line and line[0] == '1':
        pass
    else:  
        outputfile.write(line + '\n')  

for year in temp_dict:
    line = ""
    line += str(year)
    for i in temp_dict[year]:
        if len(str(i))<6:
            num = 6-len(str(i))
            i = str(i)+' '*num
        line += '\t' + str(i)
    outputfile.write(line + '\n') 


outputfile.close()
inputfile.close()
>>>>>>> 5416a5ff9784afd7c31c06bfb94906255d6a1b53
