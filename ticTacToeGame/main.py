# Tic Tac Toe 게임

inputDict = {}

while True:
    userX = input("X를 놓을 위치 번호를 선택하세요(1~9)")
    if not userX.isnumeric():
        continue

    if 0 > int(userX) and int(userX) >= 10 :
        continue
    
    userX = int(userX)
    inputDict[userX] = "X"

    for i in range(1,4):
        line = "-"*5
        
        print("{}{}{}{}{}".format(inputDict[1] if 1 in inputDict else " ","|",inputDict[2] if 2 in inputDict else " ","|",inputDict[3] if i*3 in inputDict else " "))
        print(line)
    
    break


print(inputDict)
print(inputDict.get(6))




