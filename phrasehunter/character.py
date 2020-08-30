class Character():

    def __init__(self, char):
        self.letter = char.upper()
        #spaces are automatically 'guessed'.
        if char == ' ':
            self.was_guessed = True
        else:
            self.was_guessed = False

    def __str__(self):
        if self.was_guessed:
            return self.letter
        else:
            return '_'

    def __repr__(self):
        return str(self)

    def check(self, guess):
        if guess == self.letter:
            self.was_guessed = True
