#!/usr/bin/env python3

semi_annual_raise = .07
r = .04
portion_down_payment = .25
total_cost = 1000000
max_months = 36
current_savings = 0
# annual salary
annual_salary = int(input("Enter the starting salary: "))

# bisection search
epsilon = 100  # relative error
low = 0  # floor
high = 10000  # ceiling
guess = 0
# steps for the bisection search
steps = 0

while 1:
    guess = (high + low) / 2
    steps += 1
    _annual_salary = annual_salary
    current_savings = 0

    for i in range(max_months):
        if i % 6 == 0 and i != 0:
            _annual_salary += _annual_salary * semi_annual_raise
        current_savings += (current_savings * r / 12) + ((
            (_annual_salary / 12) * guess) / 10000)

    # guess found
    if current_savings - (total_cost * portion_down_payment) >= -100 and \
    current_savings - (total_cost * portion_down_payment) <= 100:
        print("Best savings rate: %.4f" % (guess / 10000))
        print("Steps in bisection search:", steps)
        break

    #changing search values
    if current_savings - (total_cost * portion_down_payment) > 100:
        high = guess
    else:
        low = guess

    # impossible solution
    if low == high:
        print("It is not possible to pay the down payment in three years.")
        break
