class Hangman:
    def __init__(self, word):
        self.word = list(word)
        self.guessed_letters = []
        self.correct_guesses = 0
        self.hidden_word = ["_" for x in self.word]
        self.valid_letters = "asdfghjklæqwertyuiopðxcvbnmöáéýúíó"
    
    def print_status(self):
        ret_str = ""
        for x in self.hidden_word:
            ret_str += x
            ret_str+= " "
        ret_str += " \n\nYou have: " +str(11 - len(self.guessed_letters))+ " guesses left\n\n"
        return ret_str

    def guess(self, guess):
        self.valid_letters
        guess = guess.lower()
        if len(guess) > 2:
            print("Please only guess one letter")
            return False
        elif guess not in self.valid_letters:
            print("Please enter a valid letter")
        elif guess in self.guessed_letters:
            print("Please don't guess the same letter more than 1x")
        else:
            self.validate_guess(guess)

    def validate_guess(self, guess):
        found = False
        for index, i in enumerate(self.word):
            if i == guess:
                self.hidden_word[index] = guess
                found = True
                print("\nCORRECT\n")
                self.correct_guesses += 1
        if found == False:
            print("\nNOT FOUND\n")
            self.guessed_letters.append(guess)
        
    def play(self):
        victory = False
        while len(self.guessed_letters) < 11 and victory == False:
            self.guess(input("Guess a letter: "))
            if self.correct_guesses == len(self.word):
                victory = True
            print(self.print_status())
        if victory == True:
            print("YOU WIN")
        else:
            print("YOU LOSE")
        return

word = input('Choose a word: ')
hang = Hangman(word.lower())
hang.play()
    
