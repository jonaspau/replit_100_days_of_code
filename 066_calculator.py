import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("400x200")

answer = 0
lastNum = 0
operator = None


def typeAnswer(value):
    global answer
    answer = f"{answer}{value}"
    answer = int(answer)
    hello["text"] = answer


def calcAnswer(thisOperator):
    global answer, lastNum, operator
    lastNum = answer
    answer = 0
    operator = thisOperator
    hello["text"] = answer


def calc():
    global answer, lastNum, operator

    expression = f"{lastNum}{operator}{answer}"
    total = eval(expression)
    answer = total
    hello["text"] = total


hello = tk.Label(text=answer)
hello.grid(row=0, column=1)

zero = tk.Button(text="0", command=lambda: typeAnswer(0))
zero.grid(row=6, column=1)

one = tk.Button(text="1", command=lambda: typeAnswer(1))
one.grid(row=5, column=0)
two = tk.Button(text="2", command=lambda: typeAnswer(2))
two.grid(row=5, column=1)
three = tk.Button(text="3", command=lambda: typeAnswer(3))
three.grid(row=5, column=2)

four = tk.Button(text="4", command=lambda: typeAnswer(4))
four.grid(row=4, column=0)
five = tk.Button(text="5", command=lambda: typeAnswer(5))
five.grid(row=4, column=1)
six = tk.Button(text="6", command=lambda: typeAnswer(6))
six.grid(row=4, column=2)

seven = tk.Button(text="7", command=lambda: typeAnswer(7))
seven.grid(row=3, column=0)
eight = tk.Button(text="8", command=lambda: typeAnswer(8))
eight.grid(row=3, column=1)
nine = tk.Button(text="9", command=lambda: typeAnswer(9))
nine.grid(row=3, column=2)

equals = tk.Button(text="=", command=lambda: calc())
equals.grid(row=6, column=0)
add = tk.Button(text="+", command=lambda: calcAnswer("+"))
add.grid(row=6, column=3)
subtract = tk.Button(text="-", command=lambda: calcAnswer("-"))
subtract.grid(row=5, column=3)
multiply = tk.Button(text="*", command=lambda: calcAnswer("*"))
multiply.grid(row=4, column=3)
divide = tk.Button(text="/", command=lambda: calcAnswer("/"))
divide.grid(row=3, column=3)


tk.mainloop()
