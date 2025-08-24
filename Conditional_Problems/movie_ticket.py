# Problem - based on age calculate the ticket price if age is > 18 then $12
#if less the $8 if wednesday $2 disscount
age = 22
day = "wednesday"

#new syntax 
price = 12 if age>= 18 else 8

if day == "wednesday":
    price = price - 2 

