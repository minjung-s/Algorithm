#https://leetcode.com/problems/daily-temperatures
"""
Runtime: 472 ms, faster than 98.10% of Python3 online submissions for Daily Temperatures.
Memory Usage: 18.3 MB, less than 79.30% of Python3 online submissions for Daily Temperatures.
"""
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        answer = [0]*len(T)
        stack = []
        for i,cur in enumerate(T):
            while stack and cur > T[stack[-1]] :
                last = stack.pop()
                answer[last] = i- last
            stack.append(i)
        return answer
        