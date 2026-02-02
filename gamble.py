import random

name = input("Enter your name: ")
print(f"🔥 Welcome to SINGH Casino, {name} ‼️")

red_black_green = ["RED", "RED", "RED", "RED", "RED", "BLACK", "BLACK", "BLACK", "BLACK", "BLACK", "GREEN", "GREEN", "GREEN"]

balance = 1000
print("😅 We are a little new right now.. so we only have ONE game!")
print("")
print(f"💸 Balance: ${balance}")
print("")

while True:

    bet = float(input("BEFORE WE START, Enter the amount to bet: "))

    if bet <= 0 or bet > balance:
        print(f"⚠️ Invalid bet amount! You only got {balance} bucks bro/sis")
        break

    database = open("gamble.txt", "a")
    thing = f"\n{name} bet ${bet}\n"
    database.write(thing)
    database.close()

    luck = random.choice(red_black_green)

    print("🟥⬛️🟩 Would you like to bet on..\n 1: 🟥 RED\n 2: ⬛️ BLACK\n 3: 🟩 GREEN\n  Red & Black have an EQUAL amount of chance, while there is a LOW chance of green being rolled BUT you get 5x what you bet!")
    user_choice = int(input("⭐️ Enter 1, 2, or 3: "))

    database = open("gamble.txt", "a")
    thing = f"{name} chose {user_choice} to bet on.\n"
    database.write(thing)
    database.close()

    if user_choice == 1:

        if luck == "RED":
            balance += bet * 2
            print(f"⭐️ You won! New Balance: ${balance}\n")
            database = open("gamble.txt", "a")
            thing = f"{name} won ${bet}! New Balance: ${balance}\n"
            database.write(thing)
            database.close()
        else:
            balance -= bet
            print(f"🤣 You LOST! New Balance: ${balance}\n")
            print(f"🥲 By the way.. the roll was {luck} ‼️")

            database = open("gamble.txt", "a")
            thing = f"{name} lost ${bet}! New Balance: ${balance}\n"
            database.write(thing)
            database.close()

    elif user_choice == 2:

        if luck == "BLACK":
            balance += bet * 2
            print(f"⭐️ You won! New Balance: ${balance}\n")
            database = open("gamble.txt", "a")
            thing = f"{name} won ${bet}! New Balance: ${balance}\n"
            database.write(thing)
            database.close()
        else:
            balance -= bet
            print(f"🤣 You LOST! New Balance: ${balance}\n")
            print(f"🥲 By the way.. the roll was {luck} ‼️")

            database = open("gamble.txt", "a")
            thing = f"{name} lost ${bet}! New Balance: ${balance}\n"
            database.write(thing)
            database.close()

    elif user_choice == 3:

        if luck == "GREEN":
            balance += bet * 10
            print(f"⭐️ You won! New Balance: ${balance}\n")
            database = open("gamble.txt", "a")
            thing = f"{name} won ${bet * 10}! New Balance: ${balance}\n"
            database.write(thing)
            database.close()

        else:
            balance -= bet
            print(f"🤣 You LOST! New Balance: ${balance}\n")
            print(f"🥲 By the way.. the roll was {luck} ‼️")

            database = open("gamble.txt", "a")
            thing = f"{name} lost ${bet}! New Balance: ${balance}\n"
            database.write(thing)
            database.close()

    else:
        print("⚠️ Enter 1, 2, or 3!")
        continue

    if balance <= 0:
        print("🥲 You do not have enough to keep playing..")
        print("We will hear from you soon..")
        database = open("gamble.txt", "a")
        thing = f"{name} LOST EVERYTHING! Final Balance: {balance}\n"
        database.write(thing)
        database.close()
        break

    play_more = int(input("⚠️ Play again?\n 1: Play Again\n 2: Quit\n Enter 1 or 2: "))
    if play_more != 1:
        print("👎 99% of gamblers quit before they make it big!")
        print("Goodbye!")

        database = open("gamble.txt", "a")
        thing = f"{name} chose to quit! Final Balance: {balance}\n"
        database.write(thing)
        database.close()
        break
