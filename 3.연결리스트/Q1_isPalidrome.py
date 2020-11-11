# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        node = head
        list_tmp = []
        
        if node == False : # 빈 linked list이면 팰린드롬이므로 True반환
            return True
        
        while node is not None : #linked list를 list로 변환
            list_tmp.append(node.val) 
            node = node.next
        
        # print(type(list_tmp)) -> "list"
        
        if list_tmp == list_tmp[::-1]: #팰린드롬 확인
            return True
        else :
            return False