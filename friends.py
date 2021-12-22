import os, re

os.chdir(r'C:\Users\bapme\Desktop\개발노트\파이썬')

f = open('friends101.txt', 'r', encoding = 'utf8')
script101 = f.read()

#print(script101[:100])


Line = re.findall(r'Monica:.+', script101)
#print(Line[:3])

# for item in Line[:3]:
#     print(item)

# f.close()


# f = open('monica.txt', 'w', encoding = 'utf8')
# monica = ''

# for i in Line:
#     monica += i + '\n'

# f.write(monica)

# f.close()


# set() 중복 원소 제거
char = re.compile(r'[A-Z][a-z]+:')
y = set(re.findall(char, script101))
#print(y)

z = list(y)
character = []
for i in z :
    character += [i[:-1]]

#print(character)

# 한 줄로 간단히 표현
character2 = []
character2 = [x[:-1] for x in list(set(re.findall(r'[A-Z][a-z]+:', script101)))]
# print(character2)


# f = open('character3.txt', 'w', encoding = 'utf-8')

# character3 = ''
# for x in list(set(re.findall(r'\([A-Za-z].+[a-z|\.]\)', script101))):
#     character3 += x + '\n'

# f.write(character3)
# f.close()


f = open('friends101.txt', 'r')
# print(f.read(100))
# print(f.seek(0))

sentences = f.readlines()
f.close()

for i in sentences[:20]:
    if re.match(r'[A-Z][a-z]+:', i):
        print(i)

#리스트에 담기
lines = [i for i in sentences if re.match(r'[A-Z][a-z]+:', i) and re.search('would', i)]
print(lines)

newf = open('would.txt', 'w', encoding = 'utf-8')
newf.write(lines)
newf.close()