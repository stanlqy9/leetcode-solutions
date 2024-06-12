class Solution:
    def deleteDuplicates(self, head):
        if not head or head is None:
            return head
        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
