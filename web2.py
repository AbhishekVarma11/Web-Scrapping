from bs4 import BeautifulSoup
with open('courses.html','r') as courses_file:
    content=courses_file.read()

out=BeautifulSoup(content,"lxml")
print(out.prettify())
tags=out.find_all('h5')
for txt in tags:
    print(txt.text)
cards=out.find_all('div',class_='card')
for card in cards:
    course=card.h5.text
    price=card.a.text.split()[-1]
    print(f"course:{course}{'  '}price:{price}")
    
