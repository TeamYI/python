# 소수 찾기 

numberList = [1,3,5,7]

n = int(input())
numberList = map(int, input().split())
count = 0
for i in numberList:
    decimalCheck = True
    for j in range(2,i):
        if(i%j == 0):
            decimalCheck = False
            break

    if decimalCheck == True and i != 1 :
        count += 1

    
print(count)