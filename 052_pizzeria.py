import os
import time

orders = []

def main():
    loadOrders()
    while True:
        os.system("clear")
        print("--- Mario's Pizzeria ---\n")
        print("People waiting for Pizzas:")
        print(f"{'Name':<9} {'Pizzas':<7} {'Price':>7}")
        print("-" * 25)
  
        for order in orders:
            print(f"{order[0]:<10}{order[1]:<6} {order[3]:>7}$")
        print()
      
        name, qty, size, price = getOrder()
        order = [name, qty, size, price]
        orders.append(order)

        print(f"Registered order for {name}. Price: {price}\n")
        saveOrders()
        time.sleep(1)
      
        again = input("Press q to quit, press enter to continue. ")
        if again == "q":
          time.sleep(0.5)
          os.system("clear")
          break

def getOrder():
    while True:
        try:
            qty = int(input("How many pizzas? "))
            size = input("What size (s, m, l)? ")
            price = calculatePrice(qty, size)
            name = input("Name for the order: ")
            break
        except ValueError:
            print("Please enter a valid option.")
        except Exception as err:
            print("Error!")
            print(err)
    return (name, qty, size, price)

def calculatePrice(qty, size):
  if size == "s":
    price = qty * 5.99
  elif size == "m":
    price = qty * 9.99
  elif size == "l":
    price = qty * 14.99
  else:
    raise ValueError
  return price

def loadOrders():
    global orders
    try:
        with open("pizza.orders", "r") as f:
            orders = eval(f.read())
    except FileNotFoundError:
        orders = []
    except Exception as err:
        print("Error in setting up.")
        print(err)

def saveOrders():
    try:
        with open("pizza.orders", "w") as f:
            f.write(str(orders))
    except Exception as err:
        print("Error saving orders.")
        print(err)

if __name__ == "__main__":
    main()