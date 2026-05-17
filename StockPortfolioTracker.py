stock_prices = {
    "AAPL": 180,
    "TSLA": 250
}

total_investment = 0

stock_name = input("Enter stock name: ").upper()
quantity = int(input("Enter quantity: "))

if stock_name in stock_prices:

    investment = stock_prices[stock_name] * quantity

    total_investment += investment

    print("Stock:", stock_name)
    print("Price:", stock_prices[stock_name])
    print("Quantity:", quantity)
    print("Total Investment Value:", total_investment)

else:
    print("Stock not found!")