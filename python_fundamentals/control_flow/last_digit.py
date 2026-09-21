#!/usr/bin/env python3
number = __import__('random').randint(-10000, 10000)
lastnumber = abs(number) % 10

if lastnumber > 5:
    print('last digit of ' f'{number} ' 'is ' f'{lastnumber} ' 'and is greater than 5')
if lastnumber == 0:
    print('last digit of ' f'{number} ' 'is ' f'{lastnumber} ' 'and is 0')
if lastnumber <5 and lastnumber != 0:
    print('last digit of ' f'{number} ' 'is ' f'{lastnumber} ' 'and is less than 6 and not 0')
