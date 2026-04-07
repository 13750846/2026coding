# week06-3b.py 學習計畫 Bit Manipulation 第3題
# LeetCode 1318. Minimum Flips to Make a OR b Equal to c
# 你可在 a 和 b 動手腳，flip切換一些bits，希望 a OR b 得到 c
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        c2 = ~c
        ans = bin(a & c2).count('1')+ bin(b & c2).count('1')
        ans += bin(c & ~(a |b)).count('1')
        return ans
