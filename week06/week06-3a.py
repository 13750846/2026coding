# week06-3a.py 學習計畫 Bit Manipulation 第3題
# LeetCode 1318. Minimum Flips to Make a OR b Equal to c
# 你可在 a 和 b 動手腳，flip切換一些bits，希望 a OR b 得到 c
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        while a or b or c:
            if c%2==1:
                if a%2==0 and b%2==0:
                    ans +=1
            else:
                ans +=a%2 + b%2
            a,b,c = a//2,b//2,c//2
        return ans
