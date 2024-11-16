def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    If the discount is less than 20%, return the original price.

    Parameters:
        price (float): Original price of the item.
        discount_percent (float): Discount percentage.

    Returns:
        float: Final price after applying the discount (if applicable).
    """
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price


try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percentage)

   
    if discount_percentage >= 20:
        print(f"The final price after a {discount_percentage}% discount is: {final_price:.2f}")
    else:
        print(f"No discount applied. The price remains: {original_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for the price and discount.")
