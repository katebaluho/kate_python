"""
Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""

text = input('Enter string:\n>>>')
words = text.split(' ')

i = 0
while i < len(words):
    if len(words[i]) <= 10:
        print(f"{i+1}: {words[i].center(10,'*')} \n")
    else:
        print(f"{i + 1}: {words[i][:10]} \n")
    i += 1

