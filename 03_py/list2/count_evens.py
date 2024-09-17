def count_evens(nums):
    c = 0
    for num in nums:
        if num % 2 == 0:
            c += 1
    return c