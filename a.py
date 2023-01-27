try:
    year = float(input("Введите год: "))
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        leap_year = True
    else:
        leap_year = False

    total_sum = 0
    for month in range(1, 13):
        if month == 2:
            days_in_month = 29 if leap_year else 28
        elif month in [4, 6, 9, 11]:
            days_in_month = 30
        else: 
            days_in_month = 31
        for day in range(1, days_in_month + 1):
            total_sum += sum(map(int, str(day)))

    print(total_sum)
except ValueError:
    print("Введите год числом")