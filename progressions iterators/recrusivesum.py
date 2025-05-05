def iterSum(n):
    total =0
    for i in range(n):
        total+=i
    return total

# print(iterSum(12))
def recSum(n):
    if n ==1:
        return 1
    else:
        return recSum(n-1)+n