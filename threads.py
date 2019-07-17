import time
from threading import Thread
from concurrent.futures import ThreadPoolExecutor


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


the_start = time.time()
ask_user()
complex_calculation()
print('the program: {}'.format(time.time() - the_start))


thread1 = Thread(target=complex_calculation)
thread2 = Thread(target=ask_user)

the_second_start = time.time()

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print('the multi-threads program: {}'.format(time.time() - the_second_start))

the_second_start = time.time()


with ThreadPoolExecutor(max_workers=2) as pool:
    pool.submit(complex_calculation)
    pool.submit(ask_user)

print('the threadPool program: {}'.format(time.time() - the_second_start))

