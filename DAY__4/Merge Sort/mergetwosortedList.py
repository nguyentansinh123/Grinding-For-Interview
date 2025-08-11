
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        left_arr = arr[:len(arr) // 2]
        right_arr = arr[len(arr) // 2 :]

        left = merge_sort(left_arr)
        right = merge_sort(right_arr)

        return merge_two_sorted_list(left, right)


def merge_two_sorted_list(a,b):
    sorted_list = []

    len_a = len(a)
    len_b = len(b)
    i ,j = 0, 0

    while i < len_a and j < len_b:
        if a[i] < b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1

    while i < len_a:
        sorted_list.append(a[i])
        i +=1
    
    while j < len_b:
        sorted_list.append(b[j])
        j +=1

    return sorted_list


arr = [10,3,15,7,8,23,98,29] 
result = merge_sort(arr)
print(result)