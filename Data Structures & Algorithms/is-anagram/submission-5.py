class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 ={}
        for char in s:
            if char in dict1:
             dict1[char] += 1
            else:
                dict1[char]=1

        for v in t:
            if v in dict2:
             dict2[v] += 1
            else:
                dict2[v]=1


        if dict1 == dict2:
            return True
        else:
            return False


            