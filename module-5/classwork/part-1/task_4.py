# сортировка слияния
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left_part = merge_sort(arr[:mid])
    right_part = merge_sort(arr[mid:])
    return merge(left_part, right_part)

def merge(left_part, right_part):
    i = 0
    j = 0
    result = []
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            result.append(left_part[i])
            i += 1
        else:
            result.append(right_part[j])
            j +=1
    result.extend(left_part[i:])
    result.extend(right_part[j:])
    return result
print(merge_sort([3,4,5,0,-7,-4,2]))