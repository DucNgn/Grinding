#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       result = list()

       for each in range(0, len(nums)):
           need = target - nums[each]
           if need in nums:
               result.append(each)
               result.append(nums.index(need))
               break

       return result
        


