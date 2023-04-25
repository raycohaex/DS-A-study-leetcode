# exericse
from LinkedList import *
from typing import Optional

class Solution:
    # 2 pointer approach, fast pointer moves 2 steps at a time, slow pointer moves 1 step at a time
    # when fast pointer reaches the end, slow pointer will be at the middle
    def find_middle_node(self, head: Optional[Node]) -> Optional[Node]:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
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

print(middle_node.value)