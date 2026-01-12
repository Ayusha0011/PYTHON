tuple_py = ('Java','Kotlin','Ruby','Laravel')
y = list(tuple_py)
y.append("C")
tuple_py = tuple(y)

print(type(tuple_py))
print(tuple_py)

(hard, ihavenotseen, soundsexpensive , *php) = tuple_py
print(hard)
print(ihavenotseen)
print(soundsexpensive)
print(*php)
