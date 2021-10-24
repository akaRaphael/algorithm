# 1431. Kids With the Greatest Number of Candies
from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        add_candy = [candy + extraCandies for candy in candies]
        max_candy = max(candies)
        result = []
        for i in add_candy:
          if i >= max_candy:
            result.append(True)
          else: 
            result.append(False)
        return result

foo = Solution()
print(foo.kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3))
