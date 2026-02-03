MENU = {                    # 카푸치노 가격 콘솔 출력 / 에스프레소의 물의 소모량을 콘솔에 출력
    "에스프레소": {
        "재료": {
            "물": 50,
            "커피": 18,
        },
        "가격": 1.5,
    },
    "라떼": {
        "재료": {
            "물": 200,
            "우유": 150,
            "커피": 24,
        },
        "가격": 2.5,
    },
    "카푸치노": {
        "재료": {
            "물": 250,
            "우유": 100,
            "커피": 24,
        },
        "가격": 3.0,
    },
}
resources = {
    "물": 300,
    "우유": 200,
    "커피": 100,
}
profit = 0
# 자판기 보유량에서 에스프레소 두 잔을 추출했을 때 resources 의 남은 물, 우유, 커피량을 딕셔너리 형태로 보여주시오.
# 로직
# coffee = MENU["에스프레소"]["재료"]
# result = {
#     "물": resources["물"] - coffee["물"] * 2,
#     "우유": resources["우유"],
#     "커피": resources["커피"] - coffee["커피"] * 2,
# }
# print(result)
# for key in MENU["에스프레소"]["재료"]:
#     resources[key] -= MENU["에스프레소"]["재료"][key] * 2
# print(resources)

# 라떼 한 잔을 뽑았을 때 남는 resources 를 출력하고, 라떼 금액만큼 profit 더한 결과를 콘솔에 출력하시오.
# 로직
# for key in MENU["라떼"]["재료"]:
#     resources[key] -= MENU["라떼"]["재료"][key]
# profit += MENU["라떼"]["가격"]
# print(resources)
# print(profit)

def report():
    print(f"물 : {resources["물"]}ml\n우유 : {resources["우유"]}ml\n커피 : {resources["커피"]}g\n돈 : ${profit}")

def is_resource_enough(order_ingredients):
    """DocString : 함수/클래스/메서드가 어떤 작동을 하는지 '사람들에게' 설명하는 기능
    주문 받은 음료를 resources 에서 재료 차감을 하고 난 후, 음료 만들기가 가능하면 True / 아니면 False
    :param: order_ingredients
    :return: True / False
    """
    for ingredient in order_ingredients:
        if order_ingredients[ingredient] > resources[ingredient]:
            print(f"죄송합니다. {ingredient}이(가) 부족합니다. 🥱")
            return False
    return True

def process_coins():
    '''
    동전을 입력 받아 전체 금액을 반환하는 함수 call3() 유형
    :return:
    '''
    total = 0.0
    # quarters / dimes / nickels / pennies
    total += int(input("쿼터 얼마 넣을래? >>> " )) * 0.25
    total += int(input("다임 얼마 넣을래? >>> ")) * 0.10
    total += int(input("니켈 얼마 넣을래? >>> ")) * 0.05
    total += int(input("패니 얼마 넣을래? >>> ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    '''
    process_coins() 의 결과값과 음료 가격을 매개 변수로 받아 동전이 가격보다 높으면 True / 아니면 False 를 반환하는데, 금액 부족하다고 안내해줘야 합니다. 그리고 True 라면 profit 에 음료 가격만큼 추가를 해주고, 잔돈을 반환해야 합니다.
    :param money_received:
    :param drink_cost:
    :return:
    '''
    global profit  # 함수 내에서 전역 변수의 값을 바꾸는 것이 바람직하지 않아서 제한걸어뒀습니다.
    change = round(money_received - drink_cost, 2)
    if change >= 0:
        profit += drink_cost
        print(f"잔돈 ${change}를 반환합니다.")
        return True
    else:
        print(f"금액이 부족합니다. ${money_received}를 반환합니다.")
        return False

def make_coffee(drink_name, order_ingredients): # call2() 유형으로 정의
    '''resources 에 있는 재료에서 MENU["음료이름"]["재료"]들을 차감함.
        -> 차감은 무조건 이루어집니다. 음료 나오는 안내문구 작성'''
    # 재료 감하는 부분
    for ingredient in order_ingredients:
        resources[ingredient] -= order_ingredients[ingredient]
    # 커피 안내문구
    print(f"{drink_name} 가 나왔습니다.")


is_on = True
while is_on:
    choice = input("어떤 음료를 드시겠습니까? 에스프레소 / 라떼 / 카푸치노 >>> ")
    # todo - 1 : choice 가 off 라면 자판기가 종료되었습니다. 라고 출력하면서 반복 종료
    if choice == "off":
        print("자판기가 종료되었습니다.")
        is_on = False
    # todo - 2 : choice 가 report 라면 물 : 어쩌고ml ~ 커피 : 어쩌고g / 돈 : $몇달러 라고 출력될 수 있도록 작성하시오.
    elif choice == "report":
        report()
    # todo - 3 : choice 가 에스프레소 / 라떼 / 카푸치노에 해당된다면 실행문으로 다음단계로직 이라고 콘솔에 출력할 수 있도록 코드를 작성하시오.
    elif choice in ["에스프레소", "라떼", "카푸치노"]:
        drink = MENU[choice]
        if is_resource_enough(drink["재료"]):
            money_received = process_coins()
            if is_transaction_successful(money_received, drink["가격"]):
                make_coffee(choice, drink["재료"])
    # todo - 4 : 오타 발생 시에 잘못입력하셨습니다. 를 콘솔에 출력하고 다음 반복으로 넘어갈 수 있도록 코드를 작성하시오.
    else:
        print("잘못입력하셨습니다.")