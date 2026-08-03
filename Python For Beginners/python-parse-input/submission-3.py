from typing import List

def read_integers() -> List[int]:
  inte = input()
  int_list = inte.split(",")
  return(int_list)


# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
