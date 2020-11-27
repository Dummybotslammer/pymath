#This is a main program for testing the math module:
import multimath

#set seed test(int):
print("set seed integer test:")
s = 1234
for x in range(1,5):
    s = multimath.randInt(seed=s)
    print(s)
print("\n")

#random seed test(int):
print("random seed integer test:")
s = multimath.randInt()
for x in range(1,5):
    s =multimath.randInt(seed=s)
    print(s)
print("\n")

#set seed integer and set length test:
print("set seed integer and length test:")
s = 2345
for x in range(1,5):
    s = multimath.randInt(seed = s)
    print(s)
print("\n")

#set seed float rng test:
print("set seed float rng test:")
s = 3456
for x in range(1,5):
    s =multimath.rand(seed = s)
    print(s)
print("\n")

#random seed float rng test:
print("random seed float rng test:")
s = multimath.rand()
for x in range(1,5):
    s = multimath.rand(seed=s)
    print(s)
print("\n")

#random seed bool rng test:
print("random seed bool rng test:")
s = multimath.rand()
r = multimath.randBool(seed=s)
for x in range(1,5):
    s = multimath.rand(seed=s)
    r = multimath.randBool(seed=s)
    print(r)
print("\n")

