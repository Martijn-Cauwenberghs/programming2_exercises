# Write your code here
def drop_nth(xs: list, n: int):
    before_n = xs[:n]
    after_n = xs[n+1:]
    return[*before_n, *after_n]