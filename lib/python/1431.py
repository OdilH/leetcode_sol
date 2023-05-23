from typing import List


class Solution:
    def kidsWithCandies(self, candies, extraCandies: int) :
        maxL = max(candies)
        l = []
        for i in candies:
            if i + extraCandies >= maxL:
                l.append(True)
            else:
                l.append(False)
        return l


sol = Solution()
print(sol.kidsWithCandies([2, 3, 5, 1, 3], 3))
