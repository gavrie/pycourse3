"""
Write a spell checker, similar to the Unix 'spell' utility, that verifies the
spelling of its input.
The output should be a list of the *incorrectly* spelled words.
"""

import spell

def test_split_line():
    assert spell.split_line("hello world") == ["hello", "world"]
    assert spell.split_line("hello, world") == ["hello", "world"]
    assert spell.split_line("Hello, world!") == ["Hello", "world"]

def test_strip_punctuation():
    words = [
        ("hello", "hello"),
        ("hello,", "hello"),
        ("doesn't", "doesnt"),
        ("[hello]", "hello"),
        ("(hello)", "hello"),
    ]

    for before, after in words:
        assert spell.strip_punctuation(before) == after

def test_spell():
    words = [
        ("Hello world", []),
        ("Helo world", ["Helo"]),
        ("helo world", ["helo"]),
        ("It's a brave new world", []),
        ("It's a brxve new wyrld", ["brxve", "wyrld"]),
    ]

    for text, errors in words:
        assert spell.check(text) == errors
