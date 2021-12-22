import os, re

os.chdir(r'C:\Users\bapme\Desktop\개발노트\파이썬')
import usecsv

apt = usecsv.switch(usecsv.opencsv('apt_211222.csv'))


#print(len(apt))

new_list = []
for i in apt:
    try:
        if i[5] >= 120 and i[-7] <=30000 and re.match('강원', i[0]):
            new_list.append([i[0], i[4], i[-7]])
    except:
        pass
    
print(new_list)

usecsv.writecsv('over120_lower3000.csv', new_list)

    