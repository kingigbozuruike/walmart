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

cart = []

def shop():
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
        print(f'{i+1}) {item["name"]:<30}: ${item["price"]}')
    

def checkout():
    display_receipt()
    confirm = input("Would you like to proceed to checkout? (y/n): ")
    if confirm.lower() == "y":
        print("Thank you for shopping at Walmart! Your remaining balance is: ", cash)
        return True
    else:
        print("Your cart has been cleared.")
        return False

def view_cart():
    print("\nYour Cart:")
    display_cart_items()

def display_cart_items():
    if not cart:
        print("Your cart is empty.")
    else:
        total = 0
        for item in cart:
            total += item["price"] * item["quantity"]
            print(f'{item["name"]} x{item["quantity"]}: ${item["price"] * item["quantity"]:.2f}')
        print(f"Total: ${total:.2f}")

def display_receipt():
    print("\n--- Receipt ---")
    total_before_tax = 0
    tax_total = 0
    for item in cart:
        item_total = item["price"] * item["quantity"]
        tax = calculate_tax(item["price"]) * item["quantity"]
        total_before_tax += item_total
        tax_total += tax
        print(f'{item["name"]} x{item["quantity"]}: ${item_total:.2f}')
        print(f"Tax for {item['name']} (10.44%): ${tax:.2f}")
    
    print(f"\nSubtotal: ${total_before_tax:.2f}")
    print(f"Total Tax: ${tax_total:.2f}")
    print(f"Total Amount: ${total_before_tax + tax_total:.2f}")
    print(f"Amount Paid: ${total_before_tax + tax_total:.2f}")

shop()

#testing