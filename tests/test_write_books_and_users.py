from files import CSV_FILE_PATH
from files import JSON_FILE_PATH_RESULT
from files import JSON_FILE_PATH
from csv import DictReader
import json


with open(JSON_FILE_PATH, 'r') as f:
    users = json.load(f)

    lst_of_users = []
    for user in users:
        dict_user = {
            'name': user['name'],
            'gender': user['gender'],
            'address': user['address'],
            'age': user['age'],
            'books': []
        }
        lst_of_users.append(dict_user)
number_of_users = len(lst_of_users)

with open(CSV_FILE_PATH, newline='') as f:
    books = list(DictReader(f))
number_of_books = len(books)

books_for_user = number_of_books // number_of_users
remainder = number_of_books % number_of_users

book_index = 0
for i in range(number_of_users):
    for j in range(books_for_user):
        lst_of_users[i]['books'].append(books[book_index])
        book_index += 1
    if remainder > 0:
        lst_of_users[i]['books'].append(books[book_index])
        book_index += 1
        remainder -= 1

with open(JSON_FILE_PATH_RESULT, 'w') as f:
    s = json.dumps(lst_of_users, indent=4)
    f.write(s)
