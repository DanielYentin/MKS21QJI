def sum67(nums):
  sum = 0
  if len(nums) > 0:
    found6 = False
    for i in nums:
      if not found6:
        if i != 6:
          sum += i
        else:
          found6 = True
      else:
        if i == 7:
          found6 = False
  return sum

