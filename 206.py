
#206 Reverse a singly linked list.

#Iterative

class Solution:
# @param {ListNode} head
# @return {ListNode}
	def reverseList(self, head):
		prev = None
		while head:
			curr = head
			head = head.next
			curr.next = prev
			prev = curr
		return prev

#Recursion

class Solution:
# @param {ListNode} head
# @return {ListNode}
	def reverseList(self, head):
		return self._reverse(head)

	def _reverse(self, node, prev=None):
		if not node:
			return prev
		n = node.next
		node.next = prev
		return self._reverse(n, node)
		
#		
def reverseList(self, head):
	next=None
    while head:
		head.next,head,next=next,head.next,head
    return next