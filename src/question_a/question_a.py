#write functions here, don't add input('') statements here!
def test_config():
    return True

class Stock:


    def __init__(self, symbol, company_name):
        self.symbol = symbol
        self.company_name = company_name

    def call_symbol(self):
        return self.symbol
    
    def call_company_name(self):
        return self.company_name
    
    def stock_purchase_history():
    # Create 5 variables
        stock1 = Stock("AAPL", "Apple Inc")
        stock2 = Stock("CAT", "Caterpillar")
        stock3 = Stock("EK", "Eastman Kodak")
        stock4 = Stock("GOOG", "Google")
        stock5 = Stock("MSFT", "Microsoft")

    # Add the 5 variables to a dictionary
        stock_dict = {
        "AAPL": stock1,
        "CAT": stock2,
        "GOOG": stock3,
        "EK": stock4,
        "MSFT": stock5 }

    # Step c: Loop through the dictionary to display the list
        
        print("Symbol   Company Name")
        for symbol, stock in stock_dict.items():

            
            print(f"{stock.call_symbol()}      {stock.call_company_name()}")




Stock.stock_purchase_history()



