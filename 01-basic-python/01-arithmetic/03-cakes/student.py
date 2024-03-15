# Write your code here
def cakes(eggs, butter, flour):
    maxeggs = eggs//5
    maxbutter = butter//250
    maxflour = flour//250

    return min(maxeggs, maxbutter, maxflour)
