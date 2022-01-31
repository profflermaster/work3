import json
from csv import DictReader

with open('./data/books.csv', newline='') as csv_file:
    reader = DictReader(csv_file)

    # Итерируемся по данным делая из них список словарей
    books = []
    for row in reader:
        books.append(row)

with open("./data/users.json", "r") as json_file:
    users = json.loads(json_file.read())

filtered_users_list = []
for user in users:
    filtered_attr_dict = {key: value for key, value in user.items()
                          if key in ['name', 'gender', 'address', 'age']}
    filtered_users_list.append(filtered_attr_dict)

# Рассчитываем количество книг, которое должно быть у каждого пользователя
# (по принципу "максимально поровну")
int_books_amount_per_user = int(len(books) / len(filtered_users_list))

for user in filtered_users_list:
    # Раздаем кники поровну пользователям
    for book in range(int_books_amount_per_user):
        # Создаем у списка 'filtered_users_list' ключ 'books', в котором будет список книг,
        # и добавляем туда книги, исключая эти книги из списка книг 'books'
        user.setdefault('books', []).append(books.pop(0))  # https://www.rupython.com/4968-4968.html

# Раздаем оставшиеся книги пользователям (если количество книг не делится нацело на
# количество пользователей)
for user in filtered_users_list:
    if len(books) != 0:
        user['books'].append(books.pop(0))
    else:
        break

# Получившийся список для записи в json-файл
print(f"filtered_users={filtered_users_list}")

# Производим запись итогового списка словарей в json-файл
with open("result.json", "w") as json_file:
    str_ = json.dumps(filtered_users_list, indent=4)
    json_file.write(str_)