guess = int(input('guess the number of children in my basement...'))
history = []
history.append(guess)

import random
secret = (random.randint(1,10))

while secret is not guess:
    for i in range (secret):
        if secret < guess:
            guess = int(input('guess the number of children in my basement...'))
            history.append(i)
            print('lower bro!! im not insane' and history)
        if guess < secret:
            guess = int(input('guess the number of children in my basement...'))
            history.append(i)
            print('higher dude' and history)

if guess == secret:
    print('thats right!!' and history and guess)