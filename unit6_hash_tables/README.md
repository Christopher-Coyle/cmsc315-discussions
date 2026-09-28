# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment used Python dictionaries to demonstrate hash table behavior through a simple inventory management system.

The program stored inventory data using SKU values as dictionary keys and quantities as the corresponding values. This demonstrated how hash tables support efficient key-value storage and retrieval.

## Implementation

The program demonstrated the following hash table operations:

- Created and populated a Python dictionary with five inventory records.
- Used SKU values as unique keys.
- Retrieved quantities for existing SKUs.
- Updated the quantity associated with an existing SKU.
- Removed an existing inventory record.
- Safely handled a lookup for a missing SKU.
- Safely handled an attempt to remove a missing SKU.

Python dictionaries use hashing internally to locate keys efficiently. This makes them appropriate for applications such as inventory systems where records frequently need to be inserted, updated, retrieved, and removed.

## Real-World Scenario

The program modeled an inventory management system in which each SKU represented a unique product and the associated value represented the current quantity in inventory.

For example:

- `P100` represented an inventory item with a quantity of 15.
- `P200` initially had a quantity of 8 and was later updated to 14.
- `P400` was removed from the inventory.

Using SKUs as keys provides a direct way to locate specific inventory records without manually searching through every item.

## Edge Cases

Two edge cases were tested.

First, the program attempted to look up SKU `P999`, which did not exist. The `get()` method was used with a default value so the program returned `SKU not found` instead of causing a `KeyError`.

Second, the program attempted to remove SKU `P888`, which was also missing. The program checked whether the key existed before attempting deletion. This prevented an invalid deletion operation and allowed the program to continue normally.

## Reflection

While completing this assignment, I learned how Python dictionaries provide hash-table behavior through key-value pairs. I used SKU numbers as keys and inventory quantities as values, which made it easy to insert, retrieve, update, and remove records. The lookup and update operations were the most straightforward because Python handles the hashing process internally.

The main challenge was making sure missing keys were handled safely. Accessing or deleting a key that does not exist can cause a `KeyError`, so I used `get()` for a missing lookup and checked whether a key existed before deleting it.

Hash tables improve efficiency because they use a hash function to determine where a key should be stored instead of searching through every item sequentially. A collision occurs when different keys map to the same internal location. Python resolves these collisions internally, but a high number of collisions can require additional work during lookup. Under normal conditions, dictionary lookup, insertion, and deletion are generally very efficient.