from bs4 import BeautifulSoup
 
with open("basic.html",'r') as f:
    output=BeautifulSoup(f,"html.parser")

print(output)
