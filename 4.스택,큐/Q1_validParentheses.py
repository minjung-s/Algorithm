
#https://leetcode.com/problems/valid-parentheses/submissions/
"""
Runtime: 32 ms, faster than 52.02% of Python3 online submissions for Valid Parentheses.
Memory Usage: 14.3 MB, less than 13.22% of Python3 online submissions for Valid Parentheses.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table ={
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for char in s :
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False
        return len(stack) == 0