import os, time


def clear(delay):
    time.sleep(delay)
    os.system("clear")


def more(text):
    more = input(text).strip().lower()
    return more != "n"


def getInput(text):
    text = input(text)
    return text


if __name__ == "__main__":
    main()
