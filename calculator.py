## This is a simple calculator program.

while True:

    type = input('what equation would you like to do?\nfor the key, type "key" - ')
    if len(type)<1:
        print('Goodbye')
        break

#key
    if type == 'key':
        print('\naddition = 1\nsubstraction = 2\nmultiplication = 3\ndivision = 4\nexponents = 5\n')

#addition
    elif type == '1':
        num=0
        while True:
            y = input('input # - ')
            if len(y)>=1:
                try:
                    y=float(y)
                    num+=y
                    print('answer = ', num)
                except:
                    print('error: input must be a number\n')
                    continue
            else:
                break
        print('final answer = ', num, '\n')

#substraction
    elif type == '2':
        num=input('input # - ')
        while True:
            y = input('input # - ')
            if len(y)>=1:
                try:
                    num=float(num)
                    y=float(y)
                    num-=y
                    print('answer = ', num)
                except:
                    print('error: input must be a number\n')
                    continue
            else:
                break
        print('final answer = ', num, '\n')

#multiplication
    elif type == '3':
        num=1
        while True:
            y = input('input # - ')
            if len(y)>=1:
                try:
                    y=float(y)
                    num*=y
                    print('answer = ', num)
                except:
                    print('error: input must be a number\n')
                    continue
            else:
                break
        print('final answer = ', num, '\n')

#division
    elif type == '4':
        num=input('input # - ')
        while True:
            y = input('input # - ')
            if len(y)>=1:
                try:
                    num=float(num)
                    y=float(y)
                    num/=y
                    print('answer = ', num)
                except:
                    print('error: input must be a number\n')
                    continue
            else:
                break
        print('final answer = ', num, '\n')

#exponents
    elif type == '5':
        try:
            b = float(input('input base - '))
            e = float(input('input exponent - '))
            answer = b**e
            print('answer = ', answer, '\n')
        except:
            print('error: input must be a number\n')

#error message for the 'type' variable
    else:
        print('error: ', type, ' is not a valid input\n')
