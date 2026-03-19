# week04-4a.py (重寫week04-2.py )
# LeetCode 1732. Find the Highest Altitude
# 找到最高的海拔高度(一直加，就好了!)
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = H = 0
        for gg in gain:
            H +=gg
            ans = max(ans,H)
        return ans

        N = len(gain)
        ans = H = 0
        for i in range(N):
            H +=gain[i]
            ans = max(ans, H)
        return ans
