def reverse3(nums):
  a = []
  for i in range(1, len(nums) + 1):
    a.append(nums[-1 * i])

  return a