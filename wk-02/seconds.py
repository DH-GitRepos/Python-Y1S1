# PROJECT: (WK-02) Seconds
# Solution written by Darren Halpin

user_input = input("Please enter the number of seconds\n(whole number): ")

# validate input
try:
    seconds_in = int(user_input)
except ValueError:
    print("ERROR: Input is not a whole number.")
    exit()

# how many hours, and what's left in seconds
calc_hours = seconds_in // 3600
remaining_seconds = seconds_in - (calc_hours * 3600)

# how many minutes, and what's left in seconds
calc_minutes = remaining_seconds // 60
seconds_left = remaining_seconds - (calc_minutes * 60)

# output breakdown
print(
    "{:<10}{:>5}{:>15}{:>15}"
    .format("Input", "Hours", "Minutes", "Seconds")
)

print(
    "{:<10}{:>5}{:>15}{:>15}"
    .format(seconds_in, calc_hours, calc_minutes, seconds_left)
)

