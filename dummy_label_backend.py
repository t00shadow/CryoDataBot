# Initialize a list of 3 empty lists (ready to store dictionaries)
n = 5
list_of_lists_of_dicts = [[] for _ in range(n)]

# Example dictionaries to append
dict1 = {"name": "Alice", "age": 30}
dict2 = {"name": "Bob", "age": 25}
dict3 = {"name": "Charlie", "age": 35}

# Append dictionaries to the first list
list_of_lists_of_dicts[0].append(dict1)

# Append dictionaries to the second list
list_of_lists_of_dicts[1].append(dict2)

# Append dictionaries to the third list
list_of_lists_of_dicts[2].append(dict3)

# Print the result
for i, inner_list in enumerate(list_of_lists_of_dicts):
    print(f"List {i}: {inner_list}")



# Actually only need an list of an empty list
list_of_lists_of_dicts2 = [[]]
print("list_of_lists_of_dicts2", list_of_lists_of_dicts2)
list_of_lists_of_dicts2.append([])
print("list_of_lists_of_dicts2", list_of_lists_of_dicts2)
