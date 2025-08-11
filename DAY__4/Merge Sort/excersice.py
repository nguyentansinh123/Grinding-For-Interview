# https://github.com/codebasics/data-structures-algorithms-python/blob/master/algorithms/5_MergeSort/merge_sort_exercise.md

def merge_sort (arr, key):

    if len(arr) <= 1:
        return arr
    
    left_arr = arr[:len(arr) // 2]
    right_arr = arr[len(arr) // 2:]

    left = merge_sort(left_arr, key)
    right = merge_sort(right_arr, key)

    return merge_two_sort_arr(left,right, key)

def merge_two_sort_arr (a,b, key):
    merge_arr = []
    i = 0 
    j = 0 

    while i < len(a) and j < len(b):
        if a[i][key] < b[j][key]:
            merge_arr.append(a[i])
            i+=1
        else:
            merge_arr.append(b[j])
            j+=1

    while i < len(a):
        merge_arr.append(a[i])
        i+=1
    while j < len(b):
        merge_arr.append(b[j])
        j+=1 

    return merge_arr

result = merge_sort([
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ], "age")

print(result)