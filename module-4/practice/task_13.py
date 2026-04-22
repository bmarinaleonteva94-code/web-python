import random
nums = [random.randint(-50, 50) for _ in range(100)]

def min_interval_pos(i, best_poz=0, best_sum=None):
    if i+10 >len(nums):
        return best_poz
    summ = sum(nums[i:i+10])
    if best_sum == None or summ < best_sum:
        best_sum = summ
        best_poz = i
    return min_interval_pos(i+1, best_poz, best_sum)

best_poz = min_interval_pos(0)
print(f"Последовательность с минимальной суммой: {nums[best_poz: best_poz + 10]}")
print(nums)