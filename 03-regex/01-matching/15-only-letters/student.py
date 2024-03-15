
# Write your code here
import re
def only_letters(string):
    if re.fullmatch('([A-Z]|[a-z])*', string):
        return True