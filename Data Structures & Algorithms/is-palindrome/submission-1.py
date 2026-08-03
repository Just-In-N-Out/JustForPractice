class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverse_s = s[::-1].lower()
        if s == reverse_s:
            return True
        else: 
            return False
        
            
        