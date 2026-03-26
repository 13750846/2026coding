# week05-4.py 昨天 2026-03-26 的挑戰題
# LeetCode 3546. Equal Sum Grid Partition I
# grid 矩陣，能否切一刀兩邊和剛好相同
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = sum ( [sum(row) for row in grid] )

        preSum = 0 # 對應橫切一刀
        for row in grid: # 逐個row整理
            preSum +=sum(row) # 把 row 整行加進來
            if preSum == total - preSum: #上半部 == 下半部
                return True

        preSum = 0 # 對應橫切一刀
        for col in zip(*grid): # 把 transpose轉置矩陣，逐個處理
            preSum +=sum(col) # 把 row 整行加進來
            if preSum == total - preSum: # 左半部 == 右半部
                return True

        return False
