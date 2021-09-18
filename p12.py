s1 = {10, 20, 30}
print(s1)

# add ele
s1.add(40)
print(s1)
s1.add(10) # sets are unique so it only shows one element at once
print(s1) # since 10 is already in set it will show 10 only once 

s1.update([20, 50]) # update is to add more than one elements
print(s1)

# remove ele
s1.remove(20)
print(s1)
#s1.remove(20) # since 20 is already remove it will show keyword error

s1.discard(30) 
# if the element is present in set it will discard ow it remains as it is
print(s1)
s1.discard(30)
print(s1)
# its better to use discard() funtn than remove() functn

s1.clear()
print(s1)