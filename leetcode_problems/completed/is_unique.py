'''
Implement an algorithm to determine if a string has all unique characters
'''

def is_unique(string):
    store = []
    for letter in string:
        if letter in store:
            return False
        else:
            store.append(letter)
    return True

'''
What if you can't use any additional data structures?
'''

def is_unique(string):
    string_size = len(string)
    for i in xrange(string_size):
        for j in xrange(i+1,string_size):
            if string[i] == string[j]:
                return False
    return True
               
# tests

tests = [
    'uniq',
    'repeater',
    'a',
    'aa',
    'aaaaaaaaa',
    'bottle',
    ]

expected_outputs = [
    True,
    False,
    True,
    False,
    False,
    False
    ]

print(map(is_unique, tests))

