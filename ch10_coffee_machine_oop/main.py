from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# 기본 생성자를 통한 객체 생성
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# print(menu.get_items())

# 현재 상황에서 menu.menu 를 활용하여 espresso 라는 str 을 추출하려면 어떻게해야 하나요?
# print(menu.menu[1].ingredients["coffee"])
is_on = True
while is_on:
    choice = input(f"어떤 음료를 드시겠습니까? >>> {menu.get_items()}")
    if choice == "종료":
        print("자판기가 종료되었습니다.")
        is_on = False
    elif choice == "재료 확인":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink is not None:
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)