"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    print("\n=== INSERT OPERATIONS ===")

    # This dictionary represents an inventory system.
    # Each SKU is stored as a key, and the quantity is stored as its value.
    # Python dictionaries use hashing internally to locate keys efficiently.
    inventory = {}

    inventory["P100"] = 15
    inventory["P200"] = 8
    inventory["P300"] = 22
    inventory["P400"] = 5
    inventory["P500"] = 12

    print("Inventory after inserting five items:")
    print(inventory)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")

    # A dictionary lookup uses the SKU key to retrieve its associated quantity.
    # This avoids manually searching through every inventory record.
    print("Quantity for P100:", inventory["P100"])
    print("Quantity for P300:", inventory["P300"])

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")

    print("Before updating P200:")
    print(inventory)

    # Assigning a new value to an existing key updates the stored value.
    # It does not create a duplicate key.
    inventory["P200"] = 14

    # Additional test:
    # Updating an existing key should not increase the number of records
    # because dictionary keys are unique.
    print("Inventory size after update:", len(inventory))

    print("After updating P200 quantity to 14:")
    print(inventory)

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")

    print("Before deleting P400:")
    print(inventory)

    # del removes both the selected key and its associated value.
    del inventory["P400"]

    print("After deleting P400:")
    print(inventory)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")

    # Edge case 1:
    # get() safely checks for a missing SKU.
    # The default message is returned instead of raising a KeyError.
    missing_quantity = inventory.get("P999", "SKU not found")
    print("Lookup for missing SKU P999:", missing_quantity)

    # Edge case 2:
    # Check whether a key exists before trying to delete it.
    # This prevents a KeyError when the SKU is missing.
    missing_sku = "P888"

    if missing_sku in inventory:
        del inventory[missing_sku]
        print(f"{missing_sku} was removed.")
    else:
        print(f"{missing_sku} was not found, so no item was removed.")

    print("\nFinal inventory:")
    print(inventory)


if __name__ == "__main__":
    main()