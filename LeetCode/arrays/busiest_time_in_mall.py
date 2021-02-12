def find_busiest_period(data):
  max_ppl, left, result = 0, 0, 0

  while left < len(data):
    curr_ppl = max_ppl
    right = left
    while right < len(data) and data[left][0] == data[right][0]:
      if data[right][2] == 1:
        curr_ppl+=data[right][1]
      else:
        curr_ppl-=data[right][1]
      right+=1
    if curr_ppl > max_ppl:
      result = data[left][0]
    max_ppl = curr_ppl
    left = right

  return result