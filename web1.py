from bs4 import BeautifulSoup
import requests

url="https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbFZRWFhWNWxkRDU5VFp5RklnUjRhYW4wcHZJZ3xBQ3Jtc0tuWHZzVFV5djN6QmRoZ2tGYXBwSkFJd1JHMDIzN3RLbkVJU1ZzRkV2eU1xUTFFSmd0M2FGUmJOZzNiRDFvUWgzNGt3Z3RpRXZsU3VNYllTQjNkVkg5WmFLeHZEbk51UWE5WFJsMk45aGtXa0MyTFhJSQ&q=https%3A%2F%2Fwww.newegg.ca%2Fgigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd%2Fp%2FN82E16814932436%3FDescription%3D3080%26cm_re%3D3080-_-14-932-436-_-Product&v=gRLHr664tXA"
result=requests.get(url)
print(result.text)
doc=BeautifulSoup(result.text,"html.parser")
print(doc.prettify())

