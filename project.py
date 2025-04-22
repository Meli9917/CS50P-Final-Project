"""
Project Title; Akashic Password
Name; Adrian Francis T. Navarro
your GitHub and edX usernames; Meli9917, Pam99_17
your city and country; Pampanga, Philippines
Linkedin; https://www.linkedin.com/in/adrian-francis-navarro-bb3022348/
"""

import csv
import sys


upper_alphabet_e = ["F", "M", "E", "Q", "O", "B", "P", "C", "G", "A", "K", "I",
                    "V", "S", "N", "H", "R", "J", "D", "W", "T", "Z", "X", "U", "L", "Y"]
lower_alphabet_e = ["q", "z", "s", "u", "o", "c", "b", "h", "g", "n", "j", "r",
                    "m", "l", "k", "a", "v", "t", "p", "w", "d", "i", "x", "e", "y", "f"]
numbers_e = ["8", "0", "9", "3", "5", "1", "7", "6", "4", "2"]
special_chars_e = ["[", ")", "{", "@", ">", "*", ".", "+", "|", "&", "!",
                   ";", "}", "^", ":", "=", "-", "_", "$", "?", ",", "(", "#", "<", "]", "%"]

upper_alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
lower_alphabet = list("abcdefghijklmnopqrstuvwxyz")
numbers = list("0123456789")
special_chars = list("!@#$%^&*()-_+=[]{}|;:,.<>?")


class Password:
    def encrypt(self, text):
        """
        This method iterates over each letter in text
        Gets the index of the character from a corresponding list
        Replaces the character with another character from an encrypted list
        If the character is not present on any list, add it regardless
        :return: str of encrypted text
        """

        encrypted_text = ""

        for char in text:
            if char in upper_alphabet:
                index = upper_alphabet.index(char)
                encrypted_text += upper_alphabet_e[index]

            elif char in lower_alphabet:
                index = lower_alphabet.index(char)
                encrypted_text += lower_alphabet_e[index]

            elif char in numbers:
                index = numbers.index(char)
                encrypted_text += numbers_e[index]

            elif char in special_chars:
                index = special_chars.index(char)
                encrypted_text += special_chars_e[index]

            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(self, password):
        """
        This method iterates over each character in the encrypted text,
        finds its index in the encrypted lists (upper_alphabet_e, numbers_e, special_chars_e),
        and replaces it with the character at the same index in the corresponding source list.
        If the character is not present in any encrypted list, it is added unchanged.
        :param password: str of encrypted password
        :return: str of decrypted password
        """
        decrypted_text = ""

        for char in password:
            if char in upper_alphabet_e:
                index = upper_alphabet_e.index(char)
                decrypt_char = upper_alphabet[index]
                decrypted_text += decrypt_char

            elif char in lower_alphabet_e:
                index = lower_alphabet_e.index(char)
                decrypt_char = lower_alphabet[index]
                decrypted_text += decrypt_char

            elif char in numbers_e:
                index = numbers_e.index(char)
                decrypt_char = numbers[index]
                decrypted_text += decrypt_char

            elif char in special_chars_e:
                index = special_chars_e.index(char)
                decrypt_char = special_chars[index]
                decrypted_text += decrypt_char

            else:
                decrypted_text += char

        return decrypted_text


def main():
    ask = screen_1()
    if ask == "1":
        show_sites()
    elif ask == "2":
        upload()
    elif ask == "3":
        retrieve()
    elif ask == "4":
        remove_account()
    elif ask == "5":
        print("Goodbye!")
        sys.exit()


def screen_1():
    """
    This function prints a screen

    :param options: Choices the user can choose
    :type options: list of strings
    :type ask: str
    :raise ValueError: if ask is not in options
    :return: str the input of user
    :rtype: str
    """

    options = ["1", "2", "3", "4", "5"]

    while True:
        try:
            ask = input(
                """
Press number you want to run.
+-------------------+-------------------+-------------------+----------------------+----------------+
|    1. Accounts    |     2. Upload     |    3. Retrieve    |  4. Remove Account   |    5. Exit     |
+-------------------+-------------------+-------------------+----------------------+----------------+
""").strip()
            if ask in options:
                return ask
            else:
                raise ValueError("Invalid option. Please choose 1, 2, 3, 4, 5.")

        except ValueError as e:
            print(e)


