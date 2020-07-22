import json
import csv
from csv import DictReader

with open("./files/users.json", "r") as f:
    users = json.loads(f.read())

books = []
with open('./files/books.csv', newline='') as f:
    booksReader = DictReader(f)
    for row in booksReader:
        books.append(row)



class DictionaryUsers:
    config = ['name','gender','address']
    configBooks = ['Title','Author','Height']
    result = []
    readyBooksList = []


    def __init__(self, dictionaries, booksList):
        self.dictionaries = dictionaries
        self.booksList = booksList

    '''
    фильтрация полей из файла user.json
    '''
    def usersJson(self):
        for dictionary in self.dictionaries:
            user_data = {}
            for key in dictionary:
                if key in self.config:
                    user_data[key]=dictionary[key]
            user_data['books'] = []
            self.result.append(user_data)

    '''
    фильтрация полей из файла books.csv
    '''
    def fillBooksList(self):
        for book in self.booksList:
            book_data = {}
            for bookKey in book:
                if bookKey in self.configBooks:
                    book_data[bookKey.lower()] = book[bookKey]
            self.readyBooksList.append(book_data)

    '''
    присвоение пользователю книг, выполнение условия: больше книг или больше пользователей
    '''
    def booksCsv(self):
        counter = 0
        for userData in self.result:
            if counter < len(self.readyBooksList):
                userData['books'].append(self.readyBooksList[counter])
            counter += 1

    '''
    получение результата
    '''
    def getResult(self):
        return self.result




userResult = DictionaryUsers(users, books)
userResult.usersJson()
userResult.fillBooksList()
userResult.booksCsv()



with open("example.json", "w") as file:
    resaltUserJson = json.dumps(userResult.getResult(), indent=4)
    file.write(resaltUserJson)





















