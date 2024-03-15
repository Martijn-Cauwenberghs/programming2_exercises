# Write your code here
import re
def only_digits(string):
    if re.fullmatch(r'[0123456789]{0,}', string):
        return True