from MidTerm_ExchangeRate_Prog6 import exchange_lookup

def ExchangeRate_lookup():
    assert zipcode_lookup("https://api.exchangerate-api.com/v4/latest/USD",100, "INR") == 7335.450899999999
    assert zipcode_lookup("https://api.exchangerate-api.com/v4/latest/USD",200, "CAD") == 132.0121
    assert zipcode_lookup("https://api.exchangerate-api.com/v4/latest/USD","zzz", "INR") == "Invalid input"
    assert zipcode_lookup("https://api.exchangerate-api.com/v4/latest/USD",USD, "zzz") == "Invalid input"
    
