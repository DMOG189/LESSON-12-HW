# HOMEWORK 2 , 3 QUESTIONS

# 2. Why it is not recommended to use index in set?

# You can’t use indexing with a set because sets are unordered collections,
# meaning they don’t maintain a specific order of elements.
# Sets store elements based on their hash values for fast membership testing,
# not in a sequence. Since there’s no guaranteed order,
# accessing elements by index does not make sense.
# If you need ordered elements with indexing, use a list or tuple instead.


# 3. how set and dict are similar?

# set and dict are similar because both use hashing for their underlying structure:
# • In a set, each element must be unique.
# • In a dict, each key must be unique.
# • Both set elements and dict keys are stored in a hash table, allowing for fast lookups.
# • Traditionally, both set and dict do not maintain the order of elements/keys.
# • Both set and dict are mutable, meaning you can add,
# remove, or change elements (or keys and values in a dict).