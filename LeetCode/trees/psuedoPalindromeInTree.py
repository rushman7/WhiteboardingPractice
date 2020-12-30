# 1457. Pseudo-Palindromic Paths in a Binary Tree

# Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

# Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

 

# Example 1:



# Input: root = [2,3,1,3,1,null,1]
# Output: 2 
# Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).
# Example 2:



# Input: root = [2,1,1,1,3,null,null,null,null,null,1]
# Output: 1 
# Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).
# Example 3:

# Input: root = [9]
# Output: 1
 

# Constraints:

# The given binary tree will have between 1 and 10^5 nodes.
# Node values are digits from 1 to 9.

def pseudoPalindromicPaths (self, root: TreeNode) -> int:
    if not root:
        return 0
    
    total = 0
    path = {}
    def dfs(node, curr_path):
        curr_path[node.val] = curr_path.get(node.val, 0) + 1
        if not node.left and not node.right:
            if checkPalindrome(curr_path):
                nonlocal total
                total+=1
        if node.left:
            dfs(node.left, curr_path)
        if node.right:
            dfs(node.right, curr_path)
        curr_path[node.val]-=1
        if curr_path[node.val] == 0:
            del curr_path[node.val]
    
    def checkPalindrome(c_path):
        total_odds = 0
        for val in c_path.values():
            if val % 2 != 0:
                total_odds+=1
        return False if total_odds > 1 else True

    dfs(root, path)
    return total