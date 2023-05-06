from bs4 import BeautifulSoup
with open('courses.html','r') as courses_file:
    content=courses_file.read()

out=BeautifulSoup(content,"lxml")
print(out.prettify())
tags=out.find_all('h5')
for txt in tags:
    print(txt.text)