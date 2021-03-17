class Solution:
    def str2tree(self, s: str) -> TreeNode:
        if not s:
            return None
        stack = []
        i = 0
        while i < len(s):
            if s[i] not in {'(', ')'}:
                num = ''
                while i < len(s) and s[i] not in {'(', ')'}:
                    num+=s[i]
                    i+=1
                node = TreeNode(num)
                is_negative = False
                stack.append(node)
            elif s[i] == ')':
                curr_node = stack.pop()
                if stack[-1].left:
                    stack[-1].right = curr_node
                else:
                    stack[-1].left = curr_node
                i+=1
            else:
                i+=1
        return stack[-1]