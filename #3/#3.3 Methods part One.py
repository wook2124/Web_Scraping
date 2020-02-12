# function과 method의 차이
# method는 class안에 있는 function!
class Car():
  wheels = 4
  doors = 4
  windows = 4
  seats = 4

  def start():
    print("What is method.")


# python은 method를 호출할 때 그 method의 instance를 첫번째 argument로 사용하기 때문에 1 was given 이라고 오류가 뜬 것! (파이썬에만 해당되는 규칙)
class Car():
  wheels = 4
  doors = 4
  windows = 4
  seats = 4

  def start():
    print("What is method.")

porche = Car()
porche.start()


# python은 그 method를 호출한 instance를 argument로 사용함.
# porche(instance)가 method를 호출했으므로 내가 지정하지 않았어도 첫번째 argument가 자동으로 되는 것!
class Car():
  wheels = 4
  doors = 4
  windows = 4
  seats = 4

  def start(method):
    print(method.instance)
    print("What is method.")

porche = Car()
porche.instance = "This is First instance"
porche.start()


# method는 아무렇게나 이름을 정해줘도 argument는 porche로 정해져있기 때문에 method 안에 argument인 porche를 써주면 오류없이 출력이 됨!
class Car():
  wheels = 4
  doors = 4
  windows = 4
  seats = 4

  def start(this_is_nothing):
    print(porche.instance)
    print("What is method.")

porche = Car()
porche.instance = "This is First instance"
porche.start()


# 내가 만든 모든 method(class안에 있는 function)의 첫번째 argument는, 그 method를 호출한 instance가 된다.
# 때문에 porche.start()라고 method를 부른뒤 () 안에 또 porche를 입력하니 2 was given 오류가 뜬 것!
class Car():
  wheels = 4
  doors = 4
  windows = 4
  seats = 4

  def start(self):
    print(self.doors)
    print("What is method.")

porche = Car()
porche.instance = "This is First instance"
porche.start(porche)