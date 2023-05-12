class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
        vCount = 0
        vList = [s[index] for index in range(len(s)) if s[index] in vowels]
        res_str = ''
        vList.reverse()

        vOutCount = 0
        for index in range(len(s)):
            if s[index] not in vowels:
                res_str += s[index]
            else:                
                res_str += vList[vOutCount]
                vOutCount += 1

        return res_str

sol = Solution()
print(sol.reverseVowels("hiHeyBaby")) 