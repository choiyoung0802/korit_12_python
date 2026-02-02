"""
for 반복문 :
원래 python 에서의 default for 문의 경우 enhanced for 가 기본입니다.
근데 저희는 index 를 다루는 것부터 시작했었기 때문에 걔를 기준으로 먼저 강의합니다.

이 때 중요한 것이 range() 함수
"""
# 1 ~ 10 까지 출력하는 for 문
for i in range(10):
    print(i+1)
"""
이상에서 중요한 것은 i 가 0부터 시작한다는 점입니다.
range() : 몇 번 반복할 것인가를 지정하는 함수. -> 특히 for 문과 연계되어 함께 쓰이는 편입니다.

range() 함수의 응용
range((시작값), 한계값, (증강값))

시작값 : 생략 가능, 생략하면 0부터 시작
한계값 : 명시하지않으면 끝까지 진행
증감값 : 생략 가능, 생략할 경우에 1씩 증가
"""
for i in range(1, 11):
    print(i, end=' / ') # 1 / 2 / 3 / 4 / 5 / 6 / 7 / 8 / 9 / 10 /
print()
print(i) # 결과값 : 10
"""
Java 에서는 for (int i = 0 ...) 어쩌고 한 부분 잇을 때
System.out.println(i); 하면 오류났었습니다.
while 에서와 마찬가지로 지역 변수의 범위가 다르다는 점을 알 수 있습니다.

이상까지 학습했을 때 시작값 / 한계값 / 증감값을 정의하게되는 range() 함수가 필수적으로 여겨집니다.

하지만 default 형태의 python for-loop 의 경우의 형식은:
for 변수명(자유롭게가능) in iterable(반복가능객체):
    반복실행문
입니다.
"""
nums = [1,2,3,4,5]
for i in nums:
    print(i, end=" / ")

print()
if 5 in nums:
    print("5가 nums 리스트 내에 있습니다.")
else:
    print("5가 nums 리스트 내에 없습니다.")
"""
그러면 Java 를 배운 저희는 익숙하지 않지만 in 이라는 애가 생각보다 엄청 중요합니다.
in 이 적용된 무언가의 결과값의 자료형은 무엇일까요?
-> True / False 가 나오는 '연산자'
A in B 라고 했을 때 A 라는 요소가 B 라는 반복가능 객체 내에 존재하는지를 True / False 로 뽑아주게 됩니다.
"""
print(5 in nums) # 결과값 : True
