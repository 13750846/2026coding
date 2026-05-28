# week14-3a.py 學習計畫 1D DP 的第2題 Easy題
# LeetCode 746. Min Cost Climbing Stairs
# 踩在第i格的梯子上，要付出 cost[i] 的代價，每次可跨1格 or 2格
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache #函式呼叫函式，把大問題，拆成小問題
        def helper(i): # 現在踩在第i格，之後要多少錢?
            if i >= len(cost): return 0
            return cost[i] + min( helper(i+1),helper(i+2) )
        return min(helper(0),helper(1) )
