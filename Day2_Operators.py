mealCost = float(input())
tipPer = float(input())
taxPer = float(input())

tip = tipPer/100 * mealCost
tax = taxPer/100 * mealCost

total = round(mealCost + tip + tax)

print("The total meal cost is %d dollars." %total)
