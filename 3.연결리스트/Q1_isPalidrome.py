"""
Runtime: 68 ms, faster than 78.13% of Python3 online submissions for Palindrome Linked List.
Memory Usage: 24.3 MB, less than 5.10% of Python3 online submissions for Palindrome Linked List.
"""
class Solution:
    def node2list(self, node1: ListNode) -> List: #linked list -> list
        list1 = []
        while node1 != None :
            list1.append(node1.val)
            node1 = node1.next
        return list1
    
    def isPalindrome(self, head: ListNode) -> bool:
        node = head

        
        if node == False : # 빈 linked list이면 팰린드롬이므로 True반환
            return True
        
        list_tmp = self.node2list(node)
        
        if list_tmp == list_tmp[::-1]: #팰린드롬 확인
            return True
        else :
            return False