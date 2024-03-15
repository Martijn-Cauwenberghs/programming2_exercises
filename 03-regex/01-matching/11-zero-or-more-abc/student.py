# Write your code here
import re
def zero_or_more_abc(string):
    if re.fullmatch("(abc){0,}", string):
        return True