# dictionary - key value pair 
chai_types = { "Masala":"Spicy" , "Ginger":"Zesty" , "Green":"Mild"}

#Accessing the items 
print(chai_types["Masala"])
print(chai_types.get("Ginger"))

#dictionaries are mutable in python
chai_types["Ginger"] = "funn"
print(chai_types)

# Iterating over dic
#keys
for chai in chai_types:
    print(chai)
#values    
for chai in chai_types:
    print(chai_types[chai])

# one more way
for key, value in chai_types.items():
    print(key , value)        

# Questioning and conditionals 
if "Masala" in chai_types:
    print("True")        

# Len()
print(len(chai_types)) 

# pop and popitem
chai_types.pop("Masala")
chai_types.popitem()

# copy 
chai_copy = chai_types.copy()

# nested dictionaries 
tea_shop = {
    "chai": {
        "Ginger" : "Spicy",
        "Black"  : "Strong" 
    },
    "Price": {
        "Ginger" : "20",
        "Black" : "10"
    }
}
print(tea_shop["chai"]["Ginger"],tea_shop["Price"]["Ginger"])

#Squared numbers (Comprehension)
squared_nums = { X: X**2 for X in range(6)}
print(squared_nums)

# clear 
squared_nums.clear()

# making a dictionary from list of keys and value 
keys = ["Masala", "Ginger", "Green"]
default_value = "Delicious"
new_dict = dict.fromkeys(keys,default_value)
print(new_dict)