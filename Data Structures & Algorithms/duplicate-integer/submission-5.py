class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prevMap= {} # val ; index

        for i, n in enumerate(nums):
            if i in prevMap:
                return true 
            else:
                return false;
         