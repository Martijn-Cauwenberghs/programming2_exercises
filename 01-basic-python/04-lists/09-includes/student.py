# Write your code here
def includes(xs: list, ys: list):
    for y in ys:
        if y not in xs:
            return False
    return True