player = {
    "name": "Ace",
    "credits": 100,
    "location": "Earth",
    "fuel": 50,
    "max_weight": 100,
    "inventory": {"Tacos": 2, "Iron": 0, "Fuel": 5},
    "alive": True
}
# market.py

# =========================
# BASE PRICES BY PLANET
# =========================

BASE_PRICES = {
    "Earth": {
        "Fuel": 10,
        "Tacos": 5,
        "Iron": 20   # High on Earth
    },
    "Mars": {
        "Fuel": 15,
        "Tacos": 12,
        "Iron": 5    # Cheap on Mars
    },
    "Jupiter": {
        "Fuel": 25,
        "Tacos": 20,
        "Iron": 40
    },
    "Moon": {
        "Fuel": 8,
        "Tacos": 6,
        "Iron": 25
    }
}

# =========================
# SUPPLY & DEMAND SYSTEM
# =========================

# Starts at 1.0 (normal price)
demand_modifier = {
    "Fuel": 1.0,
    "Tacos": 1.0,
    "Iron": 1.0
}


def get_prices(planet):
    """
    Returns a dictionary of current prices for a planet.
    Iron is cheap on Mars and expensive on Earth by design.
    """
    prices = {}

    if planet not in BASE_PRICES:
        return {}

    for item, base_price in BASE_PRICES[planet].items():
        modified_price = base_price * demand_modifier[item]
        prices[item] = round(modified_price, 2)

    return prices


def increase_demand(item):
    """
    Increases price of an item by 5% after purchase.
    """
    if item in demand_modifier:
        demand_modifier[item] *= 1.05


# =========================
# BUY LOGIC
# =========================

def buy_item(player, item, price, quantity=1):
    """
    Allows player to buy an item.
    Checks credits before purchasing.
    """

    total_cost = price * quantity

    # Credit check (MUST use 'credits')
    if player["credits"] < total_cost:
        print(">>> Not enough credits for this purchase.")
        return False

    # Inventory safety check
    if item not in player["inventory"]:
        print(">>> Item does not exist.")
        return False

    # Deduct credits
    player["credits"] -= total_cost

    # Add to inventory
    player["inventory"][item] += quantity

    # Increase demand once per unit purchased
    for _ in range(quantity):
        increase_demand(item)

    print(f">>> Transaction Complete: Spent {total_cost} Credits.")

    return True


# =========================
# SELL LOGIC
# =========================

def sell_item(player, item, price, quantity=1):
    """
    Allows player to sell an item.
    """

    # Inventory check
    if item not in player["inventory"]:
        print(">>> Item does not exist.")
        return False

    if player["inventory"][item] < quantity:
        print(">>> You do not have enough of that item to sell.")
        return False

    total_value = price * quantity

    # Remove item
    player["inventory"][item] -= quantity

    # Add credits
    player["credits"] += total_value

    print(f">>> Sold {quantity} {item} for {total_value} Credits.")

    return True

print("Location:", player["location"])
prices = get_prices(player["location"])
print("Prices:", prices)

buy_item(player, "Iron", prices["Iron"], 2)

print("After buying Iron:")
print("Credits:", player["credits"])
print("Inventory:", player["inventory"])

# Check price increased
prices = get_prices(player["location"])
print("New Prices:", prices)
