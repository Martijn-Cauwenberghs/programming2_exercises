# Write your code here
import re

def contains_a(string):
    if re.search(r'.*a.*', string):
        return True