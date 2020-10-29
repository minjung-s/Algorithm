def reverseString(s):
    str2list = list(s)
    list2str = ''.join(list(reversed(str2list)))

    return list2str

def main():
    s = input('문자열을 입력하세요: ')
    print(reverseString(s))

if __name__ == '__main__':
    main()