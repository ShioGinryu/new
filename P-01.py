print 1
print int("1",2)

squares = [x*x for x in range(1,11)]
print filter(lambda x: (x >= 30)and(x <= 70), squares)

to_one_hundred = range(101)
backwards_by_tens = to_one_hundred[::-10]
print backwards_by_tens