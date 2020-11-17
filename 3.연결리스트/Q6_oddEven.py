class Solution:
    def node2list(self,head : Node) -> List[int]:
        node = head
        list1 = []
        while node != None :
            list1.append(node.val)
            node = node.next
        return list1
    
    def list2node(slef, l1 : List[int]) -> ListLink:
        result_node = ListLink()
        
        for i,num in enumerate(l1):
            if i == 0:
                result_node.val = num
            else :
                node = result_node
                while node.next != None:
                    node = node.next
                node.next = ListNode(num)

        return result_node


    def oddEvenList(self, head: ListNode) -> ListNode:
        