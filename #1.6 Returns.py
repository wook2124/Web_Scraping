# return은 input(입력)한 값을 return(돌려)받지 않고
# 상황을 바로 끝내는 것을 의미함
def p_plus(a, b):
  print(a + b)

def r_plus(a, b):
  return a + b

p_result = p_plus(5, 5)
r_result = 10

print(p_result, r_result)


# return 다음의 함수는 생명이 없음(작동하지 않음)
def r_plus(a, b):
  print("Something here asldfkjasdflksajdf", True)
  return a + b
  print("Hello~ Is anyone here?", False)

r_result = r_plus(3, 7)

print(r_result)


# program은 print를 신경쓰지 않는다
# print는 그저 터미널에서 보여주는 값에 불과함
def plus(a, b):
  return a + b

result = plus(3, 7)

print(result)


# None의 의미 = print해서 나온 것은 그저 보여주기용
def p_plus(a, b):
  print(a + b)

p_result = p_plus(3, 7)

print(p_result)