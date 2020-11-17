
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

    def  
        