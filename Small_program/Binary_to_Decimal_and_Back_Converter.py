"""
**Binary to Decimal and Back Converter** - 
Develop a converter to convert a decimal number to binary or a binary number to its decimal equivalent.
"""

def biniary_to_decimal(binary):
    binary_list = []
    for i in range(len(str(binary))):
        binary_list.append(str(binary)[i])
    binary_list.reverse()
    
    sum = 0 
    for i in range(0,len(binary_list)):
        sum = sum + (int(binary_list[i]))*(2**i)
    print(f'The decimal number from {str(binary)} is {sum}')

def decimal_to_biniary(decimal):
    num_d = decimal
    binary_num = []
    while decimal > 0:
        binary_num.append(decimal%2)
        decimal = decimal//2
    binary_num.reverse()
    num = ''
    for i in range(len(binary_num)):
        num += str(binary_num[i])
    print(f'The binary number from {num_d} is {num}')

def choice():
    while True:
        choice = input('If you want to change binary number to decimal number enter "b", if vice versa enter "d": ' )
        if choice.lower() == 'b' or choice.lower() == 'd':
            break
        else:
            print('Incorret value, please enter again!')
            continue
    
    if choice == 'b':
        list =[]
        while True:
            num = int(input('Enter binary number: '))
            biniary_to_decimal(num)

    elif choice =='d':
        while True:
            try:
                num = int(input('Enter decimal number: '))
                break
            except:
                print('Give a number')
                continue
            finally:
                print('Finally, I excuted!')
        decimal_to_biniary(num)
    
                
choice()