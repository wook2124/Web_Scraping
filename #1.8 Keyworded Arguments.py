# Positional Arguments(의존적인 인자)
# 여기서는 3과 a / 7과 b가 해당됨
def plus(a, b):
  print(a + b)

result = plus(3, 7)

print(result)


# print를 return으로 바꾸니 None이 없어짐
# b=4, a=3으로 인자의 위치를 바꾸고 Keyworded해줌
def plus(a, b):
  return(a - b)

result = plus(b=4, a=3)

print(result)


# return은 함수에 ()를 씌우지 않아도 읽힘
# 아직 name과 age에 {}을 안씌워줘서 안읽힘
def say_hello(name, age):
  return "Hello name, you are age years old?"

hello = say_hello("Wook", 27)
print(hello)


# f는 format임 그리고 각 argument(인자)에 {}를 씌워줘야함
def say_hello(name, age):
  return f"Hello {name}, you are {age} years old?"

hello = say_hello("Wook", 27)
print(hello)


# 이렇게 해도 나오지만..
def say_hello(name, age):
  return "Hello" + name + "you are" + age + "years old?"

hello = say_hello("Wook", "27")
print(hello)
# 이렇게 띄어쓰기까지 신경써야 완벽해짐..
# 그리고 "27"로 integer(정수)도 신경써야함!!
def say_hello(name, age):
  return "Hello " + name + " you are " + age + " years old?"

hello = say_hello("Wook", "27")
print(hello)


# 다시 Keyworded Arguments 활용하기
def say_hello(name, age):
  return f"Hello {name}, you are {age} years old?"

hello = say_hello(age="27", name="Wook")
print(hello)


# 각 str 앞에는 꼭 f(format)을 입력!
# {}의 Keyworded Arguments가 인식이됌, 띄어쓰기도 중요
# Keyworded Arguments를 활용하면 인자의 이름만 기억하면됌!
def say_hello(name, age, where_from, fav_food):
  return f"Hello {name}, you are {age} years old? " f"And {where_from} is good to live? " f"So is this your {fav_food}??"

hello = say_hello(age="27", fav_food="참치마요", where_from="Korea", name="Wook")
print(hello)


# 다시 깔끔하게 수정함
def say_hello(name, age, where_from, fav_food):
  return f"Hello {name}, you are {age} years old? And you are from {where_from} right? So {fav_food} is your favorite food??"

hello = say_hello(age="27", fav_food="참치마요", where_from="Korea", name="Wook")
print(hello)