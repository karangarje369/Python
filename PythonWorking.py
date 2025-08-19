# Internal working of python
# variables Immutable
a = 5 
b = a 
a = a + 5 
# print(a)
# print(b)
# now here first refrences of a & b were same but the moment a got +5 the value changed and refrence also changed 
# but the b variable holds refrence of 5 so it didnt vanished in garbage collector 
# But list behaves diffrent form variables because list is Mutable 
h1 = [1,2,3]
h2 = h1 
h1[0] = 6
# print(h1)
# print(h2)
#  here the 0th element got changed but refrence is same for both and the change got reflected in h2 too 

p1 = [1,2,3]
p2 = p1[:] # this makes copy so refrences are diffrent now 
p1[0] = 44
print(p1)
print(p2)
# so now changes will not reflect 
