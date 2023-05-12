from typing import List

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        B = sorted(A, key = abs) # sort by absolute values
        return [elem*elem for elem in B]

# below is testing        
sol = Solution()
print(sol.sortedSquares([-4,-2, 3,6]))