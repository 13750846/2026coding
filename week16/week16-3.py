# week16-3.py 學習計畫 Intervals 第1題
# LeetCode 435. Non-overlapping Intervals
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #intervals.sort() # 先排序，依據右邊的結束時間
        intervals.sort( key = lambda x:x[1] ) #用右邊的end大小來排序
        ans = 0
        previous_end = -inf #很左邊、遠的負無限大，先不限制
        for start, end in intervals: # 逐一取出[starts, end]
            if previous_end<=start: # 沒有重疊
                previous_end = end # 更新，現在的end的時間
            else: # 糟!竟然重疊!現在這段不能用
                ans +=1 # 要把現在這段刪掉
        return ans
