# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        n = len(numbers)//2
        from collections import Counter
        c = Counter(numbers)
        # print(c.most_common(1))
        if c.most_common(1)[0][1] > n :
            return c.most_common(1)[0][0]
        else:
            return 0
s = Solution()
print(s.MoreThanHalfNum_Solution([1,2,3,2,2,2,5,4,2]))