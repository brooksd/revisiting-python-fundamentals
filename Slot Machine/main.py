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
        
def main():
    balance = deposit()       
    
main() 