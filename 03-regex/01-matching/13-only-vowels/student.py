# Write your code here
import re
def only_vowels(string):
    if re.fullmatch("(a|e|i|o|u){0,}", string):
        return True