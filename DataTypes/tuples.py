# similar to list but tuples are immutable
tea_types = ("Black", "Green", "Oolong")
print(tea_types)
more_tea = ("Ginger", "Masala", "White")
all_tea = tea_types + more_tea

(tea1,tea2,tea3) = tea_types
print(tea1,tea2)

type(tea_types)
