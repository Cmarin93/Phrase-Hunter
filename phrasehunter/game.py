import os
import phrasehunter.phrase
import random
import re

art0 = '★・・・・・・・★・・・・・・・・★・・・・・・・★・・・・・・・★・・・・・・・・★・・・・・・・★'
art1 = '★・・・・・・・★・・・・・・・・★・・・・・・・✅・・・・・・・★・・・・・・・・★・・・・・・・★'
art2 = '★・・・・・・・★・・・・・・・・★・・・・・・・❌・・・・・・・★・・・・・・・・★・・・・・・・★'
heart = '💖️'


class Game:
    def __init__(self, phrases):
        self.phrases = self.phrase_factory(phrases)
        self.active_phrase = random.choice(self.phrases)
        self.lives = 5
        self.guesses = []
        self.running = True
        self.correct_guesses = []
        self.art = art0
        self.message = None

    def run(self):
        self.game_frame()

    def main_display(self):
        clear()
        print('')
        print('🏹  Phrase Hunter!!  🏹')
        print('')
        print(f'Active Phrase: {self.active_phrase}')
        print(f'➡️ guesses: {self.guesses}')
        print(self.art)
        # after initial guess; shows (right|wrong) responce to last guess.
        if len(self.guesses) != 0:
            print(f'You\'re guess of {self.guesses[-1]}, was {self.message}.')
        print(f'Lives: {self.heart_factory()}')

    def game_frame(self):
        while self.running:
            self.main_display()
            try:
                guess = input('Enter your guess: ').upper()
                if guess == 'QUIT':
                    clear()
                    input('Thank you for checking out "Phrase Hunter" by Carlos A. Marin')
                    self.running = False
                    break
                # if player does not 'quit', guess will be processed.
                self.process_guess(guess)
            except Exception as explanation:
                    input(explanation)

    #only processes [a-z]: guess will be either (right|wrong).
    def process_guess(self, guess):
        correct_type =  re.search(r'[a-zA-Z]', guess)
        if len(guess) != 1:
            print(art2)
            raise ValueError('1 character is required to be guessed per turn.')
        if not correct_type:
            print(art2)
            raise ValueError("Guess must be one of the 26 letters of the english alphabet; which range from 'a' to 'z'.")
        if guess in self.guesses:
            print(art2)
            raise TypeError('A character may only be guessed once per game.')
        else:
            self.guesses.append(guess)
            if guess in self.active_phrase.answers:
                self.correct(guess)
            else:
                self.incorrect()

    def correct(self, guess):
        self.correct_guesses.append(guess)
        self.active_phrase.unviel(guess)
        self.art = art1
        self.message = 'correct'
        if len(self.correct_guesses) == len(self.active_phrase.answers):
            self.active_phrase.was_guessed = True
            clear()
            print(art1)
            print(f'YOU GUSSED "{str(self.active_phrase).upper()}". YOU WON THE GAME! CONGRADULATIONS!'.center(90))
            print(art1)
            print('')
            self.prompt_play()

    def incorrect(self):
        self.art = art2
        self.message = 'incorrect'
        self.lives -= 1
        if self.lives == 0:
            clear()
            print(art2)
            print('GAME OVER.'.center(90))
            print(art2)
            print('')
            self.prompt_play()

    def prompt_play(self):
        prompt = True
        while prompt:
            try:
                replay = input('Would you like to play again? (YES or NO): ').upper()
                if replay == 'YES':
                    self.reset()
                    prompt = False
                elif replay == 'NO':
                    self.running = False
                    clear()
                    print(art0)
                    print('Thank you for taking time to check out my program! - Carlos A Marin'.center(90))
                    input(art0)
                    prompt = False
                else:
                    raise ValueError
            except ValueError:
                input('Only "YES", and "NO" are valid entries.')

    def phrase_factory(self, phrases):
        phrase_list = []
        for phrase in phrases:
            phrase_list.append(phrasehunter.phrase.Phrase(phrase))
        return phrase_list

    def heart_factory(self):
        heart_lives = ''
        for life in range(self.lives):
            heart_lives += heart
        return heart_lives

    def reset(self):
        self.active_phrase.reset()
        self.active_phrase = random.choice(self.phrases)
        self.lives = 5
        self.guesses = []
        self.running = True
        self.correct_guesses = []
        self.art = art0
        self.message = None

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')
