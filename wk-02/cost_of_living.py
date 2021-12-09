# PROJECT: (WK-02) Cost of living
# Solution written by Darren Halpin

v_rent = float(input("Rent per month: "))
v_gas = float(input("Gas payment per month: "))
v_elec = float(input("Electricity payment per month: "))
v_water = float(input("Water payment per month: "))
v_ctax = float(input("Council tax payment per month: "))

total_bills = v_rent + v_gas + v_elec + v_water + v_ctax

print("Your monthly expenses are:")

print(
    "{:<16}£{:>8.2f}"
    .format("Rent:", v_rent)
)

print(
    "{:<16}£{:>8.2f}"
    .format("Gas:", v_gas)
)

print(
    "{:<16}£{:>8.2f}"
    .format("Electricity:", v_elec)
)

print(
    "{:<16}£{:>8.2f}"
    .format("Water:", v_water)
)

print(
    "{:<16}£{:>8.2f}"
    .format("Council Tax:", v_ctax)
)

print("=" * 25)

print(
    "{:<16}£{:>8.2f}"
    .format("Total:", total_bills)
)

print("=" * 25)

