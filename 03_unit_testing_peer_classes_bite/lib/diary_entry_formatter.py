# File: lib/diary_entry_formatter.py

class DiaryEntryFormatter:
    def __init__(self, diary_entry):
        # diary_entry is an instance of DiaryEntry
        self.diary_entry = diary_entry

    def format(self):
        # Returns a nicely formatted diary entry like this:
        #   My Title (2 words): My Contents
        title = self.diary_entry.title
        contents = self.diary_entry.contents
        word_count = self.diary_entry.word_count()
        return f"{title} ({word_count} words): {contents}"