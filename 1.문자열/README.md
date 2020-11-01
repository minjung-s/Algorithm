# 문자열

## Q1. 유효한 팰린드롬 (Valid Palidrome) [leetcode](https://leetcode.com/problems/valid-palindrome/)
주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구
분하지 않으며, 영문자와 숫자만을 대상으로한다.

 ``` python
Input : "A man, a plan, a canal: Panama"
Output : true

Input : "race a car"
Output : false
```
[code1](https://github.com/minjung-s/Algorithm/blob/master/1.%EB%AC%B8%EC%9E%90%EC%97%B4/Q1_validPalindrome.py) \
[code2](https://github.com/minjung-s/Algorithm/blob/master/1.%EB%AC%B8%EC%9E%90%EC%97%B4/Q1_validPalindrome2.py)


## Q2. 문자열 뒤집기 (Revese String) [leetcode](https://leetcode.com/problems/reverse-string/)
문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열이
며, 리턴 없이 리스트 내부를 직접 조작하라.

```python
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
```
[code str2str](https://github.com/minjung-s/Algorithm/blob/master/1.%EB%AC%B8%EC%9E%90%EC%97%B4/Q2_reverseString.py) \
[code list2none](https://github.com/minjung-s/Algorithm/blob/master/1.%EB%AC%B8%EC%9E%90%EC%97%B4/Q2_reverseString_List2None.py)


## Q3. 로그파일 재정렬(Reorder Log Files)
로그를 재정렬하라.
1. 로그의 가장 앞 부분은 식별자
2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
3. 실별자는 순서에 영향을 끼치지 않지만, 문자가 동일한 경우 식별자 순으로
4. 숫자 로그는 입력순서대로한다.
```python
Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
```


## Q4. 가장 흔한 단어 [Most Common Word] [leetcode](https://leetcode.com/problems/most-common-word/)
금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력
대소문자 구분을 하지 않으며, 기호 무시

```python
Input:
  paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
  banned = ["hit"]
Output: "ball"
```
[code](https://github.com/minjung-s/Algorithm/blob/master/1.%EB%AC%B8%EC%9E%90%EC%97%B4/Q4_mostCommonWord.py)


## Q5. 그룹 애너그램 [Group Anagrams] [leetcode](https://leetcode.com/problems/group-anagrams/)
문자열 배열을 받아 애너그램 단위로 그룹핑하라.
```python
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input: strs = [""]
Output: [[""]]
```
[code](https://github.com/minjung-s/Algorithm/blob/master/1.%EB%AC%B8%EC%9E%90%EC%97%B4/Q5_groupAnagrame.py)


## Q6. 가장 긴 팰린드롬 부분 문자열 [Longest Palindrome Substring]
가장 긴 팰린드롬 부분 문자열을 출력하라.
```python
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Input: s = "cbbd"
Output: "bb"

Input: s = "a"
Output: "a"

Input: s = "ac"
Output: "a"
```


## Q7. 나는 친구가 적다 (Large) [baekjoon](https://www.acmicpc.net/problem/16172)
친구가 적은 성민이는 수업에 결석해도 시험이나 과제에 대한 정보를 제대로 얻을 수 없었다. F 학점을 받을 위기까지 아슬아슬하게 결석일 수를 유지하던 성민이는, 어느 날 갑자기 영문도 모른 채 쪽지시험을 보게 되었다!

갑작스러운 쪽지 시험으로 마음이 급해진 성민이는 매직아이를 사용해 벼락치기를 하기로 한다.

성민이가 듣는 과목의 교과서는, 알파벳 소문자(a-z)와 알파벳 대문자(A-Z)로만 이루어져 있다. 성민이가 교과서에서 찾고자 하는 키워드도 역시 알파벳 소문자와 대문자로만 이루어져 있다. 하지만, 성민이에겐 큰 문제가 생겼다. 결석한 날의 수업 내용을 친구에게 빌려 필기를 하던 중, 교과서에 숫자(0-9)를 적어버린 것이다.

키워드를 찾기 힘들어 패닉에 빠진 성민이는 몇 안 되는 친구인 당신에게 도움을 요청했다. 성민이를 도와, 교과서에서 성민이가 찾고자 하는 키워드의 존재 여부를 알려주자.
``` python
#입력 : 첫 번째 줄에는 알파벳 소문자, 대문자, 숫자로 이루어진 문자열 S가 주어진다. (1 ≤ |S| ≤ 200,000) 두 번째 줄에는 성민이가 찾고자 하는 알파벳 소문자, 대문자로만 이루어진 키워드 문자열 K가 주어진다. (1 ≤ |K| ≤ 200,000) 단, 입력으로 들어오는 키워드 문자열 K의 길이는, 교과서의 문자열 S보다 짧거나 같다.
#출력 : 첫 번째 줄에 성민이가 찾고자 하는 키워드가 교과서 내에 존재하면 1, 존재하지 않으면 0을 출력한다.
Input : 1q2w3e4r5t6y
        qwerty
Output : 1 

Input : 1ovey0uS2
        veS
Output : 0 
```
