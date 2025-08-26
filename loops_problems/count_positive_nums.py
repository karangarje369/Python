#Given list of numbers count positive numbers 
number = [-1,2,-3,1,3,5,6]
count_of_positive = 0

for num in number:
    if num > 0:
        count_of_positive += 1

print("Final count of positive numbers:",count_of_positive)