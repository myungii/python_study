y = lambda x : 3 * x
print(y(12))

add = lambda a, b : a + b
print(add(2, 3))

littlePrince = '''여섯 살 적에 나는 '체험한 이야기'라는 제목의, 원시림에 관한 책에서 기막힌 그림 하나를 본 적이 있다. 맹수를 집어삼키고 있는 보아뱀 그림이었다. 위의 그림은 그것을 옮겨 그린 것이다. 그 책에는 이렇게 씌어 있었다.
'보아뱀은 먹이를 씹지도 않고 통째로 집어삼킨다. 그리고는 꼼짝도 하지 못하고 여섯 달 동안 잠을 자면서 그것을 소화시킨다.'''

print(littlePrince[:10])

def calculator(a, b):
    return a + b, a - b, a * b, a /b

print(calculator(12, 3))

print(type(calculator(12, 3)))

a = input('숫자를 하나 입력해 보세요: ')

print(type(a))