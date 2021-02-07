# 숫자 맞추기 게임2(스트라이크 볼 게임)
# 조건
# 1. 세자리 숫자를 랜덤으로 제시
# 2. 답을 입력받기 
# 3. 랜덤으로 제시받은 3자리 숫자와 입력한 3자리 숫자를 비교했을 때, 
#    같은 자리의 같은 수 일 경우 스트라이크. 입력받은 특정한 위치의 숫자가 랜덤으로 제시받은 숫자 중에 존재할 경우 볼
import random

number = str(random.randint(100,999))
number = list(number)
print(number)
while True:
    ball = 0
    strike = 0
    answer = input("숫자를 입력해주세요 : ")
    if not answer.isnumeric():
        continue

    if len(answer) != 3:
        continue

    temp = []
    temp = list(number)
    for i in range(3):
        if answer[i] == temp[i]:
            strike += 1
            temp[i] = "s"

    for i in range(3):
        if answer[i] in temp:
            ball += 1
        
    print("strike : {} ball : {}".format(strike,ball))
    if strike == 3:
        print("정답입니다")
        break
   




    