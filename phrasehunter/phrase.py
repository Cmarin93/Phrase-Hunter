import re
from phrasehunter.character import Character


class Phrase:
    def __init__(self, phrase_string):
        phrase_string = phrase_string.upper()
        self.phrase = self.character_factory(phrase_string) # a list of character objects.
        self.original = phrase_string
        self.was_guessed = False
        self.answers = set(re.findall(r'[^ ]', phrase_string))

    def __str__(self):
        final = ''
        for char_obj in self.phrase:
            final += str(char_obj)
        return final

    def __iter__(self):
        yield from self.original

    def character_factory(self, phrase_string):
        character_list = []
        for single_character in phrase_string:
            character_list.append(Character(single_character))
        return character_list

    def reset(self):
        for character in self.phrase:
            character.was_guessed = False

    def unviel(self, letter):
        for character_obj in self.phrase:
            character_obj.check(letter)
            
