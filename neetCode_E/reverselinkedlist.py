# Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverslist(head):
    prev = None
    current = head

    while current:
        # keep the next in line
        next_node = current.next
        # switch the direction
        current.next = prev
        # move one step
        prev = current
        current = next_node
    
    return prev
        

