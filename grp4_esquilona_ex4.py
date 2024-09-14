def condition(value):
    if value > 10:
        return True
    else:
        return False
        
result = condition(15)
print(result) 

# List
favorite_things = ["pink", "unicorns", "rainbows", "coding", 56, True]
print("My favorite things: ", favorite_things)

# Tuple
daily_routine = ("wake up", "drink coffee", "code like a boss", "sleep", 56, False)
print("My daily routine: ", daily_routine)

# Set 
dreams = {"be a good coder", "travel the world", "help others", 56, True}
print("My dreams: ", dreams)

# Dictionary: A collection of key-value pairs (Mapping)
about_me = {
    "name": "Jewel",
    "age": 22, 
    "is_student": True,
    "favorite_number": 56,
    "talents": ["coding", "singing", "dancing"]
}

# Dictionary elements
print(f" And name is {about_me['name']} and I love {', '.join(about_me['talents'])}")

# Checking Boolean 
if about_me["is_student"]:
    print("I'm currently studying in PLMUN")
else:
    print("I am a successful woman")