def count_smaller(numbers, threshold):
    if not numbers:
        return None

    count = 0
    for num in numbers:
        if num < threshold:
            count += 1

    return count


def main():
    age = int(input("Whats your age: "))
    time = int(input("What time you are trying to travel: "))

    if age < 3:
        price = 0.0
    elif 3 <= age <= 15 or age >= 65:
        if 6 <= time < 18:
            price = 1.7
        elif 18 <= time < 23:
            price = 2.5
        else:
            price = 3.0
    else:
        if 6 <= time < 18:
            price = 2.7
        elif 18 <= time < 23:
            price = 3.5
        else:
            price = 4
    print(f"Your ride will cost: {price:.1f}")


def character_count():

    s = input("Enter the character: ")
    count_character = {}

    for char in s:
        if char in count_character:
            count_character[char] += 1
        else:
            count_character[char] = 1

    unique_count = 0
    for count in count_character.values():
        if count == 1:
            unique_count += 1

    print(f"The unique character count is: {unique_count}")


if __name__ == "__main__":
    main()
    character_count()
    print(f"The smaller number count is: {count_smaller([1, 2, 3], 3)}")
