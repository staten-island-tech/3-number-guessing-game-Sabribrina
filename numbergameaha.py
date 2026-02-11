history = []

import random
secret = (random.randint(1,10))
guess = 0
print(secret)
while secret is not guess:
        guess = int(input('guess the number of children in my basement...'))

        if secret < guess:
            history.append(guess)
            print('lower bro!! im not insane', history)
        elif guess < secret:
            history.append(guess)
            print('higher dude', history)

if guess == secret:
    print('HUZZAHHHHHH!! GOOD LITTLE LAD, FOR HIS LORDSHIP', history)