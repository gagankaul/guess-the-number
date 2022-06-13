#A number guessing game using the binary search algorithm

print("Welcome to the Number Guessing Game!")
print("Think of a number between 1 and 1000. I will try to guess your number in less than 11 attempts.")

master = list(range(1,1001))

index_low = 0
index_high = 999
total_attempts = 0

state = True
while state:
    index_mid = (index_low + index_high) // 2
    guess = master[index_mid]

    usr_input = input(f"\nIs the number {guess}? You can answer (y)es or (h)igh or (l)ow: ")
    total_attempts += 1

    if usr_input == "h":
        index_high = index_mid - 1
    elif usr_input == "l":
        index_low = index_mid + 1
    elif usr_input == "y":
        print(f"\nYay! I guessed it in {total_attempts} tries.")
        print("\n Thank you for playing. Have a nice day!")
        state = False
    else:
        print("\nThis is not a valid response. Please try again.")