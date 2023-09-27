def main():
    plate = input("Enter your vanity plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check if the plate starts with at least two letters
    if len(s) < 2 or not s[0].isalpha() or not s[1].isalpha():
        return False

    # Check if the length of the plate is between 2 and 6
    if len(s) > 6:
        return False

    # Check if there are any invalid characters
    for char in s:
        if not char.isalnum():
            return False

    # If there's a number, it should be at the end and should not start with '0'
    if any(char.isdigit() for char in s):
        first_digit_index = next((i for i, char in enumerate(s) if char.isdigit()), None)
        if s[first_digit_index] == '0' or any(char.isalpha() for char in s[first_digit_index+1:]):
            return False

    return True

if __name__ == "__main__":
    main()
