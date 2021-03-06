"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Input: l1 = [0], l2 = [0]
Output: [0]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumber(l1, l2):
    result = ListNode(0)
    result_tail = result 
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        carry, out = divmod(l1 + l2 + carry, 10)

        result_tail.next = ListNode(out)  # add node after result_node (sentinel)
        result_tail = result_tail.next

        # update pointers...
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    # return tail.next
    return result.tail



