fruits = ["apple", "orange", "coconut"]
fruits_char = [fruit[0] for fruit in fruits]
print(fruits_char)

num = [1,-2,5,-3,9,-54]
positive_num = [ num for number in num if number >=0]
print(positive_num)
sqnum = [ num**2 for num in range(0,10)]
print(sqnum)

all_num = [5, 9, 45, 55, 22]
filtered = [x for x in all_num if x > 10]
print(filtered)
