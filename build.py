# Lists
pages = [
    {
        "filename": "content/index.html",
        "output": "docs/index.html",
        "title": "About Me",
        "active": "{{active_home}}"
    },
    {
        "filename" : "content/blog.html",
        "output" : "docs/blog.html",
        "title" : "Blog",
        "active": "{{active_blog}}"
    },
    {
        "filename" : "content/port.html",
        "output" : "docs/port.html",
        "title" : "Portfolio",
        "active": "{{active_port}}"
    },
]
#Functions
def main():
    for page in pages:
        page_title = page["title"]
        final_file = page["output"]
        content_path = page["filename"]
        #active_link = page["active"]
        open_base()
        apply_template(content_path,page_title,final_file) #add active_link back in later
    #Opens base template 
def open_base():
    base_html = open("templates/base.html").read()
    return base_html
    #Adds page titles, active page functionality, and content to base template, saves output to /docs
def apply_template(content,title,web_page): #add act back in (if needed)
    page_content = open(content).read()
    titled_page = open_base().replace("{{title}}", title)
    #active_page= titled_page.replace(act, "active")
    full_page = titled_page.replace("{{content}}", page_content)
    open(web_page, 'w+').write(full_page)

# Script
if __name__ == "__main__":
    main()