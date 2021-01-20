def isValid(self, s: str) -> bool:
    if len(s) % 2 != 0:
        return False
    left = {
        "(":")",
        "[":"]",
        "{":"}"
    }
    
    stack = []
    for char in s:
        if char in left:
            stack.append(char)
        else:
            if not stack or char != left[stack[-1]]:
                return False
            stack.pop()
    return True if not stack else False