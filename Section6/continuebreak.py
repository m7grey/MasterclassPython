# shopping_list = ["milk", "pasta", "spam", "rice"]
# for item in shopping_list:
#     if item == 'spam':
#         break
#     print("Buy " + item)

meal = ["egg", "bacon", "spam", "sausages"]
nastyFoodItem = ''

for item in meal:
    if item == 'spam':
        nastyFoodItem = item
        break
else:
    print("I'll have a plate of that, please")

if nastyFoodItem:
    print("can't I have anything without spam in it")
