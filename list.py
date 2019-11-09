import my_library as ml



fruits = ["Apple", "Banana", "Pineapple", "Grape"]
loud_fruits1 = [fruit.lower() for fruit in fruits]
loud_fruits2 = [fruit.upper() for fruit in fruits]

print(loud_fruits1, loud_fruits2)

print(list(enumerate(loud_fruits1)))
print(list(enumerate(loud_fruits2)))

print(fruits)

new_word = 'New : '.join(reversed(fruits))

print(new_word)

net = ml.my_function(5)
print(net)
print(l)