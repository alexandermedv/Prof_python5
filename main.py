"""Задание на итераторы и генераторы"""
import wikipedia
import hashlib
import json
from datetime import datetime


class MyRange:

    def __init__(self, countries):

        self.countries = countries
        self.start = 0
        self.link = None
        self.cursor = 0

    def __iter__(self):

        return self

    def __next__(self):

        print(self.countries[self.cursor]['name']['common'])
        try:
            page = wikipedia.page(self.countries[self.cursor]['name']['common'])
            with open('result.txt', 'a') as file:
                file.write(self.countries[self.cursor]['name']['common'] + ' - ' + page.url + '\n')
        except:
            with open('result.txt', 'a') as file:
                file.write(self.countries[self.cursor]['name']['common'] + ' - ' + 'Не удалось найти страницу' + '\n')

        self.cursor = self.cursor + 1
        if self.cursor >= len(self.countries):
            raise StopIteration

        return self.cursor


def logger(path):

    def _logger(old_function):

        def new_function(*args, **kwargs):

            with open(path, 'a') as file:
                file.write(f'Дата и время: {str(datetime.now())}\n')
                file.write(f'Вызвана функция: {old_function.__name__}\n')
                file.write(f'Аргументы: {args} {kwargs}\n')
                file.write(f'Результат: {str(old_function(*args, **kwargs))}\n')
                file.write('-------------------------------------------' + '\n')

            result = old_function(*args, **kwargs)

            return result

        return new_function

    return _logger


@logger('log2.txt')
def generator(path):

    with open('result.txt', 'r') as file:
        while True:
            line = file.readline()
            print(hashlib.md5(line.encode('utf-8')).hexdigest())
            if not line:
                break


if __name__ == '__main__':

    print('Запрос существующих страниц на wiki через API и запись их в файл:')
    with open('countries.json') as json_file:
        data = json.load(json_file)

    my_range_iterator = MyRange(data)

    for item in my_range_iterator:
        pass

    print('Создание ссылок завершено.')

    print('Создание md5 хэша каждой строки из файла:')
    gen = generator('result.txt')
