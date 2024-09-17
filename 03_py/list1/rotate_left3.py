def rotate_left3(nums):
  a=[]
  for i in range(1,len(nums)):
    a.append(nums[i])
  a.append(nums[0])
  return a