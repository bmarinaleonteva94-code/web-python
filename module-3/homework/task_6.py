numbers_1 = [33,4,5,11,2,-3,-6,0,43,33,1]
numbers_2 = [5,7,33,5,1,-6,-8,0,9,44,6,21]

numbers_3 = numbers_1 + numbers_2

combined_no_dublicates = []
for item in numbers_3:
    if item not in combined_no_dublicates:
        combined_no_dublicates.append(item)

common_elements = []
for item in numbers_1:
    if item in numbers_2:             #переделать
        common_elements.append(item)

set1, set2 = set(numbers_1), set(numbers_2)
unique_elements = []
for item in numbers_1:
    if item not in set2 and item not in unique_elements:
        unique_elements.append(item)
for item in numbers_2:
    if item not in set1 and item not in unique_elements:
        unique_elements.append(item)

max_min_list = [
    min(numbers_1), max(numbers_1), min(numbers_2), max(numbers_2)
]

print(numbers_3)
print(combined_no_dublicates)
print(common_elements)
print(unique_elements)
print(max_min_list)