villages = int(input("Village count: "))
points=[]
for x in range(villages): 
    point = int(input("Point: "))
    points.append(point)
points = sorted(points)
sizes = []
for x in range(1, villages-1):
    size = ((points[x]-points[x-1])+(points[x+1]-points[x]))/2
    sizes.append(size)

print(min(sizes)) 