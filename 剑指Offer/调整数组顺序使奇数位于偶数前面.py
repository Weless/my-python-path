# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        result = []
        for i in array:
            if i & 1:
                result.append(i)
        for i in array:
            if not i & 1:
                result.append(i)
        return result