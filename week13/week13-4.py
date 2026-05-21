# week13-4.py 學習計畫 Heap / Priority Queue 第2題
# LeetCode 2336. Smallest Number in Infinite Set
class SmallestInfiniteSet:

    def __init__(self):
        self.now = 1
        self.s = set()
        self.heap = []

    def popSmallest(self) -> int:
        if self.heap:
            self.s.remove(self.heap[0])
            return heappop(self.heap)
        self.now +=1
        return self.now - 1

    def addBack(self, num: int) -> None:
        #print('zzz')
        if num < self.now:
            heappush(self.heap,num)
            self.s.add(num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
