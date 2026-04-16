# week08-5.py 學習計畫 Binary Search 第3題
# LeetCode 162. Find Peak Element 找到比左右鄰居大的那個
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 笨方法: for 迴圈不行嗎?
        N=len(nums) # 陣列大小 N
        if N==1: return 0

        for i in range(N):
            if i==0:
                if nums[i] > nums[i+1]: return i
            elif i==N-1:
                if nums[i] > nums[i-1]: return i
            # 下面會當機，因為 i-1 或 i+1可能會超過範圍。所以加上面的f
            elif nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
