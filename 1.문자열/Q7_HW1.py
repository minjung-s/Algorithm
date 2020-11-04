import re
#클래스로 짜기 귀찮다 이말이야
a = input("문제 문자열")
b = input("찾을 문자열")
k = re.sub('[^a-zA-Z]','',a).strip()

if k.find(b) != -1 :
    print("1")
else :
    print("0")