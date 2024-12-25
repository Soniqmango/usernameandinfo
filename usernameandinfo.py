import pyinputplus as pyip
import random

responses = {}
asking = True
currentusernames = []

while asking:
    lower_currentusernames = [item.lower() for item in currentusernames]
    userchoose = True
    while userchoose:
        usernamechosen = input("\nWhat would you like your username to be? ")
        usernamechosenlower = usernamechosen.lower()
        if usernamechosenlower in lower_currentusernames:
            print("\nThat username is taken. Try a different one.")
            print(f"\nSuggested usernames: {usernamechosen}{random.randint(0,999)}, {usernamechosen}0{len(usernamechosen)}")
        else:
            print(f"\nWelcome {usernamechosen}!")
            userchoose = False
    currentusernames.append(usernamechosen)

    first_name = input("\nWhat is your first name? ")
    last_name = input("\nWhat is your last name? ")
    age = pyip.inputNum("\nHow old are you? ", min=0)
    password = pyip.inputPassword("\nWhat would you like your password to be? ")

    responses[usernamechosen] = {'firstname': first_name, 'lastname': last_name, 'age': age, 'password': password}

    repeat = pyip.inputYesNo("\nIs there someone else? ").lower()
    if repeat == 'no':
        asking = False
print("\n\n\n")
print('Results'.center(97, '-'))

for name, info in responses.items():
    print(f'\nUsername: {name}')
    print(f'\tFull name: {info['firstname'].capitalize()} {info['lastname'].capitalize()}')
    print(f'\tAge: {info['age']}')
    print(f'\tPassword: {(info['password'])}')