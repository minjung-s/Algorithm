cnt = int(input()) # 처음정수 -> 받아올 정수 개수
num_arr = []

for i in range(cnt):
    num = int(input())

    if num != 0 :
        num_arr.append(num)
    else :
        num_arr.pop() # 들어온 정수가 0이면 최근 숫자 빼기

print(sum(num_arr))
