class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s):
            return 0
        i,j = 0,1
        maxlen = 1
        while j < len(s):
            if s[j] in s[i:j]:
                i = i + s[i:j].index(s[j]) + 1
            maxlen = max(maxlen, j-i+1)
            j+=1
        return maxlen




       
                

                


        