
# 연결리스트
연결 리스트(Linked List)는 컴퓨터과학에서 배열과 함께 가장 기본이 되는 대표적인 선형 자료구조 중 하나로 다양한 추상 자료형(Abstract Data Type)구현의 기반이 된다. 배열(array list)과는 다르게 엘리먼트와 엘리먼트 간의 연결(link)을 이용해서 리스트를 구현한 것이다.특정 인덱스에 접근하기 위해서는 전체를 순서대로 읽어야 하므로 상수 시간에 접근할 수 없다. 즉 탐색에는 O(n) 이 소요된다. 반면, 시작 또는 끝 지점에서 아이템을 추가하거나 삭제, 추출하는 작업은 O(1)에 가능하다. 동적으로 새로운 노드를 삽입하거나 삭제하기 간편하며, 연결 구졸르 통해 물리 메로리를 연속적으로 사용하지 않아도 되기 때문에 관리도 쉽다. 또한 데이터를 구조체로 묶어서 포인터로 연결한다는 개념은 여러가지 방법으로 다양하게 활용 가능하다.

python 의 경우 list 기본 자료형에 linked list 기능이 함께 포함되어 있다. array list에서는 엘리먼트라는 이름을 사용했지만 linked list와 같이 연결된 엘리먼트들은 노드(node, 마디, 교점의 의미) 혹은 버텍스(vertex, 정점, 꼭지점의 의미)라고 부른다.

```python
        test case input  l1 : [1,2,4]
        print(l1) -> "ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 4, next: None}}}"
        
````

**<링크드 리스트 클래스 내의 매소드>**

 - **head** : 맨 앞을 가르킨다.
 - **before** : 현재 위치 전
 - **current** : 현재 탐색위치
 - **tail** : 맨 뒤를 가르킨다.
 - **num_of_data** : 데이터의 총 개수

## Q1. 팰린드롬 연결 리스트 (Palindrome Linked List)[leetcode](https://leetcode.com/problems/palindrome-linked-list/)
연결 리스트가 팰린드롬 구조인지 판별하라.

 ``` python
Input : "1->2"
Output : false

Input : "1->2->2->1"
Output : true
```
[code]() \


## Q2. 두 정렬 리스트의 병합 (Merge Two Sorted Lists) [leetcode](https://leetcode.com/problems/merge-two-sorted-lists/)
정렬되어 있는 두 연결 리스트를 합쳐라

```python
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
```
[code]()


## Q3. 역순 연결 리스트(Reverse Linked List) [leetcode](https://leetcode.com/problems/reverse-linked-list/)
연결 리스트를 뒤집어라.
```python
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
```
[code]()


## Q4. 두 수의 덧셈 [Add Two Numbers] [leetcode](https://leetcode.com/problems/add-two-numbers/)
역순으로 저장된 연결 리스트의 숫자를 더하라.

```python
Input:(2->4->3) + (5->6->4)
Output: 7->0->8
```
[code]()
