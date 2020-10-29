import re
def validPalindrome(s):
    sentence = []
    for i in s:
        if 64<ord(i)<91 or 96<ord(i)<123 :
            sentence.append(i)

    
    return sentence

def main():
    s = input('문자열을 입력하세요: ')
    print(validPalindrome(s))

if __name__ == '__main__':
    main()