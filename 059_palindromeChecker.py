import os, time


def main():
    while True:
        print("--- Palindrome checker ---")
        word = input("Enter word: ").strip().lower()
        result = checkPalindrome(word)
        if result is True:
            print(f"{word.capitalize()} is a palindrome.")
        else:
            print(f"{word.capitalize()} is not a palindrome.")

        option = input("Press q to quit, press enter to continue: ")
        if option == "q":
            break
        time.sleep(1)
        os.system("clear")


def checkPalindrome(word):
    if len(word) == 0:
        return True
    elif word[0] != word[-1]:
        return False
    else:
        return checkPalindrome(word[1:-1])


main()
