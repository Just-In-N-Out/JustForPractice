def add_two_numbers() -> int:
    values = input().split(",")
    c=0
    for i in values:
      c += int(i)
    return(c)



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
