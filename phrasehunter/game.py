import os
from phrasehunter.phrase import Phrase
import random
import re

art0 = '\n▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀\n'
art1 = '\n▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀  Correct!  ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀\n'
art2 = '\n▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ Incorrect! ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀\n'
heart = '♥ '
press_enter = '\n Press [Enter] to continue...'


class Game:
    def __init__(self, phrases):
        self.phrases = self.phrase_factory(phrases)
        self.active_phrase = random.choice(self.phrases)
        self.guesses, self.correct_guesses  = [], []
        self.running = True
        self.lives = 5
        self.art = art0
        self.message = None

    def run(self):
        self.game_start()

    def game_start(self):
        while self.running:
            self.main_display()
            try:
                guess = input(' Enter your guess: ').upper()
                if guess == 'QUIT':
                    CLEAR()
                    BORDER('Thank you for checking out "Phrase Hunter" by Carlos A. Marin')
                    self.running = False
                    break
                # if player does not 'quit', guess will be processed.
                self.process_guess(guess)
            except Exception as explanation:
                    BORDER(str(explanation))

    def main_display(self):
        CLEAR()
        print('\n  Phrase Hunter!  \n')
        print(f' Active Phrase: {self.active_phrase}')
        print(f' guesses: {self.guesses}')
        print(self.art)
        if len(self.guesses) != 0:
            print(f' You\'re guess of {self.guesses[-1]}, was {self.message}.')
        print(f' Lives: {self.heart_factory()}')

    def process_guess(self, guess):
        correct_type =  re.search(r'[a-zA-Z]', guess)
        if len(guess) != 1:
            raise ValueError(' 1 character is required to be guessed per turn.')
        if not correct_type:
            raise ValueError(" Guess must be one of the 26 letters of the english alphabet; which range from 'a' to 'z'.")
        if guess in self.guesses:
            raise TypeError(' A character may only be guessed once per game.')
        else:
            self.guesses.append(guess)
            if guess in self.active_phrase.answers:
                self.correct(guess)
            else:
                self.incorrect()

    def correct(self, guess):
        self.correct_guesses.append(guess)
        self.active_phrase.unviel(guess)
        self.message, self.art = 'correct', art1
        if len(self.correct_guesses) == len(self.active_phrase.answers):
            self.active_phrase.was_guessed = True
            BORDER(f' You\'ve guessed the correct answer "{str(self.active_phrase).upper()}". You won the game! Congratulations!')
            self.prompt_replay()

    def incorrect(self):
        self.message, self.art = 'incorrect', art2
        self.lives -= 1
        if self.lives == 0:
            BORDER(' GAME OVER.'.center(72) )
            self.prompt_replay()

    def prompt_replay(self):
        while True:
            try:
                CLEAR()
                replay = input(art0 + ' Would you like to play again? \n' + art0 + '\n\n\t(YES or NO): ').upper()
                if replay == 'YES':
                    self.reset()
                    break
                elif replay == 'NO':
                    self.running = False
                    BORDER(' Thank you for taking time to check out my program! - Carlos A Marin')
                    break
                else:
                    raise ValueError
            except ValueError:
                BORDER(' Only "YES", and "NO" are valid entries.')

    def phrase_factory(self, phrases):
        phrase_list = []
        for phrase in phrases:
            phrase_list.append(Phrase(phrase))
        return phrase_list

    def heart_factory(self):
        # hl = [heart for life in range(self.lives)]  # list comprehension (with a conditional)
        # return hl.join()
        heart_lives = ''
        for life in range(self.lives):
            heart_lives += heart
        return heart_lives

    def reset(self):
        self.active_phrase.reset()
        self.active_phrase = random.choice(self.phrases)
        self.guesses, self.correct_guesses = [], []
        self.lives = 5


def BORDER(string):
    CLEAR()
    input(art0 + '\n' + string.center(70) + '\n' + art0 + press_enter)

def CLEAR():
    os.system('CLEAR' if os.name == 'posix' else 'cls')
