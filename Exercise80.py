import random

simulations = 10
total_flips = 0

for _ in range(simulations):
    flips = 0
    consecutive_count = 0
    previous_outcome = None

    while consecutive_count < 3:
        outcome = random.choice(["H", "T"])
        print(outcome, end=" ")
        flips += 1

        if outcome == previous_outcome:
            consecutive_count += 1
        else:
            consecutive_count = 1

        previous_outcome = outcome

    print("\nNumber of flips needed:", flips)
    total_flips += flips

average_flips = total_flips / simulations
print("\nAverage number of flips needed:", average_flips)