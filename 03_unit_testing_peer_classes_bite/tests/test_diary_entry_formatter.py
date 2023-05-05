from unittest.mock import Mock
from lib.diary_entry_formatter import DiaryEntryFormatter

def test_formats_diary_a_diary_entry():
    entry = Mock()
    entry.title = "Cool Title"
    entry.word_count.return_value = 55
    entry.contents = "Cool Contents"
    formatter = DiaryEntryFormatter(entry)
    assert formatter.format() == "Cool Title (55 words): Cool Contents"