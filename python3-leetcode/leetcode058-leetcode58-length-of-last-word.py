class Solution:
    def lengthOfLastWord(self, s: str) -> int: 
        newStr = s.strip()
        lastSpacePos = newStr.rfind(' ')
        return len(newStr) if lastSpacePos == -1 else len(newStr) - lastSpacePos - 1

sol = Solution()
print(sol.lengthOfLastWord('Hello my baby'))