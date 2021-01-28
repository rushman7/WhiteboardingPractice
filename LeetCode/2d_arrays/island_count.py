def get_number_of_islands(binaryMatrix):
  island_count = 0
  
  def helper(i,j):
    binaryMatrix[i][j] = 0

    if i > 0 and binaryMatrix[i-1][j] == 1:
      helper(i-1,j)
    if i < len(binaryMatrix)-1 and binaryMatrix[i+1][j] == 1:
      helper(i+1,j)  
    if j > 0 and binaryMatrix[i][j-1] == 1:
      helper(i,j-1)  
    if j < len(binaryMatrix[0])-1 and binaryMatrix[i][j+1] == 1:
      helper(i,j+1) 

  
  for i in range(len(binaryMatrix)):
    for j in range(len(binaryMatrix[0])):
      if binaryMatrix[i][j] == 1:
        island_count+=1
        helper(i,j)
        
  return island_count
