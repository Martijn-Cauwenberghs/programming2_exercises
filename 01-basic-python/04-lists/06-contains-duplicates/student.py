# Write your code here
def contains_duplicates(xs: list):
    ns = []
    for i in xs:
        if i not in ns:
            ns.append(i)
        else: return True
    return False