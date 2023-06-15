import random       # This is a module to random generation. 
import os           # so that i can use os.system('cls')

MAX_LINES = 3
MAX_BET_PER_LINE = 800
MIN_BET_PER_LINE = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

symbol_values= {
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def check_winnings(columns, lines, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:  # Executes if the loop completed without encountering a break
            winnings += values[symbol]
            winning_lines.append(line + 1)

    return winnings, winning_lines



def get_slot_mach_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():      # .items() gives the key and value assigned to that key in a dictionary
        for i in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]              # [:] is a SLICE operator used for copying contains
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
    
    return columns

def print_slot_mach(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):         # enumerate gives access to run two variables
            if i != len(columns) - 1:
                print(column[row], end=" | ")      #by default end is at "\n" this tell when to end a line
            else:
                print(column[row], end="")

        print()                                   # to jump to new line

def deposit():
    while True:
        amount = input("Enter the amount of money you would like to deposit:")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break;
            else:
                print("Enter an Amount greater than 0")
        else:
            print(" The amount you entered must be a Number.")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the Number of Lines you want to bet on:")
        if lines.isdigit():
            lines = int(lines)
            if lines > 0:
                break
            else:
                print("It must be greater than 0")
        else:
            print("Number of lines should be ranging from 1 to "+MAX_LINES)
    
    return lines

def get_bet():
    while True:
        bet = input("What about of Money would u like to bet on each line:")
        if bet.isdigit():
            bet = int(bet)
            if MAX_BET_PER_LINE >= bet > 0:
                break;
            else:
                print("Enter an Amount greater than " + MIN_BET_PER_LINE + " and less than " + MIN_BET_PER_LINE)
        else:
            print(" The amount you entered must be a Number ranging between " + MIN_BET_PER_LINE + " and " + MIN_BET_PER_LINE)
    return bet

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: {balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} so total bet is: ${total_bet}")

    slots = get_slot_mach_spin(ROWS, COLS, symbol_count)
    print_slot_mach(slots)
    winnings, winning_lines= check_winnings(slots, lines, symbol_values)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)                # * is called a splat or unpack operator this passes the values of variables to print function
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to PLAY (q to quit).")
        os.system('clear')                                      # to clear screen/terminal
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}")

main()