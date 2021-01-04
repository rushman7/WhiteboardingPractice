# // You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# // Merge all the linked-lists into one sorted linked-list and return it.

 

# // Example 1:

# // Input: lists = [[1,4,5],[1,3,4],[2,6]]
# // Output: [1,1,2,3,4,4,5,6]
# // Explanation: The linked-lists are:
# // [
# //   1->4->5,
# //   1->3->4,
# //   2->6
# // ]
# // merging them into one sorted list:
# // 1->1->2->3->4->4->5->6
# // Example 2:

# // Input: lists = []
# // Output: []
# // Example 3:

# // Input: lists = [[]]
# // Output: []

# def mergeKLists(self, lists):
#     final = ListNode()
#     final_list = []

#     for i in range(len(lists)):
#         curr = lists[i]
#         while curr:
#             final_list.append(curr.val)
#             curr = curr.next
#     final_list.sort()
#     curr = final
#     for x in final_list:
#         curr.next = ListNode(x)
#         curr = curr.next

#     return final.next

def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    if not lists:
        return None
    sentinal = ListNode()
    curr = sentinal
    q = []
    heapq.heapify(q)

    for i, l in enumerate(lists):
        if l:
            heapq.heappush(q, (l.val, i))
            
    while q:
        val, i = heapq.heappop(q)
        curr.next = ListNode(val)
        lists[i] = lists[i].next
        curr = curr.next
        if lists[i]:
            heapq.heappush(q, (lists[i].val, i))
    return sentinal.next
        