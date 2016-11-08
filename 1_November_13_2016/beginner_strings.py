#!/usr/bin/python

import unittest, sys
from cStringIO import StringIO
from contextlib import contextmanager

def hello_name(name):
    """ Add code to make this function print 'Hello <name>!' for the name inputted.
    For exampl,e hello_name('Mike') should print 'Hello Mike!' to the console."""

    # REPLACE 'pass' WITH YOUR CODE HERE
    pass

def make_html_tags(text, tag):
    """ Add code to return the input text surrounded by an appropriate html/xml
    tag.  For example, make_html_tage('This is my text', 'html') should return
    "<html>This is my text</html>". Note that the first tag is <tag> while the 
    second tag is </tag>.  The '/' represents a closing tag."""

    # YOUR CODE HERE - STORE THE RESULT IN THE VARIABLE NAMED 'html_tags'

    # STORE YOUR RESULT HERE
    html_tags = None
    return html_tags


def is_a_palindrome(word):
    """ A palindrome is a word that is the same spelled both forwards and 
    backwards.  For example, 'racecar' is a palindrom, as is the name 'Hannah'.
    Notably, the case (uppercase or lowercase) does not matter when determining
    whether a word is a palindrome - so 'Hannah' is considered equal to 'hannaH'.
    Your challenge is to write this function so that it takes a word and returns
    'True' if the word is a palindrome and 'False' if it is not."""

    # YOUR CODE HERE - STORE THE RESULT IN THE VARIABLE NAME 'palindrome'

    palindrome = None # Should be either True or False
    return palindrome


""" This section of the code is used to test the code you wrote.  You can safely
ignore these sections, but feel free to look and ask questions if you're interested"""

class TestStrings(unittest.TestCase):
    def test_hello_name(self):
        with capture() as out:
            hello_name('Mike')
            output = out.getvalue()
        self.assertEquals(output, 'Hello Mike!\n')

        with capture() as out:
            hello_name('Theo')
            output = out.getvalue()
        self.assertEquals(output, 'Hello Theo!\n')

    def test_html_tags(self):
        self.assertEquals(make_html_tags('Test text.', 'html'), '<html>Test text.</html>')
        self.assertEquals(make_html_tags('xml text', 'xml'), '<xml>xml text</xml>')

    def test_palindrome(self):
        self.assertTrue(is_a_palindrome('racecar'))
        self.assertTrue(is_a_palindrome('RaceCar'))
        self.assertTrue(is_a_palindrome('Hannah'))
        self.assertTrue(is_a_palindrome('NoXinNixon'))
        self.assertFalse(is_a_palindrome('palindrome'))

@contextmanager
def capture():
    oldout = sys.stdout
    try:
        out = StringIO()
        sys.stdout = out
        yield out
    finally:
        sys.stdout = oldout
        out = out.getvalue()

if __name__ == '__main__':
    unittest.main()


