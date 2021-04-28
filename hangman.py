import random
hangmanpics = [i for i in reversed(['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''])]

#Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

def inputFun(used_guesses):
    #while loop controls user input
    correctInput = False
    while correctInput == False:

        #get input from user
        letterGuess = input("guess a letter: ").lower()
        if letterGuess == "used":
            print("used letters: ", used_guesses)
            continue
        if letterGuess.isalpha() == False or letterGuess.isdigit() == True or len(letterGuess) > 1:
            print("incorrect input, please retry")
            continue
        if letterGuess in used_guesses:
            print("you already guessed that")
        else:
            correctInput = True
    return letterGuess

def hangman():
    #init word
    word = words[random.randint(0, len(words))]

    #init output word as parts_guessed
    parts_guessed = []
    [parts_guessed.append("_") for i in word]

    # init used guesses
    used_guesses = []

    #init lives
    limbs_left = 7

    #start game
    while limbs_left != 0:
        #print letters guessed
        print(" ",str("".join(parts_guessed)))

        if "".join(parts_guessed) == word:
            print("you won! the word was " + word + "!")
            inpt = input("another game? y/n")
            if inpt == "y":
                hangman()
            else:
                return limbs_left

        # this function takes only a correct input from user
        letter_guess = inputFun(used_guesses)
        used_guesses.append(letter_guess)

        #iterate through word and match letters
        if letter_guess in word:

            for iteration, letter in enumerate(word):

                if letter_guess == letter:
                    parts_guessed[iteration] = letter_guess
            continue

        #else guess is incorrect
        else:
            limbs_left = limbs_left - 1

            #logic for loseing
            if limbs_left == 0:
                print(hangmanpics[0])
                print(f"aww you died what a shame, the word was {word}")
                inpt = input("another game? y/n")
                if inpt == "y":
                    hangman()
                else:
                    return limbs_left

            print(hangmanpics[limbs_left])
            print(f"you have {limbs_left} limbs remaining")

hangman()

