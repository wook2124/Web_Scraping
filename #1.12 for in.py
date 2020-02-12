# for 변수 in sequence는 s를 나열해줌
days = ("Mon", "Tue", "Wed", "Thur", "Fri")

for variable in days:
  print(variable)


# 밑에 보이는 것과 같이 s를 설정하면 s가 나열됨
days = ("Mon", "Tue", "Wed", "Thur", "Fri")

for variable in [1, 2, 3, 4, 5]:
  print(variable)


# v에 break를 걸어주면 for loop가 
# 딱 그 v에 해당되는 곳에서 멈춤("Thur")
days = ("Mon", "Tue", "Wed", "Thur", "Fri")

for variable in days:
  if variable is "Thur":
    break
  else:
    print(variable)

 
# 정리:for문 - string, tuple 또는 list 같이 
# 배열의 요소를 순차적으로 나타내준다
# str도 python에서는 배열의 의미를 갖음
days = ("Mon", "Tue", "Wed", "Thur", "Fri")

for letter in "JH":
  print(letter)