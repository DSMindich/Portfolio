top = open("templates/top.html").read()
bottom = open("templates/bottom.html").read()
index = open("content/index.html").read()
blog = open("content/blog.html").read()
port = open("content/port.html").read()
index_page = (top + index + bottom)
blog_page = (top + blog + bottom)
port_page = (top + port + bottom)

open('docs/index.html', 'w+').write(index_page)
open('docs/blog.html', 'w+').write(blog_page)
open('docs/port.html', 'w+').write(port_page)