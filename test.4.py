import os


os.chdir(r'C:\Users\bapme\Desktop\개발노트\파이썬')
print(os.getcwd())
print(os.listdir())

f = open('test.py', 'r')
print(f.read())

#파일 커서를 처음으로 이동하라는 의미
print(f.seek(0))