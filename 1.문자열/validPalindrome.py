import re
def validPalindrome(s):
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

def main():
    s = input('문자열을 입력하세요: ')
    print(validPalindrome(s))

if __name__ == '__main__':
    main()