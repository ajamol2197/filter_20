# 10
a = [0, 1, 2, 0, 3, 0, 4]
print(a)

b = list(filter(lambda el: el != 0, a))
print(b)

# 11
a = [-2, -1, 0, 2, 4, 5, 7]
print(a)

b = list(filter(lambda el: el > 0 and el % 2 == 0, a))
print(b)

# 12
a = [-5, -4, -3, -2, -1, 0]
print(a)

b = list(filter(lambda el: el < 0 and el % 2 != 0, a))
print(b)

# 13
a = [-5, 1, 5, 10, 15, 20]
print(a)

b = list(filter(lambda el: 1 <= el <= 10, a))
print(b)

# 14
a = [2, 5, 8, 10]
print(a)

b = list(filter(lambda el: el * el < 50, a))
print(b)

# 15
a = [15, 23, 35, 42, 55]
print(a)

b = list(filter(lambda el: el % 10 == 5, a))
print(b)

# 16
a = ["apple", "banana", "kiwi", "strawberry"]
print(a)

b = list(filter(lambda el: len(el) > 5, a))
print(b)

# 17
a = ["apple", "pear", "grape", "plum"]
print(a)

b = list(filter(lambda el: "a" in el, a))
print(b)

# 18
a = ["Ali", "vali", "Sardor", "john"]
print(a)

b = list(filter(lambda el: el[0].isupper(), a))
print(b)

# 19
a = ["123", "abc", "456", "78a"]
print(a)

b = list(filter(lambda el: el.isdigit(), a))
print(b)

# 20
a = ["", "hello", "", "world"]
print(a)

b = list(filter(lambda el: el != "", a))
print(b)
