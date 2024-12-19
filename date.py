def main():
    days_in_month = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }

    for month in range(1, 13):
        for day in range(1, days_in_month[month] + 1):
            print(f"{day}.{month}.", sep="")

    # Days in each month for 2014 (non-leap year)
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Starting point: January 3rd, 2014 is a Friday
    day = 3
    month = 1
    year = 2014

    # Print the first Friday with a full stop
    print(f"{day}.{month}.")

    # Calculate subsequent Fridays
    while month <= 12:
        # Move to the next Friday
        day += 7

        # If the day exceeds the number of days in the month, move to the next month
        while day > days_in_month[month - 1]:
            day -= days_in_month[month - 1]
            month += 1
            if month > 12:  # If month exceeds December, stop the loop
                break

        # Print the current Friday with a full stop if the month is still valid
        if month <= 12:
            print(f"{day}.{month}.")


if __name__ == "__main__":
    main()
