class StringOperation:
    def get_back(self, target, text):
        idx = text.find(target)
        return text[idx+1:]

    def get_forward(self, target, text):
        idx = text.find(target)
        return text[:idx]