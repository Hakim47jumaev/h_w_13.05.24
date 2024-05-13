def digit(a,b,c):
    str1=""
    cnt=0
    for i in range(a,b+1):
        str1+=str(i)
    for i in str1:
        if str(c)==i:
            cnt+=1
    return cnt
print(digit(51,55,5))