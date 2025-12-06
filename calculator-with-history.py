HISTORY_FILE = 'history.txt'

def show_history():
    file = open(HISTORY_FILE, 'r')
    lines = file.readlines()
    if len(lines) == 0:
        print("No history found")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()

def clear_history():
    file = open(HISTORY_FILE, 'w')
    file.close()
    print("History cleared")

def save_to_history(equation, result):
    file = open(HISTORY_FILE, 'a')
    file.write(equation + " = " + str(result) + "\n")
    file.close()

def calculate(input):
    input_parts = input.split()
    if len(input_parts) != 3:
        print("Invalid input, Use format: number operator (e.g 8 + 8)")
        return
    num1 = float(input_parts[0])
    num2 = float(input_parts[2])
    opeartor = str(input_parts[1])

    if opeartor == "+":
        result = num1 + num2
    elif opeartor == "-":
        result = num1 - num2
    elif opeartor == "*":
        result = num1 * num2
    elif opeartor == "/":
        if num1 == 0 or num2 == 0:
            print("Numbers can not be zero")
            return
        else:
            result = num1/num2
    save_to_history(input, result)
    print(result)

def main():
    print("---SIMPLE CALCULATOR (type history, clear or exit)---")
    while True:
        user_input = input("Enter calculation(+ - * /) or command(history, clear, exit) ")

        if user_input == 'exit':
          print("Thanks for using the calculator. Bye")
          break
        elif user_input == "history":
          show_history()
        elif user_input == "clear":
            clear_history()
        else:
            calculate(user_input)
    
main()
