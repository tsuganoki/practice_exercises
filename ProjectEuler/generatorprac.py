def firstn(n):
    num = 0
    nums = []
    while num < n:
        nums.append(num)
        num += 1
    return nums

print(firstn(20))
