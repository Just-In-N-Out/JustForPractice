class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 ={}
        for char in s:
            dict1[char]+= 1
        else:
            dict1[char]=1
        for char in s:
            dict2[char]+= 1
        else:
            dict2[char]=1
        if dict1 == dict2:
            return True
        else:
            return False


            