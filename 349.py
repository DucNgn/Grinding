# https://leetcode.com/problems/intersection-of-two-arrays

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        s1, s2 = set(nums1), set(nums2)
        for each in s1:
            if each in s2:
                result.append(each)
        
        return result