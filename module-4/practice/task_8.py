def flat(nested_arr):
    new_list = []
    for item in nested_arr:
        for item_child in item:
            new_list.append(item_child)
    return new_list


print(flat([[1,2,3], [4,5], [6]]))