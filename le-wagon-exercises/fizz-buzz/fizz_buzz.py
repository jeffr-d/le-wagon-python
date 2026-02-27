# Start with some pseudo-code!

# for n in n

# else if n is divisible by 3 and by 5
#   => print "fizzbuzz"

# if n is divisible by 3
#   => print "fizz"

# else n is divisible by 5
#   => print "buzz"

# else 
#   => print n

for n in range(1, 100 + 1):
    
    if n % 3 == 0 and n % 5 == 0:
        print("fizzbuzz")
    
    elif n % 3 == 0:
        print("fizz")
    
    elif n % 5 == 0:
        print("buzz")
    
    else:
        print(n)