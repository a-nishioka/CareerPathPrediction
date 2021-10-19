import string
import unicodedata

class StringOperation:
    
    def __init__(self):
        return

    def __del__(self):
        return

    def get_forward(self, target, text):
        idx = text.find(target)
        if(idx > 0):
            return text[idx+1:]
        else:
            return ""

    def get_back(self, target, text):
        idx = text.find(target)
        if(idx > 0):
            return text[:idx]
        else:
            return ""

    def replace(self, target, replaced, text):
        return text.replace(target, replaced)

    def remove_punctuation(self, text):
        text = unicodedata.normalize("NFKC", text)
        result = text.translate(str.maketrans( '', '', string.punctuation + "「」、。・"))
        return result
