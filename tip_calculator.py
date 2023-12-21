food_charge = float(input("What was your food charge..? "))
tip_charge = round(food_charge*0.18,2)
tax = round(food_charge*0.07,2)
total = round(food_charge+tip_charge+tax,2)

result = f"Tip = ${tip_charge} \n Sales Tax = ${tax} \n Grand Total = ${total}"
print(result)
