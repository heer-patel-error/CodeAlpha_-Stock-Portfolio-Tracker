from stock_data import stock_prices
import csv

total_investment = 0

# Create CSV file
with open("portfolio.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Stock", "Quantity", "Price", "Investment"])

n = int(input("How many stocks do you want to enter? "))

for i in range(n):

    stock_name = input("Enter stock symbol: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:

        price = stock_prices[stock_name]
        investment = price * quantity

        total_investment += investment

        print("\nStock:", stock_name)
        print("Price:", price)
        print("Investment:", investment)

        # Save into CSV
        with open("portfolio.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(
                [stock_name, quantity, price, investment]
            )

    else:
        print("Stock not found!")

print("\nTotal Investment Value =", total_investment)

# Save report
with open("reports.txt", "w") as file:
    file.write("Total Investment Value = ")
    file.write(str(total_investment))

print("Data saved successfully.")