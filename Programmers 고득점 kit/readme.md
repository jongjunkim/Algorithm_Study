# Sorting a Hashmap in Reverse Order

## Sorting the Entire Hashmap

To sort a hashmap by its values in reverse order, you can use the `sorted` function along with the `items()` method. Here's an example:

```python
hashmap = {'A': 100, 'B': 200, 'C': 150}
sorted_hashmap = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
