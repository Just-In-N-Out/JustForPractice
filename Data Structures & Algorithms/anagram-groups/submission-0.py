class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1={}
        for x in strs:
            z=  "".join(sorted(x))
            if z in dict1:
                dict1[z].append(x)
            else:
                dict1[z]= [x]
        return list(dict1.values())
            