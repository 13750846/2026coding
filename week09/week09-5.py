# week09-5.py 學習計畫 Linked List 第1題 Medium 有點難 把中間的node刪掉
# LeetCode 2095. Delete the Middle Node of a Linked Listt
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:return []

        prev = fast = slow = head # fast兔子 slow烏龜 一開始都在最前面
        while fast != None and fast.next != None: # 兔子跳2格
            fast = fast.next.next
            prev = slow
            slow = slow.next
        # print( slow.val )
        prev.next = slow.next
        return head
