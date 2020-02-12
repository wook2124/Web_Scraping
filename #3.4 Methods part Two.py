# dir은 class안에 있는  모든 것들(properties)을 list로 보여줌
class Car():
  wheels = 4
  doors = 4
  windows = 4
  seats = 4

print(dir(Car))


# 안에 있는 '__str__'은 class안에 이미 내재되어 있는 method(function)임
# 즉 어떤 argument가 와도 str(문자열)로 출력하고자 함을 내포한 것임!
# 여기서 class 안에 있는 method 중 하나인 __str__() 을 override(재정의)하고 return 값을 해주면 내가 치는 값이 출력됨
# __str__() 에서 ()는 self를 지칭함
# python이 자동으로 porche.__str__()을 호출해서 porche를 print해도 내가 return한 값이 나오게 됨
class Car():
  wheels = 4
  doors = 4
  windows = 4
  seats = 4

  def __str__(self):
    return "I'm changing 'str' myself."

porche = Car()
print(porche)


# __init__이란 - class를 만들었을 때 바로 만들어지는 method
class Car():

  def __init__(self, *args, **kwargs):
    self.wheels = 4
    self.doors = 4
    self.windows = 4
    self.seats = 4

  def __str__(self):
    return f"Car with {self.wheels} wheels"


porche = Car()
print(porche)


# kwargs.get(k, d) - 
# k는 key(내가 원하는 것), d는 default(값)으로 내가 원하는 값이 없을 때 나타낼 값
# positional argument가 아닌 keyword argument로 지정해서 사용할 것이기 때문에 args는 사실상 필요없음!
class Car():

  def __init__(self, *args, **kwargs):
    self.wheels = 4
    self.doors = 4
    self.windows = 4
    self.seats = 4
    self.color = kwargs.get("color", "black")
    self.price = kwargs.get("price", "$20")

  def __str__(self):
    return f"Car with {self.wheels} wheels"


porche = Car(color = "Green", price = "$40")
print(porche.color, porche.price)


# mini = Car()
# ()안에 아무것도 입력하지 않아서 default value뜸
class Car():

  def __init__(self, **kwargs):
    self.wheels = 4
    self.doors = 4
    self.windows = 4
    self.seats = 4
    self.color = kwargs.get("color", "black")
    self.price = kwargs.get("price", "$20")

  def __str__(self):
    return f"Car with {self.wheels} wheels"


porche = Car(color = "Green", price = "$40")
print(porche.color, porche.price)

mini = Car()
print(mini.color, mini.price)