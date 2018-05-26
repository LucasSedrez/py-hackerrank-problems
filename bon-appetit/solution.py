# LINK: https://www.hackerrank.com/challenges/bon-appetit/problem
# Expected output for this scenario: 5

meal_prices = [3, 10, 2, 9]
anna_did_not_eat = 1
anna_will_pay = 12


def calculate_bill(meal_prices, anna_did_not_eat, anna_will_pay):
    fair_anna_bill = sum(
        meal for meal in meal_prices if meal is not meal_prices[anna_did_not_eat]
    ) // 2

    if fair_anna_bill is not anna_will_pay:
        return meal_prices[anna_did_not_eat] // 2
    else:
        return 'Bon Appetit'


print(calculate_bill(meal_prices, anna_did_not_eat, anna_will_pay))
