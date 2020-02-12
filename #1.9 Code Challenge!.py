# 내가 만든 계산기(?!) 
def change_int(lalala):
  return int(lalala)


def plus(a, b):
  return a + b

def minus(a, b):
  return a - b

def times(a, b):
  return a * b

def division(a, b):
  return a / b

def remainder(a, b):
  return a % b

def negation(a, b):
  return -a

def power(a, b):
  return a ** b

a = change_int("10")
b = change_int("3")

result = plus(a, b), minus(a, b), times(a, b), division(a, b), remainder(a, b), negation(a, b), power(a, b)

print(result)