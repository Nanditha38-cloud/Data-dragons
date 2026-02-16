def count_inventory(fruit_list: list[str]) -> dict[str, int]:
    inventory = {}

    for fruit in fruit_list:
        if fruit in inventory:
            inventory[fruit] += 1
        else:
            inventory[fruit] = 1

    return inventory


# Sample Tests
assert count_inventory(["apple", "banana", "apple", "cherry"]) == {
    "apple": 2,
    "banana": 1,
    "cherry": 1
}

assert count_inventory(["orange", "orange"]) == {"orange": 2}
assert count_inventory(["grape"]) == {"grape": 1}
assert count_inventory([]) == {}
assert count_inventory(["Apple", "apple"]) == {"Apple": 1, "apple": 1}
