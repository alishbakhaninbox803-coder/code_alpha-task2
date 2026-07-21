stocks = {
    "OGDC": 225,
    "HBL": 160,
    "ENGRO": 310,
    "LUCK": 850
}

total = 0

print("=== Pakistan Stock Portfolio Tracker ===")
print("Available Stocks:")

for stock in stocks:
    print( stock)

while True:

    name = input("\nEnter stock name (or DONE to finish): ").upper()

    if name == "DONE":
        break

    if name not in stocks:
        print("Error! Stock not found.")
        print("Please choose one of these stocks:")

        for stock in stocks:
            print(stock)

        continue

    quantity = int(input("Enter quantity: "))

    price = stocks[name]

    value = price * quantity

    total = total + value

    print("Stock Price: Rs.", price)
    print("Investment Value: Rs.", value)

print("\nTotal Investment = Rs.", total)

file = open("portfolio.txt", "w")
file.write("Pakistan Stock Portfolio\n")
file.write("Total Investment = Rs. " + str(total))
file.close()

print("Data saved in portfolio.txt")