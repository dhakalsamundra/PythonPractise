def main():
    answer = "n"
    while answer == "n":
        answer = input("Bored? (y/n)")
    print("Well, let's stop this then")

    # Multiplication table from 0 to 10
    number = int(input("Choose the number"))

    for i in range(1, 11):
        result = i * number
        print(f"{i} * {number} = {result}")

    # Multiplication table of 2 until it reach 100 using while loop
    number = int(input("Choose the number: "))
    i = 1
    while True:
        result = i * number
        print(f"{i} * {number} = {result}")
        if result > 100:
            break
        i += 1

    # Number series
    count = int(input("How many number do you want: "))
    for i in range(1, count + 1):
        if i % 3 == 0 and i % 7 == 0:
            print("zip boring")
        elif i % 3 == 0:
            print("zip")
        elif i % 7 == 0:
            print("boring")
        else:
            print(i)

    # number multiplication in both axis
    for i in range(1, 11):
        for j in range(1, 11):
            product = i * j
            print(
                f"{product:4}", end=""
            )  # product:4 gives 4 space and end="" ends as same line character. end(" ") provide space in inline end("--") add -- in same line. But by default, the end print newline character
        print()

    valid_answers = ["y", "Y", "n", "N"]

    while True:
        # Ask for the user's answer
        answer = input("Answer Y or N: ")

        # Check if the answer is valid
        if answer in valid_answers:
            print(f"You answered {answer}")
            break  # Exit the loop if the answer is valid
        else:
            print("Incorrect entry.")  # Inform the user about invalid input
    try:
        n = int(input("How many Fibonacci numbers do you want"))
        if n < 1:
            print("The number of fibonacci number should be at least one.")
            return

        previous_fib = 1
        current_fib = 1

        if n >= 1:
            print(f"1. {previous_fib}")

        if n >= 2:
            print(f"2. {current_fib}")

        for i in range(3, n + 1):
            next_fib = previous_fib + current_fib
            print(f"{i}. {next_fib}")

            previous_fib = current_fib
            current_fib = next_fib
    except ValueError:
        print("Bad input!")


if __name__ == "__main__":
    main()
