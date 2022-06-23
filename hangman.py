# HANGMAN
import random
print("What file stores the puzzle words?")
file = input()
def main():
    global count
    global display
    global words
    global word
    global already_guessed
    global length
    global play_again
    from words import words
    word = random.choice(words)
    words = random.choice(words)
    length = len(words)
    count = 0
    display = '_' * length
    already_guessed = []
    play_again = ""
def again_play():
    global play_again
    play_again = input("Would you like to play hangman (yes, no)? \n")
    while play_again not in ["yes", "no"]:
        play_again = input("Would you like to play hangman (yes, no)? \n")
    if play_again == "yes":
        main()
    elif play_again == "no":
        print("Thank for playing")
        exit()
def hangman():
    global count
    global display
    global words
    global already_guessed
    global play_again
    limit = 5
    if count == 0:
        print("You currently have "+ str(count) +" incorrect guesses.")
    guess = input("Here is your puzzle: \n" + display + "\nPlease enter your guess. \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Here is your puzzle:\n")
        hangman()

    elif guess in words:
        already_guessed.extend([guess])
        index = words.find(guess)
        words = words[:index] + "_" + words[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("\nSorry, you have guessed that letter already.")
        print("Now it counts as a miss \n")
        count += 1
        print("You currently have " + str(count) + " inccorrect guesses.")
    else:
        count += 1

        if count == 1:
            print("Sorry, that letter is NOT in the puzzle \n"+ "You currently have " + str(count) + " incorrect guesses")

        elif count == 2:
            print("Sorry, that letter is NOT in the puzzle \n"+ "You currently have " + str(count) + " incorrect guesses")
        elif count == 3:
            print("Sorry, that letter is NOT in the puzzle \n"+ "You currently have " + str(count) + " incorrect guesses")
        elif count == 4:
            print("Sorry, that letter is NOT in the puzzle \n"+ "You currently have " + str(count) + " incorrect guesses")
        elif count == 5:
            print("Sorry, you have made 5 incorrect guesses, you lose.")
            print("The correct word was " + str(words) +".")
            again_play()
    if words == '_' * length:
        print("Congratuations! You got the correct word " + str(word) + ".")
        again_play()

    elif count != limit:
        hangman()

again_play()
main()


hangman()
