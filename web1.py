from bs4 import BeautifulSoup
 
with open("basic.html",'r') as f:
    output=BeautifulSoup(f,"html.parser")

#print(output.prettify())

# tag=output.title
# print(tag.string)
# tag.string="abhishek"
# print(tag)
# print(output.prettify())

tags=output.find_all("a")
for i in tags:
    print(i.text)