def recbinarySearch(lst, low, high, target):
    if low <= high:
        mid = (low+high)//2
        if lst[mid]==target:
            return mid
        elif lst[mid]<target:
            return recbinarySearch(lst, mid+1, high, target)
        else:
            return recbinarySearch(lst, low, mid-1, target)
        

        
print(recbinarySearch([1,2,3,4,5,6,7], 0, len([1,2,3,4,5,6,7])-1,5))