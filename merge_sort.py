# # # def recmergeSort(lst):
# # #     if len(lst)==1:
# # #         return lst
    
# # #     mid = len(lst)//2
# # #     left_half = lst[:mid]
# # #     right_half = lst[mid:]

# # #     sorted_left = recmergeSort(left_half)
# # #     sorted_right = recmergeSort(right_half)

# # #     return merge(sorted_left, sorted_right)

# # # def merge(left, right):
# # #     result = []
# # #     i = j=0
# # #     while i < len(left) and j < len(right):
# # #         if left[i] < right[j]:
# # #             result.append(left[i])
# # #             i +=1

# # #         else:
# # #             result.append(left[j])
# # #             j+=1

# # #     result.extend(right[j:])
# # #     result.extend(left[i:])


# # #     return result















# # def quickSort(lst, low, high):
# #     if low < high:
# #         print(lst)
# #         pivot_index = part(lst, low, high)
# #         quickSort(lst, low, pivot_index - 1)
# #         quickSort(lst, pivot_index + 1, high)

# # def part(lst, low, high):
# #     pivot = lst[high]  
# #     print(pivot)
# #     i = low - 1        

# #     for j in range(low, high):
# #         if lst[j] < pivot:
# #             print(lst[j])
# #             i += 1
# #             # print(lst[i])
# #             lst[i], lst[j] = lst[j], lst[i] 
# #             print(lst)

# #     lst[i + 1], lst[high] = lst[high], lst[i + 1]
# #     return i + 1

# # arr = [5, 3, 8, 4, 2]
# # quickSort(arr, 0, len(arr)-1)
# # print(arr)


# def quick_sort(arr, low, high):
#     if low < high:
#         pivot_index = partition(arr, low, high)
#         quick_sort(arr, low, pivot_index - 1) #left from 0 to piv 
#         quick_sort(arr, pivot_index + 1, high)
#     return arr

# def partition(arr, low, high):
#     pivot = arr[low]
#     i = low+1
#     for j in range(i, high+1):
#         if arr[j]<=pivot:
#             arr[i], arr[j] = arr[j], arr[i]
#             i+=1
#     arr[low], arr[i-1] = arr[i-1], arr[low]
#     return i-1

# arr = [5, 3, 8, 4, 2]
# print(quick_sort(arr, 0, len(arr)-1))


def build_ruler(n):
    if n == 0:
        return []
    return build_ruler(n - 1) + [n] + build_ruler(n - 1)

def full_ruler(inches, major_tick):
    result = []
    for i in range(inches + 1):
        if i > 0:
            result += build_ruler(major_tick)
        result.append(major_tick)
    return result

print(full_ruler(2,5))
a = full_ruler(2, 3)
for i in a:
    print(i*"-")


