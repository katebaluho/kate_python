users = (
    {
        "name": "Jon",
        "surname": "Smith",
        "age": 6,
    },
    {
        "name": "Bill",
        "surname": "Suns",
        "age": 20,
    }
)

templates = (
    "{name} {surname} закончил школу",
    "{name} {surname} скоро пойдет в школу",
)

choice_of_user = 0
index_template = users[choice_of_user]['age'] >= 7
template = templates[index_template]
print(template.format(name=users[index_template]['name'], surname=users[index_template]['surname']))

choice_of_user = choice_of_user + 1
index_template = users[choice_of_user]['age'] >= 7
template = templates[index_template]
print(template.format(name=users[index_template]['name'], surname=users[index_template]['surname']))
