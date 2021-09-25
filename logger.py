from datetime import datetime


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


@logger('log1.txt')
def multiply(x, y):
    result = x*y
    return result


if __name__ == '__main__':

    multiply(2, 3)
