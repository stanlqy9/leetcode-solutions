class Solution:
    def reverseList(self, head):
        cur_node = None

        while head:
            temp = head.next
            head.next = cur_node
            cur_node = head
            head = temp
        return cur_node