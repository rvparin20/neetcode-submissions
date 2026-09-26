class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        lost = []
        for x in range(len(nums) - 2):
            if x > 0 and nums[x] == nums[x - 1]:
                continue
            target = -nums[x]
            i, j = x + 1, len(nums) - 1
            while i < j:
                s = nums[i] + nums[j]
                if s < target:
                    i += 1
                elif s > target:
                    j -= 1
                else:
                    lost.append([nums[x], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:  
                        i += 1
        return lost