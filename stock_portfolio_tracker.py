print("========================================")
print("       STOCK PORTFOLIO TRACKER")
print("========================================")

# Predefined stock prices
stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 420,
    "GOOGL": 175,
    "AMZN": 190
}

print("\nAvailable stocks:")

for stock, price in stocks.items():
    print(stock, "- $", price)

# Store user's portfolio
portfolio = {}

# Store total investment
total_investment = 0

# Take stock details from user
while True:
    stock_name = input(
        "\nEnter stock name (or 'done' to finish): "
    ).upper()

    # Finish the program
    if stock_name == "DONE":
        break

    # Check whether stock exists
    if stock_name not in stocks:
        print("Stock not found!")
        print("Please choose from the available stocks.")
        continue

    # Get valid quantity
    while True:
        try:
            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Quantity must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    # Calculate investment
    price = stocks[stock_name]
    investment = price * quantity

    # Add quantity if stock already exists
    if stock_name in portfolio:
        portfolio[stock_name] += quantity
    else:
        portfolio[stock_name] = quantity

    # Add investment to total
    total_investment += investment

    print("Stock price: $", price)
    print("Investment value: $", investment)

# Display portfolio summary
print("\n========================================")
print("         PORTFOLIO SUMMARY")
print("========================================")

print("Stock\tQuantity\tPrice\tValue")
print("----------------------------------------")

for stock, quantity in portfolio.items():
    price = stocks[stock]
    value = price * quantity

    print(
        stock,
        "\t",
        quantity,
        "\t\t$",
        price,
        "\t$",
        value
    )

print("----------------------------------------")
print("TOTAL INVESTMENT:\t\t$", total_investment)

# Save portfolio to a text file
with open("portfolio.txt", "w") as file:
    file.write("STOCK PORTFOLIO\n")
    file.write("========================\n")

    for stock, quantity in portfolio.items():
        price = stocks[stock]
        value = price * quantity

        file.write(
            f"{stock} | Quantity: {quantity} | "
            f"Price: ${price} | Value: ${value}\n"
        )

    file.write("========================\n")
    file.write(
        f"Total Investment: ${total_investment}\n"
    )

print("\nPortfolio saved successfully!")
print("File name: portfolio.txt")
