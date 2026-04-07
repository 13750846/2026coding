# week06-2b.py 學習計畫 Bit Manipulation 第2題
# LeetCode 136. Single Number
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans = ans ^ num
        return ans
