#Just do the frankenstein thing and output as a single files (this is done with w+?)

top = open("templates/top.html").read()
bottom = open("templates/bottom.html").read()
art = open("content/art.html").read()
blog = open("content/blog.html").read()
index = open("content/index.html").read()
art_page = (top + art + bottom)
blog_page = (top + blog + bottom)
index_page = (top + index + bottom)

open('docs/art.html', 'w+').write(art_page)
open('docs/blog.html', 'w+').write(blog_page)
open('docs/index.html', 'w+').write(index_page)