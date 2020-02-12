# if조건문이 False로 발동이 안되면
# 그 다음 조건문인 elif문이 True로 발동이 된다.
# elif까지 False로 발동이 안되면
# 맨 마지막인 else로 이어지고 끝이난다

# or은 조건문 둘 중 하나만 True해도 실행되고,
# and는 조건문 둘 다 True해야 실행이 된다.
def age_check(age):
  print(f"you are {age}")
  if age < 18:
    print("you can't drink")
  elif age == 18 or age == 19:
    print("you are new to this!")
  elif age > 20 and age < 25:
    print("you are still kind of young")
  else:
    print("enjoy your drink")

age_check(19)