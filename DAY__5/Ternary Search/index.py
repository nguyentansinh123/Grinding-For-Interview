
def tenarySearchAlgorithm(array, target):
    return tenarySearch(array, 0 , len(array) - 1, target)

def tenarySearch(array, l , r, target):

    while l <= r:
        mid1 = l + (r - l) // 3
        mid2 = r - (r-l) // 3

        if target == array[mid1]:
            return mid1
        if target == array[mid2]:
            return mid2
        
        if target < array[mid1]:
            r = mid1 - 1
        elif target > array[mid2]:
            l = mid2 + 1
        
        else:
            l = mid1 + 1
            r = mid2 - 1
    return -1

sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
target_to_find = 12
index = tenarySearchAlgorithm(sorted_array, target_to_find)
print(index)