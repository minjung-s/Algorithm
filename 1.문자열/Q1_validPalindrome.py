import re
class Solution:     
    def isPalindrome(self, s: str) -> bool:
        sentence = []
        for i in s:
            if 64<ord(i)<91 :
                sentence.append(i)
            elif 96<ord(i)<123 :
                sentence.append(chr(ord(i)-32))

        condition = True
        listlen = len(sentence)//2
        for i in range(listlen-1):
            if sentence[i] != sentence[len(sentence)-i-1] :
                condition = False
                break

        return condition
