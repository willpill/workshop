def sum67(nums):
  s = 0
  flag = False
  for n in nums:
    if n == 6:
      flag = True
    elif n == 7 and flag:
      flag = False
    elif not flag:
      s += n
  return s
