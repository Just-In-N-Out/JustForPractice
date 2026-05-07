from typing import List

def contains_duplicate(words: List[str]) -> bool:
    my_set = set(words)
    a = len(words)
    b = len(my_set)
    if a == b: 
        return False
    else:
        True

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
