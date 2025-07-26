import re

# File to store history
History_File = "history.txt"

# Show history
def show_history():
    file = open(History_File, 'r')
    lines = file.readlines()
    if len(lines) == 0:
        print('No History Found!')
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()

# Clear history
def clean_history():
    file = open(History_File, 'w')
    file.close()
    print('History Cleaned')

# Save a calculation to history
def save_to_history(equation, result):
    file = open(History_File, 'a')
    file.write(equation + ' = ' + str(result) + '\n')
    file.close()

# Perform calculation
def calculate(user_input):
    user_input = re.sub(r'([+\-*/])', r' \1 ', user_input)
    user_input = ' '.join(user_input.split())
    parts = user_input.split()

    if len(parts) != 3:
        print('Invalid input. Use format: number operator number (e.g. 8 + 8)')
        return

    try:
        num1 = float(parts[0])
        op = parts[1]
        num2 = float(parts[2])
    except ValueError:
        print("Invalid numbers.")
        return

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            print('Cannot divide by zero')
            return
        result = num1 / num2
    else:
        print('Invalid Operator. Use only + - * /')
        return

    if int(result) == result:
        result = int(result)

    print('Result: ', result)
    save_to_history(user_input, result)

# Main program loop
def main():
    print('Simple Calculator')
    while True:
        user_input = input('Enter calculation or command (history, clean, exit): ')
        if user_input == 'exit':
            print('Goodbye!')
            break
        elif user_input == 'history':
            show_history()
        elif user_input == 'clean':
            clean_history()
        else:
            calculate(user_input)

main()
