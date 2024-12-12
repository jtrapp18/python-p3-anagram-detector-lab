# your code goes here!

class Anagram:

    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        return [w for w in word_list if set(w)==set(self.word)]

listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana']))