class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hsm = []
        for x in nums:
            if x in hsm:
                return True
            else:
                hsm.append(x)
        return False
        