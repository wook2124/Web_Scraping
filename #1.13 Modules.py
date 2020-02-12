# 여러가지 Modules(math, date, time 등)을 import 
# 손쉽게 함수(function)를 정의할 수 있다.
import math

print(math.ceil(1.2))
print(math.fabs(-1.2))


# math 전체를 가지고 오지 않고
# 필요한 ceil, fsum만 가지고 옴
# fsum을 연산할 때는 [] list를 이용해서!
from math import ceil, fsum

print(ceil(1.2))
print(fsum([3, 5 ,6 ,7 ,8]))


# as로 fsum함수를 다른 이름 '리스트사용'으로
# 바꿔줄 수 있음, 함수 = 리스트사용
from math import fsum as 리스트사용

print(리스트사용([3, 5 ,6 ,7 ,8]))


# 내가 만든 calculator 폴더에 있는 것들을
# import(수입)해올 수 가 있음!
from  calculator import plus, minus, times, division, remainder, negation, power

print(plus(1, 2))
print(minus(6, 3))
print(times(2, 3))
print(division(8, 2))
print(remainder(10,3))
print(negation(3, 2))
print(power(2, 6))