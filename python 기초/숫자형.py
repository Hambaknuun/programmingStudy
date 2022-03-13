# 형변환 실습
a = 3.      #float
b = 6       #int
c = .7      #float
d = 12.7    #float

# 타입 출력
print(type(a), type(b), type(c), type(d))

# 형 변환
print(float(b))     #6.0
print(int(c))       #0
print(int(d))       #12
print(int(True))    # True : 1. False : 0
print(float(False)) #0.0
print(complex(3))   #(3+0j)
print(complex('3')) #(3+0j) **문자형 -> 숫자형
print(complex(False))   #0j

# 수치 연산 함수
print(abs(-7))      #절대값 (7)

x, y = divmod(100, 8)   #몫과 나머지
print(x, y)             #12 4

print(pow(5, 3), 5 ** 3) #제곱 (125 125)

# 외부 모듈
import math

print(math.pi)  #3.141592653589793

print(math.ceil(5.1)) #x 이상의 수 중에서 가장 작은 정수 (6)

