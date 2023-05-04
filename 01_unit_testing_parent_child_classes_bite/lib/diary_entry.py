class DiaryEntry:
    # Public properties:
    #   title: string
    #   contents: string

    def __init__(self, title, contents):
        # title, contents are both strings
        self.title = title
        self.contents = contents

    def count_words(self):
        # Returns the number of words in the contents
        return len(self.contents.split())
