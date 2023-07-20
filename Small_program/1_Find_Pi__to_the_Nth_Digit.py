# Find PI to the Nth Digit - Enter a number and have the program generate PI up to that many decimal places. Keep a limit to how far the program will go.

import math 

def PiPrint(n):
    if n <= 10:
        print(f'Zaokrąglenie liczby pi do {n} miejsc po przecinku wynosi: ')
        print(round(math.pi,n))
    else:
        return 'Musisz podać liczbę mniejszą od 11'

liczba = int(input('Enter digit number between 0 and 10: '))
PiPrint(liczba)