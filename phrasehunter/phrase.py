import re
from phrasehunter.character import Character


class Phrase:
    def __init__(self, string):
        phrase_string = string.upper()
        self.phrase = self.phrase_generator(phrase_string)
        self.was_guessed = False
        # a set of individual letters
        self.answers = set(re.findall(r'[^ ]', phrase_string))

    def __str__(self):
        final = ''
        for char_obj in self.phrase:
            final += str(char_obj)
        return final

    def phrase_generator(self, string):
        word = []
        for letter in string:
            word.append(Character(letter))
        return word

    def reset(self):
        for character in self.phrase:
            character.was_guessed = False

    def unviel(self, letter):
        for character_obj in self.phrase:
            character_obj.check(letter)
            
