# 숫자 맞추기 게임
# 조건
# 1.랜덤으로 숫자를 제시(1-100) 
# 2. 답을 입력받기 
# 3. 업 앤 다운으로 힌트 제공
import random

number = random.randint(1,101)

while True:
    answer = input("숫자를 입력해주세요 : ")
    if not answer.isnumeric():
        continue

    answer = int(answer)
    if number == answer:
        print("정답입니다")
        break
    elif number > answer:
        print("UP")
    else:
        print("DOWN")



    