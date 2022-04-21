import requests

def get_coin_data():
    json = requests.get("http://api.coincap.io/v2/assets").json()  # retrieves API data and converts to json.
    coins = json['data']  # assigns coins to the dictionary 'data' from the json.
    return coins


def is_coin_valid(user, coins_json):  # checks if user input is a valid coin name and returns true or false.
    is_valid = False
    for elem in coins_json:
        if user.lower() in elem['name'].lower():
            is_valid = True
    return is_valid


def check_coin_price(user, coins_json):  # Finds the price of the user inputted coin
    if user == "":  # if user enters blank input error will be displayed
        print('[ERROR] Please enter a valid cryptocurrency coin name')
        return
    for elem in coins_json:
        if user.lower() in elem['name'].lower():  # if the user entry is in
            price = float(elem['priceUsd'])  # converts the data to a float for formatting
            print(elem['name'], 'is currently priced at ${:.4f}'.format(price))


if __name__ == "__main__":
    coins_json = get_coin_data()   # assigns def get_coin_data to a variable
    user = input('Enter cryptocurrency coin name:')
    while user.lower().strip() != "done":  # makes it so Done and done or even DoNe is acceptable to finish the program
        if user == "":  # If there is no input I.E. cold start/first run of the program
            user = input('Enter cryptocurrency coin name: ')
        elif is_coin_valid(user, coins_json):  # If the user input is valid it will check the price of the coin
            check_coin_price(user, coins_json)
            user = input('Enter another cryptocurrency coin name or type \'Done\' to finish: ')
        else:  # prints that the coin could not be found then prompts user for another entry
            print('Couldn\'t find coin \'' + user + '\'')
            user = input('Enter another cryptocurrency coin name: ')
    print('Finished')  # prints once a variation of done has been entered.
