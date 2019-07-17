from collections import deque

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))


# coroutine
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


def greet(g):
    # same thing than yield from
    # g.send(None)
    # while True:
    #     greeting = yield
    #     g.send(greeting)
    yield from g


greeter = greet(friend_upper())
# priming the generator
greeter.send(None)
greeter.send('Hello')
print('Hello, world! Multitasking...')
greeter.send('How are you,')
