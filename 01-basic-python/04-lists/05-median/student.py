# Write your code here
def median(ns: list[int]) -> int:
    ns.sort()
    if len(ns) % 2 != 0:
        return ns[len(ns)//2]
    else:
        length = len(ns)
        value1 = ns[(length//2)]
        value2 = ns[(length//2)-1]
        return ((value1+value2)/2)