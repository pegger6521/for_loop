# for loop的第一個練習
# 對每一個在students清單裡面的人say hi
# Allen Tom Mayday JJ Jolin Jay Jam

students = ['Allen', 'Tom', 'Mayday', 'JJ', 'Jolin', 'Jay', 'Jam']
for student in students:
	print('Hi', student)

# for loop的第二個練習
# 檢查該東西在不再清單裡面的方式

print('Allen' in students)
print('Dylan' in students)

# for loop的第三個練習
# 用len()來取長度

print(len(students))

# for loop的第四個練習
# 用字串當清單
# 練習len()取長度
# 練習用in檢查東西有沒有在裡面, 字串可以拆成字母來檢查

cars = 'Toyota'
for car in cars: 
	print(car)
print(len(cars))
print('T' in cars)
print('y' in cars)
print('To' in cars)
print('to' in cars)
print('x' in cars)
