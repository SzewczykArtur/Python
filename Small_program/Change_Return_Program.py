"""
**Change Return Program** - The user enters a cost and then the amount of money given. 
The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change.
"""
import math 

def ask_float():
    while True:
        try:
            cost = float(input('Please enter o cost of the product: '))
        except:
            print('Looks like you did not enter an float, or use comme. Use dot!!!')
            continue
        finally:
            print('Finally, I executed!')
        return cost

def chang_program(cost):
    quaters = 0.25
    dimes = 0.1
    nickels = 0.05
    needed = 0.01

    round_worth = math.ceil(cost)
    change = round_worth - round(cost,2)
    # quater chang
    quater_change = round(change,2)/quaters
    print(f'Amount of quaters: {math.floor(quater_change)}')
    change_2 = round(change,2)-quaters*math.floor(quater_change)
    # dimes change 
    dimes_change = round(change_2,2)/dimes
    print(f'Aomunt of dimes: {math.floor(dimes_change)}')
    change_3 = round(change_2,2)-dimes*math.floor(dimes_change)
    # nickles change 
    nickles_change = round(change_3,2)/nickels
    print(f'Aomunt of nickles: {math.floor(nickles_change)}')
    change_4 = round(change_3,2)-nickels*math.floor(nickles_change)
    # needed change 
    needed_change = round(change_4,2)/needed
    print(f'Aomunt of dimes: {math.floor(needed_change)}')
    change_5 = round(change_4,2)-dimes*math.floor(needed_change)
    
cost = ask_float()
chang_program(cost)