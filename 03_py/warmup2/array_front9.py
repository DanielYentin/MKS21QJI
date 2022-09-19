def last2(str):
  if len(str)<2:
    return 0
  count=0
  last = str[len(str)-2:]
  for inc in range(len(str)-2):
    if str[inc:inc+2]==last:
        count+=1
  return count
