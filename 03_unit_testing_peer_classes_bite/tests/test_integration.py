import pytest
from unittest.mock import Mock
from lib.diary_entry_formatter import DiaryEntryFormatter
from lib.diary_entry import DiaryEntry



def test_formats_diary_a_diary_entry():
    entry = DiaryEntry("Cool Title", "Cool Contents")
    formatter = DiaryEntryFormatter(entry)
    assert formatter.format() == "Cool Title (2 words): Cool Contents"