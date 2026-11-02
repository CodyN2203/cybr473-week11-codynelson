"""
Removal of special characters
"""

import re


text = "This is %% $#.. ,? test,, !! ~~ .."

cleaned_text = re.sub(r"[^A-Za-z]", " ", text)

print(text)
print(cleaned_text)

words_complex = text.split()
words_simple = cleaned_text.split()

print(words_complex)
print(words_simple)
