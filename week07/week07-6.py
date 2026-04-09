# week07-6.py 學習計畫 Queue 第2題
# LeetCode 649. Dota2 Senate
# Dota2兩個陣營 Radiant/聖輝 和 Dire/魔魘 照 senate 字串的順序出現
# 從左到右輪，輪到的人，可把後面任一個敵對陣營除掉
# 巡完一輪，繞道前面繼續，直到全部字母都相同，問最後哪個陣營得勝
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque(list(senate))
        banR, banD = 0,0
        R,D = senate.count('R'),senate.count('D')
        while queue:
            now = queue.popleft()
            if now=='R':
                if banR>0:
                    banR -=1
                    R -=1
                    continue
                else:
                    banD +=1
                    queue.append(now)
            else:
                if banD > 0:
                    banD -=1
                    D -=1
                else :
                    banR +=1
                    queue.append(now)

            if R==0: return 'Dire'
            if D==0: return 'Radiant'
