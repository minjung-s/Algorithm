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
[code](https://github.com/minjung-s/Algorithm/blob/master/1.%EB%AC%B8%EC%9E%90%EC%97%B4/validPalindrome.py)

## Q2. 문자열 뒤집기 (Revese String)
문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열이
며, 리턴 없이 리스트 내부를 직접 조작하라.

```python
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
```
[code](https://github.com/minjung-s/Algorithm/blob/master/1.%EB%AC%B8%EC%9E%90%EC%97%B4/reverseString.py)

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


## Q4. 가장 흔한 단어 [Most Common Word]
금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력
대소문자 구분을 하지 않으며, 기호 무시

```python
Input:
  paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
  banned = ["hit"]
Output: "ball"
```


## Q5. 그룹 애너그램 [Group Anagrams]
문자열 배열을 받아 애너그램 단위로 그룹핑하라.
```python
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input: strs = [""]
Output: [[""]]
```


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
