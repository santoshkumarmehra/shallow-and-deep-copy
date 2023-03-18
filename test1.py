import copy

# 1 here is  both reference variable are points to same object.
#if we changes any variable then another also affected .
#here we are do aliasing

l1 = [1,2,3,4] 
l2=l1
l2[1] = 111
print(l1)
print(l2)
print(id(l1))
print(id(l2)) 



# 2 shallow copy

l1= [1,2,[10,20],4]
l2=copy.copy(l1)
l1[2][0] = 111
l1[2][1] = 333
print(l1)
print(l2)
print(id(l1)) #1369618138752
print(id(l2)) #1369619654720
print(id(l1[2])) #1369619863552
print(id(l2[2])) #1369619863552


# 3 Deep copy 

l1=[1,2,3,4]
l2 = copy.deepcopy(l1)

l1[1] = 999

print(l1)
print(l2)

print(id(l1))
print(id(l2)) 

#2eg..

l1=[1,2,[10,20,30],4]
l2 = copy.deepcopy(l1)

l1[1] = 999
l1[2][0] = 123
l1[2][1] = 100

print(l1)
print(l2)
print(id(l1))
print(id(l2)) 