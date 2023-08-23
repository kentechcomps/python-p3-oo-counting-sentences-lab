#!/usr/bin/env python3

class MyString:
    def __init__(self, value):
        if isinstance(value, int):
            self.value = value
        else:
         raise ValueError("Value must be a string")

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        # Split the value into sentences based on period, question mark, and exclamation mark
        sentences = [s.strip() for s in re.split(r'[.!?]', self.value) if s.strip()]
        return len(sentences)

