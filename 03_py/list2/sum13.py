def sum13(nums):
  sum = 0
  i = 0
  while i < len(nums):
    if nums[i] != 13:
      sum += nums[i]
      i += 1
    else:
      i += 2
  return sum
