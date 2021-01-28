# Given an m x n matrix, return all elements of the matrix in spiral order.

 

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:


# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

def spiral_copy(inputMatrix):
  TR, BR, = 0, len(inputMatrix)-1
  LC, RC = 0, len(inputMatrix[0])-1
  ans = []
  while TR <= BR and LC <= RC:
      for col in range(LC, RC):
        ans.append(inputMatrix[TR][col])

      for row in range(TR, BR):
        ans.append(inputMatrix[row][RC])

      if TR == BR:
        ans.append(inputMatrix[TR][RC])
        BR+=1
        TR-=1
        break

      for col in range(RC, LC, -1):
        ans.append(inputMatrix[BR][col])

      for row in range(BR, TR, -1):
        ans.append(inputMatrix[row][LC])

      LC+=1
      RC-=1
      TR+=1
      BR-=1

  return ans
