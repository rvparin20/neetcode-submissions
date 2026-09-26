class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hsm = { ")":"(" , "]":"[" , "}":"{"}
        for c in s:
            if c in hsm:
                if stack and stack.pop() == hsm[c]:
                    continue
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False


        
        