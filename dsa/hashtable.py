my_hash_set = [[None],['Jones'],[None],['Lisa'],[None],['Bob'],[None],['Siri'],['Pete'],[None]]

def hash_function(value):
    sum_of_chars = 0
    for char in value:
        sum_of_chars += ord(char)
    return sum_of_chars % 10

def add(value):
    index = hash_function(value)
    bucket = my_hash_set[index]
    if value not in bucket:
        bucket.append(value)

def contains(name):
    index = hash_function(name)
    bucket = my_hash_set[index]
    return name in bucket

add('Stuart')
# print(my_hash_set)
# print("Contains Stuart :", contains('Stuart'))

# Hash Sets  with Chaining to solve collisions
class SimleHashSet:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]
        
    def hash_function(self, value):
        sum_of_chars = 0
        for char in value:
            sum_of_chars += ord(char)
        return sum_of_chars % self.size
    def add(self, value):
        index = self.hash_function(value)
        bucket = self.buckets[index]
        if value not in bucket:
            bucket.append(value)
    def contains(self, value):
        index = self.hash_function(value)
        bucket = self.buckets[index]
        return value in bucket
    def remove(self, value):
        index = self.hash_function(value)
        bucket = self.buckets[index]
        if value in bucket:
            bucket.remove(value)
    def print_set(self):
        print("Hash set Contents")
        for index, bucket in enumerate(self.buckets):
            print(f"Bucket {index}: {bucket}")

hash_set = SimleHashSet()

hash_set.add("Charlotte")
hash_set.add("Thomas")
hash_set.add("Jens")
hash_set.add("Peter")
hash_set.add("Lisa")
hash_set.add("Adele")
hash_set.add("Micheala")
hash_set.add("Bob")

hash_set.print_set()

print("\n'Peter' is in the set:", hash_set.contains('Peter'))
print("Removing 'Peter'")
hash_set.remove('Peter')
print("'Peter' is in the set:", hash_set.contains('Peter'))
print("'Adele' has a hash code:", hash_set.hash_function('Adele'))

# I have to do Hash table with Linked List

# Hash Map with Chaining to solve collisions
class SimpleHashMap:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]
    def has_function(self, key):
        sum_of_char = 0
        for char in key:
            sum_of_char += ord(char)
        return sum_of_char % self.size
    def put(self, key, value):
        # Add or update a key-value pair
        index = self.has_function(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
    def get(self, key):
        # Retrieve a value by key
        index = self.has_function(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        return None
    def remove(self, key):
        # Remove a key-value pair
        index = self.has_function(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
    def print_map(self):
        print("Hash Map Content")
        for index, bucket in enumerate(self.buckets):
            print(f"Buckets {index}: {bucket}")

# Creating the Hash Map from the simulation      
hash_map = SimpleHashMap()


# Adding some entries
hash_map.put("123-4567", "Charlotte")
hash_map.put("123-4568", "Thomas")
hash_map.put("123-4569", "Jens")
hash_map.put("123-4570", "Peter")
hash_map.put("123-4571", "Lisa")
hash_map.put("123-4672", "Adele")
hash_map.put("123-4573", "Michaela")
hash_map.put("123-6574", "Bob")

# Print
# hash_map.print_map()

# # Retrive
# print("\nName associated with '123-4570':", hash_map.get('123-4570'))

# # Update
# print("Update the name for '123-4570' to 'James'")
# hash_map.put('123-4570', 'James')

# # Search
# print("Name associated with'123-6574':", hash_map.get('123-6574'))



# Hash Sets  with open addressing to solve collisions
class SimpleHashSetOpenAddressing:
    TOMBSTONE = object()
    
    def __init__(self, size=20):
        self.size = size
        self.count = 0
        self.buckets = [None] * size
    def resize(self):
        old_buckets = self.buckets
        
        self.size = self.size * 2
        self.buckets = [None] * self.size
        
        for value in old_buckets:
            if value is not None and value is not self.TOMBSTONE:
                self.add2(value)
    def hash_function2(self, value):
        sum_of_char = 0
        for char in value:
            sum_of_char += ord(char)
        return sum_of_char % self.size
    def add2(self, value):
        
        if self.count / self.size > 0.7:
            self.resize()
            
        index = self.hash_function2(value)
        
        for i in range(self.size):
            newIndex = (index + i) % self.size
            
            if self.buckets[newIndex] is None:
                self.buckets[newIndex] = value
                self.count += 1
                return
    def contains2(self, value):
        index = self.hash_function2(value)
        
        for i in range(self.size):
            newIndex = (index + i) % self.size
            
            if self.buckets[newIndex] is None:
                return False
            
            if self.buckets[newIndex] == value:
                return True
            
        return False
    def remove2(self, value):
        index = self.hash_function2(value)
        
        for i in range(self.size):
            newIndex = (index + i) % self.size
            
            if self.buckets[newIndex] is None:
                return
            
            if self.buckets[newIndex] == value:
                self.buckets[newIndex] = self.TOMBSTONE
                self.count -= 1
                return
    def print_set2(self):
        print("Hash Set (Open Addressing)")
        for i, val in enumerate(self.buckets):
            print(i, ":", val)

hash_set = SimpleHashSetOpenAddressing()

hash_set.add2("Charlotte")
hash_set.add2("Thomas")
hash_set.add2("Jens")
hash_set.add2("Peter")
hash_set.add2("Lisa")
hash_set.add2("Adele")
hash_set.add2("Micheala")
hash_set.add2("Ken")
hash_set.add2("Kogi")
hash_set.add2("Milna")
hash_set.add2("Last")

       
hash_set.print_set2()

print("\n'Peter' is in the set:", hash_set.contains2('Peter'))
print("Removing 'Peter'")
hash_set.remove2('Peter')
print("'Peter' is in the set:", hash_set.contains2('Peter'))
print("'Adele' has a hash code:", hash_set.hash_function2('Adele'))


