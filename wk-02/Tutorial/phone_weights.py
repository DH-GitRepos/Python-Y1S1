# phone weight example

# define constant
OUNCE = 0.035247

# define variables
phone1 = "Nokia 220"
phone2 = "Alcatel 1X"
phone3 = "Motorola Moto E6 Play"

g_phone1 = 86.5
g_phone2 = 130
g_phone3 = 140

# calculate ounce weights
oz_phone1 = g_phone1 * OUNCE
oz_phone2 = g_phone2 * OUNCE
oz_phone3 = g_phone3 * OUNCE

# output formatted table

# - long print notation
# print("Phone".ljust(22), "|", "Grams".rjust(6), "|", "Ounces".rjust(6), sep='') - or below syntax

# - short print notation (format specification mini-language)
print(
    "{0:<22}|{1:>6}|{2:>6}"
        .format("Phone", "Grams", "Ounces")
)

# print("=".center(36, "=")) - or the below line is shorter
print("=" * 36)

# print(
#    phone1.ljust(22), "|",
#    str(g_phone1).rjust(6), "|",
#    str(round(oz_phone1, 2)).rjust(6),
#    sep='')

print(
    "{:<22}|{:>6.2f}|{:>6.2f}"
        .format(phone1.title(), g_phone1, oz_phone1)
)

print(
    "{:<22}|{:>6.2f}|{:>6.2f}"
        .format(phone2.title(), g_phone2, oz_phone2)
)

print(
    "{:<22}|{:>6.2f}|{:>6.2f}"
        .format(phone3.title(), g_phone3, oz_phone3)
)



