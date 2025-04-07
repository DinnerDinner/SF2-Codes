# Pranjwal Singh - 2436027

def toCelsius(temp):
    celsius = (temp - 32)*(5/9)
    return round(celsius, 2)

inputfile = open('data.txt', 'r')
temp_dict = {}
for line in inputfile:
    if line[0][0] == '1':
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
    averages = []
    keys = list(d1.keys())
    for key in keys:
        averages.append(avgTempYear(d1, key))
    
    for i in range(len(averages)):
        for j in range(len(averages)):
            if averages[i] > averages[j]:
                averages[i], averages[j] = averages[j], averages[i]
    return averages[:3]

def avgTempMonth(d1, month):
    month_dict = {'JAN':1, 'FEB':2, 'MAR':3, 'APR':4, 'MAY':5, 'JUN':6, 'JUL':7, 'AUG':8, 'SEP':9, 'OCT':10, 'NOV':11, 'DEC':12}
    total_month = []
    for year in d1:
        total_month.append(d1[year][month_dict[month]-1])
    return round(sum(total_month)/len(total_month), 2)

print(avgTempMonth(temp_dict, 'JAN'))
inputfile.close()