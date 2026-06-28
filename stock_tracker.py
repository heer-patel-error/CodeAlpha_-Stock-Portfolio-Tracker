# Dictionary containing stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 160
}

# Variable to store total investment
total_investment = 0

# Ask user how many stocks they want to enter
n = int(input("How many stocks do you want to enter? "))

# Repeat for each stock
for i in range(n):

    stock_name = input("Enter stock symbol: ").upper()
    quantity = int(input("Enter quantity: "))

    # Check if stock exists
    if stock_name in stock_prices:

        price = stock_prices[stock_name]

        investment = price * quantity

        total_investment += investment

        print("Price =", price)
        print("Investment in", stock_name, "=", investment)

    else:
        print("Stock not found!")

# Display total investment
print("\nTotal Investment Value =", total_investment)

# Save result into text file
file = open("portfolio.txt", "w")

file.write("Total Investment Value = " + str(total_investment))

file.close()

print("Data saved successfully in portfolio.txt")