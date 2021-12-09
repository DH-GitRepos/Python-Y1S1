# PROJECT: (WK-02) Weekly shop
# Solution written by Darren Halpin

peaches_qty = int(input("Peaches\n-how many? "))
peaches_price = float(input("-price? "))
peaches_cost = peaches_price * peaches_qty

beans_qty = int(input("Beans\n-how many? "))
beans_price = float(input("-price? "))
beans_cost = beans_price * beans_qty

chicken_qty = int(input("Chicken pieces\n-how many? "))
chicken_price = float(input("-price? "))
chicken_cost = chicken_price * chicken_qty

socks_qty = int(input("Socks\n-how many? "))
socks_price = float(input("-price? "))
socks_cost = socks_price * socks_qty

water_qty = int(input("Bottle of water\n-how many? "))
water_price = float(input("-price? "))
water_cost = water_price * water_qty

total_items = peaches_qty + beans_qty + chicken_qty + socks_qty + water_qty

total_cost = peaches_cost + beans_cost + chicken_cost + socks_cost + water_cost

print("Total number of items purchased: " + str(total_items) + "\nTotal weekly shop cost: " + str(total_cost))

