#
# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for stone in S:
            if stone in J:
                count = count + 1
        return count
    


