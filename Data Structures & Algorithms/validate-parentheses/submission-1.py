class Solution:
    def isValid(self, s: str) -> bool:
        dic = { ")":"(" ,  "}":"{" , "]":"["}
        stack = []
        for c in s:
            if c in dic:
                if stack and dic[c] == stack.pop():
                    continue
                else:
                    return False
            else:
                stack.append(c)
        return not stack

        
        