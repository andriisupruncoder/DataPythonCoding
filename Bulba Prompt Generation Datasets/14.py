def is_valid(s: str) -> bool:
    """Returns True if s meets all vanity plate requirements, False otherwise."""

    # Check length
    if not (2 <= len(s) <= 6):
        return False

    # Check that it starts with two letters
    if not s[:2].isalpha():
        return False

    # Check that numbers only come at the end
    i = 0
    while i < len(s):
        if s[i].isalpha():
            i += 1
        elif s[i].isdigit():
            if i == 0 or s[i - 1].isalpha():
                return False
            else:
                break
        else:
            return False

    # Check that the first number is not 0
    if i < len(s) and s[i] == "0":
        return False

    # Check that there are no punctuation marks
    if any(c in s for c in ".,:;'\"!@#$%^&*()-_+=<>?/[]{}|\\"):
        return False

    return True


def main():
    s = input("Enter a vanity plate: ")
    if is_valid(s):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()