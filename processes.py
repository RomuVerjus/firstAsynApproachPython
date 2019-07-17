import time
from multiprocessing import Process


def ask_user():
    start = time.time()
    user_input = input('Enter your name:')
    greet = f'Hello, {user_input}'
    print(greet, 'ask_user: {}'.format(time.time() - start))


def complex_calculation():
    start = time.time()
    print('Started calculating...')
    [x**2 for x in range(20000000)]
    print('calculation: {}'.format(time.time() - start))


if __name__ == '__main__':
    process = Process(target=complex_calculation)
    process2 = Process(target=ask_user)
    process.start()
    process2.start()
    the_start = time.time()

    process.join()
    process2.join()

    print(f'program with processes execution time: {time.time() - the_start}')

