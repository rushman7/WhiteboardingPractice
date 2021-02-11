class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        result = []
        to_remove = self.check_valid(s)
        seen = set()

        def dfs(s, remove):
            if not remove:
                if len(self.check_valid(s)) == 0:
                    nonlocal result
                    result.append(s)
                return
            
            for i, char in enumerate(s):
                if char == remove[0]:
                    new_str = s[:i]+s[i+1:]
                    if new_str not in seen:
                        seen.add(new_str)
                        dfs(new_str, remove[1:])
        
        dfs(s, to_remove)
        return result

    def check_valid(self, s):
        to_remove = []
        for char in s:
            if char == ')' and to_remove and to_remove[-1] == '(':to_remove.pop()
            elif char in {')', '('}:to_remove.append(char)
        return to_remove