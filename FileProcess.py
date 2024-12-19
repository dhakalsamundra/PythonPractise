def read_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
        except ValueError:
            pass


def print_frame(width, height, mark):
    for _ in range(height):
        print(mark * width)


def readFile():
    file_name = input("Enter the name of the file: ")

    try:
        with open(file_name, "r") as file:
            for line_number, line in enumerate(file, start=1):
                print(f"{line_number} {line.rstrip()}")
    except FileNotFoundError:
        print(f"The file {file_name} was not found.")


def read_message():
    print("Enter rows of text. Quit by entering an empty rows.")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    return lines


def write_numbered_lines(file_name, lines):
    try:
        with open(file_name, "w") as file:
            for line_number, line in enumerate(lines, start=1):
                file.write(f"{line_number} {line}\n")
        print(f"File {file_name} has been written.")
    except IOError:
        print(f"Writing the file {file_name} was not successful.")


def writeFile():
    file_name = input("Enter the name of the file: ")
    try:
        with open(file_name, "w"):
            pass
    except IOError:
        print(f"Writing the file {file_name} was not successful.")
        return

    # Reading message from the user
    lines = read_message()

    # Writing numbered lines to the file
    write_numbered_lines(file_name, lines)


def score():
    file_name = input("Enter the name of the score file: ")
    scores = {}
    with open(file_name, "r") as file:
        for line in file:
            name, score = line.split()
            score = int(score)
            if name in scores:
                scores[name] += score
            else:
                scores[name] = score
    print("Contestant score:")
    for name in sorted(scores):
        print(f"{name} {scores[name]}")


def enomorusScore():
    file_name = input("Enter the name ofd the score file: ")

    try:
        with open(file_name, "r") as file:
            scores = {}

            for line in file:
                parts = line.split()

                # check if the line contains exactly two parts
                if len(parts) != 2:
                    print("There was an erroneous line in the file:")
                    print(line.strip())
                    return

                name, score_str = parts

                try:
                    score = int(score_str)
                except ValueError:
                    print("There was an erroneous score in the file")
                    print(score_str)
                    return

                if name in scores:
                    scores[name] += score
                else:
                    scores[name] - score

            print("Contestant score:")
            for name in sorted(scores):
                print(f"{name} {scores[name]}")
    except FileNotFoundError:
        print("There was an error in reading the file.")


def main():
    width = read_input("Enter the width of a frame")
    height = read_input("Enter the height of a frame")
    mark = input("Enter a print mark")
    print()
    print_frame(width, height, mark)
    readFile()
    writeFile()
    score()
    enomorusScore()


if __name__ == "__main__":
    main()
