# 문자열 생성
from curses import raw


str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4))

# 빈 문자열
str1_t1 = ''
str2_t2 = str() #Object

print(type(str1_t1), type(str2_t2)) # 모두 str
print(len(str1_t1), len(str2_t2))   # 0 0

# 이스케이프 문자 사용
"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
...

"""

print("I'm a boy")  #I'm a boy
print('I\'m a boy') #I'm a boy

print('a \t b')     #a        b
print('a \"\" b')   #a "" b
 
escape_str1 = "Do you have a \"retro game\"?"
print(escape_str1)
escape_str2 = 'What\'s on TV?'
print(escape_str2)

# 탭,줄 바꿈
t_s1 = "Click \t to start!"
t_s2 = "New line \n Check!"

print(t_s1)
print(t_s2)
print()

# Raw String
# pip install windows-curses
raw_s1 = r"D:\python\test"
print(raw_s1)
print()

# 멀티라인 입력
# 역슬래시(\)로 다음 행에 변수가 바인딩되는것을 알려줄 수 있음
multi_str = \
"""
asdasffdfasdfssdfddd
ddddddddddddddddddddddddddddddd
ddddddddddddddddddddddddddddd
"""

print(multi_str)

# 문자열 연산
str_o1 = "Python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Daejeon Busan Jinju"

print(str_o1 * 3)       # 문자열의 반복 PythonPythonPython
print(str_o1 + str_o2)  # 문자열의 합 PythonApple
print('y' in str_o1)    #True
print('z' in str_o1)    #False
print('P' not in str_o2) #True


# 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))

# ☆★☆★☆★☆★☆★
# 문자열 함수 (upper, isalnum, startswith, count, endswith, isalpha)
print("Capitaliaze: ", str_o1.capitalize())
print("endswith?: ", str_o2.endswith("e"))
print("replace: ", str_o1.replace("thon", ' Good'))
print("sorted: ",sorted(str_o1))
print("split: ", str_o4.split(' '))
print("join str: ", str_o1.join(["I'm ", "!"]))
print("reversed1: ", reversed(str_o2)) #list 형 변환
print("reversed2: ", list(reversed(str_o2)))

# 반복(시퀀스)
im_str = "Good boy!"
print(dir(im_str)) #__iter__ -> 시퀀스를 반복 할 수 있다


# 출력
for i in im_str:
    print(i)

# 슬라이싱
str_s1 = "Nice Python"

print(len(str_s1))
# 슬라이싱 연습
                    # 0 1 2 3
print(str_s1[0:3])  # |N|i|c| -> 0부터 3번째 구분까지 자른것
print(str_s1[5:])
print(str_s1[:len(str_s1)])     # str_s1[:11]
print(str_s1[:len(str_s1)-1])   # str_s1[:10]
print(str_s1[1:9:3])            # [start_index, end_index, iterate]
print(str_s1[-2:])      # on (뒤에서 2번째 부터)
print(str_s1[-5:])      # ython 
print(str_s1[1:-2])     # ice Pyth (1번째부터 뒤에서 두번째까지)
print(str_s1[::2])      # Nc yhn (2 칸 간격으로 문자를 가져옴)
print(str_s1[::-1])     # nohtyP eciN (1칸 간격으로 거꾸로 문자를 가져옴)

# 아스키 코드(또는 유니코드)
a = 'z'

print(ord(a))       # 122 (아스키 코드로)
print(chr(122))     # z   (문자로)