def show_sites():
    """
    Displays a list of all decrypted site names from the accounts.csv file.
    """
    passw = Password()
    accounts = []

    try:
        with open("accounts.csv", "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                accounts.append(row)
    except FileNotFoundError:
        print("No accounts saved yet.")
        return

    if accounts:
        print("Sites Available:")
        decrypted_sites = [passw.decrypt(account["Site"]) for account in accounts]
        for site in sorted(decrypted_sites):
            print(f"- {site}")
    else:
        print("No accounts to display.")


def upload(file_name="accounts.csv"):
    """
    This asks the user for site, username, and password input
    Requires the user to verify password
    Displays the entered information
    Asks the user to proceed or change their input
    Allows exit at any prompt
    """
    passw = Password()

    while True:
        try:
            site = input("Site: ").upper()
            username = input("Username/ Email: ")

            while True:
                password = input("Password: ").strip()
                verify_password = input("Verify Password: ")

                if password == verify_password:
                    break
                else:
                    print("Password does not match")

            print(f"""
This is your account information
Site: {site}
Username/ Email: {username}
Password: {password}
""")
            verify = input("""
Do you want to Proceed?
+-------------------+-------------------+-------------------+
|        "Y"        |        "N"        |       "Exit"      |
+-------------------+-------------------+-------------------+
""").strip().upper()
            if verify == "Y":
                break
            elif verify == "N":
                continue
            elif verify == "EXIT":
                print("Exiting upload...")
                return
            else:
                raise ValueError("Invalid option. Please choose Y, N, or Exit.")
        except ValueError as e:
            print(e)

    encrypted_password = passw.encrypt(password)
    encrypted_site = passw.encrypt(site)
    encrypted_username = passw.encrypt(username)

    accounts = []
    exists = False

    try:
        with open("accounts.csv", "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                accounts.append(row)
                if row["Site"] == site and row["Username/Email"] == username:
                    exists = True
    except FileNotFoundError:
        pass  # File will be created when writing

    if exists:
        while True:
            try:
                print("""
Do you want to overwrite the account?
+-------------------+-------------------+-------------------+
|        "Y"        |        "N"        |       "Exit"      |
+-------------------+-------------------+-------------------+
""")
                overwrite = input("Choose: ").strip().upper()
                if overwrite == "Y":
                    accounts = [row for row in accounts if not (
                        row["Site"] == site and row["Username/Email"] == username)]
                    break
                elif overwrite == "N":
                    print("Upload canceled.")
                    return
                elif overwrite == "EXIT":
                    print("Goodbye")
                    return
                else:
                    raise ValueError("Invalid option. Please choose Y, N, or Exit.")
            except ValueError as e:
                print(e)

    # Add the new/updated entry
    accounts.append({
        "Site": encrypted_site,
        "Username/Email": encrypted_username,
        "Password": encrypted_password
    })

    # Write everything back to the file
    with open(file_name, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Site", "Username/Email", "Password"])
        writer.writeheader()
        writer.writerows(accounts)


def retrieve(file_name="accounts.csv"):
    """
    This function retrieves the password from the "accounts.csv" file.
    Asks the user for the site and username.
    It decrypts the site and username from the file before matching.
    If there is a match, decrypts the password and prints it.
    If no match is found, raises a ValueError that the account doesn't exist.
    """
    passw = Password()
    site = input("Site: ").strip().upper()
    username = input("Username: ").strip()

    try:
        with open(file_name, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                decrypted_site = passw.decrypt(row["Site"])
                decrypted_username = passw.decrypt(row["Username/Email"])

                if decrypted_site == site and decrypted_username == username:
                    decrypted_password = passw.decrypt(row["Password"])
                    print(f"""
+-------------------+
|      Account      |
+-------------------+
Site: {decrypted_site}
Username: {decrypted_username}
Password: {decrypted_password}
                    """)
                    return

        raise ValueError("No account found for the given site and username.")

    except FileNotFoundError:
        print("No accounts have been saved yet.")
    except ValueError as e:
        print(e)


def remove_account(file_name="accounts.csv"):
    """
    This function removes an account from the "accounts.csv" file.
    Asks the user for the site and username to identify the account to be deleted.
    If a matching account is found, it is removed from the file.
    If no match is found, an error message is displayed.
    """
    passw = Password()
    site = input("Enter the site to remove: ").strip().upper()
    username = input("Enter the username/email to remove: ").strip()

    accounts = []
    found = False

    try:
        with open(file_name, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                decrypted_site = passw.decrypt(row["Site"])
                decrypted_username = passw.decrypt(row["Username/Email"])

                if decrypted_site == site and decrypted_username == username:
                    found = True
                else:
                    accounts.append(row)

    except FileNotFoundError:
        print("No matching account saved yet.")
        return

    if found:
        # Write back the updated list of accounts (with the removed one)
        with open(file_name, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Site", "Username/Email", "Password"])
            writer.writeheader()
            writer.writerows(accounts)

        print(f"Account for site '{site}' and username '{username}' has been removed.")
    else:
        print("No matching account found.")


if __name__ == "__main__":
    main()
