// You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

// Merge all the linked-lists into one sorted linked-list and return it.

 

// Example 1:

// Input: lists = [[1,4,5],[1,3,4],[2,6]]
// Output: [1,1,2,3,4,4,5,6]
// Explanation: The linked-lists are:
// [
//   1->4->5,
//   1->3->4,
//   2->6
// ]
// merging them into one sorted list:
// 1->1->2->3->4->4->5->6
// Example 2:

// Input: lists = []
// Output: []
// Example 3:

// Input: lists = [[]]
// Output: []

class Solution(object):
    def mergeKLists(self, lists):
        final = ListNode()
        final_list = []
        
        for i in range(len(lists)):
            curr = lists[i]
            while curr:
                final_list.append(curr.val)
                curr = curr.next
        final_list.sort()
        curr = final
        for x in final_list:
            curr.next = ListNode(x)
            curr = curr.next
        
        return final.next
        