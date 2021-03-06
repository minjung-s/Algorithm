"""
Runtime: 48 ms, faster than 9.54% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Merge Two Sorted Lists.
"""
# Definition for singly-linked list.
class Solution:
    def node2list(self, node1: ListNode) -> List: #linked list -> list
        list1 = []
        while node1 != None :
            list1.append(node1.val)
            node1 = node1.next
        return list1
    
    def list2node(self, list1: List) -> ListNode:
        result_node = ListNode()
        
        for i,num in enumerate(list1):
            if i == 0 :
                result_node.val = num
            else :
                node = result_node
                while node.next != None:
                    node = node.next
                node.next = ListNode(num)
        return result_node
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        node_l1 = l1
        node_l2 = l2
        
        result = []
        
       
        result = self.node2list(node_l1) + self.node2list(node_l2)
        result.sort() #오름차순 정렬
        
        if len(result) == 0 :
            return None
        
        else : 
            return self.list2node(result)
            
            
        
            
            
        
            
