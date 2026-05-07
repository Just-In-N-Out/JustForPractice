from typing import List

def get_last_three_elements(my_list: List[int]) -> List[int]:
    a = my_list[-1]
    b = my_list[-2]
    c = my_list[-3]
    return a,b,c


# do not modify below this line
print(get_last_three_elements([1, 2, 3]))
print(get_last_three_elements([1, 2, 3, 4, 5]))
print(get_last_three_elements([1, 2, 3, 4, 5, 6, 7, 8, 9]))
