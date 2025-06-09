# Problem: Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Difficulty: Easy

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
