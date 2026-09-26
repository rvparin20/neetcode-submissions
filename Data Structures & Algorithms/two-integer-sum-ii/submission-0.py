class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hsm = {}
        for i in range(len(numbers)):
            if target - numbers[i] in hsm:
                return [hsm[target - numbers[i]]+1,i+1]
            else:
                hsm[numbers[i]] = i
            
                    

