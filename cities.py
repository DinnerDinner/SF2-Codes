num  = int(input("> "))
input_file = open('cities.txt', 'a')
cities = []
for i in range(num):
    user = input("city: ").split()
    add = (f"{(user[0][:2], user[1])}")
    input_file.write(add +"\n")
input_file.close()

readable_file = open('cities.txt', 'r')
all = [x for x in readable_file]
cities_d = {}
for x in all: 
    x.rstrip()
    print(x)
    actual = eval(x)
    special = (actual[1], actual[0])
    print(special)
    if actual not in cities_d:
        cities_d[actual] = 0
        # a = all.remove(x)
        print(cities_d)
        for i in all:
            i.rsplit()
            actuali = eval(i)
            if actuali == special:
                print(True)
                cities_d[actual]+=1
                # b = all.remove(i)
                print(x)
    



print(cities_d)

readable_file.close()

