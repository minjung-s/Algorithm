# Definition for singly-linked list.
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        node_l1 = l1
        node_l2 = l2
        
        result = []
        
        result_node = ListNode()
        while node_l1 != None :
            result.append(node_l1.val)
            node_l1 = node_l1.next
            
        while node_l2 != None :
            result.append(node_l2.val)
            node_l2 = node_l2.next
        
        result.sort() #오름차순 정렬
        
        if len(result) == 0 :
            return None
        
        for i,num in enumerate(result): # 정렬 된 배열 element를 Node로 변환, 하나씩 추가
            if i == 0 : #빈 node일 때 val저장
                result_node.val = num
            else :
                node = result_node
                while node.next != None:
                    node = node.next #기존 node 통과해서 맨 마지막 node자리로 가기
                node.next =  ListNode(num) #맨 마지막 node에서 num을 val로 하는 node추가
       
        return result_node
            
