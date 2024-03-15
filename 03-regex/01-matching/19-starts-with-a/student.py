# Write your code here
import re

def starts_with_a(string):
    if re.search(r'^a.*',string):
        return True