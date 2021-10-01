# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
       
        ##Space: O(n), Time: O(n)
        # arr=[head]
        # while arr[-1].next:
        #     arr.append(arr[-1].next)
        # return arr[len(arr)//2]
        
        ##Space: O(1), Time: O(n)
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    