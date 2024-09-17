def array_count9(nums):
  c = 0
  for i in range(len(nums)):
    if(nums[i] == 9):
      c += 1
  return c