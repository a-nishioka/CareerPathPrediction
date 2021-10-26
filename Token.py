import janome
from janome.tokenizer import Tokenizer


class Token:
    tokenizer = Tokenizer(wakati=False)

    def __init__(self):
        self.tokenizer = Tokenizer(wakati=False)

    def __del__(self):
        del self.tokenizer

    def get_part_of_speech(self, part_of_speech_list, text):
        result = []
        for token in self.tokenizer.tokenize(text):
            pos = token.part_of_speech.split(',')[0]
            if pos in part_of_speech_list:
                result.append(token.surface)
        return result