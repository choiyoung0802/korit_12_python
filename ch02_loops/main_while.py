"""
1. while 반복문
    while 다음에 나오는 조건식이 참이라면 이하의 실행문이 반복 실행됨(조건이 False 가 될 때까지)
형식:
while 조건식1:
    반복실행문1

당연히 특정 시점에 while 반복문이 종료될 수 있도록 지정해주셔야 합니다.
중첩 while 문 당연히 가능.
"""
n = 1
while n < 11:
    print(n, end=' / ')
    n += 1      # python 에는 ++ 가 없습니다.
"""
기본 예제 # 2
10부터 1까지 역순으로 출력하시오.
"""
print()
n2 = 10
while n2 > 0:
    print(n2, end=' / ')
    n2 -= 1
print()
dan = 2
while dan < 10:                                         # 조건문1
    number = 1                                          # 반복실행문1-a
    while number < 10:                                  # 조건문2
        print(f"{dan} x {number} = {dan * number}")     # 반복실행문2
        number +=1
    dan += 1                                            # 반복실행문1-b
    print()

print(number) # 전역 / 지역 변수의 개념이 Java 와는 다릅니다.