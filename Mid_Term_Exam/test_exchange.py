from MidTerm_ExchangeRate_Prog6 import exchange_lookup

def ExchangeRate_lookup():
    assert zipcode_lookup(url,100, "INR") == 7335.450899999999
    assert zipcode_lookup(url,200, "CAD") == 132.0121
    assert zipcode_lookup(url,"zzz", "INR") == "Invalid input"
    assert zipcode_lookup(url,USD, "zzz") == "Invalid input"
    
