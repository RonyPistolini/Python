import random

# for num in range(10):
#     print(num)

for num in range(10):
    print(random.randint(1 ,50))

for num in range(10):
    print(random.random())

for num in range(10):
    print(random.uniform(20,30))

lista = [2,43,56,3,2,45,453,532,32,4,3,2]
print(lista)
random.shuffle(lista)
print(lista)