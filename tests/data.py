"""Test data"""

edit_distance_test_data = [
    ('a', 'a', 0),
    ('a', 'aa', 1),
    ('aa', 'a', 1),
    ('aoe', 'aee', 1),
    ('aaaa', 'aaaa', 0),
    ('foo bar baz', 'foobarbaz', 2),
    ('foo bar baz', 'foo barbaz', 1),
    ('foo bar baz', 'foo barbas', 2),
    ('foo bar baz', 'foo  barbas', 3)
]