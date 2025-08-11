
def quicksort (arr):
    length = len(arr)

    if length <= 1:
        return arr
    else:
        pivot = arr.pop()
    
    items_greater = []
    items_lower = [] 
    for item in arr:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quicksort(items_lower) + [pivot] + quicksort(items_greater)


result = quicksort([2,9,5,3,3])
print(result)