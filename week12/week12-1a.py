# week12-1a.py 學習計畫 Graphs - DFS 第1題 Medium 題
# LeetCode 841. Keys and Rooms
# 房間裡有鑰匙，可以在開新的房間。最後能開全部的房間嗎?
# DFS:Depth First Search 通常會利用 stack 或 function stack(函式呼叫函式)
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = [0]
        visited = set()
        visited.add(0)
        while stack:
            now = stack.pop()
            for k in rooms[now]:
                if k in visited: continue

                stack.append(k)
                visited.add(k)
        return len(rooms) == len(visited)
