from lib.diary_entry import DiaryEntry



def test_constructs_with_title_and_contents():
    entry = DiaryEntry("Cool Title", "Cool Contents")
    assert entry.title == "Cool Title"
    assert entry.contents == "Cool Contents"



def test_count_word():
    entry = DiaryEntry("Cool Title", "Cool Contents")
    assert entry.word_count() == 2