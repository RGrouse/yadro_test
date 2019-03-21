import time

logtime_data = {}

'''
Декоратор для измерения времени выполнения функции в миллисекундах
@param log_time: словарь в который положить итог измерения
@param log_name: имя с которым ассоциировать итог измерения
'''
def timing(log_time=None, log_name=None):
    def wrapper(f):
        def decorated_function(*args, **kwargs):
            ts = time.time()
            result = f(*args, **kwargs)
            te = time.time()

            f_time = (te - ts) * 1000

            if log_time is not None:
                name = log_name if log_name else f.__name__
                log_time[name] = int(f_time)
            else:
                print('%r  %2.2f ms' % (f.__name__, f_time))
            return result
        return decorated_function
    return wrapper


'''
Функция поиска и печати простых чисел по алгоритму Решето Эратосфена
@param n: верхняя граница поиска, включительно
'''
@timing(log_time=logtime_data)
def sieve_of_eratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1

    # Печатаем все простые числа
    for p in range(2, n + 1):
        if prime[p]:
            print(p)


if __name__ == '__main__':
    sieve_of_eratosthenes(1000000)
    print(logtime_data)
