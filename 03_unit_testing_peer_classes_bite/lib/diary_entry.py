class DiaryEntry:
    # Public properties:
    #   title: a string representing the title
    #   contents: a string representing the contents
    def __init__(self, title, contents):
        # title, contents are both strings
        # Side-effects: sets the title and contents properties
        self.title = title
        self.contents = contents

    def word_count(self):
        # Returns the word count of the contents
        return  len(self.contents.split())