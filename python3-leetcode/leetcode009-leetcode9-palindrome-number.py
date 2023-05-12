class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        str0 = str(x)
        reversedStr = str0[::-1]
        return reversedStr == str0
        
# Below is testing
sol = Solution()
print(sol.isPalindrome(616))