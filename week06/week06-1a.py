# week06-1a.py 學習計畫 Bit Manipulation 第ㄅ題
# LeetCode 338. Counting Bits
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range (n+1):
            ans.append( bin(i).count('1') )
        return ans
