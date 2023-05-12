from typing import List
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        if (len(A) < 3):
            return 0

        A.sort(reverse=True)
        return next(
            (
                A[i] + A[i + 1] + A[i + 2]
                for i in range(len(A) - 2)
                if A[i] < A[i + 1] + A[i + 2]
            ),
            0,
        )

# Below is testing
sol = Solution()
print(sol.largestPerimeter([4, 5, 2, 7]))