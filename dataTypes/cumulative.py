sets = (6,3,4,5,3)
print(dir(sets))
for elements in sets:
    print(f"{elements:.2f}")

dict = {"name": "solomon", "age": 12}
word = "name"
print(dict.get(word))