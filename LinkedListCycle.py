class Solution:
    def hasCycle(self, head):
        if not head:
            return False

        pointer1 = head
        while pointer1.next:
            if pointer1.next.next:
                pointer2 = head.next.next
            if pointer1.val == pointer2.val:
                return True
            else:
                pointer1 = pointer1.next
        return False
