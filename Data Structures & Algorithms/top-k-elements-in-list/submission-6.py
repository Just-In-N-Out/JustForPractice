class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1={}
        for x in nums: 
            if x in dict1:
                dict1[x] +=1
            else:
                dict1[x] = 1
        b = sorted(dict1, key = lambda f: dict1[f]  , reverse = True)
        return b[:k]

        