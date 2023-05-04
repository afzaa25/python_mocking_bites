from lib.track import Track

"""
Given a title and an artist
and a search keyword for the full title
matches is true
"""

def test_matches_full_title():
    track = Track("Cat", "Dog")
    assert track.matches("Cat") == True

"""
Given a title and an artist
and a search keyword for a partial title
matches is true
"""
def test_matches_partial_title():
    track = Track("Calm Down", "Rema ft Selena Gomez")
    assert track.matches("Calm") == True


"""
Given a title and an artist
and a search keyword for a full artist
matches is true
"""

def test_matches_full_artist():
    track = Track("Calm Down", "Rema ft Selena Gomez")
    assert track.matches("Rema ft Selena Gomez") == True


"""
Given a title and an artist
and a search keyword for a partial artist
matches is true
"""
def test_matches_partial_artist():
    track = Track("Calm Down", "Rema ft Selena Gomez")
    assert track.matches("Rema") == True


"""
Given a title and an artist
and a search keyword that does not match either
matches is false
"""
def test_does_not_match_artist_or_title():
    track = Track("Calm Down", "Rema ft Selena Gomez")
    assert track.matches("Frog") == False
