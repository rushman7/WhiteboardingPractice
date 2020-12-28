# Given an m x n matrix, return all elements of the matrix in spiral order.

 

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:


# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    r = c = r_start = c_start = 0
    r_end = len(matrix)-1
    c_end = len(matrix[0])-1
    direction = 'r'
    ans = []
    while True:
        # l -> r
        if c <= c_end and direction == 'r':
            ans.append(matrix[r][c])
            # if we reached end col, complete row by incr r_start,
            # move our r pointer down 1 and change direction
            if c == c_end:
                r_start+=1
                r+=1
                direction = 'd'
            else:
                c+=1
        # t -> b
        elif r <= r_end and direction == 'd':
            # if we reached end row, complete col by decr c_end,
            # move our c pointer left 1 and change direction
            ans.append(matrix[r][c])
            if r == r_end:
                c_end-=1
                c-=1
                direction = 'l'
            else:
                r+=1
        # r -> l
        elif c >= c_start and direction == 'l':
            # if we reached start col, complete row by decr r_end,
            # move our r pointer up 1 and change direction
            ans.append(matrix[r][c])
            if c == c_start:
                r_end-=1
                r-=1
                direction = 'u'
            else:
                c-=1
        # b -> t
        elif r >= r_start and direction == 'u':
            # if we reached start row, complete col by incr c_start,
            # move our c pointer right 1 and change direction
            ans.append(matrix[r][c])
            if r == r_start:
                c_start+=1
                c+=1
                direction = 'r'
            else:
                r-=1
        else:
            break
    return ans
                