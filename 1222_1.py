# -*- coding: utf-8 -*-

import os, re
import usecsv

os.chdir(r'C:\Users\bapme\Desktop\개발노트\파이썬\do-it-python\04')

total = usecsv.opencsv('popSeoul.csv')

newPop = usecsv.switch(total)
new = [['구', '한국인', '외국인', '외국인 비율(%)']]
for i in newPop:
    foreign = 0
    try:
        foreign = round(i[2] / (i[1] + i[2]) * 100, 1)
        if foreign > 3:
            new.append([i[0], i[1], i[2], foreign])
        
    except:
        pass
    
print(new)
usecsv.writecsv('newPop.csv', new)




    
        