# 단어 맞추기 게임
# 조건
# 1. 단어와 뜻을 여러가지 준비
# 2. 랜덤으로 단어를 제시함
# 3. 유저에게 단어의 뜻을 입력받기
# 4. 맞으면 "정답입니다", 틀리면 "다시 입력해주세요" 만약 세번 틀리면 답을 알려줌


import random

dictionary = {
    "apple" : "사과", "banana" : "바나나", "lemon" : "레몬", "grape" : "포도"
}

keys = list(dictionary.keys())
random.shuffle(keys)

for i in range(len(keys)):
    question = keys[i]
    answer = dictionary.get(question)
    
    for i in range(3):
        userAnswer = input("{}의 뜻은?".format(question))
        if answer == userAnswer:
            print("정답입니다.")
            break
        else:
            if i == 2:
                print("정답은 {}입니다.".format(answer))
            else:
                print("다시 입력해주세요.")
            

    
            
    

    