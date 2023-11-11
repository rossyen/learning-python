# add interest.py

def addInterest(balances, rate):
    for i in range(len(balances)):
        balances[i] = balances[i] * (1+rate)
    return balances

def test():
    amounts = [1000, 2200, 800, 360]
    rate = 0.05
    amounts = addInterest(amounts, rate)
    print(amounts)

test()