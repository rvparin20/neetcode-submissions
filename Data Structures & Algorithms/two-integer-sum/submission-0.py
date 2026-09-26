class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hsm = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in hsm:
                return [hsm[x], i]
            hsm[nums[i]] = i 
        return []

