# week14-4.py 學習計畫 1D DP 的第3題 Medium題
# LeetCode 198. House Robber
class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache #遇到 DP的題目，就用 Top-Down DP來思考，特別簡單
        def helper(i):
            if i >= len(nums): return 0
            return nums[i] +  max(helper(i+2), helper(i+3))
            # 函式呼叫函式，來解 Top-Down DP
        return max(helper(0), helper(1))
