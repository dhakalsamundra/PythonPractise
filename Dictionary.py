def groceryDictionary():
    PRICES = {
        "milk": 1.09,
        "fish": 4.56,
        "bread": 2.10,
        "chocolate": 2.7,
        "grasshopper": 13.25,
        "sushi": 19.9,
        "noodles": 0.97,
        "beans": 0.87,
        "bananas": 1.05,
        "Pepsi": 3.15,
        "pizza": 4.15,
    }
    while True:
        user_input = input("Enter product name: ").strip()
        if user_input == "":
            break

        item = user_input.lower()
        if item in PRICES:
            price = PRICES[item]
            print(f"The price of {item} is {price:.2f} e")
        else:
            print(f"Error: {item} is unknown.")


def touristDictionary():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}

    while True:
        command = (
            input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ").strip().upper()
        )

        if command == "W":
            word = input("Enter the word to be translated: ").strip().lower()
            if word in english_spanish:
                print(f"{word} in Spanish is {english_spanish[word]}")
            else:
                print(f"The word {word} could not be found from the dictionary.")

        elif command == "A":
            english_word = (
                input("Give the word to be added in English: ").strip().lower()
            )
            spanish_word = (
                input("Give the word to be added in Spanish: ").strip().lower()
            )
            english_spanish[english_word] = spanish_word
            # print(f"Word '{english_word}' added successfully.")

        elif command == "R":
            word = input("Give the word to be removed: ").strip().lower()
            if word in english_spanish:
                del english_spanish[word]
                # print(f"Word '{word}' removed successfully.")
            else:
                print(f"The word {word} could not be found from the dictionary.")

        elif command == "P":
            for english, spanish in sorted(english_spanish.items()):
                print(f"{english} {spanish}")

        elif command == "T":
            sentence = (
                input("Enter the text to be translated into Spanish: ").strip().lower()
            )
            words = sentence.split()
            translated_sentence = []
            for word in words:
                translated_sentence.append(english_spanish.get(word, word))
            print("The text, translated by the dictionary:")
            print(" ".join(translated_sentence))

        elif command == "Q":
            print("Adios!")
            break

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")


def print_dict_contents(dictionary):
    if dictionary:
        keys_sorted = sorted(dictionary.keys())
        print("Dictionary contents:")
        print(", ".join(keys_sorted))
    else:
        print("Dictionary is empty")


def alphabeticalOrder():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}
    print_dict_contents(english_spanish)

    while True:
        command = (
            input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ").strip().upper()
        )

        if command == "W":
            word = input("Enter the word to be translated: ").strip().lower()
            if word in english_spanish:
                print(f"{word} in Spanish is {english_spanish[word]}")
            else:
                print(f"The word {word} could not be found from the dictionary.")

        elif command == "A":
            english_word = (
                input("Give the word to be added in English: ").strip().lower()
            )
            spanish_word = (
                input("Give the word to be added in Spanish: ").strip().lower()
            )
            english_spanish[english_word] = spanish_word
            print_dict_contents(english_spanish)

        elif command == "R":
            word = input("Give the word to be removed: ").strip().lower()
            if word in english_spanish:
                del english_spanish[word]
                # print(f"Word '{word}' removed successfully.")
            else:
                print(f"The word {word} could not be found from the dictionary.")

        elif command == "P":
            print_dict_contents(english_spanish)

        elif command == "T":
            sentence = (
                input("Enter the text to be translated into Spanish: ").strip().lower()
            )
            words = sentence.split()
            translated_sentence = []
            for word in words:
                translated_sentence.append(english_spanish.get(word, word))
            print("The text, translated by the dictionary:")
            print(" ".join(translated_sentence))

        elif command == "Q":
            print("Adios!")
            break

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")


def displayAddedContent():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}
    print("Dictionary contents:")
    print(", ".join(sorted(english_spanish)))

    while True:
        command = (
            input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ").strip().upper()
        )

        if command == "W":
            word = input("Enter the word to be translated: ").strip().lower()
            if word in english_spanish:
                print(f"{word} in Spanish is {english_spanish[word]}")
            else:
                print(f"The word {word} could not be found in the dictionary.")

        elif command == "A":
            english_word = (
                input("Give the word to be added in English: ").strip().lower()
            )
            spanish_word = (
                input("Give the word to be added in Spanish: ").strip().lower()
            )
            english_spanish[english_word] = spanish_word
            print("Dictionary contents:")
            print(", ".join(sorted(english_spanish)))

        elif command == "R":
            word = input("Give the word to be removed: ").strip().lower()
            if word in english_spanish:
                del english_spanish[word]
            else:
                print(f"The word {word} could not be found in the dictionary.")

        elif command == "P":
            print("\nEnglish-Spanish")
            for word in sorted(english_spanish):
                print(f"{word} {english_spanish[word]}")

            # Create a Spanish-English dictionary for sorting by Spanish words
            spanish_english = {
                spanish: english for english, spanish in english_spanish.items()
            }
            print("\nSpanish-English")
            for spanish_word in sorted(spanish_english):
                print(f"{spanish_word} {spanish_english[spanish_word]}")
            print()  # Empty line after printout

        elif command == "T":
            sentence = (
                input("Enter the text to be translated into Spanish: ").strip().lower()
            )
            translated_sentence = [
                english_spanish.get(word, word) for word in sentence.split()
            ]
            print("The text, translated by the dictionary:")
            print(" ".join(translated_sentence))

        elif command == "Q":
            print("Adios!")
            break

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")


def wordDensityCalculator():
    word_count = {}
    print("Enter rows of text for word counting. Empty row to quit.")
    while True:
        line = input().strip().lower()
        if line == "":
            break
        words = line.split()
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    for word in sorted(word_count):
        print(f"{word} : {word_count[word]} times")


def calculate_average(song_result):
    return sum(song_result.values()) / len(song_result)


def dancingGame():
    SONG_RESULT = {
        "Bubble dancer": 93.4,
        "The Game": 92.03,
        "Vertex": 75.3,
        "Lemmings on the Run": 86.2,
        "Da Roots": 96.02,
        "Charlene": 75.3,
        "Disconnected": 86.3,
        "Fly away": 87.32,
        "Hybrid": 63.9,
        "My favourite game": 89.45,
        "Oasis": 59.5,
        "Remember December": 96.3,
        "The beginning": 90.45,
        "Tribal Style": 87.45,
        "Why Me": 97.38,
        "Xuxa": 63.84,
        "Zodiac": 83.43,
        "Queen of Light": 75.12,
        "Mouth": 98.34,
        "Pandemonium": 79.31,
    }
    average_score = calculate_average(SONG_RESULT)
    print(f"The average score of the songs is {average_score:.2f}")


def sortedByPrice():
    PRICES = {
        "milk": 1.09,
        "fish": 4.56,
        "bread": 2.10,
        "chocolate": 2.70,
        "grasshopper": 13.25,
        "sushi": 19.90,
        "noodles": 0.97,
        "beans": 0.87,
        "bananas": 1.05,
        "Pepsi": 3.15,
        "pizza": 4.15,
    }

    sorted_items = sorted(PRICES.items(), key=lambda item: item[1])
    for item, price in sorted_items:
        print(f"{item} {price:.2f}")


def main():
    groceryDictionary()
    touristDictionary()
    alphabeticalOrder()
    displayAddedContent()
    wordDensityCalculator()
    dancingGame()
    sortedByPrice()


if __name__ == "__main__":
    main()
