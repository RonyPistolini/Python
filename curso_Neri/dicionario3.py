d = dict.fromkeys(["java","python","android"])
print(d)
d.update(java=129)
print(d)
d.pop("android")
print(d)