# exericse
from LinkedList import *
from typing import Optional

class Solution:
    # fast pointer moves k ahead
    # after that, slow and fast both move 1 at a time
    # when fast reaches the end, slow will be at the kth node from the end
    def find_knth_from_end(self, head: Optional[Node], k: int) -> Optional[Node]:
        fast = head
        slow = head
        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        return slow

linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.append(6)
linked_list.append(7)
linked_list.append(8)
linked_list.append(9)

solution = Solution()

print(solution.find_knth_from_end(linked_list.head, 3).value)