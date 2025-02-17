def solution(s):
    a=len(s)
    list_1 = []
    print(a)
    if len(s)%2==0:
        for i in range(int (a/2)):
            temp=s[i*2]+s[i*2+1]
            list_1.append(temp)
        print("list_1",list_1)

    else:
        for i in range(int(a/2)):
            temp=s[i*2]+s[i*2+1]
            list_1.append(temp)
        temp_1=s[-1]+"_"
        list_1.append(temp_1)
     #   print("list_1",list_1)
    return list_1

print(solution("1asdfadsf"))