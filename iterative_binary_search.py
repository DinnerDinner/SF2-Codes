def binary_search(lst,val):
    low = 0
    high = len(lst)-1
    mid = 0

    while low <= high:
        mid = (low+high)//2
        if lst[mid] < val:
            low = mid+1

        elif lst[mid] > val:
            high = mid

        else:
            return mid
    return "target not found"


print(binary_search([1,2,3,4,5,6,7], 5))



