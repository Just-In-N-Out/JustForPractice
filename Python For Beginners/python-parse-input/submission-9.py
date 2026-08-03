from typing import List

def read_integers() -> List[int]:
  parts = input().split(",")    
  result = []
  for p in parts:
    result.append(int(p))
  return result


# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
