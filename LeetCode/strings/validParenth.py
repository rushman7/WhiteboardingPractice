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
            if not stack:
                return False
            temp = stack.pop()
            if char != left[temp]:
                return False
    
    return True if not stack else False