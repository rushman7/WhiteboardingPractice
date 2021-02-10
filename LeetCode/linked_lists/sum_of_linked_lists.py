# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    result, carry = LinkedList(0), 0
    l1, l2, curr = linkedListOne, linkedListTwo, result

    while l1 or l2:
      l1_val = l1.value if l1 else 0
      l2_val = l2.value if l2 else 0
      if l1: l1 = l1.next
      if l2: l2 = l2.next
      new_val = l1_val + l2_val + carry
      if new_val < 10:
        carry = 0
      else:
        carry = 1
        new_val-=10
      curr.next = LinkedList(new_val)
      curr = curr.next

    if carry:
      curr.next = LinkedList(carry)
        
      return result.next