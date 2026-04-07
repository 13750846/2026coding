# week06-4.py 學習計畫 Array / String 最後1題
# LeetCode 605. Can Place Flowers
# 在長長的花壇flowerbed裡，1已經種花、0還沒種花。花要間格放
# 問: 能不能再種n盆花
class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        N = len(flowerbed)
        if N==1 and flowerbed==[0]: return True

        if N>1 and flowerbed[0]==0 and flowerbed[1]==0:
            flowerbed[0] = 1
            n -= 1
        for i in range(1,N-1):
            if flowerbed[i-1]==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
                flowerbed[i] = 1
                n -=1
        if N > 1 and flowerbed[N-2]==0 and flowerbed[N-1]==0:
            flowerbed[N-1] = 1
            n -=1
        return n <=0
