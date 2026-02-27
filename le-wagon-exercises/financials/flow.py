# can you vote ?

# pseudo-code:
# define the age
# if age is over or equal 18
#   => tell the user can vote
# else
#   => tell the user cannot vote

age = int(input("How old are you?")) # Interactive
if age  >= 18:
    print(f"you are {age} so you can vote!")
    
else:
    print(f"You are {age} so you cannot vote")