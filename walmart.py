# walmart
BUDGET = 100.00
LOGO = f"{"="*60}{'\n\u2732  Walmart | Save money. Live better.\n'}{"="*60}"
cash = BUDGET
stock = [
    {"name": "FOHERE Waffle Maker", "price": 39.99},
    {"name": "Keurig Coffee Maker", "price": 59.00},
    {"name": "LEGO Classic Box", "price": 34.97},
    {"name": "Ozark Trail Sleeping Bag", "price": 24.44},
    {"name": "8-Cube Storage", "price": 84.00},
    {"name": "Mainstays Coffee Maker", "price": 19.92},
    {"name": "Great Value Water (32pk)", "price": 5.98},
    {"name": "Food Storage Set", "price": 9.97},
    {"name": "HART Claw Hammer", "price": 8.88},
    {"name": "BIC Ballpoint Pens (10pk)", "price": 2.47},
    {"name": "Crayola 24-Color Pencils", "price": 3.97},
    {"name": "Elmer's Glue Sticks (2pk)", "price": 1.97},
    {"name": "Great Value Paper Towels", "price": 4.98}
]

cart = [
    #{"index":1, "name":"Waffle Maker", "price":56.99, "quantity": 2}
]

def shop():
    # display items
    while True:
        display_items()
        choice = input("Enter item index to select item\nEnter 'c' to view cart or 'p' to proceed to checkout: ")

        # check for item adding or opening cart
        if choice.lower() == "c":
            view_cart()
        elif choice.lower() == "p":
            if checkout(): # returns true if checkout successful
                break
        else:
            while True:
                try:
                    index = int(choice)
                    if not index in range(13):
                        index = int(input("please enter a number between 0 and 12!" ))
                    else:
                        add_item(index)
                        break
                except:
                    print("please enter a valid index, c to view cart ot p to check out")



        # allow user to select item, quantity
        # notify the user if cart add unsuccessful
    

# Adding item to the cart
def add_item(index):
    global cash

    item = stock[index]
    price_with_tax = item["price"] + calculate_tax(item["price"])

    if cash >= price_with_tax:
        cash -= price_with_tax
        
        for cart_item in cart:
            if cart_item["index"] == item["index"]:
                cart_item["quantity"] += 1
                return
        
        cart.append({"index": index, "name": item["name"], "price": item["price"], "quantity": 1})
    else:
        print(f"Sorry, you don't have enough money to add {item['name']} to your cart.")

#calculating tax
def calculate_tax(price):
    return price * (10.44 / 100)    

def display_items():
    global stock
    print(LOGO)
    for i, item in enumerate(stock):
        print(f'{i}) {item["name"]:<30}: ${item["price"]}')
    
    #print("Enter the item index to add to cart: ")
def checkout():
    # displays the cart one more time and asks the user to confirm the purchase. Return false if they say no and true if they say yes
    display_receipt()
    confirm = input("Would you like to proceed to checkout? (y/n): ")
    if confirm.lower() == "y":
        print("Thank you for shopping at Walmart! Your remaining balance is: ", cash)
        return True
    else:
        print("Your cart has been cleared.")
        return False

def view_cart():
    # iterate through the array and print the cart items in a table format
    pass

def display_receipt():
    # show items with tax added. for each item multiply the price by the count 
    # if an item is $10 and you bought 3

    # item name x 3 : $30
    
    # tax : $30 @ 10.44% : 3.13
    # balance to pay : $33.13
    pass

shop()

#testing