'''
Game higer or lower. Player has to choose who has more followers.
'''

import art
import game_date
from random import randint
import random
import os

def get_random_accunt():
    # Get data from random account
    return random.choice(game_date.data)

def format_date(accunt):
    # Format account into printable format: name, description and country
    name = game_date.data[accunt]['name']
    description = game_date.data[accunt]['description']
    country = game_date.data[accunt]['country']
    return f"{name}, a {description}, from {country}"


def higer_lower():

    print(art.logo)
    score = 0

    i = randint(0,len(game_date.data))
    name_a = game_date.data[i]['name']
    description_a = game_date.data[i]['description']
    country_a = game_date.data[i]['country']
    follower_count_a = game_date.data[i]['follower_count']
    print(f'Compare A: {name_a}, a {description_a}, from {country_a}')

    print(art.vs)

    j = randint(0,len(game_date.data))
    name_b = game_date.data[j]['name']
    description_b = game_date.data[j]['description']
    country_b = game_date.data[j]['country']
    follower_count_b = game_date.data[j]['follower_count']
    print(f'Compare A: {name_b}, a {description_b}, from {country_b}')
    choice = input("Who has more followers? Type 'A' or 'B': ")

    if follower_count_a > follower_count_b and choice.upper() == 'A':
        score += 1

    while True:
        pass

higer_lower()
