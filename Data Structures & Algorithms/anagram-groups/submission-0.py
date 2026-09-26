class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            hsm={}
            o=[]
            for s in strs:
                l = [0] * 26 
                for i in range(len(s)):
                    l[ord(s[i]) - 97] += 1
                if str(l) in hsm:
                    hsm[str(l)].append(s)
                else:
                    hsm[str(l)] = [s]
            for x in hsm:
                o.append(hsm[x])
            return o
                
            

         

             
            


                
            
        