# b가 str이기 때문에 결과는 None이 뜸
def plus(a, b):
  if type(b) is str:
    return None
  else:
    return a + b

a = 12
b = "10"

result = plus(a, b)
print(result)


# is를 is not int로 바꿔줌!
# 3.1234는 int(정수)가 아니라 float(소수) 
def plus(a, b):
  if type(b) is not int:
    return None
  else:
    return a + b

a = 12
b = 3.1234

result = plus(a, b)
print(result)


# type(b)가 int, float가 아닌 경우에는
# else블록으로 이동되어 Error 표시가 뜸
def plus(a, b):
  if type(b) is int or type(b) is float:
    return a + b
  else:
    return "Error"

a = 12
b = "asdf"

result = plus(a, b)
print(result)