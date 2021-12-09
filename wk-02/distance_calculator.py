# PROJECT: (WK-02) Distance calculator
# Solution written by Darren Halpin

print("Distance calculator")
print("=" * 19)

initial_velocity = float(input("\nEnter initial velocity (u)\n(meters per second): "))       # u
time_taken = float(input("Enter time taken (t)\n(seconds): "))                               # t
acceleration = float(input("Enter acceleration rate (a) \n(meters per sec per sec): "))      # a

distance = (initial_velocity * time_taken) + 0.5 * acceleration * pow(time_taken, 2)         # s

print("\nDistance travelled (s) = " + str(distance) + " m")

