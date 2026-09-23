def add_entry(d):
    key = input("Enter new key: ")
    value = input("Enter new value: ")
    d[key] = value


def reassign_dict(d):
    name = input("Enter new name: ")
    age = int(input("Enter new age: "))
    d = {"name": name, "age": age}


name = input("Enter name: ")
age = int(input("Enter age: "))

my_dict = {"name": name, "age": age}

print("Original dictionary:", my_dict)

add_entry(my_dict)
print("After add_entry:", my_dict)

reassign_dict(my_dict)
print("After reassign_dict:", my_dict)