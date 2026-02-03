MENU = {"에스프레소": {"재료": {"물": 50,"커피": 18,},"가격": 1.5,},
    "라떼": {"재료": {"물": 200,"우유": 150,"커피": 24,},"가격": 2.5,},
    "카푸치노": {"재료": {"물": 250,"우유": 100,"커피": 24,},"가격": 3.0,},
}
resources = {"물": 300,"우유": 200,"커피": 100,}
profit = 0

def report():
    print(f"물 : {resources["물"]}ml\n우유 : {resources["우유"]}ml\n커피 : {resources["커피"]}g\n돈 : ${profit}")

def is_resource_enough(order_ingredients):
    for ingredient in order_ingredients:
        if order_ingredients[ingredient] > resources[ingredient]:
            print(f"죄송합니다. {ingredient}이(가) 부족합니다. 🥱")
            return False
    return True

def process_coins():
    total = 0.0
    total += int(input("쿼터 얼마 넣을래? >>> " )) * 0.25
    total += int(input("다임 얼마 넣을래? >>> ")) * 0.10
    total += int(input("니켈 얼마 넣을래? >>> ")) * 0.05
    total += int(input("패니 얼마 넣을래? >>> ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    global profit
    change = round(money_received - drink_cost, 2)
    if change >= 0:
        profit += drink_cost
        print(f"잔돈 ${change}를 반환합니다.")
        return True
    else:
        print(f"금액이 부족합니다. ${money_received}를 반환합니다.")
        return False

def make_coffee(drink_name, order_ingredients):
    for ingredient in order_ingredients:
        resources[ingredient] -= order_ingredients[ingredient]
    print(f"{drink_name} 가 나왔습니다.")

is_on = True
while is_on:
    choice = input("어떤 음료를 드시겠습니까? 에스프레소 / 라떼 / 카푸치노 >>> ")
    if choice == "off":
        print("자판기가 종료되었습니다.")
        is_on = False
    elif choice == "report":
        report()
    elif choice in ["에스프레소", "라떼", "카푸치노"]:
        drink = MENU[choice]
        if is_resource_enough(drink["재료"]):
            money_received = process_coins()
            if is_transaction_successful(money_received, drink["가격"]):
                make_coffee(choice, drink["재료"])
    else:
        print("잘못입력하셨습니다.")