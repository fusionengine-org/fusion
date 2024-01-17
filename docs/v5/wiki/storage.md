# Storage system
## Init

```python
my_db = fusion.JsonStorage("my_db.json")
```
This how you initialize your json storage system

## Insertion

```python
my_db.insert({"first_name": "john", "last_name": "wick", "gold": 50})
my_db.insert({"first_name": "alexander", "last_name": "wick", "gold": 20})
```
The code inserts two entries into the storage. The inserted data contains information about individuals' first names, last names, and gold amounts.

## Reading

```python
Copy code
my_db.search({"last_name": "wick"})
my_db.search({"last_name": "wick"}, get_index=True)
```
The code demonstrates reading operations. It searches for entries with the last name "wick" and retrieves results with and without index information.

## Updating

```python
alex['gold'] += 20
my_db.update(alex_index, alex)
```
The code showcases how to update data in the storage. In this case, it increases the "gold" value for an entry with the first name "alexander" by 20.

## Deleting

```python
my_db.delete(john_index)
```
The code demonstrates deletion of data by removing an entry with the first name "john" from the storage.

## Saving to Disk
```python
my_db.save()
```
The code shows how to save the modified data back to the storage file on disk.


