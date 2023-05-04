from unittest.mock import Mock
from lib.music_library import MusicLibrary


def test_searches_by_keyword_mock():
    library = MusicLibrary()
    fake_matching = Mock()
    fake_matching.matches.return_value = True
    library.add(fake_matching)
    fake_not_matching = Mock()
    fake_not_matching.matches.return_value = False
    library.add(fake_not_matching)
    assert library.search("Hello") == [fake_matching]


"""
When I add multiple tracks 
and search for keywiord
I get tracks that match that keyword
"""

# def test_searches_by_keyword():
#     library = MusicLibrary()
#     fake_matching = FakeMatchingTrack()
#     library.add(fake_matching)
#     fake_not_matching = FakeNotMatchingTrack()
#     library.add(fake_not_matching)
#     assert library.search("Hello") == [fake_matching]



# class FakeMatchingTrack():
#     def matches(self, keyword):
#         return True


# class FakeNotMatchingTrack():
#     def matches(self, keyword):
#         return False

