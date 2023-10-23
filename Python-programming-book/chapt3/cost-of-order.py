# cost-of-oder.py
#   A program that calculates the cost of a order
#   This program har two variables: price pr. pound and fixed cost

#   Get input on price pr. pound and fixed cost
#   Calculate cost per order
#   Calculate profit per order
#   Print result to user

def cost_per_oder():
    print('Enter the numbers to see cost of an order.')
    cost_weight = float(input('Cost pr. pound: '))
    cost_fixed = float(input('Fixed cost: '))
    selling_price =float(input('Selling price: '))

    total_cost = cost_fixed + cost_weight
    profit = selling_price - total_cost

    print(f'For every order you sell at {selling_price:.2f}, you spend a total of {total_cost:.2f} and earn {profit:.2f}.')

cost_per_oder()
    