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
    elif int(month) > 12 or int(month) < 1:
        count_error -= 1
        print(f'Enter correct month number. You have {count_error} attempts to enter')
        continue
    else: break

print("Ok, number month ", month)

seasons = (
    ('spring', '2/3/4'),
    ('summer', '5/6/7'),
    ('autumn', '8/9/10'),
    ('winter', '11/12/1')
)

name_season = ''
j = 0
while j < len(seasons):
    if  seasons[j][1].count(month):
        name_season = seasons[j][0]
        break
    j += 1

print(f'Month {month} is {name_season}')








