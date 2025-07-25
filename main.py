History_File = "history.txt"

def show_history():
    file = open(History_File, 'r')
    lines = file.readlines()
    if len(lines) == 0:
        print('No History Found!')
    else:
        for line in reversed(lines):
            print(line.strip())
        file.close()

def clean_history():
    file = open(History_File, 'w')
    file.close()
    print('History Cleaned')

def save_to_history(equation, result):
    file = open(History_File, 'a')
    file.write(equation + ' = ' + str(result) + '\n')
    file.close()

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print('Invalid input. Use format: number operator number (e.g 8 + 8)')
        return
    
    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            print('Cannot devide by zero')
            return
            result = num1 / num2
    else:
        print('Invalid Operator. Use only + - * /')
        return

    if int(result) == result:
        result = int(result)
    print('Result: ', result)
    save_to_history(user_input, result)

def main():
    print('Simple Calculator')
    while True:
        user_input = input('Enter Calculation or command (history, clean): ')
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

