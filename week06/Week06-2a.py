# week06-2a.py 學習計畫 Bit Manipulation 第2題
# LeetCode 136. Single Number
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for c in counter:
            if counter[c]==1: return c
