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
words = ['ant','ant','ant','ant','ant','ant']

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
    limbs_left = 8

    #start game
    while limbs_left != 0:
        #print letters guessed
        print(" ",str("".join(parts_guessed)))


        if "".join(used_guesses) == word:
            print("you won! the word was " + word + "!")
            inpt = input("another game? y/n")
            if inpt == "y":
                hangman()
            else:
                break

        # this function takes only a correct input from user
        letter_guess = inputFun(used_guesses)
        if letter_guess in word:
            used_guesses.append(letter_guess)

            for iteration, letter in enumerate(word):

                if letter_guess == letter:
                    parts_guessed[iteration] = letter_guess

            continue

        else:
            limbs_left = limbs_left - 1
            if limbs_left == 0:
                print("aww you died what a shame")
                break
            print(hangmanpics[limbs_left-1])
            print(f"you have {limbs_left} limbs remaining")



hangman()

