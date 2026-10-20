def half_pyramid(size):
    for i in range(1, size + 1):
        print("*" * i)


def pyramid(size):
    for i in range(1, size + 1):
        spaces = " " * (size - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)


def hollow_pyramid(size):
    for i in range(1, size + 1):
        spaces = " " * (size - i)
        if i == 1:
            row = "*"
        elif i == size:
            row = "*" * (2 * size - 1)
        else:
            row = "*" + " " * (2 * i - 3) + "*"
        print(spaces + row)


def number_pyramid(size):
    for i in range(1, size + 1):
        spaces = " " * (size - i)
        # % 10 keeps each cell a single character for sizes above 5
        digits = "".join(str((n % 10)) for n in range(1, 2 * i))
        print(spaces + digits)


def letter_pyramid(size):
    for i in range(1, size + 1):
        spaces = " " * (size - i)
        # % 26 wraps back to 'A' if the row is longer than the alphabet
        letters = "".join(chr(ord("A") + j % 26) for j in range(2 * i - 1))
        print(spaces + letters)


# ---------- Input helpers ----------

def show_menu():
    print("\n===== Pyramid Menu =====")
    print("1. Print a * half-pyramid")
    print("2. Print a * pyramid")
    print("3. Print a * hollow pyramid")
    print("4. Print a pyramid of numbers")
    print("5. Print a pyramid of letters")
    print("6. Exit the program")


def get_choice():
    # int() itself raises ValueError for non-numeric text
    choice = int(input("Enter your choice (1-6): "))
    if choice < 1 or choice > 6:
        raise ValueError("Choice must be between 1 and 6.")
    return choice


def get_size():
    size = int(input("Enter the size (positive whole number): "))
    if size < 1:
        raise ValueError("Size must be at least 1.")
    return size


# ---------- Main program ----------

def main():
    while True:
        show_menu()

        try:
            choice = get_choice()
        except ValueError as error:
            # Covers both non-numeric entries and our own out-of-range error
            print(f"Invalid input: {error}")
            continue

        if choice == 6:
            print("Goodbye!")
            break

        try:
            size = get_size()
        except ValueError as error:
            print(f"Invalid input: {error}")
            continue

        print()
        match choice:
            case 1:
                half_pyramid(size)
            case 2:
                pyramid(size)
            case 3:
                hollow_pyramid(size)
            case 4:
                number_pyramid(size)
            case 5:
                letter_pyramid(size)


if __name__ == "__main__":
    main()
