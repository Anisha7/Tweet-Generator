#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(N*M)(N = # buckets, M = # items in bucket) 
        Why and under what conditions?: under all conditions because it adds all the keys"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(N*M) (N = # buckets, M = # items in bucket) 
        Why and under what conditions?: under all conditions because it adds all the values"""
        # Loop through all buckets
        # Collect all values in each bucket
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(N*M)
        Why and under what conditions? all conditions since we add all the items"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets: # O(M = # buckets)
            all_items.extend(bucket.items()) # O(2N = # items in bucket)
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(N) where N is the length of items in the bucket
        Why and under what conditions?: All conditions because we need to loop 
        through all the elements"""
        
        total = 0
        # Loop through all buckets
        for i in range(len(self.buckets)):
            # Count number of key-value entries in each bucket
            total += self.buckets[i].length()
        return total
    
    # find bucket where a key belongs
    def find(self, key):
        # helper function to check if checking (key, val) == (key we are looking for)
        # data is a tuple (key, val)
        # O(N) because of the find function
        index = self._bucket_index(key)
        def quality(data):
            return data[0] == key
        
        return self.buckets[index].find(quality)

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(N) because the find function is O(N)
        Why and under what conditions?: When the element is at the end of the bucket"""
        # Find bucket where given key belongs
        result = self.find(key)
        if (result != None):
            # Check if key-value entry exists in bucket
            return True
        return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(N) because the find function
         Why and under what conditions?: when the element is at the end of the bucket"""
        # Find bucket where given key belongs
        bucket = self.find(key) # tuple (key, val)
        # Check if key-value entry exists in bucket
        if (bucket != None):
            # If found, return value associated with given key
            return bucket[1]
        # tell user get failed
        else:
            raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(N) because find/replace functions
         Why and under what conditions?: when element is at the end of the bucket"""
        # Find bucket where given key belongs
        bucket = self.find(key)
        index = self._bucket_index(key)
        # Check if key-value entry exists in bucket
        if (bucket != None):
            # If found, update value associated with given key
            self.buckets[index].replace(bucket, (key, value))
            return
        # else, insert given key-value entry into bucket
        else:
            self.buckets[index].append((key, value))

        print(str(self.buckets))

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(N) 
        Why and under what conditions?: when the element is at the end of the bucket"""
        # Find bucket where given key belongs
        bucket = self.find(key)
        index = self._bucket_index(key)
        # Check if key-value entry exists in bucket
        if (bucket != None):
            # If found, delete entry associated with given key
            self.buckets[index].delete(bucket)
            return
        # tell user delete failed
        else:
            raise KeyError('Key not found: {}'.format(key))            


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
