""" AUTHOR
 * Gautam Ankoji 
 * Saturday 17-02-2024 23:41:42 
"""

""" EXERCISE 05
    5.(b) Use built in string methods, functions and regular expressions
"""

import re

text = "Hello, this is a sample string containing 123 and some special characters like @#$."

# String methods
print("Original string:", text)
print("Uppercase:", text.upper())  # Convert to uppercase
print("Lowercase:", text.lower())  # Convert to lowercase
print("Titlecase:", text.title())  # Convert to titlecase
print("Length:", len(text))  # Length of the string
print("Count 's':", text.count("s"))  # Count occurrences of a substring

# Regular expressions
pattern = r"\d+"  # Matches one or more digits
numbers = re.findall(pattern, text)
print("Numbers found:", numbers)

# Replace special characters with spaces
clean_text = re.sub(r"[^\w\s]", " ", text)
print("Cleaned text:", clean_text)

# Split the string into words
words = text.split()
print("Words:", words)

# Filter out words containing 'is'
filteredWords = [word for word in words if "is" in word]
print("Words containing 'is':", filteredWords)


""" --------------[OUTPUT]--------------------

Original string: Hello, this is a sample string containing 123 and some special characters like @#$.
Uppercase: HELLO, THIS IS A SAMPLE STRING CONTAINING 123 AND SOME SPECIAL CHARACTERS LIKE @#$.
Lowercase: hello, this is a sample string containing 123 and some special characters like @#$.
Titlecase: Hello, This Is A Sample String Containing 123 And Some Special Characters Like @#$.
Length: 83
Count 's': 7
Numbers found: ['123']
Cleaned text: Hello  this is a sample string containing 123 and some special characters like
Words: ['Hello,', 'this', 'is', 'a', 'sample', 'string', 'containing', '123', 'and', 'some', 'special', 'characters', 'like', '@#$.']
Words containing 'is': ['this', 'is']

--------------[END-OF-OUTPUT]-------------- """
