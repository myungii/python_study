import re

pattern = r'life'
script = 'life'
re.match(pattern, script)
re.match(pattern, script).group()


data = 'a:3; b:4; c:5'

for i in re.split(r';', data):
    re.split(r':', i)




