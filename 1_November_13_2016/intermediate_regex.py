import re

def find_examples(text):
    """Find instances of the word 'example' in a block of text"""
    regex = re.compile('[eE]xample')
    matches = re.findall(regex, text)
    return matches

def find_full_names(text):
    """Define a regex pattern that will look for full names within a block of text.
    Full names are defined by the pattern of two consecutive capitalized words, where
    each word must be at least two characters long (so 'Di' should match, but not 'D')"""
    regex = re.compile('insert_names_pattern_here')
    matches = re.findall(regex, text)
    return matches

def find_zip_codes(text):
    """Zip codes should match a pattern with five consecutive digits"""
    regex = re.compile('inser_zip_code_pattern_here')
    matches = re.findall(regex, text)
    return matches

def find_city_state_addresses(text):
    """City State addresses are of the form 'City, ST', for example Boston, MA or 
    New York, NY. City names may be more than one word but must start with a capital 
    letter, whereas state abbreviations are two capital letters following a comma"""
    # Your Code Here
    pass

def find_email_addresses(text):
    """Email addresses follow the pattern 'user_name@domain.TLD'.  User names can
    essentially be anything but cannot contain special characters.  The user name 
    is seperated from the domain by the '@' symbol, and the domain is separated
    from the Top Level Domain (TLD) by a '.'."""
    # Your Code Here
    pass

if __name__ == '__main__':
    ex = "Example of finding examples!"
    names = "Hello, my name is John Smith.  My best friend's name is William Shakespeare.  My mom is Jane Smith-Johnson"
    zips = "The zip code for New York is 10031 or 10022 or similar.  The zip code in the North East is 01801. This is not a zip: 123 or 4082"
    city_st = "We live in New York, NY.  Hollywood is in Los Angeles, CA.  Silicon Valley is in San Francisco, CA.  The Eagles are from Philadelphia, PA"
    emails = "Hey, check out my new email myname@gmail.com.  My work email is potus@whitehouse.gov.  Don't use my old email, old_email@ngo.org."
    print find_examples(ex)
    print find_full_names(names)
    print find_zip_codes(zips)
    print find_city_state_addresses(city_st)
    print find_email_addresses(emails)

