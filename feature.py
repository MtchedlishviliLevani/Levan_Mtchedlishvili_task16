#1
# დაწერეთ პროგრამა რომელიც გამოიძახებს Get მეთოდს ამ საჯარო API-დან
# (https://catfact.ninja/fact) და დათვლის თუ რამდენი ხმოვანი არის response-ში.
#2.
# დაწერეთ პროგრამა, სადაც მომხმარებელი შეიყვანს თანხის რაოდენობას დოლარში
# გადაიყვანეთ bitcoin-ში ამ (https://api.coindesk.com/v1/bpi/currentprice.json) API-ზე
# არსებული კურსის გამოყენებით.
#3.
# გამოიყენეთ საჯარო API (https://api.agify.io/?name={your name}) თქვენი სახელით ასაკის
# გამოსათვლელად.

import requests

### task 1
response = requests.get("https://catfact.ninja/fact")
cat_fact_data = response.json()
fact = cat_fact_data["fact"]
vowels_set = {"a", "e", "i", "o", "u"}
amount = 0

for char in fact.lower():
    if char in vowels_set:
        amount += 1

# print(amount,cat_fact_data)


#### task2
response2 = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
response2_data = response2.json()

btc_price = float(response2_data['bpi']["USD"]["rate"].replace(',', ''))


def btc_converter(amount_of_dollars):
    return float(amount_of_dollars) / btc_price


print(btc_converter(99000))

my_name = "Levani".lower()
response3 = requests.get(f"https://api.agify.io/?name={my_name}")
response3_data = response3.json()

print(response3_data["age"])
