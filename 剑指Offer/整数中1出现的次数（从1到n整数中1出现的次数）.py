#!usr/bin/env python
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        count = 0
        for i in range(1,n+1):
            for i in str(i):
                if i == '1':
                    count+=1
        return count

s = Solution()
print(s.NumberOf1Between1AndN_Solution(55))