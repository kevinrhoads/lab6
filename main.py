# made by Kevin Rhoads
def encode(password):
    # string for encoded password to append to
    encoded_password = ""

    for num in password:
        num = int(num)
        num += 3
        # account for getting numbers over 9
        if num >= 10:
            num -= 10
        # cast num to a string to add to the encoded password
        num = str(num)
        encoded_password += num

    return encoded_password


def decode():
    pass


def main():
    # initialize variable for user's choice and encoded/decoded password
    user_choice = None
    encoded_password = None
    decoded_password = None

    while user_choice != 3:
        # display the menu
        print("Menu")
        print("-" * 13)
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print("")

        # prompt user for their choice
        user_choice = int(input("Please enter an option: "))

        # perform the indicated function
        if user_choice == 1:
            decoded_password = input("Enter your password to encode: ")
            encoded_password = encode(decoded_password)
            print(encoded_password)
            print("Your password has been encoded and stored!\n")
        elif user_choice == 2:
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.\n")
        elif user_choice == 3:
            break


if __name__ == '__main__':
    main()

