file = open('test.py','w') # write creates file if it does not exists
try:
    file.write("chai aur code")
finally:
    file.close()        

#OR
    
with open("test.py","w") as file:
    file.write("chai aur code")