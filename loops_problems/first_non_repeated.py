input_str = "aabbc"

for char in input_str:
    if input_str.count(char) == 1:
        print("char is:",char)
        break