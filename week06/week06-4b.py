# week06-4b.py 學習計畫 Array / String 最後1題
# LeetCode 605. Can Place Flowers
# 在長長的花壇flowerbed裡，1已經種花、0還沒種花。花要間格放
# 問: 能不能再種n盆花
class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        N = len(flowerbed)
        if N==1 and flowerbed==[0]: return True

        for i in range(N):
            if (i-1<0 or flowerbed[i-1]==0) and flowerbed[i]==0 and(i+1>N or flowerbed[i+1]==0):
                flowerbed[i] = 1
                n -=1
        return n <=0
