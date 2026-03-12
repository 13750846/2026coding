# week03-4.py 學習計畫Sliding Window 第3題
# LeetCode 1004. Max Consecutive Ones III
# 你可以把k個0轉變成1，那最長的一堆1，有幾個1
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = 0 #一開始的蛇蛇，肚子還沒有0
        N = len(nums) #陣列的長度N
        ans = 0 #最長的、不會中毒的蛇蛇，長度是多少?
        tail = 0 #尾巴一開始黏在0的位置，只有拉肚子，才會往右縮
        for head in range(N): ##蛇蛇的頭頭，慢慢往右吃
            if nums[head]==0: #吃到1個有毒的0
                zeros +=1 #身體內毒素增加
                #if zeros>k:超過身體可以容忍的上限，要拉肚子!
                while zeros > k: #要用 while迴圈，一直拉肚子排毒
                    if nums[tail]==0: #現在尾巴吐掉的是有毒的0
                        zeros -=1 #毒素減少!
                    tail +=1 #尾巴拉肚子、拉完後，不能留ˊ在髒髒的園地，往右縮
            #排毒完畢，身體內保證不會有太多的有毒的0
            ans  =max(ans,head-tail+1) #更新答案
        #最長的、不會中毒而死的蛇蛇，長度是ans
        return ans #最長的不會中毒而死的蛇蛇，長度是ans
