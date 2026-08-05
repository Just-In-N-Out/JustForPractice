class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1={}
        for x in strs: 
            value = "".join.sort(x)
            if value in dict1:
                dict1[value] = dict1.append(x)
            else:
                dict1[value] = dict1[x]
        return list(dict1.values())
