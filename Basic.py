def main():
    name = input("Tell your name:")  # This will show user a prompt to fill the input.
    print(f"Hi {name}")
    print(
        "Good you are doing personal development. Python is good language to Learn. Good Luck"
    )

    try:
        mood = int(input("How do you feel? (1-10)"))

        # Check the mood inputted number
        if 1 <= mood <= 10:
            if mood == 10:
                print("Wow, Great to know that you are in jolly mood.")
            elif mood == 1:
                print("So Sad to hear that you are not in Good mood.")
            elif mood > 7:
                print("Seems like something is going on today.")
            elif mood < 4:
                print(
                    "Try to do something different so that you mood may change and you feel happy."
                )
            else:
                print("Don't forget to smile.")

    except ValueError:
        print("Bad input!")

    # simple game
    try:
        # Take inputs from both players
        player1 = input(
            "Player 1, enter your choice (R/P/S): "
        ).upper()  # .Strip() method is used to remove any leading or trailing whitespace from the user input, ensuring the response is properly formatted.
        player2 = input("Player 2, enter your choice (R/P/S): ").upper()

        # Valid choices
        valid_choices = {"R", "P", "S"}

        # Check if both inputs are valid
        if player1 not in valid_choices or player2 not in valid_choices:
            raise ValueError("Invalid input! Only R, P, S are allowed.")

        # Determine the result
        if player1 == player2:
            print("It's a tie!")
        elif (
            (player1 == "R" and player2 == "S")
            or (player1 == "P" and player2 == "R")
            or (player1 == "S" and player2 == "P")
        ):
            print("Player 1 won!")
        else:
            print("Player 2 won!")

    except ValueError as e:
        print(e)

    # Bus ticket
    try:
        age = int(input("Please, enter your age: "))

        if age < 7:
            price = 0.0
        elif age < 17:
            price = 1
        elif age < 25:
            price = 1.5
        else:
            price = 3

        if price == 0.0:
            print(f"Your ride will cost: {price:.1f}")
        else:
            print(f"Your ride will cost: {price:.2f}")
    except ValueError:
        print("Bad input!")

    # Calculate Changes
    try:
        purchase_price = int(input("Purchase price: "))
        paid_price = int(input("Paid amount of money: "))

        # calculate changes
        change = paid_price - purchase_price
        if change < 0:
            print("No Changes.")
        elif change == 0:
            print("No Changes.")
        else:
            print("Offer changes: ")

            # Calculate the total count of 20 euro notes
            twenty_euro_notes = change // 20
            if twenty_euro_notes > 0:
                print(f"{twenty_euro_notes} twenty euro notes.")
            # cross check the reminder
            change %= 20

            ten_euro_notes = change // 10
            if ten_euro_notes > 0:
                print(f"{ten_euro_notes} ten euro notes.")
            change %= 10

            five_euro_notes = change // 5
            if five_euro_notes > 0:
                print(f"{five_euro_notes} five euro notes.")
            change %= 5

            two_euro_notes = change // 2
            if two_euro_notes > 0:
                print(f"{two_euro_notes} two euro notes.")
            change %= 2

            one_euro_notes = change // 1
            if one_euro_notes > 0:
                print(f"{one_euro_notes} one euro notes.")

    except ValueError:
        print("Bad input!")

    # Student monthly allowance
    try:
        # Prompt the user for the amount of study benefits
        benefits_amount = int(input("Enter your monthly allowance: "))

        # Convert the input to a floating-point number
        benefits = float(benefits_amount)

        # Define the index raise percentage
        index_raise = 1.17 / 100  # Convert the percentage to decimal

        # Calculate the first raise
        first_benefits_raise = benefits * (1 + index_raise)

        # Calculate the second raise on the new amount
        second_benefits_raise = first_benefits_raise * (1 + index_raise)

        # format the benefits
        def format_benefit1(value):
            if value < 0:
                return f"{value:.4f} euros."
            elif value == round(value, 3):
                return f"{value:.3f} euros."
            else:
                return f"{value:.6f} euros."

        def format_benefit2(value):
            if value < 0:
                return f"{value:.16f} euros."
            elif value == round(value, 10):
                return f"{value:.10f} euros"
            else:
                return f"{value:.15f} euros"

        # Print the results
        print("If the index raise is 1.17 percentage, the monthly benefits,")
        print(f"after a raise would be {format_benefit1(first_benefits_raise)}")
        print("And if there was another index raise, the study")
        print(f"benefit would be as much as {format_benefit2(second_benefits_raise)}")

    except ValueError:
        print("Bad input!")


# Below code is required to trigger main function to call
if __name__ == "__main__":
    main()
