"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
"""

count_error = 5
month = ''
while count_error > 0:
    month = input("Enter number of month: ")

    if not month.isdigit():
        count_error -= 1
        print(f'Sorry, try enter a number. You have {count_error} attempts to enter')
        continue

    month = int(month)
    print(type(month))

    if month > 12 or month < 1:
        count_error -= 1
        print(f'Enter correct month number. You have {count_error} attempts to enter')
        continue
    else:
        break

print("Ok, number month ", month)

seasons = ('spring', 'summer', 'autumn', 'winter')
print(f'Month {month} is {seasons[int(month / 3)-1]}')


# print(3/3, 4/3, 5/3)
# print(6/3, 7/3, 8/3)
# print(9/3, 10/3, 11/3)
# print(12/3, 1/3, 2/3)