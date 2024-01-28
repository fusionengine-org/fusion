import os

from fusionengine import JsonStorage


def test_jsonstorage(cleanup):
    my_db = JsonStorage("my_db.json")

    # Insert
    print("------------------- INSERT -------------------")
    my_db.insert({"first_name": "john", "last_name": "wick", "gold": 50})
    my_db.insert({"first_name": "alexander", "last_name": "wick", "gold": 20})

    print(my_db.storage)
    print("------------------- INSERT/ -------------------")

    # Read
    print("------------------- READ -------------------")
    print(my_db.search({"last_name": "wick"}))
    print(my_db.search({"last_name": "wick"}, get_index=True))

    if (
        search_result := my_db.search(
            {"first_name": "alexander", "last_name": "wick"}, True, True
        )
    ) != None:
        alex, alex_index = search_result
    if search_result := my_db.search({"first_name": "john"}, True, True):
        _, john_index = search_result
    print("------------------- READ/ -------------------")

    # Update
    print("------------------- UPDATE -------------------")
    alex["gold"] += 20
    my_db.update(alex_index, alex)
    print(my_db.storage)
    print("------------------- UPDATE/ -------------------")

    # Delete
    print("------------------- DELETE -------------------")
    my_db.delete(john_index)
    print(my_db.storage)
    print("------------------- DELETE/ -------------------")

    # Saving to disk
    print("------------------- SAVE -------------------")
    print(my_db.save())
    print("------------------- SAVE/ -------------------")
    if cleanup:
        os.remove(my_db.file_path)


if __name__ == "__main__":
    test_jsonstorage(cleanup=True)
