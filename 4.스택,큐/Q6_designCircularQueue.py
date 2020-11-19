# https://leetcode.com/problems/design-circular-queue/submissions/
"""
Runtime: 60 ms, faster than 96.87% of Python3 online submissions for Design Circular Queue.
Memory Usage: 14.5 MB, less than 54.38% of Python3 online submissions for Design Circular Queue.
"""
class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0
        self.p2 = 0
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.q[self.p2] is None:
            self.q[self.p2] = value #rear이 가르키는 자리에 value삽입
            self.p2 = (self.p2 +1) % self.maxlen # 다음 자리로 p2포인터 이동. 길이가 넘어가면 나머지 연산자를 이용하여 한바퀴 돌아서 자리찾기
            return True
        else
            return False
        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.q[self.p1] is None:
            return False #이미 내보낼것이 없는 상태 ->False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1+1) % self.maxlen
            return True
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return -1 if self.q[self.p1] is None else self.q[self.p1]
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return -1 if self.q[self.p2 -1] is None else self.q[self.p2 -1] #pop
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.p1 == self.p2 and self.q[self.p1] is None
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.p1 == self.p2 and self.q[self.p1] is not None
        


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(k)
param_1 = obj.enQueue(value)
param_2 = obj.deQueue()
param_3 = obj.Front()
param_4 = obj.Rear()
param_5 = obj.isEmpty()
param_6 = obj.isFull()