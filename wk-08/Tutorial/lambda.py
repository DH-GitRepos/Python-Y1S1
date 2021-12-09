phone_grams = [6.7, 5.2, 8.4, 4.3, 9.7]
oz_conv = map(lambda grams: float("{:.2f}".format(grams * 0.035274)), phone_grams)
phone_oz = list(oz_conv)
print(phone_grams)
print(phone_oz)
