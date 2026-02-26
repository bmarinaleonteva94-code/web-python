numbers = [0,1,2,3,4,5,6,7,8,9,10]
arithmetic_mean = sum(numbers)/len(numbers)
res = [x for x in numbers if x>arithmetic_mean]
print(arithmetic_mean)
print(res)