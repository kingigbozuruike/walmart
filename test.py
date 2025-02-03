def validate_price(price_str):
    """Validate the price input."""
    try:
        price = float(price_str)
        if price <= 0:
            return None, "Price must be greater than 0"
        if price > 10000:  # Reasonable upper limit for most items
            return None, "Price seems unrealistic. Please verify."
        return price, None
    except ValueError:
        return None, "Please enter a valid number"

def calculate_tax(price):
    """Calculate tax at 10.44%."""
    TAX_RATE = 0.1044
    return price * TAX_RATE

def display_receipt(items, prices):
    """Display the final receipt with all calculations."""
    print("\n====== RECEIPT ======")
    
    # Display individual items
    for item, price in zip(items, prices):
        print(f"{item}: ${price:.2f}")
    
    subtotal = sum(prices)
    total_tax = sum(calculate_tax(price) for price in prices)
    total = subtotal + total_tax
    
    print("\nSummary:")
    print(f"Number of items: {len(items)}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax (10.44%): ${total_tax:.2f}")
    print(f"Total: ${total:.2f}")
    print("==================")

def main():
    BUDGET_LIMIT = 100
    items = []
    prices = []
    current_total = 0
    
    while True:
        # Display current total and remaining budget
        remaining_budget = BUDGET_LIMIT - current_total
        if current_total > 0:
            print(f"\nCurrent total (with tax): ${current_total:.2f}")
            print(f"Remaining budget: ${remaining_budget:.2f}")
        
        # Get item name
        item_name = input("\nEnter item name (or 'checkout' to finish): ").strip()
        if item_name.lower() == 'checkout':
            if items:  # Only proceed if cart has items
                break
            print("Cart is empty! Please add items before checking out.")
            continue
        if not item_name:
            print("Item name cannot be empty.")
            continue
            
        # Get and validate price
        price_str = input("Enter item price: $")
        price, error = validate_price(price_str)
        if error:
            print(f"Error: {error}")
            continue
            
        # Calculate tax and check budget
        item_with_tax = price + calculate_tax(price)
        new_total = current_total + item_with_tax
        
        if new_total > BUDGET_LIMIT:
            print(f"\nAdding this item would exceed your ${BUDGET_LIMIT} budget.")
            print(f"You can spend up to ${remaining_budget:.2f} more.")
            continue_shopping = input("Would you like to continue shopping? (yes/no): ")
            if continue_shopping.lower() != 'yes':
                break
            continue
        
        # Add item to cart
        items.append(item_name)
        prices.append(price)
        current_total = new_total
        print(f"Item added! {item_name}: ${price:.2f} (${item_with_tax:.2f} with tax)")
    
    # Display final receipt if there are items
    if items:
        display_receipt(items, prices)
    else:
        print("Shopping session ended with no purchases.")

if __name__ == "__main__":
    print("Welcome to the Shopping Cart Program!")
    print(f"You can shop until your total (including 10.44% tax) reaches $100\n")
    main()