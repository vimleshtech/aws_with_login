import os
import shutil

src = r"C:\Users\vkumar15\Desktop\Desktop - Raman"
items  = os.listdir(src)

dest = r'C:\Users\vkumar15\Desktop\out'
#print(out)

for item in items:
     #print(a)
     if item.endswith('.docx'):
          print(src+'\\'+item)
          shutil.copy(src+'\\'+item,dest)




          
     
     
