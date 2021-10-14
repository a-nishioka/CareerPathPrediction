def get_back(target, text):
        idx = text.find(target)
        return text[idx+1:]

def get_forward(target, text):
        idx = text.find(target)
        return text[:idx]