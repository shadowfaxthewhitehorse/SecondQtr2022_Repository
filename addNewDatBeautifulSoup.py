## QWYKRTECH - example of using BeautifulSoup to add content to HTML code.
# 

# Adding new data using BeautifulSoup

markup = '<a href="https://www.qwykrtech.com/index.htm">Quicker learning</a>'

Bsoup = BeautifulSoup(markup)

Bsoup.a.append(" Really Liked it")

# let us see what the object Bsoup has
Bsoup

#
# output: <html><body><a href="https://www.qwykrtech.com/index.htm">Quicker learning</a></body></html>

#
#
print(Bsoup.a.contents)
# ['Must for every ', <i>Learner</i>, ' Really Liked it']
