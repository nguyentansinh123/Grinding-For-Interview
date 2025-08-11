

def quicksort(arr, right, left):
    if left <= right:
        pat_pos = partition(arr,left, right)
        quicksort(arr, pat_pos + 1, right)
        quicksort(arr, left, pat_pos - 1)

def partition (arr,left,right):

    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i +=1 

        while j > left and arr[j] >= pivot:

            j-= 1

        arr[i], arr[j] = arr[j], arr[i] 

    if arr[i] > pivot:
        arr[i], pivot = pivot, arr[i]
    return i           

arr = [22, 11, 88, 66, 55, 33, 44]
quicksort(arr, 0 , len(arr) - 1)
print(arr)