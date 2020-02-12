# class는 Blueprint(설계도)역할
# 그 안에 property인 wheels, doors, windows, seats가 있음
class Car():
  wheels = 4
  doors = 4
  windows = 4
  seats = 4

# instance는 그 설계도로 만든 결과물을 뜻함
# 즉 wheels, doors, windows, seats는 Car의 기본 요소니까 설계도에 있는대로 따라가고
# color는 차마다 다를 수 있으니까 따로 지정해준 것!
# Car() << 이것을 instantiation이라고 함 - 설계도를 가져와서 instance를 만드는 행위
porche = Car()
porche.color = "Red"


ferrari = Car()
ferrari.color = "Yellow"

mini = Car()
mini.color = "White"