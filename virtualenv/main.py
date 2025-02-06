print("hello world")
tup=(1,2,3,44,77)
print(tup)
print(tup[0])
print(tup[3])

for i in tup:
    if(i%2==0):
        print(i)


"""
Tuple in Python
----------------
A tuple is an ordered, immutable collection of elements. It is used to store multiple items in a single variable.
Tuples are written with round brackets () and can contain elements of different data types.

Characteristics of Tuples:
1. Ordered: The order of elements remains the same.
2. Immutable: Once created, elements in a tuple cannot be changed.
3. Can contain duplicate values.
4. Can store multiple data types.
5. Supports indexing and slicing.

Methods available for tuples:
- count(value): Returns the number of times a value appears in the tuple.
- index(value): Returns the index of the first occurrence of a value.

"""

# Creating a Tuple
def create_tuples():
    tuple1 = (1, 2, 3, 4, 5)
    tuple2 = ("apple", "banana", "cherry")
    tuple3 = (1, "hello", 3.14, True)
    print("Tuple 1:", tuple1)
    print("Tuple 2:", tuple2)
    print("Tuple 3:", tuple3)

# Accessing Tuple Elements
def access_tuple():
    my_tuple = (10, 20, 30, 40, 50)
    print("First element:", my_tuple[0])
    print("Last element:", my_tuple[-1])
    print("Sliced elements:", my_tuple[1:4])

# Tuple Methods
def tuple_methods():
    my_tuple = (1, 2, 2, 3, 4, 2)
    print("Count of 2:", my_tuple.count(2))
    print("Index of 3:", my_tuple.index(3))

# Tuple Packing and Unpacking
def tuple_packing_unpacking():
    packed_tuple = (5, 10, 15)
    a, b, c = packed_tuple  # Unpacking
    print("Packed Tuple:", packed_tuple)
    print("Unpacked Values: a =", a, "b =", b, "c =", c)

# Immutable Nature of Tuple
def tuple_immutable():
    my_tuple = (1, 2, 3, 4)
    try:
        my_tuple[0] = 10  # This will raise an error
    except TypeError as e:
        print("Error:", e)

# Running all functions
def main():
    print("\nCreating Tuples")
    create_tuples()
    
    print("\nAccessing Tuple Elements")
    access_tuple()
    
    print("\nTuple Methods")
    tuple_methods()
    
    print("\nTuple Packing and Unpacking")
    tuple_packing_unpacking()
    
    print("\nDemonstrating Tuple Immutability")
    tuple_immutable()

if __name__ == "__main__":
    main()
