def new_line_max_num():
    print("---------max_num------------")

def new_line_mult_lists():
    print("---------mult_lists------------")

def new_line_rev_string():
    print("---------rev_string------------")

def new_line_num_within():
    print("---------num_within------------")

def new_line_pascal():
    print("---------pascal------------")


# Write a Python function called max_num()to find the maximum of three numbers.
new_line_max_num()

def max_num(x,y,z):
    return max([x,y,z])

print(max_num(10,20,30))
print(max_num(235,12,500))


# Write a Python function called mult_list() to multiply all the numbers in a list.
new_line_mult_lists()

def mult_lists(lst):
    if len(lst) == 0:
        return 0
    prod = lst[0]

    if len(lst) > 1:
        for i in lst[1:]:
            prod = prod * i

    return prod

print(mult_lists([44,22,13]))
print(mult_lists([]))
print(mult_lists([30]))
print(mult_lists([3,2]))


# Write a Python function called rev_string() to reverse a string.

new_line_rev_string()

def rev_string(str_back):
  return str_back[::-1]

print(rev_string("1234"))
print(rev_string("black"))
print(rev_string("white"))

# Write a Python function called num_within() to check whether a number falls in a given range.
new_line_num_within()

def num_within(x,a,b):
  return x in range(a,b+1)
     
print(num_within(3,1,4))     
print(num_within(3,1,3))     
print(num_within(10,15,9))


# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
new_line_pascal()


triangle = [[1],[1,1],[2,2,2],{4}]
def pascal(n):
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      length = len(row_prev)+1
      for i in range(length):
        if i == 0:
          row.append(1)
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1
    for row in triangle:
      print(row)

pascal(2)
new_line_pascal()
pascal(5)
new_line_pascal()
pascal(8)