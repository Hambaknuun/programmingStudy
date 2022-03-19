# 리스트(List) 
# 리스트 자료형(순서O, 중복O, 수정O, 삭제O)

# 선언
a = []
b = list()
c = [70, 75, 80, 85]
d = [1000, 10000, 'Ace', 'Base', 'Captin']
e = [1000, 10000, ['Ace', 'Base', 'Captin']]
f = [21.42, 'foobar', 3.4, False, 3.14159]

# 인덱싱
print('>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1][1])
print('e - ', list(e[-1][1]))   # e -  ['B', 'a', 's', 'e']

# 슬라이싱
print('>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[-1][1:3])   # e -  ['Base', 'Captin']

# 리스트 연산
print('>>>>>')
print('c + d', c + d)   # list + list  = list
print('c * 3', c * 3)   # list 반복
print("'Test' + c[0] - ", 'Test' + str(c[0]))

# 값 비교
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])






