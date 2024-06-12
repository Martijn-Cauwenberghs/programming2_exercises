# Write your code here
def target_sum(ns: list, target: int):
    for i in ns:
        for j in ns:
            if i + j == target:
                return True
    return False