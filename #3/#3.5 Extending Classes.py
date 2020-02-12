# inherit(상속), extend(확장)하기
# class Convertible()에서 ()에 부모 class의 이름을 적으면 됨!
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


class Convertible(Car):

  def take_off(self):
    return "taking off"


porche = Convertible(color = "Green", price = "$40")
porche.take_off()
porche.wheels


# 결국 class Cars_son_of_son은 자기의 할아버지 격인 Car의 모든 method를 갖게됨!
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


class Convertible(Car):

  def take_off(self):
    return "taking off"


class Cars_son_of_son(Convertible):
  pass


porche = Convertible(color = "Green", price = "$40")
porche.take_off()
porche.wheels


# override한 것 다시 override하기
# 그러나 이렇게 override(재정의)하게 되면 말그대로 color같이 원래 갖고있는 속성도 사라지게 됨!
# 그저 __init__에 항목을 하나 더 추가하고 싶었을 뿐인데도!
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


class Convertible(Car):

  def __init__(self, **kwargs):
    self.time = kwargs.get("time", 10)

  def take_off(self):
    return "taking off"

  def __str__(self):
    return f"Car with no roof"


class Cars_son_of_son(Convertible):
  pass


porche = Convertible(color = "Green", price = "$40")
print(porche.color)


# super().를 통해서 부모클래스에 접근한 뒤 __init__ method를 호출함
# super는 father, upper class에 해당한다! (super is father)
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


class Convertible(Car):

  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.time = kwargs.get("time", 10)

  def take_off(self):
    return "taking off"

  def __str__(self):
    return f"Car with no roof"


class Cars_son_of_son(Convertible):
  pass


porche = Convertible(color = "Green", price = "$40")
print(porche.color)