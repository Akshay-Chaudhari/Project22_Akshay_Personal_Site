import bs4

with open("website.html") as file:
    contents = file.read()


class BeautifulSoup:
    pass

soup = bs4.BeautifulSoup(contents, "html.parser")
print(soup.title.string)