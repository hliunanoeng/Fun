# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
          self.val = val
          self.next = next

class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            if l1:
                n1=l1.val
            else:
                n1=0

            if l2:
                n2 = l2.val
            else:
                n2 = 0

            s = n1 + n2 + carry
            carry = s // 10
            s = s % 10
            current.next = ListNode(s)
            current = current.next

            if l1:
                l1=l1.next
            else:
                l1=None

            if l2:
                l2 = l2.next
            else:
                l2 = None

        return dummy.next