print('How old are you?')
age = input()

try:
    if int(age) <= 30:
        print('You are still young, there is so much you have to go through')
    else:
        print('You are an adult now')
except ValueError:
    print('Please enter a valid number')
