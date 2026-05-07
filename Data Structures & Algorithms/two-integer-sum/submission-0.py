class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, x in enumerate(nums):
            b = target - x 
            if b in seen:
                return [seen[b], index]   
            else:
                seen[x] = index

            
             