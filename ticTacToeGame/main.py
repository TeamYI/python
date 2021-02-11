# Tic Tac Toe 게임

inputList = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]

def checkDuplicate(position):
    duplicateCheck = False
    sum = 0
    for row in range(len(inputList)):
        for j in range(len(inputList[row])):
            sum += 1
            if position == sum:
                if inputList[row][j] != " ":
                    duplicateCheck = True
                    break

        if duplicateCheck == True:
            break 
    return duplicateCheck

def setData(position,value):
    sum = 0
    for row in range(len(inputList)):
        for j in range(len(inputList[row])):
            sum += 1
            if position == sum:
                inputList[row][j] = value
    


def printBoard():
    rowsCount = len(inputList)
    for row in range(rowsCount):
        print("{}|{}|{}".format(inputList[row][0],inputList[row][1],inputList[row][2]))
        if row != 2:
            print("------")

def confirmVictory(turn):
    if inputList[0][0] == turn and inputList[0][1]  == turn and inputList[0][2] == turn:
         return True
    elif inputList[0][0] == turn and inputList[1][1]  == turn and inputList[2][2] == turn:
         return True
    elif inputList[0][0] == turn and inputList[1][0]  == turn and inputList[2][0] == turn:
         return True
    elif inputList[1][0] == turn and inputList[1][1]  == turn and inputList[1][2] == turn:
         return True
    elif inputList[2][0] == turn and inputList[2][1]  == turn and inputList[2][2] == turn:
         return True
    elif inputList[0][1] == turn and inputList[1][1]  == turn and inputList[2][1] == turn:
         return True
    elif inputList[2][0] == turn and inputList[1][1]  == turn and inputList[0][2] == turn:
         return True
    elif inputList[0][2] == turn and inputList[1][2]  == turn and inputList[2][2] == turn:
         return True
    else:
         return False
         
def isValid(value):
    isValid = True
    if not value.isnumeric():
        print("숫자가 아닙니다.　다시 입력해주세요.")
        isValid = False
    elif 0 > int(value) and int(value) >= 10 :
        print("0~9 범위의 숫자가 아닙니다.　다시 입력해주세요.")
        isValid = False
    elif checkDuplicate(int(value)) == True:
        print("중복된 위치입니다. 다른 번호를 입력해주세요") 
        isValid = False
    
    return isValid


turn = "X"
count = 0
while True:
    if turn == "X":
        positionX = input("X를 놓을 위치 번호를 선택하세요(1~9)")
        valueX = "X"
        
        if isValid(positionX) == False:
            continue

        setData(int(positionX),valueX)
        printBoard()
        count += 1

        isVictory = confirmVictory(turn)

        if isVictory == True:
            break
        else:
            turn = "O"

    elif turn == "O":
        positionO = input("O를 놓을 위치 번호를 선택하세요(1~9)")
        valueO = "O"

        if isValid(positionO) == False:
            continue

        setData(int(positionO),valueO)
        printBoard()
        count += 1

        isVictory = confirmVictory(turn)

        if isVictory == True:
            break
        else:
            turn = "X"

    if count == 10:
        break


if count == 10:
    print("무승부입니다")
else:
    print("승리는 '{}'입니다".format(turn))






