# PROJECT: (WK-04) Conditions
# Solution written by Darren Halpin

# define test vars
a = 5
b = 4
c = 3

# do calculations
test_a = a < b
test_b = a != b
test_c = a > b | a < c
test_d = a > b or a < c
test_e = a - 1 == b
test_f = not b > c

print("TEST A is: {} \nTEST B is: {} \nTEST C is: {} \nTEST D is: {} \nTEST E is: {} \nTEST F is: {} \n "
      .format(test_a, test_b, test_c, test_d, test_e, test_f))

