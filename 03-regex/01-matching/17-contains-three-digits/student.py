
# Write your code here
import re

def contains_three_digits(string):
    if re.fullmatch(r'(...*[0-9])', string):
        return True