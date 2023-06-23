import random
import time
print('Dice Stimulator')
while True:
    print("Dice Rolling")
    time.sleep(1)
    n=random.randint(1,6)
    if n==1:
        print('---')
        print()
        print(' o ')
        print()
        print('---')
    if n==2:
        print('---')
        print(' o ')
        print()
        print(' o ')
        print('---')
    if n==3:
        print('---')
        print()
        print('ooo')
        print()
        print('---')
    if n==4:
        print('---')
        print('o o')
        print()
        print('o o')
        print('---')
    if n==5:
        print('---')
        print('o o')
        print(' o ')
        print('o o')
        print('---')
    if n==1:
        print('---')
        print('o o')
        print('o o')
        print('o o')
        print('---')
    print("Play Again!? Y Or N")
    playAgain=input()
    if playAgain.lower()=='n':
        break

