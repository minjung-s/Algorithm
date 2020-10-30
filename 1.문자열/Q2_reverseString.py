class Solution:
    def reverseString(self, s: str) -> str:
        str2list = list(s)
        list2str = ''.join(list(reversed(str2list)))
        return list2str

