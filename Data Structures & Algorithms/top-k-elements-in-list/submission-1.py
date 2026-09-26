class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hsm={}
        for i in nums:
           hsm[i] = 1 + hsm.get(i, 0)
        dict_copy = {}
        for key, val in hsm.items():
            dict_copy[key] = val
        top_k = []
        for c in range(k):
            if not dict_copy:
                break
            max_l = -1
            max_k = None
            for key,val in dict_copy.items():
                if val > max_l:
                    max_l = val
                    max_k = key
            top_k.append(max_k)
            del dict_copy[max_k]
        return top_k

                
            
