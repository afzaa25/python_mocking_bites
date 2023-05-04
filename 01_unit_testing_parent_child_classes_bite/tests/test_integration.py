import pytest
from lib.music_library import MusicLibrary
from lib.track import Track

"""
When I add multiple tracks
They are reflected in the track list
"""

def test_adds_and_lists_multiple_track():
    library = MusicLibrary()
    track_1 = Track("Calm Down", "Rema ft Selena Gomez")
    track_2 = Track("Calm Down", "Rema ft Selena Gomez")
    library.add(track_1)
    library.add(track_2)
    assert library.tracks == [track_1, track_2]


"""
When I add multiple tracks
and I search for a track title
Then i get the matching track back
"""

def test_searches_for_trac_by_full_title():
    library = MusicLibrary()
    track_1 = Track("Calm Down", "Rema ft Selena Gomez")
    track_2 = Track("Peru", "Fireboy DML")
    library.add(track_1)
    library.add(track_2)
    assert library.search("Calm Down") == [track_1]