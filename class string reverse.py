class StringReverse:
    def __init__(self, text):
        self.__text = text

    def reverse_words(self):
        words = self.__text.split()
        reversed_words = words[::-1]
        return " ".join(reversed_words)

    def __str__(self):
        return self.reverse_words()


s = StringReverse("Hello World from Python")
print(s)
