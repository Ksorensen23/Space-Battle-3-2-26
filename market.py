player = {
    "name": "Ace",
    "credits": 100,
    "location": "Earth",
    "fuel": 50,
    "max_weight": 100,
    "inventory": {"Tacos": 2, "Iron": 0, "Fuel": 5},
    "alive": True
}

BASE_PRICES = {
    "Earth": {
        "Fuel": 10,
        "Tacos": 5,
        "Iron": 20
    },
    "Mars": {
        "Fuel": 15,
        "Tacos": 12,
        "Iron": 5
        
demand_modifier = {
    "Fuel": 1.0,
    "Tacos": 1.0,
    "Iron": 1.0
}

def get_prices(planet):
    prices = {}
    for item, base_price in BASE_PRICES[planet].items():
        modified_price = base_price * demand_modifier[item]
        prices[item] = round(modified_price, 2)

    return prices


def increase_demand(item):
    if item in demand_modifier:
        demand_modifier[item] *= 1.05

def buy_item(player, item, price, quantity):
    
    total_cost = price * quantity
    
    if player["credits"] < total_cost:
        print(">>> Not enough credits for this purchase.")
        return False

    player["inventory"][item] += quantity
    
    player["credits"] -= total_cost
    
    for _ in range(quantity):
        increase_demand(item)

    print(f"Purchase Complete: Spent {total_cost} Credits.")
    return True

def sell_item(player, item, price, quantity=1):
    if item not in player["inventory"]:
        print(">>> Item does not exist.")
        return False

    if player["inventory"][item] < quantity:
        print("You do not have enough of that item to sell.")
        return False

    total_value = price * quantity

    player["inventory"][item] -= quantity

    player["credits"] += total_value

    print(f" Sold {quantity} {item} for {total_value} Credits.")

    return True
