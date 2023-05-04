from unittest.mock import Mock
from lib.diary import Diary


def test_diary_counts_words_in_all_entries_with_mocks():
    diary = Diary()

    fake_two_word_diary_entry = Mock()
    fake_two_word_diary_entry.count_words.return_value = 2

    fake_three_word_diary_entry = Mock()
    fake_three_word_diary_entry.count_words.return_value = 3

    diary.add(fake_two_word_diary_entry)
    diary.add(fake_three_word_diary_entry)

    assert diary.count_words() == 5


# def test_diary_counts_words_in_all_entries():
#     diary = Diary()
#     entry_mock_1 = Mock()
#     entry_mock_1.count_words.return_value = 4 
#     diary.add(FakeThreeWordDiaryEntry())
#     diary.add(FakeTwoWordDiaryEntry())
#     assert diary.count_words() == 6

    
# class FakeTwoWordDiaryEntry:
#     def count_words(self):
#         return 4


# class FakeThreeWordDiaryEntry:
#     def count_words(self):
#         return 2