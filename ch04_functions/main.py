"""
1. 함수의 종류
    1) 파이썬 내장 함수
    2) 메서드(methods)
    3) 사용자 정의 함수
2. 함수 용어 정리
    1) 함수 정의 : 사용자 정의 함수를 새로 만드는 것을 의미(def : define)
    2) 인수(argument) : 함수에 전달할 입력값(input)
    3) 매개변수(parameter) : argument 를 받아서 저장하는 변수를 의미
    4) 반환값/결과값/return 값 : 함수의 출력값(output)
    5) 함수 호출(call) : 함수를 실제로 사용하는 것을 의미
3. (사용자 정의) 함수의 형식 :
    1) 함수 정의 부분
def 함수_이름(매개변수1, 매개변수2):
    실행문
    return 뭐 어쩌고

    2) 함수 호출 부분
변수 = 함수_이름(argument1, argument2)
"""
# eng_name = input("당신의 이름을 영어로 입력하세요. >>> ")
# eng_name_low = eng_name.lower()
# eng_name_up = eng_name.upper()
# print(f"{eng_name_low} / {eng_name_up}")
"""
str 자료형에 딸려있는 .메서드명() 으로 호출하는 애들이 메서드입니다.
.lower() 는 str 데이터를 전부 소문자로 바꿔주고,
.upper() 는 str 데이터의 문자들을 전부 대문자로 바꿔주네요.
특정 클래스에 종속되어있는 함수들을 method 라고 합니다.
함수는 독립적으로 사용이 가능합니다.
Java / JS 때와 마찬가지로 call1() ~ call4() 유형으로 정의할 수 있습니다.
"""
# def multiply(n):
#     for i in range(1, 10):
#         print(f"{n} x {i} = {n * i}")
# dan = int(input("몇 단을 출력하시겠습니까? >>> "))
# multiply(dan)
"""
연산자 중에 또 파이썬에만 있는거 소개 해야합니다.
+
-
*
/
%
**
// : 몫
"""
print(5%2)
print(5//2)
print(5/2)
"""
700 원 짜리 음료수를 뽑을 수 잇는 자판기 프로그램을 구현하시오. 돈을 넣으면 몇 잔의 음료수를 뽑을 수 있는지, 그리고 잔돈은 얼마인지 모든 경우의 수를 출력하도록 합니다.

함수 정의
- 반환값 : 없음(call1 ~ call4 중 어떤 유형일지 고민할 필요가 있습니다)
- 함수 이름 : vending_machine()
- 매개변수 : 정수 money

코드 구성
def vending_machine():
    # 함수 구현
    
vending_machine(3000)

실행 예
음료수 = 0개, 잔돈 = 3000원
음료수 = 1개, 잔돈 = 2300원
음료수 = 2개, 잔돈 = 1600원
음료수 = 3개, 잔돈 = 900원
음료수 = 4개, 잔돈 = 200원
"""
def vending_machine(money):
    drink = 700
    for i in range(money // drink+1):
        print(f"음료수 = {i}개, 잔돈 = {money-i*drink}원")
vending_machine(3000)

# 저희 기본 전제는 메인 단계에서 굴려보고 함수화하는거라서 좀 큰 사이즈의 hangman 으로 갑니다.