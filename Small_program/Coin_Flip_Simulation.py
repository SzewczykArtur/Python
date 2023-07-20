"""
**Coin Flip Simulation** - Write some code that simulates flipping a single coin however many times the user decides. 
The code should record the outcomes and count the number of tails and heads.
"""
import random

def flip_coin():
    side = ''
    coin = random.randint(0,1)
    if coin == 0:
        side = 'tails'
        return side
    else:
        side = 'heads'
        return side
    
count_of_tails = 0
count_of_heads = 0
input('Coin Flip simulations. Do you want play? Press enter!')
while True:
    x = flip_coin()
    if x == 'tails':
        count_of_tails += 1
        print('TAILS !')
    elif x == 'heads':
        count_of_heads += 1
        print('HEADS !')
    print(f'Tails: {count_of_tails}')
    print(f'Heads : {count_of_heads}')
    # y = input('Do you want plaay again? Press y if yes or n if no: ')
    # if y.lower() == 'y':
    #     continue
    # elif y.lower() == 'n':
    #     break
    # else:
    #     print('I do not understand. END GAME')
    #     break
    # while True:
    try:
        y = input('Do you want plaay again? Press y if yes or n if no: ')
        if y.lower() == 'y':
            continue
        elif y.lower() == 'n':
            break
    except:
        print('I do not understand')
    finally:
        print('Finally, I executed!')
