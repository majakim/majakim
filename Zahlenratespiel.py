import random 

print()
print("Let's play: Guess the number!")
print()

game_active = True
tries = 5
max_range = 10
level = 1

while game_active:

    print(f"Level {level}: Guess the number between 0 and {max_range} inclusive. You have {tries} guesses.")
    num = random.randrange(max_range+1)
    guess = tries

    while guess > 0:
        user_guess = int(input("Guess: "))

        if user_guess > num:
            print("Your guess was too high.")

        
        elif user_guess < num:
            print("Your guess was too low.")

        else:
            print("Congratulations! You guessed the number.")
            answer = input("Want to try a harder level or play again? (level_up/play_again): ")
            if answer == "play_again":
                pass
            else: 
                tries += 1
                max_range *= 10
                level += 1
            break
        
        guess -= 1  

        if guess == 0:
            print("Game over!")
            play = input("Do you want to play again? (yes/no): ")
            
            if play == "no":
                game_active = False
                print("Goodbye! Thanks for playing.")
            else:
                tries = 5
                max_range = 10
                level = 1

        else: 
            print(f"You have {guess} guesses left.")