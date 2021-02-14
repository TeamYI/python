'''
fizz, bizz, buzz 찾기
fizz : 3의 배수
bizz : 5의 배수
buzz : 7의 배수
결과 값 : 해당 배수일 경우 fizz,bizz,buzz 를 출력한다
example) 1 2 fizz 4 bizz fizz buzz 8 fizz bizz 11 fizz 13 buzz fizzbizz 16
'''

inputValue = input("범위를 입력해주세요 : ")

for i in range(1,int(inputValue)+1):
    outValue = ""
    if i%3 == 0:
        outValue = "fizz"
    if i%5 == 0:
        outValue = outValue + "bizz"
    if i%7 == 0:
        outValue = outValue + "buzz"
    
    print(i if outValue == "" else outValue )
