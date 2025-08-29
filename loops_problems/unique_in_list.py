items = [ "apple" , "banana" , "orange" , "apple"]

unique = set()

for item in items:
    if item in unique:
        print("duplicate",item)
    unique.add(item)    