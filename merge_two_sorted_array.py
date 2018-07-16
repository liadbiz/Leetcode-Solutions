"""
description:

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

Idea:
    This is a classic problem. Key idea is to iterate two ListNodes at the same
    time, select the smaller one to the new ListNodes, until one of input
    ListNodes is empty.

Issue:
    There is only one issue:
    Since the input is single-linked, so we need to keep a anchor pointer in the front
    of the list, and use another pointer to do operation. And return the
    anchor.next.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """


        result = ListNode(0)
        anchor = result
        while l1 or l2:
            if l1 and l2:
                if l1.val >= l2.val:
                    result.next = l2
                    l2 = l2.next
                else:
                    result.next = l1
                    l1 = l1.next
            elif l1 and not l2:
                result.next = l1
                break
            elif l2 and not l1:
                result.next = l2
                break
            result = result.next
        return anchor.next



