values_match = "a" == "b"
match values_match:
    case True:
        print("Values are the same")
    case False:
        print("Values are different")

boolVal = "a" == "b"
match boolVal:
    case True:
        print("Values are the same")
    case False:
        print("Values are different")


drink = input("coffee, tea, or hot chocolate: ")
strength = input("weak, normal, strong: ")
sugar = input("Do you want sugar (y/n)?: ")

if sugar.casefold() == "y":
    sugar_qty = input("How many sugars: ")

else:
    match drink.casefold():
        case "coffee":
            print("coffee, " + strength + ", sugar: " + sugar)
        case "tea":
            print("tea, " + strength + ", sugar: " + sugar)
        case "hot chocolate":
            print("hot chocolate, " + strength + ", sugar: " + sugar)
