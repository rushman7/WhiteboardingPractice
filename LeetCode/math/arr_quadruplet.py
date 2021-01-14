# Array Quadruplet
# Given an unsorted array of integers arr and a number s, write a function findArrayQuadruplet that finds four numbers (quadruplet) in arr that sum up to s. Your function should return an array of these numbers in an ascending order. If such a quadruplet doesn’t exist, return an empty array.

# Note that there may be more than one quadruplet in arr whose sum is s. You’re asked to return the first one you encounter (considering the results are sorted).

# Explain and code the most efficient solution possible, and analyze its time and space complexities.

# Example:

# input:  arr = [2, 7, 4, 0, 9, 5, 1, 3], s = 20

# output: [0, 4, 7, 9]

from collections import defaultdict

def find_array_quadruplet(arr, s):
  hash_map = defaultdict(tuple)
  arr.sort()
  ans = []
  
  for i in range(len(arr)):
    for j in range(i+1, len(arr)):
      hash_map[s-(arr[j]+arr[i])] = (i, j)
  
  for i in range(len(arr)):
    for j in range(i+1, len(arr)):
      pair = arr[i] + arr[j]
      if pair in hash_map:
        p_i, p_j = hash_map[pair]
        
        if (i != p_i and i != p_j) and (j != p_i and j != p_j):
          ans = [arr[i],arr[j], arr[p_i], arr[p_j]]
          ans.sort()
          return ans
        
  return ans