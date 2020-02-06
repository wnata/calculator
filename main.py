import re
import sys


def get_number1():

    x = input('If you want to quit type "q" \nPlease type first number: ')

    if x.upper() == 'Q':
        sys.exit('Good Bye!')

    check_d = re.search(r'\D', x)
    while check_d != None:
        print('\nPlease input only digits!')
        x = input('Please type first number: ')
        check_d = re.search(r'\D', x)
        if x.upper() == 'Q':
            sys.exit('Good Bye!')

    return x


def get_number2():

    x = input('Please type second number: ')
    check_d = re.search(r'\D', x)
    while check_d != None:
        print('\nPlease input only digits!')
        x = input('Please type second number: ')
        check_d = re.search(r'\D', x)

    return x


def get_mark():
    print('Tell me what you gonna do')
    m = input('Choose / * - + // **: ')
    possible_moves = ['/', '*', '-', '+', '//', '**']

    while m not in possible_moves:
        print('Please choose correct move!')
        m = input('Choose / * - + // **: ')

    return m


def main():
    x = get_number1()
    mark = get_mark()
    y = get_number2()

    if mark == '/' and int(y) == 0:
        result = 'you cannot divide by zero'
    elif mark == '*':
        result = int(x) * int(y)
    elif mark == '-':
        result = int(x) - int(y)
    elif mark == '+':
        result = int(x) + int(y)
    elif mark == '//':
        result = int(x) // int(y)
    elif mark == '**':
        result = int(x)**int(y)
    elif mark == '/':
        result = int(x) / int(y)

    print('\nYour result is: ' + str(result))
    print('---------------------------------')


while True:
    if __name__ == '__main__':
        main()
