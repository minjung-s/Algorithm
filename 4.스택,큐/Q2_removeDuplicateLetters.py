# https://leetcode.com/problems/remove-duplicate-letters/submissions/
"""
Runtime: 24 ms, faster than 98.89% of Python3 online submissions for Remove Duplicate Letters.
Memory Usage: 14.2 MB, less than 33.32% of Python3 online submissions for Remove Duplicate Letters.
"""
import collections

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []
        
        for char in s :
            counter[char] -= 1
            if char in seen :
                continue
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)
        
        return ''.join(stack)
        