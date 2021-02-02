from collections import defaultdict
def taskAssignment(k, tasks):
    ans, left, right = [], 0, len(tasks)-1
    indecies = defaultdict(list)
    for i in range(len(tasks)):
      indecies[tasks[i]].append(i)
    tasks.sort()

    while left < right:
      left_index = indecies[tasks[left]].pop()
      right_index = indecies[tasks[right]].pop()
      ans.append([left_index, right_index])
      left+=1
      right-=1
      
    return ans
