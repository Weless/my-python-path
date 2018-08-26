
# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here

        s = sorted(tinput)
        if len(s) < k:
            return []
        return s[:k]