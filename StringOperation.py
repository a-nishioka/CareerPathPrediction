class StringOperation:
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