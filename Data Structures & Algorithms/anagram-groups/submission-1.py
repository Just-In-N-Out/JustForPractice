class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1={}
        for x in strs: 
            value = "".join(sorted(x))
            if value in dict1:
                dict1[value].append(x)
            else:
                dict1[value]=[x]
        return list(dict1.values())
        
