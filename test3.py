def seperate():
    a = int(input('자연수 중 하나를 입력하세요. : '))

    if a % 2 == 0:
        print('짝수')
    else:
        print('홀수')



for i in range(10):
    if i % 2 is not 0:
        print(i, '홀수')

    else:
        print(i, '짝수')

