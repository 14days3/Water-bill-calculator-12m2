from colorama import Fore, Style
record = []
tally = []
day = 0
def menu():
    print("Welcome to our program. What would you like to do?")
    print("[1] Calculate cost\n[2]Exit")
    option = str(input("\nEnter a number of the choice above.\n"))
    if option == "1":
        user_input()
    else:
        exit()
#computation function
def computation(cubic_used):
    if cubic_used <= 30:
        return cubic_used * 20
    elif cubic_used > 30:
        return (30 * 20) + ((cubic_used - 30) * 30)
#main input block
def user_input():
    global day
    while True:
        try:
            print(f"\nDay {day}")
            cubic_used = float(input("Enter cubic meters used: "))
            day += 1
            record.append(cubic_used)
        except:
            ValueError
            print(Fore.RED + '❌ Enter a valid number!' + Style.RESET_ALL)
            return user_input()
        if cubic_used > 50:
            print(Fore.YELLOW + '️⚠️ Warning: Water usage exceeded 50 cubic meters!\n' + Style.RESET_ALL)

        #formulas and shit
        avg = sum(record) / (day)
        cost = computation(cubic_used)
        tally.append(cost)
        total_cost = sum(tally)

        #print statements stuff

        print(Fore.GREEN + "--- Calculation Results: ---" + Style.RESET_ALL)
        print(Fore.LIGHTGREEN_EX + f"Total water usage: {cubic_used} cubic meters")
        print(f"Total cost: ₱{cost}")
        print(f"Usage so far: {record}" + Style.RESET_ALL)
        print(Fore.GREEN + "=" * 31 + Style.RESET_ALL)

        retry = input("\nDo you want to enter another day's data? (Y/N): ").upper()
        if retry == "Y":
            user_input()
            break
        else:
            print(Fore.GREEN + "\n--- Water Usage Statistics ---" + Style.RESET_ALL)
            print(Fore.MAGENTA + f"Maximum usage: {max(record)}m³")
            print(f"Minimum usage: {min(record)}m³")
            print(f"Average usage: {avg:.2f}m³")
            print(f"Total usage: {sum(record)}m³")
            print(f"Total cost: ₱{total_cost}" + Style.RESET_ALL)
            print(Fore.GREEN + "=" * 31 + Style.RESET_ALL)
            break

#just calling the menu function lol
menu()