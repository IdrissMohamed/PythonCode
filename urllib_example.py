import urllib.request urlopen

url = "https://en.wikipedia.org/wiki/Super_Mario"

page = ul.urlopen(url)

print(type(page))

page_contents = page.readlines()

print(len(page_contents))
print(type(page_contents))
print(type(page_contents[0]))

# for line in page.readlines():
#     print(line)