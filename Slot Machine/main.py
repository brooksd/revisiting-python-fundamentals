# Global Constant dictating the number wof lines in the slot machine
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

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
    bet = get_bet()
    total_bet =  bet * lines
    
    print(f"You are betting ${bet} on &{lines} lines. Total bet is equal to ${total_bet}")
    # print(balance, lines)

main()
