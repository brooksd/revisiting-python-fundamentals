import random

# Global Constant dictating the number wof lines in the slot machine
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "A": 4,
    "A": 6,
    "A": 8,
}

# Generate the items that are in the Slot machine
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
        
    return columns

# Transposing the matrix to display the rows vertically
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1 :
                print(column[row], "|")
            else:
                print(column[row])
        

#function accepts users monetary value input
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amount must be greter than $0.")
        else:
            print("Please enter a Number.")

    return amount


#accepts the number of gambling lines 
def get_number_of_lines():
    while True:
        lines= input("Enter the number of line to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a Number.")

    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"amount must ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a Number.")
        
    return amount 

def main():
    balance = deposit()
    lines = get_number_of_lines()
    # checks for the balance and breaks is the amount is insufficient
    while True:
        bet = get_bet()
        total_bet =  bet * lines
        
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is ${balance}")
        else:
            break
    
    print(f"You are betting ${bet} on &{lines} lines. Total bet is equal to ${total_bet}")
    # print(balance, lines)

main()
