# PROJECT: (WK-01) Break even
# Solution written by Darren Halpin

cost_per_item = float(20.00)
cost_fixed = float(50000.00)
sale_price = float(40.00)

item_profit = sale_price - cost_per_item
units_to_breakeven = cost_fixed / item_profit

print("Cost to produce each item: " + str(cost_per_item))
print("Sale price for each item: " + str(sale_price))
print("Fixed costs: " + str(cost_fixed))
print("Profit per item: " + str(item_profit))
print("Breakeven: " + str(units_to_breakeven) + " items.")

