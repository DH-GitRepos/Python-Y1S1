# PROJECT: (WK-03) Bandwidth headache
# Solution written by Darren Halpin

MAX_NETWORK_BANDWIDTH_MEGABITS = 1000
NUMBER_CON_USERS = 200
BANDWIDTH_APP_A_BPS = 200000
BANDWIDTH_APP_B_BPS = 100000
BANDWIDTH_APP_NEW = 350000

bps_network_capacity = MAX_NETWORK_BANDWIDTH_MEGABITS * pow(10, 6)

bps_current_usage = (BANDWIDTH_APP_A_BPS + BANDWIDTH_APP_B_BPS) * NUMBER_CON_USERS

bps_current_availability = bps_network_capacity - bps_current_usage

bps_new_app_req = BANDWIDTH_APP_NEW * NUMBER_CON_USERS

bps_with_new_app = bps_network_capacity - (bps_new_app_req + bps_current_usage)
mbps_with_new_app = bps_with_new_app * pow(10, -6)

print("=" * 54)

print(
    "{:<35}|{:>5}|{:>12}"
    .format("BANDWIDTH INFO", "UNIT", "QTY")
)

print("=" * 54)

print(
    "{:<35}|{:>5}|{:>12}"
    .format("Current network capacity:", "bps", bps_network_capacity)
)

print(
    "{:<35}|{:>5}|{:>12}"
    .format("Current usage:", "bps", bps_current_usage)
)

print(
    "{:<35}|{:>5}|{:>12}"
    .format("Current availability:", "bps", bps_current_availability)
)

print(
    "{:<35}|{:>5}|{:>12}"
    .format("New application requirement:", "bps", bps_new_app_req)
)

print("-" * 54)

print(
    "{:<35}|{:>5}|{:>12}"
    .format("Bandwidth available with new app", "Mbps", int(mbps_with_new_app))
)

print("=" * 54)

