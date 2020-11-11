cnt = int(input())

for i in range(cnt):
    ox_str = input()
    ox_arr = list(ox_str)
    o_cnt = 0
    total_score = 0
    for j in range(ox_arr):
        if j != 'X':
            o_cnt +=1
        else :
            total_score += o_cnt
            o_cnt = 0
    print(total_score)




