class Diary:
    # Public properties:
    #   entries: a list of instances of DiaryEntry

    def __init__(self):
        self.entries = []

    def add(self, entry):
        self.entries.append(entry)

    def count_words(self):
        # Returns the number of words in all entries
        return sum([entry.count_words() for entry in self.entries]) 