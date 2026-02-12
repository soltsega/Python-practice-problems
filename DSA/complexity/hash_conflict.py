# Hash conflicts occur when two different keys are mapped to the same index in a hash table. This can happen due to collisions in the hash function. There are several strategies to handle hash conflicts:
# 1. Separate chaining: Each slot in the hash table contains a linked list of key-value pairs. When a collision occurs, the new key-value pair is added to the end of the linked list.
# 2. Open addressing: Each slot in the hash table contains a single key-value pair. When a collision occurs, the hash function is rehashed to find an empty slot.
# 3. Linear probing: Each slot in the hash table contains a single key-value pair. When a collision occurs, the hash function is rehashed to find the next available slot.


# what is the difference beteween hash value, hash index, and digest?
# A hash value is the output of a hash function, which is a fixed-size string of characters that is generated from input data of any size. 
# A hash index is the index in a hash table where a key-value pair is stored. 
# A digest is a fixed-size output that is generated from input data using a cryptographic hash function, which is designed to be irreversible and collision-resistant.
# other names of digest are checksum, 

# Hashing algorithm is a function that takes an input or message and returns a fixed size string of bytes. The output is typically a hash value that is unique to the input data. 
# Hashing algorithms are commonly used in data structures like hash tables, as well as in cryptography for password hashing and data integrity verification. Some popular hashing algorithms include MD5, SHA-1, and SHA-256. 

# There are about 4 requirements of a good hashing algorithm
# 1. It has to