todayDate = input("Today's date? ")
breakfast = int(input("Breakfast calories? "))
lunch = int(input("Lunch calories? "))
dinner = int(input("Dinner calories? "))
snack = int(input("Snack calories? "))
print(f'Calorie content for {todayDate}: {breakfast + lunch + dinner + snack}')