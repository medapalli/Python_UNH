import re
import urllib.request
import json


api_endpoint = "https://api.exchangerate-api.com/v4/latest/"



def exchange_lookup(url, amt, toCur):
    
    try:
        
        if (urllib.request.urlopen(url)):
            page = urllib.request.urlopen(url)
            content=page.read().decode("utf-8")
            data =json.loads(content)
            #print(data['rates'][toCur])
            exrate=data['rates'][toCur]
            output_amt=exrate*float(amt)
            print(output_amt)
            if not exrate:
                return "exchange rate not found"
           
        else:
            print("ERROR:invalid API endpoint")
            return "exchange rate not found"
            exit()

        return output_amt

    except:
        return "exchange rate not found"

def main():
    

    while(True):
        user_input_amt = input("Enter Amount for Exchange Rate Conversion (q to quit):")
        if(user_input_amt=='q' or user_input_amt=='Q'):
            print("Existing")
            break

        regexp_amt = re.compile(r"^\d+\.?\d+$")

        if not regexp_amt.search(user_input_amt):
            print("Invalid input {}".format(user_input_amt))
            print("Existing")
            break

        else:
            user_input_from = str(input("Enter From Currency :"))
            regexp_from = re.compile(r"^[A-Z][A-Z][A-Z]$")
            if not regexp_from.search(user_input_from):
                print("Invalid From input {}".format(user_input_from))
                print("Existing")
                break
        
            else:
                user_input_to = str(input("Enter To Currency :"))
                regexp_to = re.compile(r"^[A-Z][A-Z][A-Z]$")
                if not regexp_from.search(user_input_to):
                    print("Invalid To input {}".format(user_input_to))
                    print("Existing")
                    break

                else:
                    print(exchange_lookup(api_endpoint+str(user_input_from),user_input_amt, user_input_to ))
                
if __name__ == '__main__':
    main()

