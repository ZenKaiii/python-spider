from bs4 import BeautifulSoup
import requests
request = requests.get("http://www.nike.com/cn/launch/")
html = request.text

bs = BeautifulSoup(html,"html.parser")
# print(bs.prettify())
# print(bs.title)

# img_tags = bs.findAll("div")
# for tag in img_tags:
#     print(tag.name)
#
# div_tag = bs.find("div")
# children = div_tag.descendants
# for child in children:
#     print(child.name)

# parents = bs.find("div").parents
# for parent in parents:
#     print(parent.name)

sibs = bs.find("div").next_siblings #还有previous
for sib in sibs:
    if sib.name:
        print(sib.name)
        print(sib.get("class"))