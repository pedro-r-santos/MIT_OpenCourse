#!/usr/bin/env/python3

# annual salary
annual_salary = int(input("Enter your annual salary: "))
# save a portion from the salary for the down payment
portion_saved = float( \
input("Enter the percent of your salary to save, as a decimal: "))
# dream home total_cost
total_cost = int(input("Enter the cost of your dream home: "))
# portion of the cost needed for a down payment
portion_down_payment = .25
# amount saved thus far
current_savings = 0
# annual return
r = .04
# current_savings*r/12
months = 0

while current_savings < (total_cost * portion_down_payment):
 months += 1
 current_savings += (current_savings*r/12) + ((annual_salary/12)*portion_saved)

print("Number of months:", months)
