streamAmount = int(input())
flows = []
for x in range(streamAmount): 
    flows.append(int(input()))

# flag=True
while True: 
    ask = int(input())
    if ask == 99: 
        stream = int(input())-1
        amount = int(input())/100
        flows.insert(stream+1, flows[stream]*amount)
        flows[stream] = (1-amount)*flows[stream]
    if ask == 88: 
        stream = int(input())-1
        flows[stream] = flows[stream]+flows[stream+1]
        flows.pop(stream+1)
    if ask == 77:
        break

print(" ".join(map(str, map(int, flows))))