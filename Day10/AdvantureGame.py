inventory = []
player_hp = 100
def add_item(item):
    if item not in inventory:
        inventory.append(item)
        print(f"You have added {item} into your inventory.")
    else:
        print(f"You already have {item}")
def display_inventory():
    if inventory:
        print("Your inventory contains: ")
        for item in inventory:
            print(f"- {item}")
    else:
        print("Inventory is empty.")