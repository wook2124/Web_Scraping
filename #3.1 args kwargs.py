# *args는 positional arguments를 무제한으로 나타나게해줌!
# 때문에 이것을 출력하면 a, b에 해당하는 3, 5는 return 되고
# 뒤에 있는 1, 1, 1이 () tuple로 묶여서 출력됨!
def plus(a, b, *args):
  print(args)
  return a + b

plus(3, 5, 1, 1, 1)


# **kwargs는 keyword arguments를 무제한으로 나타나게해줌!
# 이것은 {} dictionary로 묶여서 출력됨!
def plus(a, b, *args, **kwargs):
  print(args)
  print(kwargs)
  return a + b

plus(1, 1, 1, 1, 1, hello=True, helloo=True, hellooo=True)


# 계산기 만들기
# *args를 통해 positional arguments를 무제한으로 나타나게 하고
# result = 0 으로 정한뒤,  for number(라고명명) in args(무제한 positional argumets를 불러옴)
# 마지막으로 result += number (여기서 +다음 =를 바로 붙여주지 않으면 동작이 안됨)
def plus(*args):
  result = 0
  for number in args:
    result += number
  print(result)

plus(1, 1, 1, 1, 1, 21, 549, 23, 26, 94)