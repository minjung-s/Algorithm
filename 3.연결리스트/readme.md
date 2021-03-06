
# 연결리스트
연결 리스트(Linked List)는 컴퓨터과학에서 배열과 함께 가장 기본이 되는 대표적인 선형 자료구조 중 하나로 다양한 추상 자료형(Abstract Data Type)구현의 기반이 된다. 배열(array list)과는 다르게 엘리먼트와 엘리먼트 간의 연결(link)을 이용해서 리스트를 구현한 것이다.특정 인덱스에 접근하기 위해서는 전체를 순서대로 읽어야 하므로 상수 시간에 접근할 수 없다. 즉 탐색에는 O(n) 이 소요된다. 반면, 시작 또는 끝 지점에서 아이템을 추가하거나 삭제, 추출하는 작업은 O(1)에 가능하다. 동적으로 새로운 노드를 삽입하거나 삭제하기 간편하며, 연결 구졸르 통해 물리 메로리를 연속적으로 사용하지 않아도 되기 때문에 관리도 쉽다. 또한 데이터를 구조체로 묶어서 포인터로 연결한다는 개념은 여러가지 방법으로 다양하게 활용 가능하다.

python 의 경우 list 기본 자료형에 linked list 기능이 함께 포함되어 있다. array list에서는 엘리먼트라는 이름을 사용했지만 linked list와 같이 연결된 엘리먼트들은 노드(node, 마디, 교점의 의미) 혹은 버텍스(vertex, 정점, 꼭지점의 의미)라고 부른다.

```python

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
test case input  l1 : [1,2,4]
print(l1) -> "ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 4, next: None}}}"
        
````
Node->Node
next : 다음 노드 주소값
head tail = None으로 초기화
동적배열에서 node날리는거 -> 시간복잡도 크다
liked list : 그냥 node연결을 끊는것 -> 시간 복잡도 O(1)
더블 링크드 리스트 : {val,next,prev} 메모리공간 세개 필요

시간복잡도

접근 n
탐색 n
삽입 1
삭제 1

## Q1. 234 팰린드롬 연결 리스트 (234 Palindrome Linked List)[leetcode](https://leetcode.com/problems/palindrome-linked-list/)
연결 리스트가 팰린드롬 구조인지 판별하라.

 ``` python
Input : "1->2"
Output : false

Input : "1->2->2->1"
Output : true
```
[code](https://github.com/minjung-s/Algorithm/blob/master/3.%EC%97%B0%EA%B2%B0%EB%A6%AC%EC%8A%A4%ED%8A%B8/Q1_isPalidrome.py)

데크 : 더블링크드리스트

## Q2. 21 두 정렬 리스트의 병합 (21 Merge Two Sorted Lists) [leetcode](https://leetcode.com/problems/merge-two-sorted-lists/)
정렬되어 있는 두 연결 리스트를 합쳐라

```python
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
```
[code](https://github.com/minjung-s/Algorithm/blob/master/3.%EC%97%B0%EA%B2%B0%EB%A6%AC%EC%8A%A4%ED%8A%B8/Q2_mergeTwoLists.py)


## Q3. 206 역순 연결 리스트(206 Reverse Linked List) [leetcode](https://leetcode.com/problems/reverse-linked-list/)
연결 리스트를 뒤집어라.
```python
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
```
[code](https://github.com/minjung-s/Algorithm/blob/master/3.%EC%97%B0%EA%B2%B0%EB%A6%AC%EC%8A%A4%ED%8A%B8/Q3_reverseLinkedList.py)


## Q4. 2 두 수의 덧셈 (2 Add Two Numbers) [leetcode](https://leetcode.com/problems/add-two-numbers/)
역순으로 저장된 연결 리스트의 숫자를 더하라.

```python
Input:(2->4->3) + (5->6->4)
Output: 7->0->8
```
[code](https://github.com/minjung-s/Algorithm/blob/master/3.%EC%97%B0%EA%B2%B0%EB%A6%AC%EC%8A%A4%ED%8A%B8/Q4_addTwoNumbers.py)


## Q5. 24 페어의 노드 스왑 (24 Swap Nodes in Paris) [leetcode](https://leetcode.com/problems/swap-nodes-in-pairs/)
연결 리스트르 ㄹ입력받아 페어(pari)단위로 스왑하라

```python
Input: 1->2->3->4
Output: 2->1->4->3
```
[code]()


## Q6. 328 홀짝 연결 리스트 (328 Odd Even Linked List) [leetcode]()
