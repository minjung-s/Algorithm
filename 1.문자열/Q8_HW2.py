import re 
while True: 
    
    string = inputs()
    if string == "*":
        break

    list_str = list(string)
    check = 1
    for i,element in enumerate(range(0,len(list_str)-2)) :
        list_tmp = list_str[i+1:]
        result = []
        for j in range(len(list_tmp)):
            result.append(list_str[j] +list_tmp[j])
        result_set = set(result)
        
        if list(result_set).sort() != result.sort():
            check = 0
    if check == 0:
        print(string +" is not surprising.")
    else : 
        print(string +" is surprising.")
