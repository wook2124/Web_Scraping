# 인자(argument, who) 추가하기
def say_hello(who):
  print("hello", who)

# 유효한 타입이면 다 인자로 출력가능
say_hello(True)


# 계산 연습하기와 default value(=0)
def plus(a, b):
  print(a + b)

def minus(a, b, c, d=0):
  print(a - b - c - d)

print(15 + 75)
plus(1234, 4321)
minus(1823, 1000, 800)


# default 연습
def say_hello(name="anonymous"):
  print("hello", name)

say_hello()
say_hello("Wook")

# 배운거 복습하기!
def 안녕이라고_말하는_함수(a, b):
  print("안녕", "hello~~", a, b)

안녕이라고_말하는_함수("나는", "코딩 공부중이야")