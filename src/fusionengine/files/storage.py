import json
import typing
from pathlib import Path

from fusionengine.files.exceptions import InvalidType, JsonStorageInvalidIndex


class JsonStorage:
    """JsonStorage is a storage class for saving json databases, currently all data is loaded from
    disk and saved to memory when you done with the storage you can just save it to the disk file
    using save method

    Attributes:
        file_path (str): The path to the storage file on disk
        storage (list): The storage variable saved to memory
    """

    def __init__(self, file_path: str):
        self.storage = []
        self.file_path = Path(file_path)

        if self.file_path.exists():
            with open(self.file_path, mode="r", encoding="utf8") as file:
                self.storage = json.load(file)

    def insert(self, _dict: dict[typing.Any, typing.Any]) -> bool:
        try:
            if not isinstance(_dict, dict):
                raise InvalidType(f"_dict excepted to be dict not {type(_dict)}")

            self.storage.append(_dict)
            return True
        except Exception:
            return False

    def search(
        self,
        search_dict: dict[typing.Any, typing.Any],
        first: bool = False,
        get_index: bool = False,
    ) -> typing.Union[dict, list, tuple, None]:
        """Search for a entry based on the search_dict

        Args:
            search_dict (dict): search_dict is a dictionary describing keys:values to search for
            in the entries
            first (bool, optional): only return the first result that found
            nested_search (bool, optional): if its true if will search for keys and values
            based on search_dict in nested data structures (like another dictionary in the
            parent main dict entry)

        Returns:
            typing.Union[dict, list, tuple, None]: The entries that found if
            first is False otherwise the first entry that found
            if get_index is true then it will return a tuple
            containing two values which being the index of the entry
            aside the value of it(returns None if nothing found)
        """
        if first:
            # Only search for the first entry
            for index, entry in enumerate(self.storage):
                passed_every_search = True
                for sk, sv in search_dict.items():
                    if entry.get(sk) != sv:
                        passed_every_search = False
                if passed_every_search:
                    if get_index:
                        return (entry, index)
                    else:
                        return entry
        else:
            # Search for all entries
            founded_entries = []
            for index, entry in enumerate(self.storage):
                passed_every_search = True
                for sk, sv in search_dict.items():
                    if entry.get(sk) != sv:
                        passed_every_search = False
                if passed_every_search:
                    if get_index:
                        founded_entries.append((entry, index))
                    else:
                        founded_entries.append(entry)
            return founded_entries

    def update(self, index: int, new_entry: dict[typing.Any, typing.Any]) -> bool:
        """Update the entry based on the index to new_dict

        Args:
            index (int): The index of the entry you want to update
            new_entry (dict): The new updated entry

        Returns:
            bool: Wether the action was successful or not

        Raises:
            InvalidType: In case the index parameter is not an integer or new_entry
            is not a dict
            JsonStorageInvalidIndex: In case the index is out of range and couldn't be find
            in the entries
        """
        if not isinstance(index, int):
            raise InvalidType(f"index excepted to be integer not {type(index)}")
        if not isinstance(new_entry, dict):
            raise InvalidType(f"new_entry excepted to be dict not {type(new_entry)}")
        try:
            self.storage[index] = new_entry
            return True
        except IndexError:
            raise JsonStorageInvalidIndex(
                "Invalid index, couldn't find the index in entries"
            )
        except:
            return False

    def delete(self, index: int) -> bool:
        """Delete an entry based on the index given

        Args:
            index (int): The index of the entry you want to delete

        Returns:
            bool: Wether the action was successful or not

        Raises:
            InvalidType: In case the index parameter is not an integer
            JsonStorageInvalidIndex: In case the index is out of range and couldn't be find
            in the entries
        """
        if not isinstance(index, int):
            raise InvalidType(f"index excepted to be integer not {type(index)}")
        try:
            del self.storage[index]
            return True
        except IndexError:
            raise JsonStorageInvalidIndex(
                "Invalid index, couldn't find the index in entries"
            )
        except:
            return False

    def save(self) -> bool:
        """Saves the storage variable into disk

        Returns:
            bool: Wether the action was successful or not
        """
        try:
            with open(self.file_path, mode="w", encoding="utf8") as file:
                json.dump(self.storage, file)
            return True
        except:
            return False
