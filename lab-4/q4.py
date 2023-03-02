# Write a program that keeps name and birthday in a dictionary as key-value pairs. The program should display a menu that lets the user search a person's birthday, add a new name and birthday, change an existing birthday, and delete an existing name and birthday.
birthdays = {}

def print_menu():
    print('1. Look up a birthday')
    print('2. Add a new birthday')
    print('3. Change a birthday')
    print('4. Delete a birthday')
    print('5. Quit')
    
def look_up_birthday():
    name = input('Enter a name: ')
    if name in birthdays:
        print(name + '\'s birthday is ' + birthdays[name])
    else:
        print('Sorry, we don\'t have ' + name + '\'s birthday.')
        
def add_birthday():
    name = input('Enter a name: ')
    birthday = input('Enter a birthday: ')
    birthdays[name] = birthday
    print('Birthday added.')
    
def change_birthday():
    name = input('Enter a name: ')
    if name in birthdays:
        birthday = input('Enter the new birthday: ')
        birthdays[name] = birthday
        print('Birthday updated.')
    else:
        print('Sorry, we don\'t have ' + name + '\'s birthday.')
        
def delete_birthday():
    name = input('Enter a name: ')
    if name in birthdays:
        del birthdays[name]
        print('Birthday deleted.')
    else:
        print('Sorry, we don\'t have ' + name + '\'s birthday.')
        
while True:
    print_menu()
    choice = input('Enter your choice: ')
    if choice == '1':
        look_up_birthday()
    elif choice == '2':
        add_birthday()
    elif choice == '3':
        change_birthday()
    elif choice == '4':
        delete_birthday()
    elif choice == '5':
        break
    else:
        print('Invalid input. Please enter a number from 1 to 5')