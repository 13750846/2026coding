# week10-3.py 學習計畫 Binary Tree - DFS 第3題
# LeetCode 1448. Count Good Nodes in Binary Tree
# 函式呼叫函式解 Tree的問題
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root, big):
            if root==None: return 0
            ans = 0
            if root.val >=big:
                ans +=1
                big = root.val
            ans +=helper(root.left,big)
            ans +=helper(root.right,big)
            return ans
        return helper(root, root.val)
