# Coffee shop using new python programming
# concepts
# print("Hello, welcome to DC-CoffeeShop")

# print("What is your name?")

name = input("What is your name?\n")

print("Hello " + name + " ,thank you so much for coming in today!\n\n\n")

menu = "Black Coffee, Espresso, Latte, Cappucino"

print(
    name +
    ", what would you like from our menu today? Here is what we are serving.\n"
    + menu)

order = input()

print("Sounds good " + name + ", we will have that" + order +
      "ready for you in a moment")
