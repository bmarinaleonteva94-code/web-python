#  алгоритм быстрой сортировки
#  берем опорный элемент и ищем элементы, которые больше него и меньше него
#  в результате образуется список из элементов меньше, опорного элемента и элементов больше

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [ i for i in arr[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)
print(quick_sort([1,4,5,3,2,-8]))