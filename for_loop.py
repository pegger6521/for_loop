# list的清單符號適用中括號
# list可以混裝不同資料型別

# 第一個練習
# 對每一個在students清單(list)裡面的人say hi
# Allen Tom Mayday JJ Jolin Jay Jam

students = ['Allen', 'Tom', 'Mayday', 'JJ', 'Jolin', 'Jay', 'Jam']
for student in students:
	print('Hi', student)

# 第二個練習
# 用in檢查東西在不在清單(list)裡面

print('Allen' in students) #TRUE
print('Dylan' in students) #FALSE

# 第三個練習
# 用.append()來加東西進清單

students.append('Peggy')
for student in students:
	print(student)

# 第四個練習
# 用len()來取長度

print(len(students))

# 第五個練習
# 用字串當清單
# 練習len()取長度
# 練習用in檢查東西有沒有在裡面
# 字串可以拆成字母來檢查

cars = 'Toyota'
for car in cars: 
	print(car)
print(len(cars))
print('T' in cars) #TRUE
print('y' in cars) #TRUE
print('To' in cars) #TRUE
print('to' in cars) #FALSE
print('x' in cars) #FALSE
