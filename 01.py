# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
#
#
# Example 2 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

class Solution:
    def __init__(self, numbs, target):
        self.numbs = numbs
        self.target = target

    def TwoSum(self):
        for i in self.numbs:
            print(self.numbs.index(i))

        if self.target == 0:
            pass


lst = [1, 2, 3, 4]

a = Solution(lst, 0)
a.TwoSum()
