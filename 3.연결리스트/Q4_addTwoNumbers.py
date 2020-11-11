"""
Runtime: 76 ms, faster than 32.65% of Python3 online submissions for Add Two Numbers.
Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Add Two Numbers.
"""
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
        
        
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node1 = l1
        node2 = l2 
        
        #linked list -> list
        list1 = self.node2list(node1)
        list2 = self.node2list(node2)
        

        # 배열 뒤집기
        list1.reverse()
        list2.reverse()
        
        #배열 -> join -> int
        num1 = int(''.join(str(a) for a in list1))
        num2 = int(''.join(str(a) for a in list2))
        result = list(str(num1+num2))
        result.reverse()
        
        return self.list2node(result)
        
        
                