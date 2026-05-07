class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prevMap= {} # val ; index

        for n in nums:
            if n in prevMap:
                return True
            else:
                return False
         