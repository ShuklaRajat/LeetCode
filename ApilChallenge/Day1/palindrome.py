# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        currPoint = head
        dummylist = []

        while currPoint is not None:
            dummylist.append(currPoint.val)
            currPoint = currPoint.next

        return dummylist == dummylist[::-1]

