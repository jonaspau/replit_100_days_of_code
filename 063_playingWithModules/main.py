import modules

count = 1
while True:
    print(count)
    count += 1

    text = modules.getInput("Enter the text: ")
    print(text)

    if not modules.more("Continue? "):
        break
    modules.clear(1)
