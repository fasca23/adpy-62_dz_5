import datetime

def logger(old_function):
    def new_function(*args, **kwargs):
        now = datetime.datetime.now().strftime("%d-%m-%Y_%H:%M")
        result = old_function(*args, **kwargs)
        with open('main.log','a', encoding='utf-8') as f:
            f.write(f'\nВремя вызова - {now}'
                    f'\nВызвана функция: {old_function.__name__}'
                    f'\nС аргументами :{args}, {kwargs}'
                    f'\nРезультат: {result}\n'
                    )
        return result
    return new_function

def logger_with_name (name_file):
    def logger1(old_function):
        def new_function(*args, **kwargs):
            now = datetime.datetime.now().strftime("%d-%m-%Y_%H:%M")
            result = old_function(*args, **kwargs)
            with open(name_file,'a', encoding='utf-8') as f:
                f.write(f'\nВремя вызова - {now}'
                        f'\nВызвана функция: {old_function.__name__}'
                        f'\nС аргументами :{args}, {kwargs}'
                        f'\nРезультат: {result}\n'
                        )
            return result
        return new_function
    return logger1