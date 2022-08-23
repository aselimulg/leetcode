# 234. Palindrome Linked List
# easy
# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head: Optional[ListNode]) -> bool:
    n_list = []
    node = head[0]
    while node:
        n_list.append(node.val)
        node = node.next
    if n_list == n_list[::-1]:
        return True
    return False

d = ListNode(1)
c = ListNode(2, d)
b = ListNode(2, c)
a = ListNode(1, b)

print(isPalindrome([a, b, c, d]))