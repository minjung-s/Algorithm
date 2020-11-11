"""
Runtime: 1112 ms, faster than 5.87% of Python3 online submissions for Reverse Linked List.
Memory Usage: 16.1 MB, less than 7.98% of Python3 online submissions for Reverse Linked List.
"""
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node = head
        result = []
        
        
        while node != None :
            result.append(node.val)
            node = node.next
            
        result.reverse() #순서 뒤집기
        
        result_node = ListNode()
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
            
        